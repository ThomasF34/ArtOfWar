#coding:utf-8
#=== ==== INITIALISATION ==== ===

    #Les deux joueurs récupèrent leur Roi avec 3 unité (3 unités au hasard)
    #Une autre unité tirée est démobilisée et envoyée au royaume 
    #J1 : Une carte est envoyée au front
    #J2 : Une carte est envoyée au front 
    #J1 : Une carte est envoyée en reserve
    #J2 : Une carte est envoyée en reserve
    
#=== ==== La partie commence ==== === 
#
#   #=== ==== Déroulement d'un tour ==== ===
        #JA = Joueur actif
        #==== Phase Préparation : ===== 
        # JA : Redresse ses cartes du champ de bataille en vertical (prêt à attaquer)     
        # JA : Mobilise une nouvelle unité = Pioche une carte
        # 
        #==== Phase Action ====
        # JA doit soit : 
            # == AUCUNE ACTION == 
            
            # == Met en Reserve ==
                #Envoi une unité de sa main sur la reserve

            # == Déployer une unité ==
            
                # 1 - Met une unité sur la champ de bataille 
                #   Si JA a une unité dans sa réserve : 
                        # La carte est placée sur le champ de bataille
                #   Si il n'a de carte en réserve :       
                        # La carte provient de sa main (Main -> Champ de bataille)
                    
                # 1.b - L'unité doit être placée sur le front ou derrière une unité déjà présente au front 
                    #Si c'est la premiere unité:
                        #elle va au front.
                # 1.c - Une unité (C2) peut être placée sur une carte placée (C1) : 
                    #C1 va dans la reserve en fin de file 
                    
            # ==================
                    
            # == Attaquer ==
            
                while(JA a au moins une carte verticale && il souhaite encore attaquer):
                    positionCible = input("Quelle est la position de la cible à attaquer ?")
                    #Verification à faire ? Vérifier qu'il y a bien une carte ? Vérfier que la position est bien du type A ou F + 1 2 ou 3 
                    estPosition(positionCible)
                    cible = obtenirCarte(positionCible, JoueurAdverse)
                    
                # JA choisi une cible 
                    while(JA a encore des cartes verticales && il souhaite encore attaquer la cible && la cible est toujours la)
                        positionCarte = input("Quelle est la position de votre unité qui attaque ?")
                        while estVide(positionCarte) : 
                            positionCarte = input("Il semblerait qu'il n'y ait pas de carte ici. Quelle est la position de votre unité qui attaque ?")
                        
                        
                        
                        carte = obtenirCarte(positionCarte)
                        
                        
                        #Verification à faire
                            estPosition(PositionCarte) 
                            estVerticale()
                            
                            
                # JA choisi sa / ses cartes d'attaque (boucle pour chaque carte) 
                #    # La carte doit être verticale (position défensive) 
                    estVerticale(Carte)
                #    # Elle passe en position offensive
                    changementMode(Carte)
                #    # Attaque la cible 
                #
                #        #  = Resultat de l'attaque =   
                #        #    # Si L'attaque de la carte = Defense cible et Degat == 0 :
                                if (pointAttaque(Carte) == pointDefense(Cible)) and pointDegat(Cible) == 0 :
                #        #        # La cible est capturée
                                    capture(Cible)
         ???    #        #           # La carte va dans Royaume de JA = devient citoyen (Cartes gardent role dans royaume voir figure)
                                    entrerRoyaume(Carte)
                #        #    # Sinon si Attaque C1 < Defense Cible - Degats déjà subits 
                                elif (pointAttaque(Carte) < pointDefense(Cible) - pointDegat(Cible) : 
                #        #        # La cible recoit autant de dégat que de point d'attaque de la carte de JA
                                    
                #        #        # Degat += Attaque carte
        ???                       mise en place des Getters / Setters ? 
                                    setPointDegat(Cible,pointDegat(Cible)+pointAttaque(Cible))      
                #        #        # Elle reste en place et pourra etre rattaquée 
                                    
                #        #    # Sinon:
                                else : 
                #        #        # La carte va au cimetière (RIP)
                                    entrerCimetiere(Carte)
                #        #        # Si une unité se trouve derrière elle, elle prend sa place
                                    if verifArriere(Carte) :
                                        avancerCarte(??) 
        ??? On différencie deplacerCarte selon la destination ??? 
                #        #        # Il faut vérifier si le champ de bataille adverse est vide
                #        #        # Si le champ est vide:
                                    if champEstVide(JoueurAdverse) : ??? Fonction du joueur adverse ??? 
                                        print("Attention il semblerait que le champ de bataille du "+ JoueurAdverse +" soit vide !")

                #        #            #Si il y a deux unités dans la réserve : 
                                        if (nbCarte(reserve(JoueurAdverse)) >= 2 :
                                            ??? reserve(Joueur) renvoie la reserve et nb carte renvoi le nb de carte ?? il existe case en python ?? 
                                            print("Super il y a assez de cartes dans la réserve !")
                                            
                                            for i in range(2) :
                                                positionCarte = input(JoueurAdverse + ", où voulez-vous placer la carte de votre réserve ?")
                                                while(not(estPosition(positionCarte)) or not(estVide(positionCarte))) : 
                                                #Arret : Qd la position est bonne & qd la position est vide
                                                #pousuite : qd la position est fausse ou qd la position est non vide
                                                    positionCarte = input(JoueurAdverse + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre réserve ?")
                                                Carte = premiereCarteReserve(reserve(JoueurAdverse))
                                                placerCarte(Carte,positionCarte)
                                        
                #        #                #On place sur le champs de bataille
                                        else : 
                                            if nbCarte(reserve(JoueurAdverse)) == 1 : 
                                                if nbCarte(main(JoueurAdverse)) >= 1 : 
                                            
                                               ??? ici il semblerait que je doive mettre quelque chose de similaire à ce qu il y a plus haut.
                                            ??? On peut faire des fonctions hors du main qui ne sont pas dans la spec fonctionnelle ?? 
                                                
                                                else : 
                                                    
                                                    ? ici le royaume s effondre
                                                
                                            elif nbCarte(reserve(JoueurAdverse)) == 0 : 
                                            
                                                if nbCarte(main(JoueurAdverse)) >= 2 : 
                                                
                                                ?? Pareil qu'en haut'
                                            
                                                else : 
                                                     le royaume s effrondre
                                            
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
        #        
        # ==== FIN PHASE DEVELOPPEMENT ====
    
#FIN DU TOUR
# Changement de joueur actif (JA)

#Condition de fin de partie : 
#    #Soit l'effondrement : Si un joueur n'a plus de quoi rajouter des unités sur le CHAMP DE BATAILLE
#    
#    #Soit l'execution : Si le roi d'un joueur est capturé
#    
#    #Soit Fin de la guerre : Aucun joueur n'a de pioche 
    
    
   
    
    
    
    