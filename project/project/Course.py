from .models import Course

def add_course(title,instructor,group):
    return Course.objects.create(title=title, instructor=instructor, group=group)

def get_course(title):
    return Course.objects.get(title=title)

def delete_course(title):
    return Course.objects.get(title=title).delete()



def list_course():
    return Course.objects.all()