from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post

admin.site.site_header = 'Blog Admin'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    list_filter = ('created',)


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)
