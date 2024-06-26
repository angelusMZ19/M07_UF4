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
    path('formP/', views.form_professor , name='form_P'),
    path('formS/', views.form_student, name='form_S'),
    # rutas update para ambas listas
    path('updateP/<int:pk>', views.updateProfessor, name='updateP'),
    path('updateS/<int:pk>', views.updateStudent, name='updateS'),

    path('deleteP/<int:pk>', views.deleteProfessor, name='deleteP'),
    path('deleteS/<int:pk>', views.deleteStudent, name='deleteS')


]