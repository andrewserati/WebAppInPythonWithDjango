from django.contrib import admin
from core.models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'createdIn')
    list_filter = ('title',)

admin.site.register(Event, EventAdmin)
