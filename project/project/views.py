from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.files.storage import FileSystemStorage

def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'project/home.html', context)

def about(request):
    context = {
        'courses': Course.objects.all(),
        'groups': request.user.groups.all()
    }
    return render(request, 'project/about.html', context)

#COURSE

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
    
    success_url = reverse_lazy('courses')
    
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        
        new_group, created = Group.objects.get_or_create(name=form.instance.title)
        if created:
            form.instance.group = new_group
            self.request.user.groups.add(new_group)
            return super().form_valid(form)
        else:
            return render(self.request, 'project/courses.html', {'message': "That course already exists."})
        
class courseDeleteView(DeleteView):
    model=Course
    
    def setup(self, request, course_id):
        self.request = request
        if not (request.user == self.course.instructor):
            return render(request, '')
    
    def get_success_url(self):
        return reverse_lazy('courses')
    
def coursejoin(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    request.user.groups.add(course.group)
    
    return render(request, 'project/joinsuccess.html', {'course': course})

def courseleave(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    request.user.groups.remove(course.group)
    coursename = course.title
    if request.user == course.instructor:
        course.group.delete()
        course.delete()
    
    return render(request, 'project/leavesuccess.html', {'coursename': coursename})
#ASSIGNMENTS
    
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

class assignmentCreateView(CreateView):
    model=Assignment
    fields=['title', 'details', 'points_possible']
    
    def setup(self, request, course_id):
        self.course = get_object_or_404(Course, pk=course_id)
        self.request = request
        self.success_url = reverse_lazy('assignments',args=[course_id])
        if not (request.user == self.course.instructor):
            return render(request, '')

    def form_valid(self,form):
        form.instance.course = self.course
        return super().form_valid(form)
    
class assignmentUpdateView(UpdateView):
    model=Assignment
    fields=['title', 'details', 'points_possible']
    
    def setup(self, request, course_id):
        self.course = get_object_or_404(Course, pk=course_id)
        self.request = request
        if not (request.user == self.course.instructor):
            return render(request, '')
    
    def get_success_url(self):
        return reverse_lazy('assignmenthome', args=[self.object.course.id, self.object.id])
    
class assignmentDeleteView(DeleteView):
    model=Assignment
    
    def setup(self, request, course_id):
        self.course = get_object_or_404(Course, pk=course_id)
        self.request = request
        if not (request.user == self.course.instructor):
            return render(request, '')
    
    def get_success_url(self):
        return reverse_lazy('assignments', args=[self.object.course.id])

#GRADES

@login_required
def instructorgrades(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = User.objects.filter(groups__name=course.title)
    context = {
        'students': students,
        'course': course,
    }
    return render(request, 'project/instructorgrades.html', context)

@login_required
def individualgrades(request,course_id,student_id):
    course = get_object_or_404(Course, pk=course_id)
    student = get_object_or_404(User, pk=student_id)
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
            submissions.append(Submission.objects.get(assignment = assignment, student = student))
        except:
            pass
    
    pointsreceived = 0

    for submission in submissions:
        pointsreceived = pointsreceived + submission.points_received

    pointratio = 0
    if totalpoints != 0:
        
        pointratio = pointsreceived/totalpoints
    
    context = {
        'assignments': assignments,
        'student': student,
        'course': course,
        'submissions': submissions,
        'points': [pointsreceived,totalpoints,round(100*pointratio,2)],
    }
    
    return render(request, 'project/individualgrades.html', context)

#DISCUSSION

@login_required
def discussion(request,course_id):
    course=get_object_or_404(Course, pk=course_id)
    context = {
        'discussion': Post.objects.filter(course = course),
        'course': course,
    }
    return render(request, 'project/discussion.html', context)

@login_required
def discussionhome(request,course_id,discussion_id):
    course = get_object_or_404(Course, pk=course_id)
    discussion = get_object_or_404(Post, pk=discussion_id)
    #discussion = Post.objects.get(title=title, author = request.user)      
    context = {
        'discussion': discussion,
        'course': course,
        
    }
    return render(request, 'project/discussionhome.html', context)

class discussionCreateView(CreateView):
    model=Post
    template_name='project/discussion_new.html'
    fields=['title', 'body']
    
    def setup(self, request, course_id):
        self.course = get_object_or_404(Course, pk=course_id)
        self.request = request
        self.success_url = reverse_lazy('discussion',args=[course_id])

    def form_valid(self,form):
        form.instance.time = datetime.now()
        form.instance.author = self.request.user
        form.instance.course = self.course
        
        return super().form_valid(form)

class discussionDeleteView(DeleteView):
    model=Post
    
    def get_success_url(self):
        return reverse_lazy('discussion', args=[self.object.course.id])

#SUBMISSION
    
@login_required
def submissionhome(request,course_id,submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    #discussion = Post.objects.get(title=title, author = request.user)      
    context = {
        'submission': submission,
        'course': course,
        
    }
    return render(request, 'project/submissionhome.html', context)

class submissionCreateView(CreateView):
    model=Submission
    template_name='project/assignment_form.html'
    fields=['title', 'body']
    
    def setup(self, request, course_id, assignment_id):
        self.assignment = get_object_or_404(Assignment, pk=assignment_id)
        self.request = request
        self.success_url = reverse_lazy('assignmenthome',args=[course_id, assignment_id])
        
    def form_valid(self,form):
        form.instance.time = datetime.now()
        form.instance.student = self.request.user
        form.instance.points_received = 0
        form.instance.assignment_id = self.assignment.id
        submission = Submission.objects.filter(assignment = self.assignment, student = self.request.user)
        if submission:
            submission.delete()
        return super().form_valid(form)
    
class submissionUpdateView(UpdateView):
    model=Submission
    fields=['points_received']
    
    def get_success_url(self):
        return reverse_lazy('individualgrades', args=[self.object.assignment.course.id, self.object.student.id])

#class TestClassView(TemplateView):
#    template_name='users/TestClass.html'
#
#class discussionView(ListView):
#    model=Post
#    template_name='users/discussion.html'

#class discussionDetailView(DetailView):
#    model=Post
#    template_name='users/discussion_detail.html'
#
#class discussionCreateView(CreateView):
#    model=Post
#    template_name='users/discussion_new.html'
#    fields=['title', 'author', 'body']
#
#class discussionUpdateView(UpdateView):
#    model=Post
#    template_name='users/discussion_edit.html'
#    fields=['title', 'body']
#
#class discussionDeleteView(DeleteView):
#    model=Post
#    template_name='users/discussion_delete.html'
#    success_url= reverse_lazy('discussion')
    

    

#def studentListView(request,url_name):
#    model=Course
#    url_name=Course.title
#    
#    context = {
#        'students': User.objects.filter(groups__name=Course.title),
#        'url_name': url_name
#    }
#    return render(request, 'users/studentList.html', context)



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
