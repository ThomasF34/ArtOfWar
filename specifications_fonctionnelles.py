# ===== ===== ===== SPECIFICATION FONCTIONNELLE ===== ===== ===== #


Joueur : 
    
- creerJoueur(Royaume,Front,Arriere,Reserve,Pioche,Cimetière) : -> Joueur
    #Pre-condition : Aucune
    #resultat : Renvoi un element de Type Joueur
    
Royaume : # Ensemble des fonctions liées au type Royaume 
    - creerRoyaume() -> Royaume
        # Pre-condition : Aucune
        # Post-condition : Aucune
        # Resultat : Créer un element de Type Royaume
    - extraireRoyaume(Carte, )
    - entrerRoyaume(Carte,Royaume)-> Royaume 

    - ajouterCarteRoyaume(Carte,Royaume) -> Royaume 
        # Pre-condition :
        # Post-condition : 
        # Resultat :


    - ajouterRoyaume(Carte, Royaume) -> Royaume
        # Pre-condition :
        # Post-condition : 
        # Resultat : Créer un element de Type Royaume

Front : 
    - creerFront() -> Front
        # Pre-condition : Aucune
        # Post-condition : Aucune 
        # Resultat : Créer un element de Type Front

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
        # Resultat : Créer un element de Type Cimetière
    
Carte : 
    
    - estVerticale(Carte)-> Bool
    
    
    - changementPosition(Carte)->Carte
    
    
ATTAQUES :
    
    - pointAttaque(Carte)-> Int
    - pointDefense(Carte)-> Int
    - pointDegat(Carte)-> Int
    - capture(Carte)-> Carte
    - 