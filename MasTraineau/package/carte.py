###carte

#creer_carte: int x string x string -> carte
#Crée une carte. 
#pré-condition :    
#-les cartes ne peuvent pas avoir l'identifiant 0 et 1 car c'est l'identifiant des rois créé dans le main
#-chaque cartes a un identifiant unique
#id : entier qui identifie la carte.
#type : chaine de caractère qui représente le type de la carte, e.g : "Soldat" FG : Valeur parmi "Soldat" "Archer" "Garde" "Roi1" "Roi2" 
#posture : chaine de caractère qui représente la posture de la carte, e.g : "def", par défaut les cartes sont créées en posture défensive
def creer_carte(ident, typeCarte, posture):
    return 0

#get_type: carte -> string
#Renvoie le type de la carte c
def get_type(c):
    return 0

#get_position: carte x cdb -> int
#Renvoie la position (coordonnée) de la carte c sur le champ de bataille cdb
def get_position(c,cdb):
    return 0

#est_en_posture_defensive: carte x cdb-> bool
#vérifie si une carte est en position défensive dans un cdb
#pré-condition : la carte doit être dans le cdb
#résultat : True si la carte est en position défensive, false sinon
def est_en_posture_defensive(c,cdb):
    return 0

#mettre_en_offensif: carte -> carte
#met une carte c en état offensif en in/out
def mettre_en_offensif(c):
    return 0

#mettre_en_defensive: carte -> carte
#met une carte c en état défensif in/out
def mettre_en_defensive(c):
    return 0

#get_attaque : carte -> int
#renvoie l’attaque d’une carte c
def get_attaque(c):
    return 0

#get_point_de_defense : carte -> int
#Renvoie la défense d’une carte c. On prend en compte la position de la carte (offensive ou défensive)
def get_point_de_defense(c):
    return 0

#FG : Il manque une fonction getID(carte) qui renvoie l'identifiant de la carte donnée 
def getID(c):
	return 0 

# COMBAT
#touche: carte x carte -> bool
#Indique si la carte c2 est à portée de la carte c1
#Résultat : true si c2 est à portée de c1
def touche(c1,c2):
    return 0

#attaquer: carte x carte -> carte
#La première carte c1 attaque la deuxième carte c2, on soustrait les points de défenses  
#de la carte 2 par les points d’attaques de la carte 1 les paramètres sont passés en in/out
#Ne pas oublier de vérifier si la carte attaqué et en position offensive ou défensive

#FG : La modification de aEteTouche n'est pas définie. On passera aEteTouche à True quand la carte a été touchée. 
def attaquer(c1,c2):
    return 0

#aEteTouche : carte -> bool
#Indique si la carte a été touché dans le tour
def aEteTouche(c):
    return 0