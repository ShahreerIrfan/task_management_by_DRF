from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
