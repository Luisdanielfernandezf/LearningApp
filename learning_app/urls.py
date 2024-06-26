from django.contrib import admin
from django.urls import path
from quiz import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.subject_list, name='subject_list'),
    path('subject/<int:subject_id>/', views.question_list, name='question_list'),
    path('subject/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

