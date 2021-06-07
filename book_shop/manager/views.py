from django.db.models import Count, Prefetch, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import View

from manager.models import Book, LikeBookUser, Comment, LikeCommentUser


class MainPage(View):
    def get(self, request):
        query = Comment.objects.annotate(count_like=Count('comment_likes')).select_related('author')
        comments = Prefetch('comments', query)
        context = {}
        books = Book.objects.prefetch_related('authors', comments)
        context['books'] = books
        context['stars'] = range(1, 6)
        return render(request, 'index.html', context)


class AddLike(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        if request.user.is_authenticated:
            lbu = LikeBookUser.objects.create(book=book, user=request.user)
            return redirect('the-main-page')


class AddCommentLike(View):
    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        if request.user.is_authenticated:
            lbu = LikeCommentUser.objects.create(comment=comment, user=request.user)
            return redirect('the-main-page')


class AddRate(View):
    def get(self, request, id, rate, location=None):
        book = Book.objects.get(id=id)
        if request.user.is_authenticated:
            LikeBookUser.objects.create(book=book, user=request.user, rate=rate)
        if location is None:
            return redirect('the-main-page')
        else:
            return redirect('book_detail', id=id)

class BookPage(View):
    def get(self, request, id):

        context = {}
        comment_query = Comment.objects.annotate(count_like=Count('comment_likes')).select_related('author')
        comments = Prefetch('comments', comment_query)
        # book = Book.objects.filter(id=id)
        # query = book.first().comments.all().annotate(count_like=Count('comment_likes')).select_related('author')
        # comments = Prefetch('comments', query)
        # context['book'] = book.prefetch_related(comments)
        context['book'] = Book.objects.prefetch_related('authors', comments).get(id=id)
        context['stars'] = range(1, 6)
        return render(request, 'book_detail.html', context)
