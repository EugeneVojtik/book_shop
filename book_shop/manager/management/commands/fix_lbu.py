from django.core.management import BaseCommand

from manager.models import LikeBookUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in LikeBookUser.objects.all():
            obj.delete()

