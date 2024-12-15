from django.contrib import admin
from django.utils.html import format_html

from shop.models import Customers, Article


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image_tag"]
    # fields = ["title","picture"]
    def image_tag(self, obj):
        """Return an HTML <img> tag to display the image in the list view."""
        if obj.picture:
            ob = obj
            return format_html(f'<img src="{ob.picture.url}" width="50" height="50" />')
        return 'No Image'

    image_tag.short_description = 'Image'  # Set column header text for the image
    image_tag.allow_tags = True


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')  # Add the fields you want to display

admin.site.register(Customers, CustomersAdmin)
