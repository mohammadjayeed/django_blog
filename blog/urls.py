from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
   
    path('<int:category_id>/', views.posts_by_category, name='post-by-category')
]
