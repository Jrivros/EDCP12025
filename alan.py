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
