from django.shortcuts import render
from .serializers import UserListSerializer, UserCreateSerializer, UserModifySerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
"""
List : GET
Create : POST
Retrieve : GET
Update : PUT, PATCH
Destroy : Delete
"""

class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer
    # 원하는 검색 항목 추가
    filterset_fields = ('username', 'first_name')

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(pk=self.request.user.id)
        return queryset


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserUpdateView(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserModifySerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()


