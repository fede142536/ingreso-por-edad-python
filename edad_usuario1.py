#-------------------------
#Problematica: 
#            El usuario quiere saber si puede entrar a una discoteca segun la edad del cliente
#-------------------------

#-------------------------
#Algoritmo:
#            1. Solicitar al usuario la edad del cliente
#            2. Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca
#            3. Mostrar al usuario puede o no ingresar a la discoteca
#-------------------------

#-------------------------
#Pseudocodigo:
#            Inicio
#                1. Solicitar al usuario la edad del cliente
#                mostrar un mensaje: "Por favor, ingrese su edad"
edad = int(input("Por favor, ingrese su edad"))
#                Leer el dato ingresado y asignarle la variable edad
#                2. Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca
#                Si edad es >= 18 entonces:
if edad >= 18:
    print("Puedes ingresar a la discoteca")
else:
    print("No puedes ingresar a la discoteca por ser menor de edad")
#                    Asignarle a la variable permitido que sea verdadero
#                si edad < 18 entonces:
#                    Asignarle a la variable permitido que sea falso
#                FIN SI
#                3. Mostrar al usuario se su cliente puede ingresar a la discoteca.
#                si permitido es verdadero:
#                    mostrar mensaje: "Puedes ingresar a la discoteca"
#                si permitido es falso:    
#                    mostrar mensaje: "Lo sentimos, no puedes ingresar a la discoteca"
#                FIN SI
#            Fin del programa        