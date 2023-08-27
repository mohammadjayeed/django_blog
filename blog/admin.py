from django.contrib import admin
from .models import Category, Blog
# Register your models here.
admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','is_featured','category','status')
    search_fields = ('title','author','status')
    list_editable = ('status',)



admin.site.register(Blog, BlogAdmin)