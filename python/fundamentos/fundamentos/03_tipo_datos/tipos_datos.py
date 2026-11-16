#🔹 Tipos de datos primitivos
#Estos son los elementos básicos de un lenguaje. La mayoría de los lenguajes comparten estos en común.

#🔘 Booleanos: Se utiliza para representar valores de verdad en la lógica. Solamente puede tener dos valores: 
#True o False (Nota que ponemos la T y la F en mayúsculas).
mayor_edad = True
tiene_bigote = False

#🔢 Números: Aquí podemos tener números enteros, de punto flotante 
#(también conocidos como números decimales) o complejos.
mayoria_edad = 18
altura = 1.72

#🔤 Strings: También conocidas como cadenas, se refiere a textos o cadenas de caracteres.
frase = "Anita lava la tina"

#🧩 Tipos de datos compuestos
#Estas con colecciones compuestas de los datos primitivos vistos anteriormente.


#📋 1)Listas: Tipo de datos mutable (que puede cambiar) y contiene un conjunto de distintos valores. 
#Suele utilizarse para almacenar información relacionada.

lista_vacia = [] #[] Arreglo o lista (Array)

gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) #Imprime: Hello Kitty
gatos[1] = "Tom" #Modifica el valor 1

gatos.append("Felix") #Agrega un nuevo val0r al final de la lista con Append
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']

gatos.pop() #Borra el ultimo elemento de la lista
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']

gatos.pop(1) #Borra un elemento en específico de la lista
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']


# 2)Matrices o Arreglos multidemensiónales: Son lostas que contienen otras listas

Ejemplo_matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(Ejemplo_matriz[1][2]) #Imprime: 6
print(Ejemplo_matriz[2][2]) #Imprime: 9

#Tarea
#Crear una variable de 4x4 y mostrar el número 16 en la terminal.

Tarea = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(Tarea[3][3])


#🔒 2)Tuplas: Tipo de datos inmutable (que no se puede modificar) y contiene un conjunto de distintos valores. 
#Pueden contener distintos tipos de datos.
#() Las Paréntesis se usan para Tuplas
#Ejemplo: ("Lunes", "martes")

perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
perro[2] = "comida de perro" 
#ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)


#🗂️ 3)Diccionarios: Nos permite almacenar contenido a través de una llave y un valor. 
#Podemos acceder a sus datos a través de su índice único (que en este caso llamaremos llave o clave). 
#Encuentra algunos métodos integrados de los diccionarios aquí.


diccionario_vacio = {}
persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente
print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': 
# ['jugar videojuegos', 'programación']}
altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
print(altura)    # Imprime: 1.71
print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 
#⚙️ Funciones comunes
#En caso de no conocer el tipo de dato de una variable o valor, 
#gracias a la función type podemos saberlo fácilmente. Por ejemplo:
print(type(3.1416)) #Imprime: <class 'float'>
print(type(persona)) #Imprime <class 'dict'>

#En tipos de datos que tienen tamaño (por ejemplo: listas, tuplas, diccionarios, cadenas), 
#podemos usar la función len, que es diminutivo de length (tamaño en español) y 
#que nos regresa la longitud de este.
print(len(persona)) #Imprime: 4 (la cantidad de pares de clave-valor)
print(len("Me encanta programar")) #Imprime: 20