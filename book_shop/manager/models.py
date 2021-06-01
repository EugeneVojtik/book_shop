from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    title = models.CharField(max_length=50, verbose_name='Наименование', help_text='ну это типа название книги')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата',
                                help_text='Если нет даты, то заполняется автоматически', null=True)
    description = models.TextField(null=True, default='Book description to be added soon')
    authors = models.ManyToManyField(User, related_name='books')
    likes = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'комментарий № {self.id}'


class LikeBookUser(models.Model):
    class Meta:
        unique_together = ['book', 'user']

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_like')

    def save(self, *args, **kwargs):
        try:
            super(LikeBookUser, self).save()
            self.book.likes += 1
        except Exception as e:
            self.book.likes -= 1
            LikeBookUser.objects.get(book=self.book, user=self.user).delete()
            print(f'Like has already been added, here is an exception description: {e}')
        self.book.save()
