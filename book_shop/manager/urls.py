from django.urls import path

from manager.views import MainPage, AddLike

urlpatterns = [
    path('', MainPage.as_view(), name='the-main-page'),
    path('add_like/<int:id>/', AddLike.as_view(), name='add_like')
]



