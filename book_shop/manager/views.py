from django.contrib.auth import login, logout
from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from manager.forms import BookForm, CommentForm, CustomAuthenticationForm
from manager.models import Book, LikeBookUser, Comment, LikeCommentUser


class MainPage(View):
    def get(self, request):
        query = Comment.objects.annotate(count_like=Count('comment_likes')).select_related('author')
        comments = Prefetch('comments', query)
        context = {}
        books = Book.objects.prefetch_related('authors', comments)
        context['books'] = books
        context['stars'] = range(1, 6)
        context['form'] = BookForm
        context['login_form'] = CustomAuthenticationForm
        return render(request, 'index.html', context)


class AddLike(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        if request.user.is_authenticated:
            lbu = LikeBookUser.objects.create(book=book, user=request.user)
            return redirect('the-main-page')


class AddCommentLike(View):
    def get(self, request, id, location=None):
        comment = Comment.objects.get(id=id)
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(comment=comment, user=request.user)
            if location is None:
                return redirect('the-main-page')
            return redirect('book_detail', id=comment.book.id)


class AddRate(View):
    def get(self, request, slug, rate, location=None):
        if request.user.is_authenticated:
            book_id = Book.objects.get(slug=slug).id
            LikeBookUser.objects.create(book_id=book_id, user=request.user, rate=rate)
        if location is None:
            return redirect('the-main-page')
        return redirect('book_detail', slug=slug)


class BookPage(View):
    def get(self, request, slug):
        context = {}
        comment_query = Comment.objects.annotate(count_like=Count('comment_likes')).select_related('author')
        comments = Prefetch('comments', comment_query)
        context['book'] = Book.objects.prefetch_related('authors', comments).get(slug=slug)
        context['comment_form'] = CommentForm
        context['stars'] = range(1, 6)
        return render(request, 'book_detail.html', context)


class AddBook(View):
    def post(self, request):
        if request.user.is_authenticated:
            bf = BookForm(data=request.POST)
            book = bf.save(commit=True)
            book.authors.add(request.user)
            book.save()
        return redirect('the-main-page')


class AddComment(View):
    def post(self, request, slug):
        if request.user.is_authenticated:
            cf = CommentForm(data=request.POST)
            comment = cf.save(commit=False)
            comment.author = request.user
            comment.book = Book.objects.get(slug=slug)
            comment.save()
        return redirect('book_detail', slug=slug)


class LoginView(View):
    def get(self, request):
        return render(request, 'login_page.html', {'form': CustomAuthenticationForm})

    def post(self, request):
        user = AuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
        return redirect('the-main-page')

def logout_user(request):
    logout(request)
    return redirect('the-main-page')