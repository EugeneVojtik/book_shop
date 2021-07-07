from django.core.management import BaseCommand

from manager.models import LikeBookUser, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in LikeBookUser.objects.all():
            obj.delete()

        books = Book.objects.all()
        for book in books:
            book.rating = 0
            book.total_stars = 0

        Book.objects.bulk_update(books, ['rating', 'total_stars'])
