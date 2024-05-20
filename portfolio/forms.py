#from django import forms
#from . models import Project,WorkExperience,Education,Certification
#
#class ProjectForm(forms.ModelForm):
#
#    class Meta:
#        model= Project
#        fields=['title','description','link']

#class WorkExperienceForm(forms.ModelForm):

#    class Meta:
 #       model=WorkExperience
 #       fields=['company','role','start_date','end_date','description']

#class EducationForm(forms.ModelForm):
#
 #   class Meta:
 #       model=Education
 #       fields=['institution','degree','start_date','end_date']

#class CertificationForm(forms.ModelForm):
#
#    class Meta:
 #       model=Certification
 #       fields=['name','institution','date_obtained']

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

