from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Experience URLs
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/create/', views.experience_create, name='experience_create'),
    path('experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    path('experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),
    
    # Education URLs
    path('education/', views.education_list, name='education_list'),
    path('education/create/', views.education_create, name='education_create'),
    path('education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),
    
    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Skill URLs
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Info URLs
    path('info/', views.info_list, name='info_list'),
    path('info/create/', views.info_create, name='info_create'),
    path('info/<int:pk>/edit/', views.info_edit, name='info_edit'),
    path('info/<int:pk>/delete/', views.info_delete, name='info_delete'),
    
    # CV Generation URLs
    path('cv/create/', views.cv_create, name='cv_create'),
    path('cv/generate/', views.cv_generate, name='cv_generate'),

    # Cover Letter URLs
    path('cover-letters/', views.cover_letter_list, name='cover_letter_list'),
    path('cover-letters/create/', views.cover_letter_create, name='cover_letter_create'),
    path('cover-letters/<int:pk>/edit/', views.cover_letter_edit, name='cover_letter_edit'),
    path('cover-letters/<int:pk>/delete/', views.cover_letter_delete, name='cover_letter_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
