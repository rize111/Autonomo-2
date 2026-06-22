cantidad_estudiantes= int(input("ingrese la cantidad de estudiantes:"))
suma_notas=0
aprobadas=0
reprobadas=0

for estudiantes in range (1,cantidad_estudiantes+1):
    nota=float(input("Ingrese la nota del estudiante:"))
    suma_notas+=nota
    if nota>7:
        aprobadas +=1
    else:
        reprobadas +=1

promedio=suma_notas/cantidad_estudiantes
print("Promedio General:",promedio)
print("Estudiantes Aprobados:",aprobadas)
print("Estudiantes reprobados:",reprobadas)

