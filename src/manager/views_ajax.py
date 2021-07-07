from django.http import HttpResponse, JsonResponse
from rest_framework import status

from manager.models import LikeCommentUser, Comment, Book, LikeBookUser as RateBookUser


def add_like2comment(request):
    if request.user.is_authenticated:
        comment_id = request.GET.get('comment_id')
        lku = LikeCommentUser.objects.create(user=request.user, comment_id=comment_id)
        count_likes = lku.comment.likes
        return JsonResponse({"likes": count_likes}, status=status.HTTP_201_CREATED)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)


def delete_comment_ajax(request):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=request.GET.get('comment_id'))
        if comment.author == request.user:
            comment.delete()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)

def add_rate_ajax(request):
    if request.user.is_authenticated:
        rate = float(request.GET.get('rate'))
        book = Book.objects.get(slug=request.GET.get('book_slug'))
        RateBookUser.objects.create(book=book, user=request.user, rate=rate)
        return JsonResponse({'rating': book.rating}, status=status.HTTP_200_OK)
    return JsonResponse({}, status=status.HTTP_401_UNAUTHORIZED)
    # if request.user.is_authenticated:
    #     book = Book.objects.get(slug=slug)
    #     LikeBookUser.objects.create(book=book, user=request.user, rate=rate)
