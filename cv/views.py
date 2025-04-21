from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Experience, ExperienceEnglish, ExperienceGerman,
    Education, EducationEnglish, EducationGerman,
    Project, ProjectEnglish, ProjectGerman,
    Skill, SkillEnglish, SkillGerman
)

def dashboard(request):
    """Main dashboard view showing overview of all sections"""
    experiences = Experience.objects.all()
    return render(request, 'cv/dashboard.html', {
        'experiences': experiences,
    })

# Experience Views
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'cv/experience_list.html', {
        'experiences': experiences,
    })

def experience_create(request):
    if request.method == 'POST':
        # Create base experience
        experience = Experience.objects.create(
            company=request.POST.get('company'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
        )
        
        # Create English version
        ExperienceEnglish.objects.create(
            experience=experience,
            position=request.POST.get('position_en'),
            description_short=request.POST.get('description_short_en'),
            description_long=request.POST.get('description_long_en'),
        )
        
        # Create German version
        ExperienceGerman.objects.create(
            experience=experience,
            position=request.POST.get('position_de'),
            description_short=request.POST.get('description_short_de'),
            description_long=request.POST.get('description_long_de'),
        )
        
        messages.success(request, 'Experience created successfully!')
        return redirect('experience_list')
    
    return render(request, 'cv/experience_form.html', {
        'action': 'Create',
    })

def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    english = get_object_or_404(ExperienceEnglish, experience=experience)
    german = get_object_or_404(ExperienceGerman, experience=experience)
    
    if request.method == 'POST':
        # Update base experience
        experience.company = request.POST.get('company')
        experience.start_date = request.POST.get('start_date')
        experience.end_date = request.POST.get('end_date')
        experience.save()
        
        # Update English version
        english.position = request.POST.get('position_en')
        english.description_short = request.POST.get('description_short_en')
        english.description_long = request.POST.get('description_long_en')
        english.save()
        
        # Update German version
        german.position = request.POST.get('position_de')
        german.description_short = request.POST.get('description_short_de')
        german.description_long = request.POST.get('description_long_de')
        german.save()
        
        messages.success(request, 'Experience updated successfully!')
        return redirect('experience_list')
    
    return render(request, 'cv/experience_form.html', {
        'action': 'Edit',
        'experience': experience,
        'english': english,
        'german': german,
    })

def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience deleted successfully!')
        return redirect('experience_list')
    return render(request, 'cv/experience_confirm_delete.html', {
        'experience': experience,
    })

# Education Views
def education_list(request):
    educations = Education.objects.all()
    return render(request, 'cv/education_list.html', {
        'educations': educations,
    })

def education_create(request):
    if request.method == 'POST':
        # Create base education
        education = Education.objects.create(
            school=request.POST.get('school'),
            end_date=request.POST.get('end_date'),
            degree=request.POST.get('degree'),
            grade=request.POST.get('grade'),
        )
        
        # Create English version
        EducationEnglish.objects.create(
            education=education,
            description=request.POST.get('description_en'),
        )
        
        # Create German version
        EducationGerman.objects.create(
            education=education,
            description=request.POST.get('description_de'),
        )
        
        messages.success(request, 'Education created successfully!')
        return redirect('education_list')
    
    return render(request, 'cv/education_form.html', {
        'action': 'Create',
    })

def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    english = get_object_or_404(EducationEnglish, education=education)
    german = get_object_or_404(EducationGerman, education=education)
    
    if request.method == 'POST':
        # Update base education
        education.school = request.POST.get('school')
        education.end_date = request.POST.get('end_date')
        education.degree = request.POST.get('degree')
        education.grade = request.POST.get('grade')
        education.save()
        
        # Update English version
        english.description = request.POST.get('description_en')
        english.save()
        
        # Update German version
        german.description = request.POST.get('description_de')
        german.save()
        
        messages.success(request, 'Education updated successfully!')
        return redirect('education_list')
    
    return render(request, 'cv/education_form.html', {
        'action': 'Edit',
        'education': education,
        'english': english,
        'german': german,
    })

def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education deleted successfully!')
        return redirect('education_list')
    return render(request, 'cv/education_confirm_delete.html', {
        'education': education,
    })

# Project Views
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'cv/project_list.html', {
        'projects': projects,
    })

def project_create(request):
    if request.method == 'POST':
        # Create base project
        project = Project.objects.create(
            internal_tag=request.POST.get('internal_tag'),
        )
        
        # Create English version
        ProjectEnglish.objects.create(
            project=project,
            description_short=request.POST.get('description_short_en'),
            description_long=request.POST.get('description_long_en'),
        )
        
        # Create German version
        ProjectGerman.objects.create(
            project=project,
            description_short=request.POST.get('description_short_de'),
            description_long=request.POST.get('description_long_de'),
        )
        
        messages.success(request, 'Project created successfully!')
        return redirect('project_list')
    
    return render(request, 'cv/project_form.html', {
        'action': 'Create',
    })

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    english = get_object_or_404(ProjectEnglish, project=project)
    german = get_object_or_404(ProjectGerman, project=project)
    
    if request.method == 'POST':
        # Update base project
        project.internal_tag = request.POST.get('internal_tag')
        project.save()
        
        # Update English version
        english.description_short = request.POST.get('description_short_en')
        english.description_long = request.POST.get('description_long_en')
        english.save()
        
        # Update German version
        german.description_short = request.POST.get('description_short_de')
        german.description_long = request.POST.get('description_long_de')
        german.save()
        
        messages.success(request, 'Project updated successfully!')
        return redirect('project_list')
    
    return render(request, 'cv/project_form.html', {
        'action': 'Edit',
        'project': project,
        'english': english,
        'german': german,
    })

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    return render(request, 'cv/project_confirm_delete.html', {
        'project': project,
    })

# Skill Views
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'cv/skill_list.html', {
        'skills': skills,
    })

def skill_create(request):
    if request.method == 'POST':
        # Create base skill
        skill = Skill.objects.create(
            name=request.POST.get('name'),
        )
        
        # Create English version
        SkillEnglish.objects.create(
            skill=skill,
            description=request.POST.get('description_en'),
        )
        
        # Create German version
        SkillGerman.objects.create(
            skill=skill,
            description=request.POST.get('description_de'),
        )
        
        messages.success(request, 'Skill created successfully!')
        return redirect('skill_list')
    
    return render(request, 'cv/skill_form.html', {
        'action': 'Create',
    })

def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    english = get_object_or_404(SkillEnglish, skill=skill)
    german = get_object_or_404(SkillGerman, skill=skill)
    
    if request.method == 'POST':
        # Update base skill
        skill.name = request.POST.get('name')
        skill.save()
        
        # Update English version
        english.description = request.POST.get('description_en')
        english.save()
        
        # Update German version
        german.description = request.POST.get('description_de')
        german.save()
        
        messages.success(request, 'Skill updated successfully!')
        return redirect('skill_list')
    
    return render(request, 'cv/skill_form.html', {
        'action': 'Edit',
        'skill': skill,
        'english': english,
        'german': german,
    })

def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skill_list')
    return render(request, 'cv/skill_confirm_delete.html', {
        'skill': skill,
    })
