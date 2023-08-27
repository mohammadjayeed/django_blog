from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

STATUS = [('Draft','Draft'),
        ('Published','Published'),]

class Blog(models.Model):
    
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=200, blank=True, null=True)
    blog_body = models.CharField(max_length=2000)
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title