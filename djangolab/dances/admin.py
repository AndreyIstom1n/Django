from django.contrib import admin
from .models import *

class DanceModeAdmin(admin.ModelAdmin):
    list_display = ['type','comment']
    list_display_links = ['type']
    search_fields = ['type']
    list_filter = ['type']
    list_editable = ['comment']
    class Meta:
        model=Dance

class DancerModeAdmin(admin.ModelAdmin):
    list_display = ['name','surname','contact']
    search_fields = ['name','surname','contact']
    list_filter = ['name','surname','contact']
    list_editable = ['contact']
    class Meta:
        model=Dancer

class ActionModeAdmin(admin.ModelAdmin):
    list_display = ['action_comment']
    list_display_links = ['action_comment']
    search_fields = ['action_comment']
    list_filter = ['action_comment']

    class Meta:
        model=Action
class PlaceModeAdmin(admin.ModelAdmin):
    list_display = ['address']
    search_fields = ['address']
    list_filter = ['address']
    class Meta:
        model=Place

admin.site.register(Dance,DanceModeAdmin)
admin.site.register(Dancer,DancerModeAdmin)
admin.site.register(Action,ActionModeAdmin)
admin.site.register(Place,PlaceModeAdmin)
