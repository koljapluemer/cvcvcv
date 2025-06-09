from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Experience, ExperienceEnglish, ExperienceGerman,
    Education, EducationEnglish, EducationGerman,
    Project, ProjectEnglish, ProjectGerman,
    Skill, SkillEnglish, SkillGerman,
    Info, InfoEnglish, InfoGerman,
    CoverLetter
)
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import os

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
            name=request.POST.get('name_en'),
            description_short=request.POST.get('description_short_en'),
            description_long=request.POST.get('description_long_en'),
        )
        
        # Create German version
        ProjectGerman.objects.create(
            project=project,
            name=request.POST.get('name_de'),
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
        english.name = request.POST.get('name_en')
        english.description_short = request.POST.get('description_short_en')
        english.description_long = request.POST.get('description_long_en')
        english.save()
        
        # Update German version
        german.name = request.POST.get('name_de')
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

# Info Views
def info_list(request):
    infos = Info.objects.all()
    return render(request, 'cv/info_list.html', {
        'infos': infos,
    })

def info_create(request):
    if request.method == 'POST':
        # Create base info
        info = Info.objects.create(
            internal_tag=request.POST.get('internal_tag'),
        )
        
        # Create English version
        InfoEnglish.objects.create(
            info=info,
            key=request.POST.get('key_en'),
            value=request.POST.get('value_en'),
            alternative_value=request.POST.get('alternative_value_en'),
        )
        
        # Create German version if provided
        if request.POST.get('key_de'):
            InfoGerman.objects.create(
                info=info,
                key=request.POST.get('key_de'),
                value=request.POST.get('value_de'),
                alternative_value=request.POST.get('alternative_value_de'),
            )
        
        messages.success(request, 'Info created successfully!')
        return redirect('info_list')
    
    return render(request, 'cv/info_form.html', {
        'action': 'Create',
    })

def info_edit(request, pk):
    info = get_object_or_404(Info, pk=pk)
    english = get_object_or_404(InfoEnglish, info=info)
    german = InfoGerman.objects.filter(info=info).first()
    
    if request.method == 'POST':
        # Update base info
        info.internal_tag = request.POST.get('internal_tag')
        info.save()
        
        # Update English version
        english.key = request.POST.get('key_en')
        english.value = request.POST.get('value_en')
        english.alternative_value = request.POST.get('alternative_value_en')
        english.save()
        
        # Update German version if it exists or create new one if provided
        if german:
            if request.POST.get('key_de'):
                german.key = request.POST.get('key_de')
                german.value = request.POST.get('value_de')
                german.alternative_value = request.POST.get('alternative_value_de')
                german.save()
            else:
                german.delete()
        elif request.POST.get('key_de'):
            InfoGerman.objects.create(
                info=info,
                key=request.POST.get('key_de'),
                value=request.POST.get('value_de'),
                alternative_value=request.POST.get('alternative_value_de'),
            )
        
        messages.success(request, 'Info updated successfully!')
        return redirect('info_list')
    
    return render(request, 'cv/info_form.html', {
        'action': 'Edit',
        'info': info,
        'english': english,
        'german': german,
    })

def info_delete(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        info.delete()
        messages.success(request, 'Info deleted successfully!')
        return redirect('info_list')
    return render(request, 'cv/info_confirm_delete.html', {
        'info': info,
    })

def cv_create(request):
    """Display the CV creation form with all items for individual selection"""
    # Get all items in both languages
    info_items = InfoEnglish.objects.all()
    education_items = EducationEnglish.objects.all()
    experience_items = ExperienceEnglish.objects.all()
    project_items = ProjectEnglish.objects.all()
    skill_items = SkillEnglish.objects.all()
    cover_letters = CoverLetter.objects.all()
    
    context = {
        'info_items': info_items,
        'education_items': education_items,
        'experience_items': experience_items,
        'project_items': project_items,
        'skill_items': skill_items,
        'cover_letters': cover_letters,
    }
    
    return render(request, 'cv/cv_form.html', context)

def cv_generate(request):
    """Generate CV based on form submission with individual item selections"""
    if request.method != 'POST':
        return redirect('cv_create')
    
    # Get language selection
    language = request.POST.get('language', 'en')
    
    # Get cover letter if selected
    cover_letter_id = request.POST.get('cover_letter')
    cover_letter = None
    if cover_letter_id:
        cover_letter = get_object_or_404(CoverLetter, id=cover_letter_id)
    
    # Get appropriate models based on language
    if language == 'en':
        info_model = InfoEnglish
        education_model = EducationEnglish
        experience_model = ExperienceEnglish
        project_model = ProjectEnglish
        skill_model = SkillEnglish
    else:
        info_model = InfoGerman
        education_model = EducationGerman
        experience_model = ExperienceGerman
        project_model = ProjectGerman
        skill_model = SkillGerman
    
    # Initialize context
    context = {
        'language': language,
        'cover_letter': cover_letter,
        'info_items': [],
        'education_items': [],
        'experience_items': [],
        'project_items': [],
        'skill_items': [],
        'section_titles': {
            'experience': 'Experience' if language == 'en' else 'Arbeitserfahrung',
            'education': 'Education' if language == 'en' else 'Akademisch',
            'projects': 'Projects' if language == 'en' else 'Projekte',
            'skills': 'Skills' if language == 'en' else 'Fähigkeiten',
        }
    }
    
    # Process info items
    for info in info_model.objects.all():
        include_type = request.POST.get(f'info_{info.id}')
        if include_type != 'none':
            # Get the corresponding English version if we're in German mode and the German version is missing
            if language == 'de' and not hasattr(info, 'value'):
                english_info = InfoEnglish.objects.get(info=info.info)
                item = {
                    'item': english_info,  # Use English version
                    'use_alternative': request.POST.get(f'info_alt_{info.id}') == 'on',
                    'is_short': False
                }
            else:
                item = {
                    'item': info,
                    'use_alternative': request.POST.get(f'info_alt_{info.id}') == 'on',
                    'is_short': False
                }
            context['info_items'].append(item)
    
    # Process education items
    education_items = []
    for education in education_model.objects.all():
        include_type = request.POST.get(f'education_{education.id}')
        if include_type != 'none':
            item = {
                'item': education,
                'is_short': include_type == 'short',
                'sort_date': education.education.end_date  # Add sort_date for sorting
            }
            education_items.append(item)
    # Sort education items by end_date in ascending order (oldest first)
    context['education_items'] = sorted(education_items, key=lambda x: x['sort_date'])
    
    # Process experience items
    experience_items = []
    for experience in experience_model.objects.all():
        include_type = request.POST.get(f'experience_{experience.id}')
        if include_type != 'none':
            item = {
                'item': experience,
                'is_short': include_type == 'short',
                'sort_date': experience.experience.start_date  # Add sort_date for sorting
            }
            experience_items.append(item)
    # Sort experience items by start_date in descending order (most recent first)
    context['experience_items'] = sorted(experience_items, key=lambda x: x['sort_date'], reverse=True)
    
    # Process project items
    if request.POST.get('include_projects') == 'on':
        for project in project_model.objects.all():
            include_type = request.POST.get(f'project_{project.id}')
            if include_type != 'none':
                item = {
                    'item': project,
                    'is_short': include_type == 'short'
                }
                context['project_items'].append(item)
    
    # Process skill items
    if request.POST.get('include_skills') == 'on':
        for skill in skill_model.objects.all():
            include_type = request.POST.get(f'skill_{skill.id}')
            if include_type != 'none':
                item = {
                    'item': skill,
                    'is_short': include_type == 'short'
                }
                context['skill_items'].append(item)
    
    # Render HTML template
    html_string = render_to_string('cv/cv_template.html', context)
    
    # Configure fonts
    font_config = FontConfiguration()
    
    # Generate PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf(font_config=font_config)
    
    # Create response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    
    return response

# Cover Letter Views
def cover_letter_list(request):
    cover_letters = CoverLetter.objects.all()
    return render(request, 'cv/cover_letter_list.html', {
        'cover_letters': cover_letters,
    })

def cover_letter_create(request):
    if request.method == 'POST':
        cover_letter = CoverLetter.objects.create(
            internal_tag=request.POST.get('internal_tag'),
            content=request.POST.get('content'),
        )
        messages.success(request, 'Cover letter created successfully!')
        return redirect('cover_letter_list')
    
    return render(request, 'cv/cover_letter_form.html', {
        'action': 'Create',
    })

def cover_letter_edit(request, pk):
    cover_letter = get_object_or_404(CoverLetter, pk=pk)
    
    if request.method == 'POST':
        cover_letter.internal_tag = request.POST.get('internal_tag')
        cover_letter.content = request.POST.get('content')
        cover_letter.save()
        messages.success(request, 'Cover letter updated successfully!')
        return redirect('cover_letter_list')
    
    return render(request, 'cv/cover_letter_form.html', {
        'action': 'Edit',
        'cover_letter': cover_letter,
    })

def cover_letter_delete(request, pk):
    cover_letter = get_object_or_404(CoverLetter, pk=pk)
    if request.method == 'POST':
        cover_letter.delete()
        messages.success(request, 'Cover letter deleted successfully!')
        return redirect('cover_letter_list')
    return render(request, 'cv/cover_letter_confirm_delete.html', {
        'cover_letter': cover_letter,
    })
