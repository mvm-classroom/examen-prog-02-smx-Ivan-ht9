#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random

def obtenir_nom():
    # Llista de noms incorrectes
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]

    # Llista de cognoms incorrectes
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]

    nom_aleatori = random.choice ([noms,cognoms]) #Sirve para crear un nombre aleatorio gracias a la funcion random.choice.
    return (nom_aleatori)
    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista):
    print("PENDENT: afegir_nom")
    nom_aleatori = obtenir_nom ()
    llista = []
    llista.append(nom_aleatori)
    return llista 
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom

def llistar_noms(llista):
    print("PENDENT: llistar_noms")
    for nombre in llista:
        print (nombre)
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

def ordenar_noms(llista):
    llista.sort()
    return llista
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
    valores_permitidos = "a","l","o","f"
    seleccion_user = input("Dime que opcion deseas seleccionar: ")
    seleccion_user = seleccion_user.lower()
    while seleccion_user not in valores_permitidos:
        menu = mostrar_menu ()
        input("Dime que opcion deseas seleccionar: ")
    else:
        if seleccion_user == valores_permitidos:
            return seleccion_user
        print ("Has selecionat l'opcio: ",seleccion_user)

    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada        

def gestionar_opcio(opcio, llista):
    print("PENDENT: gestionar_opcio")
    opcion = demanar_opcio ()
    match opcion:
        case "a":
            afegir_nom ()
        case "l":
            llistar_noms ()
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
demanar_opcio()
gestionar_opcio ()
ordenar_noms ()

# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
