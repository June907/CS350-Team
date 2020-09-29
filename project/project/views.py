from django.views.generic import ListView,DetailView
from .models import Post
from django.shortcuts import render

users = [
    {
        'name': 'Erik Halenkamp',
        'id': '00001',
        'role': 'admin',
        'date_joined': 'August 24 , 2020'
    },
    {
        'name': 'Junwen Huang',
        'id': '00002',
        'role': 'admin',
        'date_joined': 'August 24 , 2020'
    },
    {
        'name': 'Yusuf Kortobi',
        'id': '00003',
        'role': 'admin',
        'date_joined': 'August 24 , 2020'
    },
    {
        'name': 'Asepha Shaeffer',
        'id': '00004',
        'role': 'admin',
        'date_joined': 'August 24 , 2020'
    }
]

def home(request):
    context = {
        'users': users
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'users': users
    }
    return render(request, 'about.html', context)

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
