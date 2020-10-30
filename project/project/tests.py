from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import *
from django.test import SimpleTestCase, TestCase
from .Course import *
from .Post import *

def create_test_user():
    return get_user_model().objects.create_user(username='TestUser',password='password')





class UserTests(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create_user(username='TestUser',password='password')
    def check_user_name(self,pk,name):
        check=User.objects.get(pk=pk)
        self.assertEqual(check.name,name)                                                                                                                                                                                                                                                                                   
 # This is for Course testing
class CourseTest(TestCase):

    def check_course_title(self,pk,title):
        course=Course.objects.get(pk=pk)
        self.assertEqual(course.title, title)

    def check_course_insructor(self,pk,instructor):
        course=Course.objects.get(pk=pk)
        self.assertEqual(course.instructor, instructor)

    def check_num_course(self,num):
        self.assertEqual(len(list_course()),num)

    def setUp(self):
        self.user=create_test_user()

        self.course=add_course('testclass',self.user,None)

    def test_crouse_model(self):
        self.check_num_course(1)
        self.check_course_title(1,'testclass')
        self.check_course_insructor(1,self.user)

    
    def test_create_course(self):
        self.check_num_course(1)
        add_course('testclass',self.user,None)
        self.check_course_title(2,'testclass')
        self.check_course_insructor(2, self.user)
        self.check_num_course(2)
    
    def test_list_course(self):
        self.check_num_course(1)
        self.assertEqual(get_course('testclass').pk,1)
        

    def test_update_course(self):
        self.check_num_course(1)
        course=get_course('testclass')
        course.title= 'anohterClass'
        course.save()
        self.check_course_title(1,'anohterClass')

    
    def test_delete_course(self):
        delete_course('testclass')
        self.check_num_course(0)

# This is for post

class PostTest(TestCase):

    def check_post_course(self, pk, title):
        p=Post.objects.get(pk=pk)
        self.assertEqual(p.course.title, title)
    
    def check_post_author(self, pk, author):
        p=Post.objects.get(pk=pk)
        self.assertEqual(p.author, author)

    def check_post_title(self, pk, title):
        p=Post.objects.get(pk=pk)
        self.assertEqual(p.title, title)

    def check_post_body(self, pk, text):
        p=Post.objects.get(pk=pk)
        self.assertEqual(p.body, text)

    def check_num_post(self, num):
        self.assertEqual(len(list_post()),num)

    def setUp(self):
        self.user=create_test_user()
        course=add_course('testclass',self.user, None)
        self.post=add_post('testpost',None,self.user,'sometext')

    def test_post_content(self):
        self.assertEqual(self.post.title, 'testpost')
        self.assertEqual(self.post.author,self.user)
        self.assertEqual(self.post.course,None)
        self.assertEqual(self.post.body,'sometext')

    def test_post_model(self):
        self.check_num_post(1)
        self.check_post_title(1, 'testpost')
        self.check_post_author(1,self.user)

    def test_create_post(self):
        self.check_num_post(1)
        author=get_post_author(self.user)
        add_post('anotherpost',None,self.user,'moretext')
        self.check_num_post(2)
        self.check_post_title(2,'anotherpost')

    def test_list_post(self):
        add_post('#2post',None,self.user,'thetext')
        add_post('#3post',None,self.user,'#4text')
        self.check_num_post(3)

    
    def test_update_post(self):
        self.check_num_post(1)
        g=get_post('testpost')
        g.title='realpost'
        g.save()
        self.check_post_title(1,'realpost')

    def test_post_body(self):
        self.check_post_body(1,'sometext')
        g=get_post('testpost')
        g.body='This is a course discussion post'
        g.save()
        self.check_post_body(1,'This is a course discussion post')
    
    def test_delete_post(self):
        delete_post('testpost')
        self.check_num_post(0)

    




    
        


    

    
    
        
    
    
    
    
        






# Create your tests here.
