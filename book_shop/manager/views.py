from django.shortcuts import render, redirect

from django.views import View

from manager.models import Book, LikeBookUser


class MainPage(View):
    def get(self, request):
        context = {'books': Book.objects.all()}
        return render(request, 'index.html', context)

class AddLike(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        if request.user.is_authenticated:
            lbu = LikeBookUser.objects.create(book=book, user=request.user)
            return redirect('the-main-page')