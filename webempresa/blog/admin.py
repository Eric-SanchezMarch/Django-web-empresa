from re import search
from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoriAdmin(admin.ModelAdmin):
    readonli_fields = ('created','upadetd')

class postAdmin(admin.ModelAdmin):
    readonli_fields = ('created','upadetd')
    list_display = ('title','author','published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content', 'author__username', 'categories__name' )
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories (self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "CATEGORIAS"


admin.site.register(Category, CategoriAdmin)
admin.site.register(Post, postAdmin)