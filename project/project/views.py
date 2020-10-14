from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView
from .models import Course
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
    
    success_url = "{% url 'studentPage' %}"
    
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        new_group, created = Group.objects.get_or_create(name=form.instance.title)
        form.instance.group = new_group
        self.request.user.groups.add(new_group)
        return super().form_valid(form)


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
