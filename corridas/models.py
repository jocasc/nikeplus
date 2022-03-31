from django.db import models


class Running(models.Model):
    WEATHER = (
        ('CL', 'ceu limpo'),
        ('PN', 'parcialmente nublado'),
        ('NU', 'nublado'),
        ('CH', 'chuva'),
        ('VE', 'ventania')
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    temperature = models.IntegerField()
    weather = models.CharField(max_length=2, choices=WEATHER, blank=False, null=False, default='CL')
    total_distance = models.FloatField()
    running_start = models.DateTimeField()
    running_end = models.DateTimeField()
    elapsed_time = models.DurationField()
    calories = models.IntegerField()
    cadence = models.IntegerField()
    elevation_gain = models.IntegerField()
    elevation_loss = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Distance(models.Model):
    running = models.ForeignKey(Running, on_delete=models.CASCADE)
    km = models.FloatField()
    avg_pace = models.DurationField()
    elevation = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




