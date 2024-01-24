from django.contrib import admin
from django.utils.html import format_html
from .models import Thing , Category , Image

class ThingImageInline(admin.TabularInline):
    model = Image

@admin.register(Thing)
class ThingsAdmin(admin.ModelAdmin):
    list_display = ['name','category_title','get_link']
    list_select_related = ['category']
    list_filter = ['category']
    inlines =[ThingImageInline]
    search_fields = ['name']

    def category_title(self,obj):
        return obj.category.title
    
    def get_link(self,obj):
        return format_html("<a href='{url}'>{slug}</a>", url=obj.link , slug='click')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug']
    
admin.site.register(Image)


