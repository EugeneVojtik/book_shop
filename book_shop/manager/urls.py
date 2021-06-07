from django.urls import path

from manager.views import MainPage, AddLike, AddCommentLike, AddRate, BookPage

urlpatterns = [

    path('add_like/<int:id>/', AddLike.as_view(), name='add_like'),
    path('add_comment_like/<int:id>/', AddCommentLike.as_view(), name='add_comment_like'),
    path('add_rate/<int:id>/<int:rate>/', AddRate.as_view(), name='add_rate'),
    path('add_rate/<int:id>/<int:rate>/<str:location>/', AddRate.as_view(), name='add_rate_location'),
    path('book_view_detail/<int:id>/', BookPage.as_view(), name='book_detail'),
    path('', MainPage.as_view(), name='the-main-page')
]



