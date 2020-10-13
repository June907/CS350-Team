from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView
from .models import Course
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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



class courseAddView(CreateView):
    template_name="users/course_add.html"
    model=Course
    fields='__all__'


#def my_view(request):
    #username=request.Post['username']
    #password=request.Post['password']
    #user=authenticate(request,username=username, password=password)
   #if user is not None:
     #   login(request, user)
        #return redirect('user/studentPage.html')

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
