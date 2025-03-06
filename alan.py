calificaciones =[]
for i in range (5):
  c = float(input(f'Registre las notas del alumno (entre 0 y 10): '))
  while c < 0 or c >10:
    print(f'La nota no es válida')
    c = float(input(f'Ingrese una nota (entre 0 y 10): '))
  calificaciones.append(c)    
print(f'Las notas son: {calificaciones}')
print(f'La nota máxima es: {max(calificaciones)}')
print(f'La nota mínima es: {min(calificaciones)}')
print(f'El promedio de las notas es: {sum(calificaciones)/len(calificaciones)}')

#Registro de notas de toda la clase

clase = {}
est=int(input('Ingrese el número de estudiantes de la clase: '))
for x in range(est):
  nombre=input('Ingrese el nombre del estudiante: ')
  clase.update({nombre:[]})
  n = int(input(f'Ingrese el número de notas de {nombre}: '))
  for y in range(n):
    nota = float(input(f'Ingrese la nota {y+1}: '))
    while nota < 0 or nota > 10:
      print(f'La nota no es válida')
      nota = float(input(f'Ingrese una nota (entre 0 y 10): '))
    clase[nombre].append(nota)
    promedio = sum(clase[nombre])/len(clase[nombre])
  print(f'Las notas de {nombre} son: {clase[nombre]}')
  print(f'El promedio de {nombre} es: {promedio}')
