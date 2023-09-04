from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name = 'home'),
    path('category/', include('blog.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)