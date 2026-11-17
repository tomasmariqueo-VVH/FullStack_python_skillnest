# 🧮 4)%-formatting
# Quizás en algún código te puedas topar con un método que se utilizaba antes de que existiera 
# las formas vistas antes de interpolación. En lugar de utilizar llaves, se utiliza el símbolo % 
# para indicar un parámetro; %s para indicar una cadena y %d para indicar un número. 
# Una vez establecida la cadena, se coloca de nuevo % para separar el texto de las variables que serán 
# interpoladas. 
# Por ejemplo:

nombre5 = input("Ingrese su nombre: ")
edad3 = 29
print("Mi nombre es %s y tengo %d años de edad." % (nombre5, edad3))
# #Imprime: Mi nombre es Marcelo y tengo 29 años de edad.