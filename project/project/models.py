from django.db import models
from django.contrib.auth.models import User


#class Post(models.Model):
#    title = models.CharField(max_length=200)
#    author = models.ForeignKey(
#        'auth.User',
#        on_delete=models.CASCADE,
#    )
#    body = models.TextField()
#
#    def __str__(self):
#        return self.title

class Course(models.Model):
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    points_possible = models.DecimalField(max_digits=5,decimal_places=2)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Submission(models.Model):
    title = models.CharField(max_length=50)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    file = models.FileField()
    points_received = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.title

# Create your models here.
