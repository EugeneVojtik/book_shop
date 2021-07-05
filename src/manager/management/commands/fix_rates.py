from django.core.management import BaseCommand

from manager.models import Book


class Command(BaseCommand):
    def handle(self,*obj, **options):
        # queryset = Book.objects.all()
        # for b in queryset:
        #     b.rating = 0
        # Book.objects.bulk_update(queryset, ['rating'])
        queryset = Book.objects.all()
        for b in queryset:
            b.total_stars = 0
            b.rating = 0
        Book.objects.bulk_update(queryset, ['total_stars', 'rating'])
