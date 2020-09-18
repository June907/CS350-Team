from django.urls import path
from .views import HomePageView,HomeDetailView

urlpatterns= [
    path('post/<int:pk>/',HomeDetailView.as_view(),name='post_detail'),

    path('',HomePageView.as_view(),name='home'),
]