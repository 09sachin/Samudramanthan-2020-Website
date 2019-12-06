from django.contrib import admin
from .models import events
from .models import sponsers
from .models import FeedBack
from .models import team
from .models import gallery
from .models import RegisterForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class eventResource(resources.ModelResource):
    class Meta:
        model = events

# Register your models here.

# admin.site.register(events)
# admin.site.register(sponsers)
admin.site.register(FeedBack)
# admin.site.register(team)
admin.site.register(gallery)
admin.site.register(RegisterForm)

@admin.register(events)
class EventsAdmin(ImportExportModelAdmin):
    pass


@admin.register(sponsers)
class SponsorsAdmin(ImportExportModelAdmin):
    pass

@admin.register(team)
class TeamAdmin(ImportExportModelAdmin):
    pass


