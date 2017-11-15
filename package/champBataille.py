# === === Champs Bataille === === #
    
def redresseCartes(Champ_Bataille)->Champ_Bataille
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Toutes les cartes du champ de bataille sont verticales. Le champ de bataille est donc modifié et renvoyé.

def creerChampBataille(Joueur)-> Champ_Bataille
    # Pre-condition : Le joueur entré en paramètre ne doit pas avoir de champ de bataille existant
    # Post-condition : Aucune
    # Resultat : Toute les cartes du champ de bataille sont verticales 

def estVide(Champ_Bataille)->Bool
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne True si aucune carte n'est placée sur le champs de bataille, false sinon

def obtenirCarte(Champ_Bataille,Position)
    # Pre-condition : La position entrée en paramètre doit correspondre à une position du plateau et une carte doit se trouver à cet emplacement. 
    # Post-condition : Aucune
    # Resultat : Indique la carte se trouvant à cette position

def nbCarteCHampBataille(Champ_Bataille)->Int
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Indique le nombre 

def front(Champ_Bataille)->Front
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : retourne le champ de bataille du joueur entré en paramètre

def arriere(Champ_Bataille)->Arriere
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : retourne l'arriere du joueur entré en paramètre

def setArriere(Joueur,Arriere)->Arriere
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Assigne une nouvelle reserve au joueur donné en paramètre

def setFront(Joueur,Front)->Front
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Assigne une nouvelle reserve au joueur donné en paramètre

def touteHorizontale(Champ_Bataille)->Bool
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne True si toute les cartes du champs de bataille sont horizontal, retourne False sinon

def estVidePosition(Champ_Bataille,String)->Bool
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne True si la position contient une carte (en utilisant les fonction estVideFront et estVideArriere)

def verifArriere(Champ_Bataille,String)->Bool
    # Pre-condition : Soit String (chaine de caractère) correspondant la position de la carte cible.
    # Post-condition : Aucune
    # Resultat : Retourne True si l'Arriere situé derrière la carte cible est occupé, retourne False sinon (ou si la carte cible donnée en paramètre n'est pas au front).

def avancerCarte(Champ_Bataille,Str)->Champ_Bataille
    # Pre-condition : La carte donnée en paramètres est au front et une autre carte se situe derriere elle
    # Post-condition : Aucune
    # Resultat : Renvoi un champs de bataille dans lequel la carte (située à l'arriere) est envoyée au front
    
    
   