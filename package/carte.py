# === === Carte === === #
    
def estVerticale(Carte)-> Bool
    # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
    # Post-condition : Aucune
    # Resultat : Retourne True si la carte est verticale, retourne False sinon

def changementMode(Carte)->Carte
    # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
    # Post-condition : Aucune
    # Resultat : Le mode de la carte a été modifié :  Vertical si Horizontal et inversement

def positionCarte(Carte)-> Str 
    # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
    # Post-condition : Aucune
    # Resultat : Retourne la chaine de caractère représentant la position de la carte sur le plateau ("F1","F2",...,"A3")  
    
def setPositionCarte(Carte,Str) -> Carte
    # Pre-Cond :

def pointAttaque(Carte)-> Int
    # Pre-condition : La carte doit avoir une position de plateau
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point d'attaque de la carte

def pointDefense(Carte)-> Int
    # Pre-condition : La carte doit avoir une position de plateau
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de defense de la carte EN FONCTION DE SON MODE (enjoy)

def pointDegat(Carte)-> Int
    # Pre-condition : La carte doit avoir une position de plateau
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de dégat subits de la carte

def capture(Carte)-> Carte
    # Pre-condition : La carte doit avoir une position de plateau
    # Post-condition : Aucune
    # Resultat : Place la carte dans le Royaume

def setPointDegat(Carte,Int)->Carte
    # Pre-condition : La carte doit avoir une position de plateau
    # Post-condition : Aucune
    # Resultat : Renvoi une carte avec des points de degat modifiés

def roleCarte(Carte)->Str
    # Pre-condition : Aucune
    # Post-condition : Renvoi un string parmis ces valeurs : Garde, Archer, Soldat, Roi
    # Resultat : Renvoi le rôle de la carte entrée en paramètre
    
def estAPortee(carte,cible) : 
    # Pre-condition : carte et cible sont toutes deux des Carte présentent sur le champ de bataille
    # Post-condition : 
    # Resultat : Renvoie True si la cible est à portée de la carte, False sinon
    
    pass
    
    