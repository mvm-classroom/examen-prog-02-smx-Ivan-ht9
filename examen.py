#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random

def obtenir_nom():
    # Llista de noms incorrectes
    noms = "Ivan"

    # Llista de cognoms incorrectes
    cognoms = "Herrera"
    
    noms = random.choice ([noms]) #Sirve para crear un nombre aleatorio gracias a la funcion random.choice.
    cognoms = random.choice ([cognoms])  #Sirve para crear un nombre aleatorio gracias a la funcion random.choice.
    nom_aleatori_complet = noms + cognoms #Creamos el nombre completo sumando los dos valores
    return (nom_aleatori_complet) #Devolvemos el nombre completo random

    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista): #ESTA HECHO
    nom_aleatori = obtenir_nom () #Cogemos el nombre aleatoria de la funcion obtenir nom ()
    llista = [] #Creamos una lista vacia
    llista.append(nom_aleatori) #Añadimos el nombre aleatoria a la lista
    return llista #Devolvemos la lista
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom

def llistar_noms(llista): #ESTA HECHO
    for nombre in llista: # Cogemos cada nombre que este dentro de la lista
        print (nombre) # Dibujamos elnombtes por pantalla
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

def ordenar_noms(llista):#ESTA HECHO
    llista.sort() #Ordenamos los elementos de la lista en orden Ascendente 
    return llista #Devolvemos la lista
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms

def mostrar_menu(): #ESTA HECHO
    print ("---------------------------------")
    print ("MENU DE SELECCIO")
    print ("---------------------------------")
    print("[A] Afegir nom")
    print("[L] Llistar noms")
    print("[O] Ordenar noms")
    print("[F] Finalizar")
    # Hem de mostrar el menú que ens demanen a l'enunciat

def demanar_opcio(): #ESTA HECHO
    valores_permitidos = "a","l","o","f" #Aqui creamos la lista de valores permitidos
    seleccion_user = input("Dime que opcion deseas seleccionar: ") #Le preguntamos al usuario que opcion quiere
    seleccion_user = seleccion_user.lower() #Convertimos la seleccion del usuario a letras minusculas
    while seleccion_user not in valores_permitidos: #Comenzamos el bucle dicendo que si no estan los valores permitidos se muetre el menu
        menu = mostrar_menu () #Mostramos el menu
        input("Dime que opcion deseas seleccionar: ")# Le volvemos a preguntar
    else:
        if seleccion_user == valores_permitidos: # Si los valores son os permitidos
            return seleccion_user # Que devuelva el valor seleccionado
        print ("Has selecionat l'opcio: ",seleccion_user) # Mensaje de queopcion a elegido

    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada        

def gestionar_opcio(opcio, llista):
    opcio = demanar_opcio ()
    match opcio:
        case "a":
            afegir_nom (llista)
        case "l":
            llistar_noms (llista)
        case "o":
            ordenar_noms (llista)
        case "f":
            print ("Programa Finalitzat")

    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    



# Programa principal

print("PENDENT: programa principal")
mostrar_menu ()
demanar_opcio ()



# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar