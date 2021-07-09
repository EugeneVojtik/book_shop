from django.conf.urls import url
from django.urls import path, include

from django.views.decorators.cache import cache_page

from manager.oauth_views import brazzers_view, brazzers_callback_view
from manager.views import MainPage, AddCommentLike, AddRate, BookPage, AddBook, AddComment, LoginView, logout_user, \
    FeedbackPage, AddFeedback, book_delete, BookUpdate, RegisterView, UsersAccount, BasketPage, remove_from_basket

from manager.views import BookPurchase
from manager.views_ajax import add_rate_ajax, DeleteComment, AddLike2Comment, CreateBook, AddRating

urlpatterns = [
    path('add_comment_like/<int:id>/', AddCommentLike.as_view(), name='add_comment_like'),
    path('add_comment_like/<int:id>/<str:location>', AddCommentLike.as_view(), name='add_comment_like_location'),
    path('add_rate/<str:slug>/<int:rate>/', AddRate.as_view(), name='add_rate'),
    path('add_rate/<str:slug>/<int:rate>/<str:location>/', AddRate.as_view(), name='add_rate_location'),
    path('book_view_detail/<str:slug>/', BookPage.as_view(), name='book_detail'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('add_comment/<str:slug>/', AddComment.as_view(), name='add_comment'),
    path('feedback_page', FeedbackPage.as_view(), name='feedback_page'),
    path('add_feedback', AddFeedback.as_view(), name='add_feedback'),
    path('delete_book/<str:slug>/', book_delete, name='delete_book'),
    path('update_book/<str:slug>/', BookUpdate.as_view(), name='update_book'),
    path('login_page/', LoginView.as_view(), name='login_page'),
    path('register_page', RegisterView.as_view(), name='register_page'),
    path('logout/', logout_user, name='logout'),
    path('add_to_basket/<str:slug>/', BookPurchase.as_view(), name='add_to_basket'),
    path('go_to_basket', BasketPage.as_view(), name='basket_page'),
    path('user_account', UsersAccount.as_view(), name='user_account'),
    path('to_the_main', MainPage.as_view(), name='to_the_main'),
    path('remove_from_basket/<str:slug>/', remove_from_basket, name='remove_from_basket'),
    path('brazzers/', brazzers_view, name='brazzers'),
    path('brazzers/github/', brazzers_callback_view, name='brazzers_callback'),
    path('', MainPage.as_view(), name='the-main-page'),
    path('add_like2comment_ajax/<int:id>', AddLike2Comment.as_view()),
    path('delete_comment_ajax/<int:id>', DeleteComment.as_view()),
    path('add_rate_ajax/<int:pk>', AddRating.as_view()),
    path('create_book_ajax/', CreateBook.as_view()),
]


