from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import Tweet
from .permissions import *

class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetListSerializers

    search_fields = ('text','author__username')

    def create(self, request, *args, **kwargs):
        print(request)
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)

from rest_framework.permissions import IsAuthenticated
class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers
    # 원래 로그인해야만 view 가 보이도록 설정되어 있는데, permission_classes 를 함으로써 오버라이드할 수 있다.
    permission_classes = [IsAuthenticated, IsOwnerAndAdminOnly]

# class TweetListView(generics.ListAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetListSerializers
#
# class TweetCreateView(generics.CreateAPIView):
#     serializer_class = TweetSerializers
#
# class TweetDatailView(generics.RetireveAPIView):
#     queryset = Tweet.objects.all()
#     serializers = TweetListSerializers
#
# class TweetUpdateView(generics.UpdateAPIView):
#     queryset = Tweet.objects.all()
#     serializers = TweetSerializers
#
# class TweetDeleteView(generics.DestroyAOIView):
#     queryset = Tweet.objects.all()