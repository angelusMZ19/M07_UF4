from django.forms import ModelForm
from .models import Student, Professor

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields='__all__'

        
class ProfessorForm(ModelForm):
    class Meta:
        model= Professor
        fields='__all__'
