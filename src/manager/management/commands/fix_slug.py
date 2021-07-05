from django.core.management import BaseCommand
from slugify import slugify

from manager.models import Book


class Command(BaseCommand):
    def handle(self, *obj, **options):
        queryset = Book.objects.all()
        for book in queryset:
            book.slug = slugify(book.title)
            try:
                book.save()
            except:
                book.slug += str(book.id)
                book.save()