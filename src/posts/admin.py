from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # fields = ('title',)
    list_display = ('id', 'title')


admin.site.register(Post, PostAdmin)
