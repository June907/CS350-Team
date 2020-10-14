from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import courseAddView, TestClassView

urlpatterns= [
#    path('post/<int:pk>/',HomeDetailView.as_view(),name='post_detail'),
#
#    path('',HomePageView.as_view(),name='home'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('studentPage/',user_views.studentPage,name='studentPage'),
    path('add',courseAddView.as_view(template_name='project/course_add.html'),name='course_add'),
    path('studentPage/TestClass/', TestClassView.as_view(),name='TestClass'),
    #path('<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    

]