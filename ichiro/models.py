from django.db import models


class Scrape(models.Model):
    """
    A batch of scraped data.
    """
    datetime = models.DateTimeField()
    json = models.TextField()

    class Meta:
        ordering = ("-datetime",)
        get_latest_by = 'datetime'

    def __str__(self):
        return str(self.datetime)
