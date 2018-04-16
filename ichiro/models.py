from django.db import models
from ichiro import managers


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
        ('the-bat-ros', 'The Bat (RoS)'),
        ('the-bat-adjusted-ros', 'The Bat (Adjusted RoS)'),
        ('zips', 'ZiPS (Update)'),
        ('depth-charts-ros', 'Depth Charts (RoS)'),
        ('depth-charts-adjusted-ros', 'Depth Charts (Adjusted RoS)'),
    )
    projection = models.CharField(max_length=500, choices=PROJECTION_CHOICES)
    ab = models.IntegerField()
    objects = managers.ProjectionManager()

    def __str__(self):
        return str(self.datetime)
