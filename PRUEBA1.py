import random
def obtenir_nom():
    # Llista de noms incorrectes
    noms = "Ivan"

    # Llista de cognoms incorrectes
    cognoms = "Herrera"
    
    noms = random.choice ([noms]) #Sirve para crear un nombre aleatorio gracias a la funcion random.choice.
    cognoms = random.choice ([cognoms]) 
    nom_aleatori_complet = noms + cognoms
    return (nom_aleatori_complet)

    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista):
    nom_aleatori = obtenir_nom ()
    llista = []
    llista.append(nom_aleatori)
    return llista 
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom

def llistar_noms(llista):
    for nombre in llista:
        print (nombre)
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

def ordenar_noms(llista):
    llista.sort()
    return llista

llistar_noms (afegir_nom(obtenir_nom))
ordenar_noms (llistar_noms(afegir_nom(obtenir_nom)))