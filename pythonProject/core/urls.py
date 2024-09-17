from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('video/', include('videos.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
