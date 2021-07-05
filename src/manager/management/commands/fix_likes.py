from django.core.management import BaseCommand

from manager.models import Book


class Command(BaseCommand):
    def handle(self, *obj, **options):
        query = Book.objects.all()

        for book in query:
            book.likes = 0
            book.save()
