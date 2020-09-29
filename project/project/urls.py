from django.urls import path
from . import views
#from .views import HomePageView,HomeDetailView

urlpatterns= [
#    path('post/<int:pk>/',HomeDetailView.as_view(),name='post_detail'),
#
#    path('',HomePageView.as_view(),name='home'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]