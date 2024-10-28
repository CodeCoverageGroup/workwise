from django.urls import path
from .views import JobListView, JobDetailView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:id>/', JobDetailView.as_view(), name='job_detail'),
]