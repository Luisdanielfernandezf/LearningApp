# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('subject/<int:subject_id>/', views.question_list, name='question_list'),
    path('subject/<int:subject_id>/theory/', views.theory_list, name='theory_list'),
    path('theory/<int:theory_id>/', views.theory_detail, name='theory_detail'),
]
