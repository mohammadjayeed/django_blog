from django.shortcuts import render
from .models import Category, Blog
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    categories = Category.objects.all()
    blog = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    blog_normal = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    
    return render(request,'home-blogs.html',{'categories': categories, 'blogs':blog, 'blog_posts':blog_normal})

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category = category_id)


    context = {'posts':posts}

    return render(request, 'blog/posts_by_category.html', context)


