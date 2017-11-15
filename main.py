#coding:utf-8
# =========== Diverses fonctions nécessaires pour l'interfece ================ 
def verifAction(action) : 
    if action < 0 or action > 3 : 
        return False
    else : 
        return True 
                             
def estPosition(choix) :
    if(choix[0]=='A' or choix[0]=="F") :
        if(int(choix[1]) >= 1 and int(choix[1]) <= 3):
            return True
        else:
            return False
    else :
        return False
                                            
                                            
def positionValide(choix) : 
    if(choix[0] == "A"):
        return estPosition(choix) and not(estVideFront(choix[1])) #La position est valide à l'arriere si le front est occupé au meme indice 
    else : 
        return estPosition(choix)
                            
def askAttaque(joueur):
    choix = int(input(nom(joueur)+" voulez-vous encore attaquer ? 1 = Oui, 0 = Non\nChoix : "))
    if(choix == 0):
        return False
    elif(choix == 1):
        return True
    else :
        return askAttaque(joueur)
                                            
def askAttaqueCible(joueur):
    choix = int(input(nom(joueur)+" voulez-vous encore attaquer cette cible ? 1 = Oui, 0 = Non\nChoix : "))
    if(choix == 0):
        return False
    elif(choix == 1):
        return True
    else :
        return askAttaqueCible(joueur) 

def demandeDevelop(JA):
    print(descriptionMain(main(JA)))
    choix = input("Voulez-vous mettre une carte de votre main au royaume ?\n1 = Oui , 0 = Non. Choix : ")
    if choix == 0 :
        return False 
    elif choix == 1 : 
        return True
    else:
        return demandeDevelop(JA)
        
#================= fin des fonctions diverses ============================

# === Création de la partie === # 
nom1 = input("Entrez le nom du joueur 1 : ")
JA = creerJoueur(1,nom1)

nom2 = input("Entrez le nom du joueur 2 : ")
JoueurAdverse = creerJoueur(2,nom2)

Partie = creerPartie(JA,JoueurAdverse)



        
    

#=== ==== INITIALISATION ==== ===


    #Les deux joueurs récupèrent leur Roi avec 3 unité (3 unités au hasard)
    #Une autre unité tirée est démobilisée et envoyée au royaume 
    #J1 : Une carte est envoyée au front
    #J2 : Une carte est envoyée au front 
    #J1 : Une carte est envoyée en reserve
    #J2 : Une carte est envoyée en reserve
    
#=== ==== La partie commence ==== === 
          
while(not(finDePartieEff) and not(finDePartieRoi) and not(finDePartiePioche)) :
    #=== ==== Déroulement d'un tour ==== ===
    #JA = Joueur actif
    JA = joueurCourant(Partie)
    JoueurAdverse = joueurAdverse(Partie, JA)

    #==== Phase Préparation : ===== 
    # JA : Redresse ses cartes du champ de bataille en vertical (prêt à attaquer)
    redresseCartes(champBataille(JA))

    # JA : Mobilise une nouvelle unité = Pioche une carte
    nouvelleMain = ajouterCarteMain(main(JA),piocher(pioche(JA)))
    JA = setMain(JA,nouvelleMain)

    # 
    #==== Phase Action ====
    # JA doit soit : 
    action = int(input(nom(JA) + " que voulez vous faire dans ce tour ? \n0 : Rien \n1 : Mettre une carte en réserve \n2 : Déployer une unité \n3: Attaquer une cible\nAction : "))
    while not(verifAction(action)) :
        print(nom(JA) + " vous n'avez pas entré une action correcte ! ")
        action = int(input("Que voulez vous faire dans ce tour ? \n0 : Rien \n1 : Mettre une carte en réserve \n2 : Déployer une unité \n3: Attaquer une cible\nAction : "))

    #Une fois sorti de la boucle, action est un entier compris entre 0 et 3.

    if action == 0 : #Aucune action 
        print(nom(JA)+" ne fait aucune action !")
    elif action == 1 : 
    # == Met en Reserve ==
        #Envoi une unité de sa main sur la reserve
        if nbCarteMain(main(JA)) >= 1 :

            ??????????????????????????
            print(descriptionMain(main(JA)))
            choix = int(input("Quelle carte voulez-vous envoyer en réserve ?"))
            
            
            Carte = extraireCarteMain(main(JA),choix) ?? Il faut aussi enlever la carte de la main ?? 
            ??????????????????????????
            ?? Comment savoir quelle carte il veut ?? Reussir à afficher une "liste" de carte ?? Comment faire 

            nouvelleReserve = envoiReserve(reserve(JA),Carte) 
            JA = setReserve(JA, nouvelleReserve)

            print("Votre carte est maintenant dans la réserve")
        else : #Si j'ai pas d'unité dans ma main je peux rien faire 
            print("Comment voulez-vous ajouter une carte à votre réserve si vous n'avez pas de carte dans votre main ?")

    elif action == 2 : #déploie une unité 
    # == Déployer une unité ==

    # 1 - Met une unité sur la champ de bataille 
    #   Si JA a une unité dans sa réserve : 
        if nbCarteReserve(reserve(JA)) >= 1 : 
            Carte = premierCarteReserve(reserve(JA))
        elif nbCarteMain(main(JA)) >= 1 : 
            print(descriptionMain(main(JA)))
            choix = int(input("Quelle carte voulez-vous envoyer en réserve ?"))
            Carte = extraireCarteMain(main(JA),choix)
        else : 
            print("Wesh t'as pas de carte à poser gros !")

    # La carte est placée sur le champ de bataille

    # 1.b - L'unité doit être placée sur le front ou derrière une unité déjà présente au front
        if nbCarteFront(front(champBataille(JA))) + nbCarteArriere(arriere(champBataille(JA))) == 0 : 
        #Si c'est la premiere unité:
            choix = int(input("Votre carte doit aller au front. A quelle position voulez vous la mettre. 1, 2 ou 3\n Choix : "))#avec int() on vérifie que l'utilisateur nous renvoie bien un int
            position = "F"+str(choix)
            nouveauFront = envoyerFront(front(champBataille(JA)),Carte,position) 
            JA = setFront(JA,nouveauFront)
        else : 
            choix = input("Où voulez-vous placer votre carte ?\nPosition : ")
            while(not(positionValide(choix))):
                choix = input("Attention, vous avez entré une mauvaise position !\nOù voulez-vous placer votre carte ?\nPosition : ")
    # 1.c - Une unité (C2) peut être placée sur une carte placée (C1) : 

            if(choix[0]=="F"):
                if(not(estVideFront(choix))):
                    #C1 va dans la reserve en fin de file 
                    CarteDejaPlacee = extraireFront(front(champBataille(JA)),choix)
                    nouvelleReserve = envoiReserve(reserve(JA),CarteDejaPlacee) 
                    JA = setReserve(JA, nouvelleReserve)
                nouveauFront = envoyerFront(front(champBataille(JA),Carte,choix))
                JA = setFront(champBataille(JA),nouveauFront)
            else : #si choix[0] == "A"
                nouveauArriere = envoyerArriere(arriere(champBataille(JA)),Carte,choix)
                JA = setArriere(champBataille(JA),nouveauArriere)

    else : #action == 3  #Attaque 
        # == Attaquer ==
            veutAttaquer = True
            while(not(touteHorizontale(champBataille(JA))) and veutAttaquer):                
                # JA choisi une cible 
                positionCible = input("Quelle est la position de la cible à attaquer ?\nChoix (sous la forme A1,A2,A3,F1,F2,F3) : ")
                #Verification à faire :
                        #Vérifier qu'il y a bien une carte ? Vérfier que la position est bien du type A ou F + 1 2 ou 3 
                while(not(estPosition(positionCible)) or estVidePosition(champBataille(JoueurAdverse),positionCible)) :
                    print("Attention la coordonnée entrée n'est pas valide")
                    positionCible = input("Quelle est la position de la cible à attaquer ?\nChoix (sous la forme A1,A2,A3,F1,F2,F3) : ")

                cible = obtenirCarte(champBataille(JoueurAdverse,positionCible))
                ciblePresente = True #La cible est dans le combat. Elle en sortira si elle est capturée ou tuée

                # JA choisi sa / ses cartes d'attaque (boucle pour chaque carte) 
                veutAttaquerCible = True
                while(not(touteHorizontale(champBataille(JA))) and veutAttaquerCible and ciblePresente) :
                    positionCarte = input("Quelle est la position de votre unité qui attaque ?")
                    while (estVidePosition(champBataille(JA),positionCarte) or not(estPosition(positionCarte)) or not(estVerticale(obtenirCarte(champBataille(JA),positionCarte)))) :
                        positionCarte = input("Il semblerait qu'il n'y ait pas de carte ici. Quelle est la position de votre unité qui attaque ?")
                          
                    Carte = obtenirCarte(champBataille(JA),positionCarte)
                    

                # La carte doit être verticale (position défensive)                 #    
                # Elle passe en position offensive
                    changementMode(Carte)
                # Attaque la cible 

                # = Resultat de l'attaque =   
                # Si L'attaque de la carte = Defense cible et Degat == 0 :
                    if (pointAttaque(Carte) == pointDefense(Cible)) and pointDegat(Cible) == 0 :
                        # La cible est capturée
                        capture(Cible)
                        if roleCarte(Cible) == "Roi" : 
                            finDePartieRoi = True 
                        ciblePresente = False #La cible quitte le combat 
                        # La carte va dans Royaume de JA = devient citoyen (Cartes gardent role dans royaume voir figure)
                        entrerRoyaume(royaume(JA),Carte)
                        # Sinon si Attaque C1 < Defense Cible - Degats déjà subits 
                    elif (pointAttaque(Carte) < pointDefense(Cible) - pointDegat(Cible)) : 
                        # La cible recoit autant de dégat que de point d'attaque de la carte de JA
                        # Degat += Attaque carte
                        Cible = setPointDegat(Cible,pointDegat(Cible)+pointAttaque(Cible))   
                        ?? on sauvegarde le changement quelque part ?? 
                        # Elle reste en place et pourra etre rattaquée 
                    else : 
                        # La carte va au cimetière (RIP)
                        JA = setCimetiere(JA, entrerCimetiere(cimetiere(JA), Carte))
                        ciblePresente = False #La cible quiite le combat  
                        # Si une unité se trouve derrière elle, elle prend sa place
                        if verifArriere(champBataille(JoueurAdverse),positionCible) :
                            avancerCarte(champBataille(JA),positionCible) 
                    # Il faut vérifier si le champ de bataille adverse est vide
                    # Si le champ est vide:
                        if champEstVide(JoueurAdverse) : 
                            print("Attention il semblerait que le champ de bataille du "+ nom(JoueurAdverse) +" soit vide !")

                            #Si il y a deux unités dans la réserve : 
                            if (nbCarte(reserve(JoueurAdverse))) >= 2 :
                                print("Super il y a assez de cartes dans la réserve !")
                                for i in range(2) :
                                    positionCarteSecours = input(nom(JoueurAdverse) + ", où voulez-vous placer la carte de votre réserve ?")
                                    while(not(estPosition(positionCarteSecours)) or not(estVidePosition(champBataille(JoueurAdverse),positionCarteSecours))) : 
                                    #Arret : Qd la position est bonne & qd la position est vide
                                    #pousuite : qd la position est fausse ou qd la position est non vide
                                        positionCarteSecours = input(nom(JoueurAdverse) + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre réserve ?")
                                    Carte = premiereCarteReserve(reserve(JoueurAdverse))

                                    #On place sur le champs de bataille
                                    if(positionCarteSecours[0] == "F"): 
                                        
                                        nouveauFront = envoyerFront(front(champBataille(JoueurAdverse)),Carte,positionCarteSecours) 
                                        JA = setFront(JA,nouveauFront)
                                    else: #si choix[0] == "A"
                                        
                                        nouveauArriere = envoyerArriere(arriere(champBataille(JoueurAdverse)),Carte,positionCarteSecours)
                                        JA = setArriere(champBataille(JA),nouveauArriere)

                            else:
                                
                                if nbCarte(reserve(JoueurAdverse)) == 1 :
                                    if nbCarte(main(JoueurAdverse)) >= 1 :
                                        ??? ici il semblerait que je doive mettre quelque chose de similaire à ce qu il y a plus haut.
                                        ??? On peut faire des fonctions hors du main qui ne sont pas dans la spec fonctionnelle ?? 
                                    else :
                                        print("Le royaume s'effrondre")
                                        effronde(royaume(JoueurAdverse))
                                        finDePartieEff = True
                                        
                                elif nbCarte(reserve(JoueurAdverse)) == 0 :
                                    if nbCarte(main(JoueurAdverse)) >= 2 :
                                        ?? Pareil qu'en haut'
                                    else : 
                                        print("Le royaume s'effrondre")
                                        effronde(royaume(JoueurAdverse))
                                        finDePartieEff = True

                                        

                                ??VeutAttaquer et veutattaquerCible 
            #        #            #Sinon Si on peut compléter: 
            #        #                #On utilise une (ou aucune) carte de la reserve et on complète avec les cartes de son royaume
            #        #                # Impossible de poser la seconde carte sur la premiere
            #        #            #Sinon : 
            #        #                #Le royaume s'effondre
            #        #                
            #        # = FIN Resultat de l'attaque =
            #
            # 

# == FIN de l'attaque ==
# ==== FIN de la phase ACTION ====


    # ==== PHASE Developpement ==== 
    #    # Si sa main >= 6 cartes :                      
    #        # JA doit ajouter au royaume une carte de sa main
    #    # Sinon 
    #        # JA peut ajouter au royaume une carte de sa main

    if(nbCarteMain(JA)>=6 or demandeDevelop(JA)):
        ??????????????????????????
        print(descriptionMain(main(JA)))
        choix = int(input(nom(JA) + " Quelle carte voulez-vous envoyer au royaume ?"))
        Carte = extraireCarteMain(main(JA),choix) ?? Il faut aussi enlever la carte de la main ?? 
        ??????????????????????????
        ?? Comment savoir quelle carte il veut ?? Reussir à afficher une "liste" de carte ?? Comment faire 

        nouveauRoyaume = entrerRoyaume(royaume(JA),Carte) 
        JA = setRoyaume(JA, nouveauRoyaume)

    # ==== FIN PHASE DEVELOPPEMENT ====
    
#FIN DU TOUR
            
    #Condition de fin de partie : 
        #Soit l'effondrement : Si un joueur n'a plus de quoi rajouter des unités sur le CHAMP DE BATAILLE
              
        #Soit l'execution : Si le roi d'un joueur est capturé
   
        #Soit Fin de la guerre : Aucun joueur n'a de pioche
    if(nbCartePioche(pioche(JA)) == 0 and nbCartePioche(pioche(JoueurAdverse)) == 0):
        finDePartiePioche = True
    
              
# Changement de joueur actif (JA)
    Partie = changeJoueurCourant(Partie)
    
if finDePartiePioche : 
    if nbCarteRoyaume(royaume(JA)) > nbCarteRoyaume(royaume(JoueurAdverse)) :
        print("Bravo " + nom(JA) + ", vous avez remporté cette partie !!")
    elif  nbCarteRoyaume(royaume(JA)) < nbCarteRoyaume(royaume(JoueurAdverse)) :
        print("Bravo " + nom(JoueurAdverse) + ", vous avez remporté cette partie !!")
    else : 
        print("Egalité !!")