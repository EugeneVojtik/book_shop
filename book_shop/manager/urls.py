from django.urls import path

from manager.views import MainPage, AddCommentLike, AddRate, BookPage, AddBook, AddComment, LoginView, logout_user, \
    FeedbackPage, AddFeedback, book_delete, BookUpdate

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
    path('logout/', logout_user, name='logout'),
    path('', MainPage.as_view(), name='the-main-page')
]



