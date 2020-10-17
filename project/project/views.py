from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login


def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'project/home.html', context)

def about(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'project/about.html', context)



class courseAddView(CreateView):
    model=Course
    fields=['title']
    
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        new_group, created = Group.objects.get_or_create(name=form.instance.title)
        form.instance.group = new_group
        self.request.user.groups.add(new_group)
        return super().form_valid(form)

class TestClassView(TemplateView):
    template_name='users/TestClass.html'

class discussionView(ListView):

    model=Post
    template_name='users/discussion.html'

class discussionDetailView(DetailView):
    model=Post
    template_name='users/discussion_detail.html'

class discussionCreateView(CreateView):
    model=Post
    template_name='users/discussion_new.html'
    fields=['title', 'author', 'body']

class discussionUpdateView(UpdateView):
    model=Post
    template_name='users/discussion_edit.html'
    fields=['title', 'body']

class discussionDeleteView(DeleteView):
    model=Post
    template_name='users/discussion_delete.html'
    success_url= reverse_lazy('users/discussion')

class assignmentView(ListView):
    model=Assignment
    template_name='users/assignment.html'
    
class assignmentCreateView(CreateView):
    model=Assignment
    template_name='users/assignment_create.html'
    fields=['title','due_date', 'points_possible']
    success_url=reverse_lazy('users/assignment')
    

    

def studentListView(request,url_name):
    model=Course
    url_name=Course.title
    
    
    context = {
        'students': User.objects.filter(groups__name=Course.title),
        'url_name': url_name
    }
    return render(request, 'users/studentList.html', context)



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
