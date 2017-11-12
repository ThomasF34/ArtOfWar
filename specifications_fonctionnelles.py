# ===== ===== ===== SPECIFICATION FONCTIONNELLE ===== ===== ===== #


Joueur : 
    
- creerJoueur(Royaume,Champs_Bataille,Reserve,Pioche,Cimetière) : -> Joueur
    #Pre-condition : Aucune
    #resultat : Renvoi un element de Type Joueur
    
Royaume : # Ensemble des fonctions liées au type Royaume 
    - creerRoyaume() -> Royaume
        # Pre-condition : Aucune
        # Post-condition : Aucune
        # Resultat : Créer un element de Type Royaume
    - extraireRoyaume(Carte, )
    - entrerRoyaume(Carte,Royaume)-> Royaume 

    - ajouterCarteRoyaume(Carte,Royaume,Joueur) -> Royaume 
        # Pre-condition : Aucune
        # Post-condition :
        # Resultat : La carte est placée dans le royaume du joueur

Champs_bataille :
    - creerChampBataille()-> Champ_Bataille
    
    - estVide(ChampBataille)

Front : 
    - creerFront() -> Front
        # Pre-condition : Aucune
        # Post-condition : Aucune 
        # Resultat : Créer un element de Type Front
    - envoyerFront(Carte,Front,Arriere )->Front
        # Pre-condition : La carte doit être situé à l'arrière
        # Post-condition : Aucune 
        # Resultat : La carte située à l'arrière est envoyée au front

Arriere : 
    - creerArriere() -> Arriere
        # Pre-condition : Aucune
        # Post-condition : Aucune
        # Resultat : Créer un element de Type Front

Reserve : 
    - creerReserve() -> Reserve
        # Pre-condition : Aucune
        # Post-condition : Aucune
        # Resultat : Créer un element de type Reserve   

Pioche : 
    - creerPioche() -> Pioche
        # Pre-condition : Aucune
        # Post-condition : Aucune
        # Resultat : Créer un élément de Type Pioche 


Cimetière : 
    - creerCimetiere() -> Cimetière
        # Pre-condition : Aucune 
        # Post-condition : Aucune
        # Resultat : Créer un "element" de Type Cimetière
    - allerCimetiere(Carte,Cimetiere)-> Cimetière
        # Pre-condition : La carte doit etre issus du champs de bataille. Le cimetière doit etre celui du joueur qui possède la carte, pas de celui qui attaque
        # Post-condition : Aucune
        # Resultat : La carte est ajoutée à l'entité cimetière
    
Carte : 
    
    - estVerticale(Carte)-> Bool
        # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
        # Post-condition : Aucune
        # Resultat : Retourne True si la carte est verticale, retourne False sinon
    
Position : 
    
    - estPosition(Carte) -> Position 
        # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
        # Post-condition : Aucune
        # Resultat : Retourne True si la carte est verticale, retourne False sinon
        
        
    - positionCarte(Carte)-> Str
        # Pre-condition : La carte entrée en paramètre doit être positionnée sur le plateau. 
        # Post-condition : Aucune
        # Resultat : Retourne la chaine de caractère représentant la position de la carte sur le plateau ("F1","F2",...,"A3")
        
        
    - changementPosition(Carte)->Carte
     
    
    
Cible : 
    
    - positionCible(Carte) -> Str
        # Pre-condition : La position doit etre de type : A1,A2,A3 
        # Post-condition : Aucune
        # Resultat : Créer un element de Type Cimetière
        
        
ATTAQUES :
    
    - pointAttaque(Carte)-> Int
        # Pre-condition : La carte doit avoir une position de plateau
        # Post-condition : Aucune
        # Resultat : retourne le nombre de point d'attaque de la carte
        
    - pointDefense(Carte)-> Int
        # Pre-condition : La carte doit avoir une position de plateau
        # Post-condition : Aucune
        # Resultat : retourne le nombre de point de defense de la carte
        
    - pointDegat(Carte)-> Int
        # Pre-condition : La carte doit avoir une position de plateau
        # Post-condition : Aucune
        # Resultat : retourne le nombre de point de dégat subits de la carte
        
    - capture(Carte)-> Carte
        # Pre-condition : La carte doit avoir une position de plateau
        # Post-condition : Aucune
        # Resultat : Place la carte dans le Royaume
        
    - setPointDegat(Carte)