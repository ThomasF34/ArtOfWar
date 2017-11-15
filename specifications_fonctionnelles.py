# ===== ===== ===== SPECIFICATION FONCTIONNELLE ===== ===== ===== #
# ===== ===== == THOMAS FALCONE & LUCAS GONCALVES == ===== ===== #

# === === Pioche === === #
    
def créerPartie(Joueur,Joueur)->Partie
    # Pre-condition : Il faut deux joueurs différents
    # Post-condition : Aucune
    # Resultat : Retourne un element Joueur qui est le Joueur Adverse du joueur actuel.

def joueurAdverse(Joueur)-> Joueur
    # Pre-condition : Il faut deux joueurs différents
    # Post-condition : Aucune
    # Resultat : Retourne un element Joueur qui est le Joueur Adverse du joueur actuel.

def changeJoueurCourant(Joueur,Partie)->Joueur
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne le joueur adverse théorique du joueur actif. Le joueur adverse du joueur actif devient joueur actif
        
        

# === === Joueur === === #
    
def setChampBataille(Joueur,Champ_Bataille)->Joueur
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Toute les cartes du champ de bataille sont verticales 

def setMain(Joueur,Main)->Joueur
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Assigne une nouvelle main au joueur donné en paramètre

def setReserve(Joueur,Reserve)->Joueur
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Assigne une nouvelle reserve au joueur donné en paramètre

def setCimetiere(Joueur,Cimetiere)->Cimetiere
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Assigne une nouvelle reserve au joueur donné en paramètre

def nom(Joueur)->Str
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Renvoi le nom du joueur entré en paramètre

def champBataille(Joueur)-> Champ_Bataille
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : retourne le champ de bataille du joueur entré en paramètre

def main(Joueur)->Main
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : retourne le champ de bataille du joueur entré en paramètre

def royaume(Joueur)->Royaume
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : Renvoi le royaume du joueur

def setRoyaume(Joueur,Royaume)->Royaume
    # Pre-condition : Le joueur doit être de la partie
    # Post-condition : Aucune
    # Resultat : Renvoi le royaume du joueur

def creerJoueur(Royaume,Champs_Bataille,Reserve,Pioche,Cimetière) -> Joueur
    #Pre-condition : Aucune
    #Post-condition :Aucune
    #resultat : Renvoi un element de Type Joueur

def estPositionValide(String) -> Bool 
    # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
    # Post-condition : Aucune
    # Resultat : Retourne True 

def pioche(Joueur)-> Pioche
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne la pioche du joueur entré en paramètre

def cimetiere(Joueur)-> Cimetière
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne le cimetiere du joueur entré en paramètre
        
        
    
    
# === === Royaume === === #
    
def creerRoyaume() -> Royaume
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Royaume

def extraireRoyaume(Royaume,Carte,Joueur) -> Carte x Royaume 
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Royaume

def entrerRoyaume(Royaume,Carte)-> Royaume 
    # Pre-condition : Aucune 
    # Post-condition : Aucune
    # Resultat : Ajoute la carte entrée en paramètre dans le royaume 

def nbCarteRoyaume(Royaume)->Int
    # Pre-condition : Aucune 
    # Post-condition : Aucune
    # Resultat : Retourne le nombre de citoyens (cartes) dans le royaume placé en paramètre 

def estEffondre(Royaume,Joueur) -> Bool 
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Indique si le royaume du joueur passé en paramètre est effondré 

def effondre(Royaume,Joueur)->Royaume
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Modifie l'état d'éffondrement du Royaume du joueur passé en paramètre
    
    
    
    
# === === Main === === #
    
def afficheMain(Main)
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de type Reserve

def ajouterCarteMain(Carte)-> Main
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de type Reserve 

def nbCarteMain(Joueur)-> Int
    # Pre-condition : Il faut que la main soit celle d'un des deux joueurs.
    # Post-condition : Aucune
    # Resultat : Indique le nombre de carte présente dans la main
        
        
        
# === === Champs Bataille === === #
    
def redresseCartes(Champ_Bataille)->Champ_Bataille
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Toute les cartes du champ de bataille sont verticales 

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
    
    
    
# === === Front === === #
    
def creerFront() -> Front
    # Pre-condition : Aucune
    # Post-condition : Aucune 
    # Resultat : Créer un element de Type Front

def envoyerFront(Carte,Front,Str)->Front #======= ======== On a enlevé larriere attention si on doit le remettre
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : La carte est envoyé au front à la position indiquée en paramètre

def nbCarteFront(Front)->Int
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur le front

def estVideFront(Str)->Bool
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : Renvoi True si la position est vide, renvoi False sinon

def extraireFront(Front,Str)->Carte 
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Royaume
        
        
        
# === === Arriere === === #

def creerArriere() -> Arriere
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Front

def envoyerArriere(Arriere,Carte,Str)->Arriere
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : La carte située à l'arrière est envoyée à l'arriere

def nbCarteArriere(Front)->Int
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur l'arriere
        
        

# === === Reserve === === #
    
def creerReserve() -> Reserve
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de type Reserve   

def premiereCarteReserve(Reserve)-> Carte
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne la premiere carte de la reserve du joueur

def nbCarteReserve(Joueur)-> Int
    # Pre-condition : Il faut que la reserve soit celle d'un des deux joueurs.
    # Post-condition : Aucune
    # Resultat : Indique le nombre de carte présente dans la réserve

def envoiReserve(Reserve,Carte)-> Reserve
    # Pre-condition : La carte envoyée en réserve doit provenir de la main du joueur
    # Post-condition : Aucune
    # Resultat : La carte est retirée de la main et envoyée en reserve !! EN FIN DE FILE !!
    
    
    
# === === Pioche === === #

def creerPioche() -> Pioche
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un élément de Type Pioche 

def piocher(Pioche)->Carte
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Renvoi la premiere carte de la pioche.

def nbCartePioche(Pioche)->Int
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Renvoi le nombre de carte restant dans la pioche entrée en paramètre
        
# === === Cimetière === === #
    
def creerCimetiere() -> Cimetière
    # Pre-condition : Aucune 
    # Post-condition : Aucune
    # Resultat : Créer un "element" de Type Cimetière

def entrerCimetiere(Cimetiere,Carte)-> Cimetière
    # Pre-condition : Le cimetière doit etre celui du joueur qui possède la carte, pas de celui qui attaque
    # Post-condition : Aucune
    # Resultat : La carte est ajoutée à l'entité Cimetière
    
    
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
    