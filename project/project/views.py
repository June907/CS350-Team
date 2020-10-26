from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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

@login_required
def courses(request):
    return render(request, 'project/courses.html', {'courses': Course.objects.filter(group__in = request.user.groups.all())})

@login_required
def coursehome(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'project/coursehome.html', {'course': course})

class courseAddView(CreateView):
    model=Course
    fields=['title']
    
    success_url =reverse_lazy('users/studentPage')
    
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        new_group, created = Group.objects.get_or_create(name=form.instance.title)
        form.instance.group = new_group
        self.request.user.groups.add(new_group)
        return super().form_valid(form)

@login_required
def assignments(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'assignments': Assignment.objects.filter(course = course),
        'course': course,
    }
    return render(request, 'project/assignments.html', context)

@login_required
def assignmenthome(request,course_id,assignment_id):
    course = get_object_or_404(Course, pk=course_id)
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    try:
        submission = Submission.objects.get(assignment = assignment, student = request.user)
    except:
        submission = None
        
    context = {
        'assignment': assignment,
        'course': course,
        'submission': submission,
    }
    return render(request, 'project/assignmenthome.html', context)

@login_required
def grades(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    assignments = []
    submissions = []
    try:
        assignments = Assignment.objects.filter(course = course)
    except:
        pass
    
    totalpoints = 0
    
    for assignment in assignments:
        totalpoints = totalpoints + assignment.points_possible
        try:
            submissions.append(Submission.objects.get(assignment = assignment, student = request.user))
        except:
            pass
    
    pointsreceived = 0

    for submission in submissions:
        pointsreceived = pointsreceived + submission.points_received
    
    context = {
        'assignments': assignments,
        'course': course,
        'submissions': submissions,
        'points': [pointsreceived,totalpoints,100*pointsreceived/totalpoints],
    }
    return render(request, 'project/grades.html', context)

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
    success_url= reverse_lazy('discussion')
    
class assignmentCreateView(CreateView):
    model=Assignment
    template_name='users/assignment_create.html'
    fields=['title','due_date', 'points_possible']
    success_url=reverse_lazy('assignment')
    

    

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
