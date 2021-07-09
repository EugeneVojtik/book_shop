from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from manager.models import Comment, Book, LikeBookUser as RateBookUser, LikeCommentUser
from manager.permissions import IsAuthor
from manager.serializers import CommentSerializer, LKUSerializer, BookSerializer, AddRateSerializer


# def add_like2comment(request, comment_id):
#     if request.user.is_authenticated:
#         lku = LikeCommentUser.objects.create(user=request.user, comment_id=comment_id)
#         count_likes = lku.comment.likes
#         return JsonResponse({"likes": count_likes}, status=status.HTTP_201_CREATED)
#     return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


class AddLike2Comment(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LKUSerializer
    queryset = LikeCommentUser.objects.all()
    lookup_field = 'id'

    def get_object(self):
        user = self.request.user
        comment_id = self.kwargs['id']
        query_set = LikeCommentUser.objects.filter(user=user, comment_id=comment_id)
        if query_set.exists():
            return query_set.first()

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            LikeCommentUser.objects.create(user=self.request.user, comment_id=self.kwargs['id'])
        else:
            obj.delete()
        return Response({'likes': LikeCommentUser.objects.filter(comment_id=self.kwargs['id']).count()},
                        status=status.HTTP_200_OK)


def add_rate_ajax(request):
    if request.user.is_authenticated:
        rate = float(request.GET.get('rate'))
        book = Book.objects.get(slug=request.GET.get('book_slug'))
        RateBookUser.objects.create(book=book, user=request.user, rate=rate)
        return JsonResponse({'rating': book.rating}, status=status.HTTP_200_OK)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)

class AddRating(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = RateBookUser.objects.all()
    serializer_class = AddRateSerializer

    def get_object(self):




class DeleteComment(DestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"

class CreateBook(ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()













