###MAIN

#Crée une main vide
#FG / Structure de donnée 
# (Carte)[0] puis on append à chaque ajout (c'est donc une liste)
def creer_main():
    return 0

#placer_dans_main : carte x main -> main
#ajoute carte c dans la main m du joueur, in/out
def placer_dans_main(c,m):
    return 0

#Retirer_de_main : ident x main -> main
# retire la carte c de la main m, in/out
#CI : on vérifie que cette carte c est bien dans m
def retirer_de_main(c,m):
    return 0

#main_vide : main -> bool
#Renvoie True si la main m est vide
def main_vide(m):
    return 0

#get_nombre_carte_main: main ->int
#Renvoie le nombre de carte qu’il y a dans la main m
def  get_nombre_carte_main(m):
    return 0

#affiche_main : main -> string
#Décrit une main, par ex : "Roi, Garde, Garde, Soldat, Archer, Archer"
#FG : On change la description en y intégrant l'Ident de la carte. On a alors px "1 Garde, 12 Garde, 30 Soldat, 28 Archer, 24 Archer" 
def decrire_main(j):
    return 0

#est_dans_main: carte x main -> bool
#renvoie true si il existe au moins une carte de type c dans la main m
def est_dans_main(c,m):
    return 0



