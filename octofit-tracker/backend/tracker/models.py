from django.db import models


class Activity(models.Model):
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.type} ({self.duration_minutes}m)"
