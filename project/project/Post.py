from .models import Post

def add_post(title,course,author,body):
        return Post.objects.create(title=title, course=course, author=author, body=body)

def list_post(author=None):
    if author:
        return Post.objects.filter(author=author)
    
    else:
        return Post.objects.all()

def get_post(title):
    return Post.objects.get(title=title)

def get_post_author(author):
    return Post.objects.get(author=author)

def get_post_id(pk):
    return Post.objects.get(pk=pk)

def delete_post(title):
    Post.objects.get(title=title).delete()