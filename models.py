from django.db import models

from django.contrib.auth.models import User

class Location(models.Model):
    LOCATION_TYPE_CHOICES = [
        ('KIOSK', 'Digital Kiosk'),
        ('UTILITY', 'Utility'),
        ('TICKET', 'Ticket Counter'),
        ('STATION', 'Station Entrance/Exit'),
        ('ACCESSORY', 'Accessories Shop'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    z_coordinate = models.FloatField()

    def __str__(self):
        return self.name

class Path(models.Model):
    start_location = models.ForeignKey(Location, related_name='path_start', on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, related_name='path_end', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.start_location} to {self.end_location}"
