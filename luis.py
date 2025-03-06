for i in lista1:
    print(f"{i} elevado al cuadrado es {i**2} y elevado al cubo es {i**3}")

# Crea dos listas vacías para almacenar textos.
lista = []
lista2 = []

# Solicita al usuario que ingrese 5 textos y los agrega a la lista 'lista'.
for z in range(0, 5):
    texto = str(input("Ingresa un texto "))
    lista.append(texto)

# Copia los elementos de 'lista' a 'lista2' y luego invierte el orden de 'lista2'.
lista2.extend(lista)
lista2.reverse()

# Imprime la lista original y la lista invertida.
print(lista)
print(lista2)

# Solicita al usuario que ingrese 5 notas, validando que estén en el rango de 0 a 10.
nota1 = int(input("ingresa la primer nota "))
while nota1 > 10:
    print("Nota no valida")
    nota1 = int(input("ingresa la primer nota "))
while True:
    if nota1 <= 10:
        break

nota2 = int(input("ingresa la segunda nota "))
while nota2 > 10:
    print("Nota no valida")
    nota2 = int(input("ingresa la segunda nota "))
while True:
    if nota2 <= 10:
        break

nota3 = int(input("ingresa la tercer nota "))
while nota3 > 10:
    print("Nota no valida")
    nota3 = int(input("ingresa la tercer nota "))
while True:
    if nota3 <= 10:
        break

nota4 = int(input("ingresa la cuarta nota "))
while nota4 > 10:
    print("Nota no valida")
    nota4 = int(input("ingresa la cuarta nota "))
while True:
    if nota4 <= 10:
        break

nota5 = int(input("ingresa la quinta nota "))
while nota5 > 10:
    print("Nota no valida")
    nota5 = int(input("ingresa la quinta nota "))
while True:
    if nota5 <= 10:
        break

# Almacena las 5 notas en una tupla llamada 'notas'.
notas = (nota1, nota2, nota3, nota4, nota5)

# Imprime las notas ingresadas.
print(f"Las notas son las siguientes {nota1}, {nota2}, {nota3}, {nota4}, {nota5}")

# Calcula y muestra la nota máxima, la nota mínima y el promedio de las notas.
print(f"La nota maxima es {max(notas)}, la nota minima es {min(notas)}, la media es {sum(notas)/5}")

# Crea un diccionario vacío para almacenar los nombres y calificaciones de los alumnos.
alumnos = {}

# Solicita al usuario que ingrese la cantidad de alumnos que desea registrar.
no_alumnos = int(input("Cantidad de alumnos que va a ingresar "))

# Itera sobre el número de alumnos para registrar sus nombres y calificaciones.
for x in range(no_alumnos):
    # Solicita el nombre del alumno y valida que no esté repetido.
    Nombres = str(input("Ingresa el nombre del alumno "))
    while Nombres in alumnos:
        print("Alumno no valido")
        Nombres = str(input("Ingresa el nombre del alumno "))

    # Crea una lista vacía para almacenar las calificaciones del alumno.
    calificaciones = []

    # Permite al usuario ingresar múltiples calificaciones hasta que ingrese un número negativo.
    while True:
        nota = int(input(f"Ingresa la calificación de {Nombres} "))
        if nota < 0:
            break
        else:
            calificaciones.append(nota)

    # Almacena el nombre del alumno y sus calificaciones en el diccionario 'alumnos'.
    alumnos[Nombres] = calificaciones

# Imprime el diccionario con los nombres y calificaciones de los alumnos.
print(alumnos)

# Crea una tupla con los nombres de los meses del año.
año = ("enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# Bucle infinito para que el usuario ingrese números y obtenga el mes correspondiente.
while True:
    numero = int(input("Ingresa un Numero del 1 al 12 "))
    if numero >= 1 and numero <= 12:
        # Muestra el mes correspondiente al número ingresado.
        print(f"{año[numero-1]}")
    elif numero == 0:
        # Si el usuario ingresa 0, el programa se apaga.
        print("Programa apagado")
        break
    else:
        # Si el número está fuera del rango, muestra un mensaje de error.
        print("error número alto")
