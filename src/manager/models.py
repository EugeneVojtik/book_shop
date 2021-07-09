from json import loads, dumps

from django.contrib.auth.models import User
from django.db import models
from slugify import slugify


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    likes = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return f'комментарий № {self.id}'


class LikeBookUser(models.Model):
    class Meta:
        unique_together = ['book', 'user']

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_like')
    rate = models.PositiveIntegerField(null=True, default=0)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_likes',
                             null=True, blank=True)

    def __str__(self):
        return f'Книга {self.book}, пользователь {self.user}, оценка {self.rate}'

    def save(self, *args, **kwargs):
        try:
            super().save()
        except:
            lbu = LikeBookUser.objects.get(book=self.book, user=self.user)
            self.book.total_stars -= lbu.rate
            lbu.delete()
            super().save()

        self.book.total_stars += self.rate
        self.book.rating = self.book.total_stars / self.book.book_likes.count()
        self.book.save()


class LikeCommentUser(models.Model):
    class Meta:
        unique_together = ['comment', 'user']

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_comment_likes')




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
    rating = models.FloatField(null=True, default=0.0)
    total_stars = models.PositiveIntegerField(null=True, default=0)
    slug = models.SlugField(unique=True, primary_key=True)
    id = models.PositiveIntegerField(null=True, blank=True, auto_created=True)
    price = models.SmallIntegerField(default=100)

    def __str__(self):
        return f'{self.title}'

    def save(self, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)
        try:
            super().save(**kwargs)
        except:
            self.slug += str(self.date)
            super().save(**kwargs)


class CustomersFeedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.TextField(help_text='please enter your feedback right here')

    def __str__(self):
        return f'{self.customer} - {self.id}'


class ShoppingBasketUser(models.Model):
    class Meta:
        unique_together = ['customer']

    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customers_basket')


class BasketContent(models.Model):
    basket = models.ForeignKey(ShoppingBasketUser, on_delete=models.CASCADE, related_name='users_purchase_list')
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='basket')

    def __str__(self):
        return f'Пользователь: {self.basket.user}, товар: {self.product}'


class UsersBooks(models.Model):
    class Meta:
        unique_together = ['book', 'user']

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='users_to_read')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_in_read')

    def __str__(self):
        return f'книга {self.book}'


class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='git_hub_user')
    github_account = models.CharField(max_length=100, null=True)
    _github_repos = models.TextField(null=True)

    @property
    def github_repos(self):
        if self._github_repos is not None:
            return loads(self._github_repos)
        return []

    @github_repos.setter
    def github_repos(self, value):
        assert isinstance(value, list), "you can set list only"
        self._github_repos = dumps(value)
