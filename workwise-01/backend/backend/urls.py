# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the homepage!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # Example inclusion of another app's URLs
    path('api/', include('departments.urls')),
    path('api/', include('machines.urls')),
     path('api/', include('notifications.urls')),
    path('', home_view),
    path('jobs/', include('jobs.urls')), # Example inclusion of another app's
]