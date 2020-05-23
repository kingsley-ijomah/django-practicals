from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Comment

admin.site.site_header = 'Blog Admin'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.title


# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'active', 'created_on')
    list_filter = ('active',)
    search_fields = ('name', 'content',)
    actions = ('approve',)

    def approve(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.unregister(Group)
