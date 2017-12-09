###carte
# Carte(ident: Int, TypeCarte: Str, posture : Str, position : Int, Attaque : Int, Defense : Int)
#creer_carte: int x string x string -> carte
#Crée une carte. 
#pré-condition :    
#-les cartes ne peuvent pas avoir l'identifiant 0 et 1 car c'est l'identifiant des rois créé dans le main
#-chaque cartes a un identifiant unique
#id : entier qui identifie la carte.
#type : chaine de caractère qui représente le type de la carte, e.g : "Soldat" FG : Valeur parmi "Soldat" "Archer" "Garde" "Roi1" "Roi2" 
#posture : chaine de caractère qui représente la posture de la carte, e.g : "def", par défaut les cartes sont créées en posture défensive



# Carte(ident:Int, TypeCarte:Str, posture:Str,  Attaque:Int, Defense:[Int](2) )


def creer_carte(ident, typeCarte, posture, defense1, defense2):
    carte = {"ident" : ident, "typeCarte" : typeCarte, "posture" : posture, "defenseDef" : defense1, "defenseOff" : defense2}
    return carte


#get_type: carte -> string
#Renvoie le type de la carte

def get_type(carte):
    return carte["typeCarte"]



#est_en_posture_defensive: Carte x cdb-> bool
#vérifie si une carte est en position défensive dans un cdb
#pré-condition : la carte doit être dans le cdb
#résultat : True si la carte est en position défensive, false sinon

#POURQUOI CHAMPS BATAILLE CON
def est_en_posture_defensive(carte,cdb):
    return carte["posture"] == "def"
         
    
#mettre_en_offensif: carte -> carte
#met une carte c en état offensif en in/out
def mettre_en_offensif(carte):
    carte["posture"] = "off"
    return carte

#mettre_en_defensive: carte -> carte
#met une carte c en état défensif in/out
def mettre_en_defensive(carte):
    carte["posture"] = "def"
    return carte

#get_attaque : carte -> int
#renvoie l’attaque d’une carte c
def get_attaque(carte,main):
    types = ["Archer","Garde","Roi1","Roi2"]
    if (carte["typeCarte"] in types) :
        attaque = 1
    
    else:
        carte["typeCarte"] == "Soldat":
        attaque = get_nombre_carte_main(main)
        
    return attaque
        
#get_point_de_defense : carte -> int
#Renvoie la défense d’une carte c. On prend en compte la position de la carte (offensive ou défensive)

#POURQUOI CHAMPS BATAILLE CON
def get_point_de_defense(carte,cdb):
    if est_en_posture_defensive(carte,cdb) :
        point_defense = carte["defenseDef"]
    else:
        point_defense = carte["defenseOff"]
        
    return point_defense


#FG : Il manque une fonction getID(carte) qui renvoie l'identifiant de la carte donnée

def getID(carte):
	return carte["ident"] 

# COMBAT
#touche: carte x carte -> bool
#Indique si la carte c2 est à portée de la carte c1
#Résultat : true si c2 est à portée de c1
def touche(c1,c2,cdb1,cdb2):
    
    positionC1 = get_position(c1,cdb1)
    positionC2 = get_position(c2,cdb2)
    
    if c1["typeCarte"] == "Archer":
        if positionC1 == 0:
            return positionC2 == 3
        elif positionC1 == 1:
            return ((positionC2 == 3) or (positionC2 == 5))
        elif positionC1 == 2:
            return (positionC2 == 4)
        elif positionC1 == 3:
            return ((positionC2 == 1) or (positionC2 == 3))    
        elif positionC1 == 4:
            return ((positionC2 == 2) or (positionC2 == 0))
        else:
            return (positionC2 == 1)
            
    elif ((c1["typeCarte"] == "Soldat") or (c1["typeCarte"] == "Garde")) :
        if positionC1 == 0:
            return (positionC2 == 3)
        elif positionC1 == 1:
            return ((positionC2 == 3) or (positionC2 == 5))
        elif positionC1 == 2:
            return (positionC2 == 4)
        elif (positionC1 == 3)
            return ((positionC2 == 1) or (positionC2 == 3))
        elif positionC1 == 4:
            return ((positionC2 == 2) or (positionC2 == 0))
        else:
            return (positionC2 == 1)

    else :
        if positionC1 == 0:
            return ((positionC2 == 3) or (positionC2 == 5) or (positionC2 == 2))
        elif positionC1 == 1:
            return ((positionC2 == 1) or (positionC2 == 4))
        elif positionC1 == 2:
            return (positionC2 == 5)
        elif (positionC1 == 3)
            return ((positionC2 == 4) or (positionC2 == 0) or (positionC2 == 5) or (positionC2 == 2))
        elif positionC1 == 4:
            return ((positionC2 == 4) or (positionC2 == 1) or (positionC2 == 5) or (positionC2 == 3))
        else:
            return ((positionC2 == 3) or (positionC2 == 0) or (positionC2 == 4) or (positionC2 == 2))
        
#attaquer: carte x carte -> carte
#La première carte c1 attaque la deuxième carte c2, on soustrait les points de défenses  
#de la carte 2 par les points d’attaques de la carte 1 les paramètres sont passés en in/out
#Ne pas oublier de vérifier si la carte attaqué et en position offensive ou défensive

#FG : La modification de aEteTouche n'est pas définie. On passera aEteTouche à True quand la carte a été touchée. 

def attaquer(c1,c2,cdb1,cdb2):
    attaque = get_attaque(c1)
    nbDef = get_point_de_defense(c2,cdb2)
    nouvelleDefense = nbDef - attaque
    if est_en_posture_defensive(carte2,cdb2):
        c2["defenseDef"] = nouvelleDefense
    else : 
        c2["defenseOff"] = nouvelleDefense
        
#aEteTouche : carte -> bool
#Indique si la carte a été touché dans le tour
def aEteTouche(carte):
    
    #On récupère la défense de la carte
    defenseCarte = get_defense(carte)
    
    #On récupère la défense originale du dico
    defenseOriginale =getCarte(carte)
    
    if defenseCarte < defenseOriginale:
        return True
    else:
        return False