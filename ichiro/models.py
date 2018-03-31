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


class Projection(models.Model):
    """
    Ichiro's projection for the season at a particular time.
    """
    datetime = models.DateTimeField()
    PROJECTION_CHOICES = (
        ('steamer-update', 'STEAMER (Update)'),
        ('the-bat-ros', 'The Bat (RoS)')
    )
    projection = models.CharField(max_length=500, choices=PROJECTION_CHOICES)
    ab = models.IntegerField()

    def __str__(self):
        return str(self.datetime)
