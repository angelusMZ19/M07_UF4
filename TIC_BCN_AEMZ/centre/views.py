from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm
# 
from django.template import Context, loader


studentList = [
        {
            'id': 1,
            'nom': 'Angelo Enrique',
            'surname1': 'Montenegro',
            'surname2': 'Zavala',
            'email': 'angelo@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 2,
            'nom': 'Oscar',
            'surname1': 'Perez',
            'surname2': 'Mengual',
            'email': 'oscar@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 3,
            'nom': 'Adria',
            'surname1': 'Garcia',
            'surname2': 'Perez',
            'email': 'adria@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 4,
            'nom': 'Gemma',
            'surname1': 'Garrigosa',
            'surname2': 'Frances',
            'email': 'gemma@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 5,
            'nom': 'Facundo Calixto',
            'surname1': 'Barrios',
            'surname2': '',
            'email': 'facundo@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 6,
            'nom': 'Neus',
            'surname1': 'Bravo',
            'surname2': 'Arias',
            'email': 'neus@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 7,
            'nom': 'Joana Jiayun',
            'surname1': 'Lin',
            'surname2': 'Chen',
            'email': 'joana@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 8,
            'nom': 'Veronica',
            'surname1': 'Cartagena',
            'surname2': 'Jaldin',
            'email': 'veronica@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 9,
            'nom': 'Oriana Saray',
            'surname1': 'Rojas',
            'surname2': 'Guedez',
            'email': 'oriana@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 10,
            'nom': 'Eric',
            'surname1': 'Sanchez',
            'surname2': 'Vazquez',
            'email': 'eric@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 11,
            'nom': 'Junhong',
            'surname1': 'Zhu',
            'surname2': 'Zhang',
            'email': 'junhong@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 12,
            'nom': 'Alexander',
            'surname1': 'Andreev',
            'surname2': 'Apukhtina',
            'email': 'alexander@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 13,
            'nom': 'Jesus',
            'surname1': 'Pujada',
            'surname2': 'Montoya',
            'email': 'oriana@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 14,
            'nom': 'Anxo',
            'surname1': 'Aragundi',
            'surname2': 'Mesias',
            'email': 'anxo@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 15,
            'nom': 'Carlos Andres',
            'surname1': 'Zambrano',
            'surname2': 'Aray',
            'email': 'andres@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 16,
            'nom': 'Joel',
            'surname1': 'Ghanem',
            'surname2': 'Gomez',
            'email': 'joel@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 17,
            'nom': 'Angel',
            'surname1': 'Ivanov',
            'surname2': 'Spasov',
            'email': 'angel@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
        ,
        {
            'id': 18,
            'nom': 'Dinar',
            'surname1': 'Khazimullin',
            'surname2': '',
            'email': 'dinar@iticbcn.cat',
            'course': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
    ]

professorList = [
        {
            'id': 1,
            'nom': 'Roger',
            'surname1': 'Sobrino',
            'surname2': 'Gil',
            'email': 'roger@iticbcn.cat',
            'course': 'DAM2B',
            'tutor': False,
            'moduls': 'M07'
        },
        {
            'id': 2,
            'nom': 'Juanma',
            'surname1': 'Sanchez',
            'surname2': 'Bel',
            'email': 'juanma@iticbcn.cat',
            'course': 'DAW2A',
            'tutor': True,
            'moduls': 'M06'
        },
        {
            'id': 3,
            'nom': 'Xavi',
            'surname1': 'Quesada',
            'surname2': 'Puertas',
            'email': 'xavi@iticbcn.cat',
            'course': 'ASIX2A',
            'tutor': False,
            'moduls': 'M08, MAH'
        },
        {
            'id': 4,
            'nom': 'Oriol',
            'surname1': 'Roca',
            'surname2': 'Fabra',
            'email': 'oriol@iticbcn.cat',
            'course': 'DAW2B',
            'tutor': False,
            'moduls': 'M09'
        }
    ]
def index(request):
    template=loader.get_template('index_centre.html')
    return HttpResponse(template.render())
# funcion student
def students(request):
    return render(request, 'student.html', {'estudiante': studentList})

# funcion professor
def professor(request):
    return render(request, 'professor.html', {'teacher': professorList})

# funcion de +info professor
def infoProfessor(request, pk):
    profe = None
    for i in professorList:
        if i['id'] == pk:
            profe = i
    return render(request, 'info_prof.html', {'professor':profe}) 

# funcion de +info students
def infoStudents(request, pk):
    estudiante = None
    for i in studentList:
        if i['id'] == pk:
            estudiante = i
    return render(request, 'info_student.html', {'student':estudiante})


# funcion para formulario
def form_user(request):
    form= PersonForm()
    context={'form': form}
    return render(request, 'form.html', context)
