from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=40)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    course= models.ForeignKey(
        Course, on_delete=models.CASCADE,
        null=True
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    time = models.DateTimeField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion_detail', args=[str(self.id)])

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField(null=True)
    points_possible = models.DecimalField(max_digits=5,decimal_places=2)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    
class Submission(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    points_received = models.DecimalField(max_digits=5,decimal_places=2)
    

# Create your models here.
