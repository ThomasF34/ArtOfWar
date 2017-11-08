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
                    
                # JA choisi une cible 
                    while(JA a encore des cartes verticales && il souhaite encore attaquer la cible && la cible est toujours la)
                        positionCarte = input("Quelle est la position de votre unité qui attaque ?")
                        while estVide(positionCarte) : 
                            positionCarte = input("Il semblerait qu'il n'y ait pas de carte ici. Quelle est la position de votre unité qui attaque ?")
                        
                        
                        
                        carte = obtenirCarte(positionCarte)
                        
                        
                        #Verification à faire
                            estPosition(PositionCarte) 
                            estVerticale
                            
                            
                # JA choisi sa / ses cartes d'attaque (boucle pour chaque carte) 
                #    # La carte doit être verticale (position défensive) 
                    estVerticale(Carte)
                #    # Elle passe en position offensive
                    changementPosition(Carte)
                #    # Attaque la cible 
                #
                #        #  = Resultat de l'attaque =   
                #        #    # Si L'attaque de la carte = Defense cible et Degat == 0 :
                                if (pointAttaque(Carte) == pointDefense(Cible)) && pointDegat(Cible) == 0 :
                #        #        # La cible est capturée
                                    capture(Cible)
         ???    #        #           # La carte va dans Royaume de JA = devient citoyen (Cartes gardent role dans royaume voir figure)
                                    entrerRoyaume()
                #        #    # Sinon si Attaque C1 < Defense Cible - Degats déjà subits 
                #        #        # La cible recoit autant de dégat que de point d'attaque de la carte de JA
                #        #        # Degat += Attaque carte
                #        #        # Elle reste en place et pourra etre rattaquée 
                #        #    # Sinon:
                #        #        # La carte va au cimetière (RIP)
                #        #        # Si une unité se trouve derrière elle, elle prend sa place
                #        #        # Il faut vérifier si le champ de bataille adverse est vide
                #        #        
                #        #        # Si le champ est vide:
                #        #            #Si il y a deux unités dans la réserve : 
                #        #                #On place sur le champs de bataille
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
    
    
   
    
    
    
    