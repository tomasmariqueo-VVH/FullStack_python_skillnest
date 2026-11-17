# 🔢 Números 
# Existen 3 tipos de números básicos en Python:

# int: números enteros, positivos o negativos. Por ejemplo: 156
# float: números con punto flotante o decimales, positivos o negativos. Por ejemplo: 3.1416
# Complejos: pertenecen al conjunto de números reales y son comúnmente identificados con la letra J. 
# Por ejemplo: 2+5j. Si no estás seguro de necesitar este tipo de número, puedes ignorarlos por ahora.

# 🧪 1)Type
# Como lo vimos en el capítulo anterior, 
# si no estás seguro del tipo de un número podemos usar type para verificarlo.

print(type(1.1)) #Imprime: <class 'float'>
print(type(615)) #Imprime: <class 'int'>
print(type(2j)) #Imprime: <class 'complex'>


# 🔄 2)Conversión
# Todos los objetos en Python tienen métodos que podemos utilizar para convertir de un tipo de número a otro.

entero_a_decimal = float(123)
decimal_a_entero = int(22.5)
entero_a_complejo = complex(35)
print(entero_a_decimal) #Imprime: 123.0
print(decimal_a_entero) #Imprime: 22
print(entero_a_complejo) #Imprime: (35+0j)


# 🎲 3)Número aleatorio
# Para generar un número aleatorio importamos la librería random. 
# Puedes ver la documentación oficial de la librería aquí.

import random
num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
print(num_aleatorio) #Imprime el número aleatorio generado

# TAREA
# Generar variables con input, ingresar 2 números, transformarlos a decimal, 
# sumarlos, promediarlos y mostrar el resultado en pantalla.

valor1 = input('Ingrese el primer valor: ')
valor2 = input('Ingrese el segundo valor: ')
decimal1 = float(valor1)
decimal2 = float(valor2)
suma = decimal1 + decimal2
promedio = int(suma)
print(f'Resultado final: {promedio}')