import json
import logging
import collections
from datetime import datetime
from django.conf import settings
from ichiro.models import Scrape
from requests_html import HTMLSession
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Scrape the stats
        data = self.get_ichiro_stats()
        data.update(self.get_mariners_stats())
        # Write out to a JSON file
        obj = Scrape.objects.create(
            datetime=str(datetime.now()),
            json=json.dumps(data, indent=4)
        )
        print("Created {}".format(obj))

    def get_mariners_stats(self):
        """
        Scrape some stats about the Mariners season is going. You know. For context.
        """
        # Grab the HTML
        session = HTMLSession()
        mariners_url = "https://www.baseball-reference.com/leagues/AL/2017.shtml"
        print("Requesting {}".format(mariners_url))
        r = session.get(mariners_url)

        # Grab the table with team stats
        table = r.html.find('table#teams_standard_batting', first=True)
        # Grab all the rows
        row_list = table.xpath("//tr")
        # Loop through them
        for row in row_list:
            # Keep going until you get to the Mariners
            team = row.find("th", first=True).text
            if team == 'SEA':
                print(" - Scraping {}".format(team))
                # Then when you hit it return the number of games they've played so far.
                return dict(
                    mariners_games_played=int(row.xpath("//td[@data-stat='G']", first=True).text)
                )


    def get_ichiro_stats(self):
        """
        Scrape a few Ichiro stats from baseball-reference.com.

        Returns them as an OrderedDict with season's year as the key.
        """
        # Grab HTML from baseball-reference
        session = HTMLSession()
        ichiro_url = "https://www.baseball-reference.com/players/s/suzukic01.shtml"
        print("Requesting {}".format(ichiro_url))
        r = session.get(ichiro_url)

        # Drill down to the table with major league stats by year
        table = r.html.find('table#batting_standard', first=True)
        year_list = table.xpath("//tr[starts-with(@id,'batting_standard')]")

        # Loop through the years...
        data_dict = collections.OrderedDict()
        for year in year_list:
            # ... pull out the year number ...
            season = int(year.find("th", first=True).text)
            print("- Scraping {}".format(season))
            # ... pull out the stats we're looking for.
            data_dict[season] = dict(
              g=int(year.xpath("//td[@data-stat='G']", first=True).text),
              pa=int(year.xpath("//td[@data-stat='PA']", first=True).text),
              ab=int(year.xpath("//td[@data-stat='AB']", first=True).text)
            )

        # Return what we've got.
        return data_dict
