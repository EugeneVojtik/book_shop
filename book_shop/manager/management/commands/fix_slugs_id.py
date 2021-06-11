from django.core.management import BaseCommand

from manager.models import  TMPBook, LikeBookUser, Comment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Creating of temperary Book table and filling all the fields with data from Books

        # book_set = Book.objects.all()
        # for book in book_set:
        #     tmp_book = TMPBook.objects.create(
        #         title=book.title,
        #         description=book.description,
        #         date=book.date,
        #         id=book.id,
        #     )
        #     for author in book.authors.all():
        #         tmp_book.authors.add(author)
        #     tmp_book.save()

        # Setting correct relations with

        # lbu_set = LikeBookUser.objects.all()
        # for lbu in lbu_set:
        #     lbu.tmp_book = TMPBook.objects.get(id=lbu.book.id)
        # LikeBookUser.objects.bulk_update(lbu_set, ['tmp_book'], batch_size=10)
        #

        # delete all the books

        # query_set = TMPBook.objects.all()
        # for book in query_set:
        #     book.delete()

        # update rating and total stars

        # query_set = TMPBook.objects.all()
        # for book in query_set:
        #     old_book = Book.objects.get(id=book.id)
        #     book.rating = old_book.rating
        #     book.total_stars = old_book.total_stars
        # TMPBook.objects.bulk_update(query_set, ['rating', 'total_stars'], batch_size=10)

        # comments_set = Comment.objects.all()
        # for comment in comments_set:
        #     comment.tmp_book = TMPBook.objects.get(id=comment.book_id)
        #
        # Comment.objects.bulk_update(comments_set,['tmp_book'], batch_size=20)
        lbu_set = LikeBookUser.objects.all()
        for obj in lbu_set:
            obj.book.delete()
        LikeBookUser.objects.bulk_update(lbu_set, ['book_id'], batch_size=20)