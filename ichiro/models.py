from django.db import models


class Scrape(models.Model):
    """
    A batch of scraped data.
    """
    datetime = models.DateTimeField()
    json = models.TextField()

    def __str__(self):
        return str(self.datetime)
