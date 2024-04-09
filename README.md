# M07_UF4
## View Templates 

* parte_1:

```java
    Renderizacion Estudiantes parte 1:
```
![students_table](./img/student1.png)
![students_Url](./img/studentURL.png)


```java
    Renderizacion Profesores parte 1:
```

![students_table](./img/professor1.png)
![students_Url](./img/professorURL.png)


* parte_2:

<video width="320" height="240" controls>
  <source src="./img/ejecucionParte2.mp4" type="video/mp4">
</video>


[enlace_video_por_si_no_funciona_](https://drive.google.com/file/d/1gonG844Nb09yqamL8pfdfiT97wvPjzZz/view?usp=sharing)




# MODEL (PRACTICA 2)

se usa el comando par
```java
  python manage.py makemigrations
```
para preparar la migracion como se ve a continuacion:
![students_table](./img/makeMigration.png)

y para realizar la migracion a plenitud se ejecuta el comando:
```java
  python manage.py migrate
```
![students_Url](./img/migrate.png)


* En el sigueinte enlace al video se podra observar como se generan las migraciones en una base de datos que se encuentra vacia:

[video_migracion](https://drive.google.com/file/d/1s32ln-H2QW4rcMpI7q6KeZbPbzFE1wUO/view?usp=sharing)


# FORM (PRACTICA 3)

Evidencia CON uso de ('as_p'):
```java
<form action="" method="POST">
    {%csrf_token%}
    {{ form.as_p }}
    <input type="submit">
</form>
{% endblock %}
```
![con('as_p')](./img/formCON.png)

Evidencia SIN uso de ('as_p'):
```java
<form action="" method="POST">
    {%csrf_token%}
    {{ form }}
    <input type="submit">
</form>
{% endblock %}
```
![sin('as_p')](./img/formSIN.png)

# CRUD (PRACTICA 4)

[video_demostracion_CRUD](https://drive.google.com/file/d/1v_oeY5NRXb4MLCmcvxRBdW0e197lyhX4/view?usp=sharing)

Evidencias(Estudiante):

* Create Student:

![Create_Student](./img/createS.png)

* Update Student:

![Update_Student](./img/editS.png)

* Delete Student:

![Delete_Student](./img/deleteS.png)

* Read despues del Delete Student:

![Read_DeleteS](./img/despuesDeleteS.png)



Evidencias(Professor):

* Create Professor:

![Create_Professor](./img/createP.png)

* Update Professor:

![Update_Professor](./img/editP.png)

* Delete Professor:

![Delete_Professor](./img/deleteP.png)

* Read despues del Delete Professor:

![Read_DeleteP](./img/despuesDeleteP.png)