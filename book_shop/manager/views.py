from django.shortcuts import render

from django.views import View

from manager.models import Book


class MainPage(View):
    def get(self, request):
        context = {'books': Book.objects.all()}
        return render(request, 'index.html', context)
