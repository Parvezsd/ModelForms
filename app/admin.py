from django.contrib import admin # type: ignore
from app.models import *
class CustomizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','email','url']
    list_display_links=['topic_name']
    list_editable=['name']
    list_per_page=2
    list_filter=['name']
    search_fields=['name']
class CustomizeAccess(admin.ModelAdmin):
    list_display=['name','author','date']
    list_display_links=['date']
    list_editable=['name']
    list_per_page=2
    list_filter=['author']
    search_fields=['name']
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage,CustomizeWebpage)
admin.site.register(AccessRecord,CustomizeAccess)