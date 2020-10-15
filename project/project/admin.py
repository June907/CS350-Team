from django.contrib import admin
from .models import Course,Assignment,Submission,Post


admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Post)