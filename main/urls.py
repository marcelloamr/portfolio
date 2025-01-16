from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),  # Home route
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
]
