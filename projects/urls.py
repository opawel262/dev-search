from django.urls import path
from . import views


app_name = 'projects'


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<uuid:pk>/', views.single_project, name='single_project'),
    path('create/', views.create_project, name='create_project'),
    path('update/<uuid:pk>/', views.update_project, name='update_project'),
    path('delete/<uuid:pk>/', views.delete_project, name='delete_project')
]
