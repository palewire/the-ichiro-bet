import json
import logging
import collections
from requests_html import HTMLSession
logger = logging.getLogger(__name__)


def get_ichiro_stats():
    """
    Scrape a few Ichiro stats from baseball-reference.com.

    Returns them as an OrderedDict with season's year as the key.
    """
    # Grab HTML from baseball-reference
    session = HTMLSession()
    ichiro_url = "https://www.baseball-reference.com/players/s/suzukic01.shtml"
    logger.debug("Requesting {}".format(ichiro_url))
    r = session.get(ichiro_url)

    # Drill down to the table with major league stats by year
    table = r.html.find('table#batting_standard', first=True)
    year_list = table.xpath("//tr[starts-with(@id,'batting_standard')]")

    # Loop through the years...
    data_dict = collections.OrderedDict()
    for year in year_list:
        # ... pull out the year number ...
        season = int(year.find("th", first=True).text)
        logger.debug("- Scraping {}".format(season))
        # ... pull out the stats we're looking for.
        data_dict[season] = dict(
          g=int(year.xpath("//td[@data-stat='G']", first=True).text),
          pa=int(year.xpath("//td[@data-stat='PA']", first=True).text),
          ab=int(year.xpath("//td[@data-stat='AB']", first=True).text)
        )

    # Return what we've got.
    return data_dict


if __name__ == "__main__":
    # Scrape the stats
    ichiro_stats = get_ichiro_stats()
    # Write out to a JSON file
    logger.debug("Writing to ichiro.json")
    json.dump(ichiro_stats, open("./ichiro.json", "w"), indent=4)
