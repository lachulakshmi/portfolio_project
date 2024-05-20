#from django.shortcuts import render,redirect
#from django.contrib.auth.decorators import login_required
#from . forms import ProjectForm, WorkExperienceForm, EducationForm, CertificationForm
#from . models import Project,WorkExperience,Education,Certification

# Create your views here.

#@login_required
#def customize_portfolio(request):

 #   if request.method=='POST':

#        project_form=ProjectForm(request.POST,prefix='project')
#        work_form=WorkExperienceForm(request.POST,prefix='work')
#        education_form=EducationForm(request.POST,prefix='education')
#        cert_form=CertificationForm(request.POST,prefix='cert')

 #       if project_form.is_valid():
 #           project= project_form.save(commit=False)
#            project.user=request.user
#            project.save()

 #       if work_form.is_valid():
#            work=work_form.save(commit=False)
#            work.user=request.user
#            work.save()

 #       if cert_form.is_valid():
#            cert=cert_form.save(commit=False)
#            cert.user=request.user
#            cert.save()
#
#        return redirect('customize_portfolio')
#    else:
 #       project_form=ProjectForm(prefix='project')
#        work_form=WorkExperienceForm(prefix='work')
#        education_form=EducationForm(prefix='education')
#        cert_form=CertificationForm(prefix='cert')
#
 #       return render(request,'portfolio',{
#            'project_form': project_form,
#            'work_form':work_form,
#            'education_form':education_form,
 #           'cert_form':cert_form,

 #       })
# views.py

#from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from .models import Project, WorkExperience, Education, Certification
#from .forms import ProjectForm, WorkExperienceForm, EducationForm, CertificationForm


#@login_required
#def portfolio(request):
 #   project_showcase = Project.objects.filter(user=request.user)
#    work_experiences = WorkExperience.objects.filter(user=request.user)
 #   educations = Education.objects.filter(user=request.user)
#    certifications = Certification.objects.filter(user=request.user)

#    context = {
 #       'project_showcase': project_showcase,
#        'work_experiences': work_experiences,
#        'educations': educations,
 #       'certifications': certifications,
 #   }

#    return render(request, 'portfolio.html', context)


#@login_required
#def add_project(request):
 #   if request.method == 'POST':
 #       form = ProjectForm(request.POST)
 #       if form.is_valid():
#            project = form.save(commit=False)
#            project.user = request.user
#            project.save()
#            return redirect('portfolio')
#    else:
#        form = ProjectForm()

#    return render(request, 'edit_project.html', {'form': form})


#@login_required
#def add_work_experience(request):
#    if request.method == 'POST':
 #       form = WorkExperienceForm(request.POST)
 #       if form.is_valid():
 #           work_experience = form.save(commit=False)
 #           work_experience.user = request.user
 #           work_experience.save()
 #           return redirect('portfolio')
 #   else:
#        form = WorkExperienceForm()

#    return render(request, 'edit_work_experience.html', {'form': form})


#@login_required
#def add_education(request):
 #   if request.method == 'POST':
 #       form = EducationForm(request.POST)
#        if form.is_valid():
 #           education = form.save(commit=False)
 #           education.user = request.user
 #           education.save()
 #           return redirect('portfolio')
#    else:
 #       form = EducationForm()
#
#    return render(request, 'edit_education.html', {'form': form})


#@login_required
#def add_certification(request):
#    if request.method == 'POST':
#        form = CertificationForm(request.POST)
#        if form.is_valid():
 #           certification = form.save(commit=False)
#            certification.user = request.user
 #           certification.save()
 #           return redirect('portfolio')
 #   else:
 #       form = CertificationForm()
#
#    return render(request, 'edit_certification.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_showcase/project_list.html', {'project_showcase': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_showcase/project_detail.html', {'project': project})














