from datetime import date

from rest_framework import generics
from django.http import JsonResponse, HttpResponse

from api.serializers import AuthorSerializer, AuthorPostSerializer
from core.models import Author, Post


class AuthorDetail(generics.RetrieveAPIView):
    serializer_class = AuthorPostSerializer
    queryset = Author.objects.filter(post_list__created__date=date.today())


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.filter(post_list__created__date=date.today())


def idf(request, pk):
    if 'word' in request.GET:
        word = request.GET.get('word')
        post = Post.objects.get(pk=pk)
        tf_idf = post.get_tf_idf(word)
        return JsonResponse({'tf_idf': tf_idf})
    else:
        return HttpResponse("ADD ?word=my_word")
