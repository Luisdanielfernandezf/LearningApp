from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.subject_list, name='subject_list'),
    path('subject/<int:subject_id>/', views.question_list, name='question_list'),
]
