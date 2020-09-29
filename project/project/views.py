from django.views.generic import ListView,DetailView
from .models import Course
from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'project/home.html', context)

def about(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'project/about.html', context)

#class HomePageView(ListView):
#    model=Post
#    template_name='home.html'
#    context = {
#        'users': users
#    }
#
#class HomeDetailView(DetailView):
#    model=Post
#    template_name='post_detail.html'

# Create your views here.
