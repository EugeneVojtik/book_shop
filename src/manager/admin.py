from django.contrib import admin

from manager.models import Comment, Book


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 2


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    readonly_fields = ['rating']
    exclude = ['total_stars', 'likes']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
