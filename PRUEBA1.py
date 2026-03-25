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
obtenir_nom ()
afegir_nom (obtenir_nom())
llistar_noms (afegir_nom(obtenir_nom))