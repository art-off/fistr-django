from django.contrib import admin

from . import models
from .services.getters import get_rate_organizers


@admin.register(models.Grant)
class Grant(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')


@admin.register(models.Organizer)
class Organizer(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Volunteer)
class Volunteer(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Event)
class Event(admin.ModelAdmin):
    list_display = ('id', 'name', 'rate', 'get_organizers', 'get_volunteers', 'grant')

    def get_organizers(self, obj):
        return ', '.join([o.name for o in obj.organizers.all()])

    def get_volunteers(self, obj):
        return ', '.join([o.name for o in obj.volunteers.all()])


@admin.register(models.OrganizerRate)
class OrganizerRate(admin.ModelAdmin):
    change_list_template = 'admin/organizers_rate_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        response.context_data['rage_organizers'] = get_rate_organizers()
        return response
