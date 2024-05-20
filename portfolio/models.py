#from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

#class Project(models.Model):
#
#    user=models.ForeignKey(User,on_delete=models.CASCADE)
 #   title=models.CharField(max_length=200)
#    description=models.TextField()
#    link=models.URLField(blank=True,null=True)
#    date_created=models.DateField(auto_now_add=True)
#
#class WorkExperience(models.Model):
#
#    user=models.ForeignKey(User,on_delete=models.CASCADE)
#    company=models.CharField(max_length=200)
 #   role=models.CharField(max_length=200)
#    start_date=models.DateField()
 #   end_date=models.DateField(blank=True,null=True)
#    description=models.TextField()

#class Education(models.Model):
#
#    user=models.ForeignKey(User,on_delete=models.CASCADE)
#    institution=models.CharField(max_length=200)
 #   degree=models.CharField(max_length=200)
 #   start_date=models.DateField()
 #   end_date=models.DateField(blank=True,null=True)

#class Certification(models.Model):
#    user=models.ForeignKey(User,on_delete=models.CASCADE)
#    name=models.CharField(max_length=200)
#    institution=models.CharField(max_length=200)
#    date_obtained=models.DateField()


from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
