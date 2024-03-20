from django.urls import path
from . import  views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('students', views.students, name= 'students'),
    path('professor', views.professor, name= 'professor'),

    #path para la parte de +info, para ello se pasara el pk correspondiente al id
    path('students/plusStudent/<int:pk>', views.infoStudents, name= 'plus_students'),
    path('professor/plusProfessor/<int:pk>', views.infoProfessor, name= 'plus_professor'),
    # se crea ruta de formulario 
    path('form/', views.form_user , name='formUser')
]