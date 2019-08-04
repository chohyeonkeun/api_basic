from django.urls import path
from .views import *
urlpatterns = [
    path('', TweetListCreateView.as_view()),
    path('<int:pk>/', TweetDetailView.as_view()),
    # path('update/<int:pk>/', TweetUpdateView.as_view()),
    # path('detail/<int:pk>/', TweetDetailView.as_view()),
    # path('delete/<int:pk>/', TweetDeleteView.as_view()),
]