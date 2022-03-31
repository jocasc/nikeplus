from django.contrib import admin
from corridas.models import Running, Distance


class Runs(admin.ModelAdmin):
    list_display = ['name', 'description', 'total_distance', 'running_start', 'running_end',
                    'elapsed_time', 'calories', 'cadence', 'elevation_gain', 'elevation_loss']
    list_display_links = ['name']
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Running, Runs)


class Distances(admin.ModelAdmin):
    list_display = ['avg_pace', 'elevation']


admin.site.register(Distance, Distances)