
#from django.urls import path
#from . import views

#urlpatterns=[
#    path('',views.customize_portfolio,name='customize_portfolio'),
# urls.py

#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.portfolio, name='portfolio'),
#    path('add_project/', views.add_project, name='add_project'),
#    path('add_work_experience/', views.add_work_experience, name='add_work_experience'),
#    path('add_education/', views.add_education, name='add_education'),
#    path('add_certification/', views.add_certification, name='add_certification'),
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]

