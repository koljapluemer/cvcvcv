from django.db import models

# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.company

class ExperienceEnglish(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return f'{self.experience.company} - {self.position} (EN)'

class ExperienceGerman(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return f'{self.experience.company} - {self.position} (DE)'

class Education(models.Model):
    school = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)

    def __str__(self):
        return self.school
    
class EducationEnglish(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.education.school} - {self.degree} (EN)'

class EducationGerman(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.education.school} - {self.degree} (DE)'
    

class Project(models.Model):
    internal_tag = models.CharField(max_length=200)

    def __str__(self):
        return self.internal_tag
    
class ProjectEnglish(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return f'{self.project.internal_tag} (EN)'
    
class ProjectGerman(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return f'{self.project.internal_tag} (DE)'
    
class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class SkillEnglish(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.skill.name} (EN)'
    
class SkillGerman(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.skill.name} (DE)'

class Info(models.Model):
    internal_tag = models.CharField(max_length=200)

class InfoEnglish(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    key = models.CharField(max_length=200)
    value = models.TextField()
    alternative_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.info.internal_tag} (EN)'
    
class InfoGerman(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    key = models.CharField(max_length=200, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    alternative_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.info.internal_tag} (DE)'
    
    # if stuff doesn't exist on the german info, use the english info
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.info.english.key
        if not self.value:
            self.value = self.info.english.value
        super().save(*args, **kwargs)


class CoverLetter(models.Model):
    internal_tag = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f'{self.internal_tag}'
    
    
