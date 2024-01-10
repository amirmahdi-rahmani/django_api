from django.contrib import admin
from django.utils.html import format_html
from .models import Thing , Category , Image

class ThingImageInline(admin.TabularInline):
    model = Image

@admin.register(Thing)
class ThingsAdmin(admin.ModelAdmin):
    list_display = ['name','category','get_link']
    list_select_related = ['category']
    list_filter = ['category']
    inlines =[ThingImageInline]
    search_fields = ['name']

    def get_link(self,obj):
        return format_html("<a href='{url}'>{slug}</a>", url=obj.link , slug='click')

    

admin.site.register(Category)
admin.site.register(Image)


