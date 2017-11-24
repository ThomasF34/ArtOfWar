def main():
    joueur1 = 1
    joueur2 = 2
    #On crée toutes les composantes nécessaires au jeu
    creer_pioche(joueur1)
    creer_pioche(joueur2)
    creer_main(joueur1)
    creer_main(joueur2)
    creer_royaume(joueur1)
    creer_royaume(joueur2)
    creer_cdb(joueur1)
    creer_cdb(joueur2)
    creer_cimetiere(joueur1)
    creer_cimetiere(joueur2)
    creer_reserve(joueur1)
    creer_reserve(joueur2)
    #---

    #On mélange les deux pioches avant la mise en place    
    melanger_pioche(joueur1)
    melanger_pioche(joueur2)
    #---


#Début de la phase de mise en place
    #On place dans la main du joueur 1 son Roi ainsi que 3 cartes tirées au hasard
    placer_dans_main(roi1, joueur1)
    placer_dans_royaume(piocher_carte(joueur1),joueur1) #La première carte pioché est placer directement dans le royaume     
    placer_dans_main(piocher_carte(joueur1),joueur1)
    placer_dans_main(piocher_carte(joueur1),joueur1)
    #---

    #On place dans la main du joueur 2 son Roi ainsi que 3 cartes tirées au hasard
    placer_dans_main(roi2, joueur2)
    placer_dans_royaume(piocher_carte(joueur2),joueur2) #La première carte pioché est placer directement dans le royaume
    placer_dans_main(piocher_carte(joueur2),joueur2)
    placer_dans_main(piocher_carte(joueur2),joueur2)    
    #---
    
    #Le premier joueur choisit une carte de sa main et la place sur sa ligne de front 
    #On affiche la main pour que le joueur connaisse les cartes qu'il a en main
    afficher_main(get_main(joueur1))
    carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 1")
    while not est_dans_main(carte_choisi) :
        carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 1")
        
    #On affiche le champ de bataille pour que le joueur connaisse les positions disponibles
    afficher_cdb(get_position_utilisable_cdb(get_cdb(joueur1)))
    case_choisi = input("Quelle case de la ligne de front ?" )
    while not est_position_utilisable(case_choisi):
        case_choisi = input("Quelle case de la ligne de front ?" )
    placer_cdb(carte_choisi, get_cdb(joueur1), case_choisi)
    retirer_de_main(carte_choisi, get_main(joueur1))
    #---
    
    #Le second joueur choisit une carte de sa main et la place sur sa ligne de front
    afficher_main(get_main(joueur2))
    carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 2")
    while not est_dans_main(carte_choisi) :
        carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 2")
        
    afficher_cdb(get_position_utilisable_cdb(get_cdb(joueur2)))
    case_choisi = input("Quelle case de la ligne de front ?")
    while not est_position_utilisable(case_choisi) :
        case_choisi = input("Quelle case de la ligne de front ?")
    placer_cdb(carte_choisi, get_cdb(joueur2), case_choisi)
    retirer_de_main(carte_choisi, get_main(joueur1))
    #---

    #Le premier joueur choisit une carte de sa main et la place en réserve 
    afficher_main(get_main(joueur1))
    carte_choisi = input("Choisir la carte à placer en réserve du joueur 1")
    while est_dans_main(carte_choisi) :
        carte_choisi = input("Choisir la carte à placer en réserve du joueur 1")    
    placer_dans_reserve(carte_choisi, get_reserve(joueur1))
    retirer_de_main(carte_choisi, get_main(joueur1))
    #---     

    #Le second joueur choisit une carte de sa main et la place en réserve 
    afficher_main(get_main(joueur2))
    carte_choisi = input("Choisir la carte à placer en réserve du joueur 2")
    while not est_dans_main(carte_choisi) :
        carte_choisi = input("Choisir la carte à placer en réserve du joueur 2")    
    placer_dans_reserve(carte_choisi, get_reserve(joueur2))
    retirer_de_main(carte_choisi, get_main(joueur2))
    #---
#Fin de la phase de mise en place


    joueur = 1 #Le joueur 1 commence le premier

     
#début de la boucle de jeu
    while not partie_fini :

    #Début de la phase conscription
        
        #On test si la conscription est possible, si elle ne l'est pas alors on sort de la boucle de jeu (effondrement)
        cdb_vide = get_nombre_carte_cdb(get_cdb(joueur))==0
        nb_reserve = get_nombre_carte_reserve(get_reserve(joueur))
        nb_royaume = get_nombre_carte_royaume(get_royaume(joueur))
        if cdb_vide and (nb_reserve + nb_royaume)<2 :
            partie_fini = true
            raison_fin = "ef"
            joueur_perdant = joueur
            break
        #---Fin test conscription
        
        #On vérifie si l'on doit entrer en phase de conscription en fonction du nombre de cartes restantes sur le champ de bataille
        if get_nombre_carte_cdb(get_cdb(joueur))==0:
            print("Vous n'avez plus de carte sur le champs de bataille, vous devez recruter de force deux unités")
            if get_nombre_carte_reserve(get_reserve(joueur))==1:
                #On choisit la position à laquelle on place la dernière carte provenant de notre réserve 
                print("Vous n'avez plus qu'une seule carte dans votre réserve")
                afficher_reserve(get_reserve(joueur))
                print("A quelle position voulez-vous la placer ?")
                afficher_cdb(get_cdb(joueur))
                
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(get_cdb(joueur),case_choisi) : 
                    case_choisi = input("Position choisie : ")
                derniere_carte_reserve = piocher_dans_reserve(get_reserve(joueur))
                placer_cdb(derniere_carte_reserve, get_cdb(joueur), case_choisi)
                #---
                
                #On choisit la carte de notre royaume et sa position sur le champ de bataille
                print("Quelle carte de votre royaume souhaitez vous placer sur le champ de bataille")
                afficher_royaume(get_royaume(joueur))
                
                carte_choisi = input("Carte choisie : ")
                while not est_dans_royaume(carte_choisi) : 
                        carte_choisi = input("Carte choisie : ")
                print("A quelle position voulez-vous la placer ?")
                afficher_cdb(get_cdb(joueur))
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(case_choisi):
                    case_choisi = input("Position choisie : ")
                placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)            
                retirer_du_royaume(get_royaume(joueur), carte_choisi)

            if get_nombre_carte_reserve(get_reserve(joueur))>1:
                #On choisit la carte de notre reserve et on indique la position à laquelle on souhaite la poser sur le champ de bataille
                print("Les deux premières cartes de votre réserve vont être placées sur le champ de bataille")
                afficher_reserve(get_reserve(joueur))
                
                case_choisi = input("A quelle position souhaitez vous placer la première carte de votre réserve ? : ")
                while not est_position_utilisable(case_choisi) :
                    carte_choisi = input("A quelle position souhaitez vous placer la première carte de votre réserve ? : ")
                placer_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)
                
                case_choisi = input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : ")
                while not est_position_utilisable(case_choisi) :
                    carte_choisi = input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : ")
                placer_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)
                
            else :
                print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
                print("Veuillez choisir la première carte de votre royaume que vous souhaitez placer sur le champ de bataille")
                afficher_royaume(get_royaume(joueur))
                
                carte_choisi = input("Carte choisie : ")
                while not est_dans_royaume(carte_choisi) : 
                        carte_choisi = input("Carte choisie : ")
                print("A quelle position voulez-vous la placer ?")
                afficher_cdb(get_cdb(joueur))
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(case_choisi):
                    case_choisi = input("Position choisie : ")
                placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)
                retirer_du_royaume(get_royaume(joueur), carte_choisi)
                
                print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
                print("Veuillez choisir la deuxième carte de votre royaume que vous souhaitez placer sur le champ de bataille")
                afficher_royaume(get_royaume(joueur))
                
                carte_choisi = input("Carte choisie : ")
                while not est_dans_royaume(carte_choisi) : 
                        carte_choisi = input("Carte choisie : ")
                print("A quelle position voulez-vous la placer ?")
                afficher_cdb(get_cdb(joueur))
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(case_choisi):
                    case_choisi = input("Position choisie : ")
                placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)            
                retirer_du_royaume(get_royaume(joueur), carte_choisi)
            
    #--- Fin de la phase de conscription
    
    #Début de la phase de préparation
        mettre_en_position_def(get_cdb(joueur))
        
        #On vérifie si le joueur a encore des cartes dans sa pioche, dans le cas contraire la partie est fini et on sort de la boucle de jeu (Fin de la guerre)
        if pioche_vide(get_pioche(joueur)):
            partie_fini = true
            raison_fin = "f"
            joueur_sans_carte = joueur
            break
            
        placer_dans_main(piocher_carte(get_pioche(joueur)),get_main(joueur))
    #---Fin de la phase de préparation

    #Début de la phase d'action
        print("Votre champ de bataille :")
        afficher_cdb(get_cdb(joueur))
        print("Votre royaume :")
        afficher_royaume(get_royaume(joueur))
        print("Votre main :")
        afficher_main(get_main(joueur))
        print("Votre réserve :")
        afficher_reserve(get_reserve(joueur))
        
        #On demande l'action et on vérifie si c'est une action qui existe
        action = input("Que souhaitez vous faire ? /n (Action possible : -Ne rien faire (n) /n -Mettre en réserve (r) /n -Déployer unité (d) /n -Attaquer (a)")
        action_valide = false    
        if(action == "n" or action == "r" or action == "d" or action == "a" ) :
            action_valide = true
        while (action_valide==false) :
            print("L'action demandé n'existe pas, veuillez choisir une action qui existe")
            action = input("Que souhaitez vous faire ? /n (Action possible : -Ne rien faire (n) /n -Mettre en réserve (r) /n -Déployer unité (d) /n -Attaquer (a)")
            if(action == "n" or action == "r" or action == "d" or action == "a" ) :
                action_valide = true
                
        #Mise en réserve    
        if action == "r" :
            afficher_main(get_main(joueur))
            carte_choisi = input("Quelle carte souhaitez vous envoyer en réserve ?")
            while not est_dans_main(carte_choisi):
                carte_choisi = input("Quelle carte souhaitez vous envoyer en réserve ?")
            placer_dans_reserve(carte_choisi, get_reserve(joueur))
            retirer_de_main(carte_choisi, get_main(joueur))
        
        #Déploiement d'unité
        if action == "d" :
            if not reserve_vide(get_reserve(joueur)):
                afficher_reserve(get_reserve(joueur))
                carte_choisi = piocher_dans_reserve(joueur)
                print("A quelle position souhaitez vous placer votre carte ??")
                afficher_cdb(get_cdb(joueur))
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(case_choisi):
                    case_choisi = input("Position choisie : ")
                placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)            

            else :
                print("Vous n'avez plus de cartes en réserve, choisissez une carte de votre main")
                afficher_main(get_main(joueur))
                carte_choisi = input("Quelle carte souhaitez vous envoyer sur le champ de bataille?")
                while not est_dans_main(carte_choisi):
                    carte_choisi = input("Quelle carte souhaitez vous envoyer sur le champ de bataille?")
                
                print("A quelle position voulez-vous la placer ?")
                afficher_cdb(get_cdb(joueur))
                case_choisi = input("Position choisie : ")
                while not est_position_utilisable(case_choisi):
                    case_choisi = input("Position choisie : ")
                placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)            
                retirer_de_main(get_main(joueur), carte_choisi)
        
        #Attaque
        if action == "a" : #Les points de défenses des cartes attaquées seront remis à leur valeur par défaut une fois la phase d'attaque terminé
            if joueur == 1:
                print("Champ de bataille du joueur 2 : ")
                afficher_cdb(2)
                print("Champ de bataille du joueur 1 : ")
                afficher_cdb(1)
            else :
                print("Champ de bataille du joueur 1 : ")
                afficher_cdb(1)
                print("Champ de bataille du joueur 2 : ")
                afficher_cdb(2)
                
            fin_attaque = false
            
            #On commence la boucle d'attaque, le joueur va faire attaquer ses cartes une par une
            while not fin_attaque :
                #On demande la carte qui va attaquer et on effectue les vérifications nécessaires dessus
                #elle doit être dans le cdb du joueur et en position défensive
                carte_choisi = input("Avec quelle carte souhaitez vous attaquer ?")
                while not est_dans_cdb(carte_choisi,get_cdb(joueur)) or not est_en_position_defensive(carte_choisi,get_cdb(joueur)):
                    if not est_dans_cdb(carte_choisi,get_cdb(joueur)) :
                        carte_choisi = input("Cette carte n'est pas dans le champ de bataille, veuillez en choisir une autre")
                    elif not est_en_position_defensive(carte_choisi,get_cdb(joueur)) :
                        carte_choisi = input("Cette carte est déjà en position offensive, elle ne peut plus attaquer du tour, veuillez en choisir une autre")
                
                #On demande la cible à attaquer et on effectue les vérifications dessus 
                cible = input("Quelle carte adverse souhaitez vous attaquer ?")
                
                #Vérification de portée
                est_a_portee = touche(carte_choisi, cible)
                
                #Vérification de présence de la cible dans le cdb adverse
                if joueur == 1 :
                    est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(2))
                if joueur == 2 :
                    est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(1))
                
                while not est_a_portee or not est_dans_cdb_adverse :
                    if not est_dans_cdb_adverse :
                        cible = input("La cible n'est pas dans le cdb adverse, veuillez en choisir une autre")
                        if joueur == 1 :
                            est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(2))
                        if joueur == 2 :
                            est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(1))
                    elif not est_a_portee :
                        cible = input("La cible n'est pas à portée, veuillez en choisir une autre")
                        est_a_portee = touche(carte_choisi, cible)
                
                passer_en_position_offensive(carte_choisi,get_cdb(joueur))
                attaquer(carte_choisi,cible)
                
                #On vérifie le nombre de points de défense restant à la carte attaquer et on agit en fonction
                if get_point_de_defense(cible) == 0 : #Cas où la cible est capturée
                    if joueur == 1:
                        position = get_position_carte(cible,get_cdb(2))
                        retirer_cdb(cible,get_cdb(2))
                        avancer_unite(position,get_cdb(2))
                        placer_dans_royaume(cible,get_royaume(1))
                    else :
                        position = get_position_carte(cible,get_cdb(1))
                        retirer_cdb(cible,get_cdb(1))
                        avancer_unite(position,get_cdb(1))
                        placer_dans_royaume(cible,get_royaume(2))
                elif get_point_de_defense(cible) < 0 : #Cas où la cible est détruite
                    if joueur == 1 :
                        position = get_position_carte(cible,get_cdb(2))
                        retirer_cdb(cible,get_cdb(2))
                        avancer_unite(position,get_cdb(2))
                        placer_dans_cimetiere(cible,get_cimetiere(2))
                    else :
                        position = get_position_carte(cible,get_cdb(1))
                        retirer_cdb(cible,get_cdb(1))
                        avancer_unite(position,get_cdb(1))
                        placer_dans_cimetiere(cible,get_cimetiere(1))
                
                
                #On vérifie maintenant si la carte capturé ou tuer est le roi adverse pour savoir si la partie est fini (exécution)
                #on sort uniquement de la boucle d'attaque il faut donc refaire la vérif après ce while pour sortir de la boucle de jeu (ligne 362)
                if get_point_de_defense(cible) <= 0 and est_roi(cible):
                    partie_fini = true
                    raison_fin = "ex"
                    if joueur == 1 :
                        joueur_perdant = 2
                    else :
                        joueur_perdant = 1
                    break
                
                #On veut maintenant savoir si le joueur continue à attaquer, on stoppe la phase d'attaque si toutes les cartes du joueur sont en positions offensives
                #ou si il n'a plus de cartes pouvant attaquer                 
                suite = "o"
                if joueur == 1 :
                    possibilite_attaquer = possibilite_attaquer(get_cdb(1),get_cdb(2))
                else :
                    possibilite_attaquer = possibilite_attaquer(get_cdb(2),get_cdb(1))
                    
                if not possibilite_attaquer:
                    suite = "n"
                else :                
                    suite = input("Voulez vous continuer à attaquer ? (o\/n")
                    suite_valide = false
                    if suite == "n" or suite == "o" :
                        suite_valide = true
                    while not suite_valide :
                        print("Veuillez entrer 'o' ou 'n'")
                        suite = input("Voulez vous continuer à attaquer ? (o\/n")
                        if suite == "n" or suite == "o" :
                            suite_valide = true
                    
                if suite == "n" :
                    fin_attaque = true
            #---Fin de la boucle d'attaque si fin_attaque == true, soit le joueur ne peut plus attaquer, soit il décide d'arrêter d'attaquer

            #On remet les points de défense des cartes de l'adversaire à leur état initial
            if joueur == 1:
                reinitialiser_carte(2) 
            else :
                reinitialiser_carte(1)
            
            
        #On sort de la boucle de jeu si la partie est fini (exécution)
        if partie_fini==true:
            break
    #---Fin de la phase d'action




    #Début de la phase de développement
        print("Début de la phase de développement")
        print("Votre main :")
        afficher_main(get_main(joueur))
        
        if get_nombre_carte_main(get_main(joueur))==6 :
            print("Vous êtes obligé de faire un développement car vous possédez plus de 6 cartes en main")
            R=input("Quelles cartes voulez vous envoyer dans votre royaume")
            while not est_dans_main(R):
                print("Cette carte n'est pas dans votre main")
                R=input("Choisissez une autre carte")
        else :
            Y=input("Voulez vous envoyer une carte de votre main dans le royaume? (o/n)")
            input_valide = false
            if Y == "o" or Y=="n" :
                input_valide = true
            while not input_valide :
                print("Veuillez entrer 'o' ou 'n'")
                Y=input("Voulez vous envoyer une carte de votre main dans le royaume? (o/n)")
                if Y == "o" or Y=="n" :
                    input_valide = true
        
        if Y=="o":
            R=input("Quelles cartes voulez vous envoyer dans votre royaume")
            while not est_dans_main(R):
                print("Cette carte n'est pas dans votre main")
                R=input("Choisissez une autre carte")
        
        placer_dans_royaume(R, get_royaume(joueur))
    #---Fin de la phase de développement
    
        if joueur == 2 :
            joueur = 1
        else:
            joueur = 2
    #---Fin de la boucle de jeu
    
    if raison_fin == "ef" :
        print("Le royaume du joueur " + str(joueur_perdant) + "s'est effondré !  Fin de la partie ! ")
    elif raison_fin == "ex" :
        print("Le roi du joueur " + str(joueur_perdant) +"est mort !  Fin de la partie ! ")
    elif raison_fin == "f":
        nb_carte_royaume_joueur1 = get_nombre_carte_royaume(get_royaume(1))
        nb_carte_royaume_joueur2 = get_nombre_carte_royaume(get_royaume(2))
        print("Le joueur " + joueur_sans_carte + "n'a plus de carte dans sa pioche !  Fin de la guerre ! ")
        print("Le joueur 1 possède " + nb_carte_royaume_joueur1 + " dans son royaume")
        print("Le joueur 2 possède " + nb_carte_royaume_joueur2 + " dans son royaume")
        if nb_carte_royaume_joueur1 > nb_carte_royaume_joueur2 :        
            print("Le joueur 1 remporte la partie ! ")
        elif nb_carte_royaume_joueur1 < nb_carte_royaume_joueur2 :
            print("Le joueur 2 remporte la partie ! ")
        else :
            print("Egalité ! ")

            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    ################### Début spécification fonctionnelle ################        


#Les fonctions creer main, reserve, royaume, cimetière,
#champ de bataille sont des in/out à affilier à un joueur, 
#le paramètre int est l’identifiant du joueur, la fonction renvoi 0

#Beaucoup de nos fonctions utilisent le principe de in/out, c'est donc la/les variable(s) passée(s) en paramètre qui est/sont modifiée(s) 
#on accorde donc peu d'importance à la valeur de retour des fonctions dans la plupart des cas


#Renvoie la réserve d’un joueur
#getReserve : joueur -> reserve
def get_reserve(joueur):
    return 0

#Renvoie le royaume d’un joueur
#getRoyaume : joueur -> royaume
def get_royaume(joueur):
    return 0

#Renvoie le cimetière d’un joueur
#getCimetière : joueur -> cimetière
def get_cimetiere(joueur):
    return 0

#Renvoie la main d’un joueur
#getMain(joueur) : joueur -> Main
def get_main(joueur):
    return 0

#get_joueur_entitee: entitee ->joueur
#renvoie le joueur auquel appartient l’entitee e
def get_joueur_entitee(e):
    return 0
    
def test6_getJoueurEnt():
    p= get_joueur_entitee(get_royaume(1))
    return p==1
    


###PIOCHE

#Pour creer une pioche on utilise la fonction
#creer_carte et on ajoute ces cartes dans la pioche (on rappelle qu'au début de la partie il y a 9 Soldats, 6 Gardes et 5 Archers)

#CreerPioche: int -> int
#Creer la pioche d’un joueur j, avec les cartes qu’on veut dedans en in/out
def creer_pioche(j):
    return 0


#Placer_dans_pioche: pioche, carte, nb -> pioche
#Place dans la pioche p le nombre nb cartes c
#CI: carte doit être de type connue (archer, garde, soldat, roi), la pioche doit exister
def placer_dans_pioche(p,c,nb):
    return 0


#getPioche : joueur -> pioche
#Renvoie la pioche d’un joueur j
#CI: la pioche et le joueur doivent exister
def get_pioche(j):
    return 0


#melanger_pioche : joueur -> int
#Melange la pioche d’un joueur j en in/out (modifie la pioche)
#CI la pioche doit exister
def melanger_pioche(j):
    return 0

#Piocher_Carte: pioche -> carte 
#Renvoie la première carte de la pioche p et la retire de la pioche
#CI : la pioche doit exister
def piocher_carte(p):
    return 0

#get_type_carte: carte -> type
#renvoie le type de la carte c
def get_type_carte(c):
    return 0

#pioche_vide: pioche -> bool
#renvoie true si la pioche p n’a plus de carte
def pioche_vide(p):
    return 0

def test1_creerPioche():
    p=creer_pioche(1)
    return get_joueur(p) ==1

def test7_melangerPioche():
    P= creer_pioche()
    T=P
    melanger_pioche(P)
    return T!=P

def test9_getTypeCarte():
    P= creer_carte(creer_carte(creer_archer()))
    return get_type_carte(P)==  "archer"
    
def test8_piochercarte():
    j=creer_pioche(1)
    P=piocher_carte(j)
    return get_type(P)!= null
    

###MAIN

#La main est vide quand on la crée, on la remplit dans le main du programme

#Creer_main: int -> int
#Creer la main d’un joueur en in/out
def creer_main():
    return 0

#Placer_dans_main : carte x mains-> int
#ajoute carte c dans la main m du joueur modifie en in/out
def placer_dans_main(c,m):
    return 0

#Afficher_main : main -> affichage
#Affiche la main du joueur j, avec les types marqué
def affiche_main(j):
    return 0

#Retirer_de_main : carte x main -> int
# retire une carte du même type que la carte c de la main m, en in/out
#CI : on vérifie que cette carte est dans main
def retirer_de_main(c,m):
    return 0

#main_vide : main -> bool
#Renvoie True si la main m est vide
def main_vide(m):
    return 0

#get_nombre_carte_main: main ->int
#Renvoie le nombre de carte qu’il y a dans la main m
def  get_nombre_carte_main(m):
    return 0


#est_dans_main: type x main -> bool
#renvoie true si il existe au moins une carte du type t dans la main m
def est_dans_main(t,m):
    return 0

def test2_creerMain():
    p=creer_main(1)
    return get_joueur(p) ==1


def test10_PlacerdansMain():
    P= creer_main(1)
    placer_dans_main(creer_carte(creer_archer()),P)
    return est_dans_main(creer_carte(creer_archer()),P)

def test11_EstDansMain():
    P=creer_main(1)
    placer_dans_main(creer_carte(creer_archer()),P)
    if not est_dans_main(creer_carte(creer_archer()),P):
        return False
    retirer_de_main(creer_carte(creer_archer()),P)
    return not est_dans_main(creer_carte(creer_archer()),P)


def test12_retirer_de_main():
    P=creer_main(1)
    placer_dans_main(creer_carte(creer_archer()),P)
    retirer_de_main(creer_carte(creer_archer()),P)
    return not est_dans_main(creer_carte(creer_archer()),P)

def test13_get_nombre_carte_main():
    P=creer_main(1)
    i=1
    while i<10 :
        placer_dans_main(creer_carte(creer_archer()),P)
        if i != get_nombre_carte_main(P):
            return False
        i+=1
    return True
    

###CHAMP DE BATAILLE 

#Le champ de bataille est vide quand on le crée,
#on le remplit dans le main du programme

#Creer_cdb: int -> int
#Creer le champ de bataille d’un joueur j, avec les positions. en in/out
def creer_cdb(j):
    return 0

#Placer_cdb : carte x champ_de_bataille x position-> int
#Ajoute une carte c sur le champ de bataille cdb à la position p si celle-ci est une position vide, en in/out.
#Il ne faut pas oublier de prendre en compte le fait que si on place une carte sur une position occupé
#alors la carte occupant la position est remplacée et renvoyée dans la main
#resultat : champ_de_bataille auquel on a ajouté c 
def placer_cdb(c, cdb, p):
    return 0

def test14_PlacerdansCDb(position):
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P,position)
    return est_dans_cdb(creer_carte(creer_archer()),P)

#est_dans_cdb: type x cdb -> bool
#renvoie true si il existe au moins une carte du type t dans le champ de bataille cdb
def est_dans_cdb(t,cdb):
    return 0

def test11_EstDansCdb():
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P)
    if not est_dans_cdb(creer_carte(creer_archer()),P):
        return False
    retirer_cdb(creer_carte(creer_archer()),P)
    return not est_dans_cdb(creer_carte(creer_archer()),P)

#position_vide : position x champ_de_bataille -> bool
#Renvoie True si la position p du champ_de_bataille cdb est vide
def position_vide(p, cdb):
    return 0

def test15_positionVide(position):
    P=creer_cdb(1)
    if not position_vide(position,P):
        return false
    placer_cdb(creer_carte(creer_archer()),P,position)
    return position_vide((position,P))

#Retirer_cdb: position x cdb -> int
#Retire la carte sur la position p du champ de bataille cdb, en in/out
def retirer_cdb(p,cdb):
    return 0

def test16_retirerCDB(position):
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P,position)
    retirer_cdb(position,P)
    return not est_dans_cdb(creer_carte(creer_archer()),P)


#is_front: position, cdb -> bool
#Renvoie true si il y a une carte devant la position p du champ de bataille cdb
#CI: position doit exister dans champ de bataille
def is_front(p, cdb):
    return 0
    
def test17_isfront(positionFront,positionarriere):
    P= creer_cdb(1)
    if not is_front(positionarriere,P):
        return false
    placer_cdb(creer_carte(creer_archer()),P,positionFront)
    return is_front(positionarriere,P)

#get_Position_Utilisable : cdb -> positions utilisables
#Renvoie les positions du champ de bataille cdb où il est possible de poser une #unité (si il y a pas une carte sur le front devant peut pas poser derrière sur le ligne #arrière. Il faut utiliser position_vide() et is_front()
def get_position_utilisable(cdb):
    return 0


#Est_position_utilisable: cdb x position -> bool
#renvoie true si la position p est utilisable sur le champ de bataille cdb (utiliiser get_position_utiliisable
def est_position_utilisable(cdb,p):
    return 0

#Afficher_cdb: cdb -> affichage
#Affiche champ de bataille du joueur j
def afficher_cdb(cdb):
    return 0

#Mettre_en_position_def: cdb -> int
#Met toutes les cartes d’un champ de bataille cdb en position defensive
def mettre_en_position_def(cdb):
    return 0


def test18_MettreEnpositionDef():
    P= creer_cdb(1)
    C=creer_archer()
    placer_cdb(C,P,position)
    put_offensive(C)
    mettre_en_position_def(P)
    return est_en_position_defensive(C,P)
    
#get_nombre_carte_cdb: cdb -> int
#Renvoie le nombre de carte qu’il y a sur le champ de bataille cdb
def get_nombre_carte_cdb(cdb):
    return 0

def test20_get_nombre_carte_cdb():
    P=creer_cdb(1)
    i=1
    while i<10 :
        placer_cdb(creer_carte(creer_archer()),P)
        if i != get_nombre_carte_cdb(P):
            return False
        i+=1
        return True

#reste_carte_en_position_defensive: cdb -> bool:
#Renvoie True si il reste au moins une carte en position défensive
def reste_carte_en_carte(cdb):
    return 0

#possibilité_attaquer: cdb x cdb -> bool
#renvoie true si le champ de bataille cdb1 a des cartes pouvant attaquer une des 
#cartes du cdb2
def possibilite_attaquer(cdb1,cdb2):
    return 0

#unite_precedente: position -> bool
#renvoie true si la position p une unite derrière elle
def unite_precedente(p):
    return 0

#avancer_unite: position x cdb -> int
#Avance la carte sur le front, modifie en in/out le champ de bataille
#Le front ne doit pas être occupé par une autre carte
def avancer_unite(p, cdb):
    return 0

def test3_creerCdb():
    p=creer_cdb(1)
    return get_joueur(p) ==1



###RESERVE 

#La réserve est vide quand on la crée, on la remplit dans le main du programme

#Creer_reserve: int -> int
#Creer la réserve d’un joueur j, en in/out
def creer_reserve(j):
    return 0

#placer_dans_reserve : carte x reserve -> int
#Met en réserve une carte c dans la reserve r, en in/out
#resultat : 0
def placer_dans_reserve(c, r):
    return 0

def test10_PlacerdansReserve():
    P= creer_reserve(1)
    placer_dans_reserve(creer_carte(creer_archer()),P)
    return est_dans_reserve( creer_carte(creer_archer()),P)

#est_dans_reserve: carte x res -> bool
#return true si carte c est dans réserve res
def est_dans_reserve(c,res):
    return 0

def test11_EstDansreserve():
    P=creer_reserve(1)
    placer_dans_reserve(creer_carte(creer_archer()),P)
    if not est_dans_reserve(creer_carte(creer_archer()),P):
        return False
    retirer_de_reserve(creer_carte(creer_archer()),P)
    return not est_dans_reserve(creer_carte(creer_archer()),P)

#Afficher_Reserve: reserve -> affichage
#Affiche à l’écran la réserve r
def afficher_reserve(r):
    return 0

#get_nombre_carte_reserve: reserve ->int
#Renvoie le nombre de carte qu’il y a dans la reserve r
def get_nombre_carte_reserve(r):
    return 0

def test19_get_nombre_carte_reserve():
    P=creer_reserve(1)
    i=1
    while i<10 :
        placer_dans_reserve(creer_carte(creer_archer()),P)
        if i!= get_nombre_carte_reserve(P):
            return False
        i+=1
        return True

#piocher_reserve: reserve -> carte
#Retourne la première carte mise dans réserve res et la retire
def piocher_dans_reserve(res):
    return 0

def test5_creerReserve():
    p=creer_reserve(1)
    return get_joueur(p) ==1



###ROYAUME

#Le royaume est vide quand on le crée, on le remplit dans le main du programme

#Creer_royaume: int -> int
#Creer le royaume d’un joueur j, en in/out
def creer_royaume(j):
    return 0

#placer_dans_royaume : carte x royaume -> int
#Place une carte c dans le royaume r, en in/out
def placer_dans_royaume(c, r):
    return 0
    
def test10_PlacerdansRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    return est_dans_royaume(creer_carte(creer_archer()),P)


#get_nombre_carte_royaume: royaume -> int
#Renvoie le nombre de carte d’un royaume roy 
def get_nombre_carte_royaume(roy):
    return 0

def test21_get_nombre_carte_royaume():
    P=creer_royaume(1)
    i=1
    while i<10 :
        placer_dans_royaume(creer_carte(creer_archer()),P)
        if i != get_nombre_carte_royaume(P):
            return False
        i+=1
        return True

#Afficher_Royaume: royaume -> affichage
#affiche le royaume roy
def afficher_royaume(roy):
    return 0

#Retirer_carte_royaume: royaume x carte -> int
#Retire une carte c du royaume r, en in/out
def retirer_du_royaume(r,c):
    return 0

def test10_retirerCarteRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    retirer_carte_royaume(t)
    return not est_dans_royaume(creer_carte(creer_archer()),P)


def test4_creerRoyaume():
    p=creer_royaume(1)
    return get_joueur(p) ==1

#verif

#est_dans_royaume: type -> bool
#renvoie true si il existe au moins une carte du type t dans le royaume
def est_dans_royaume(t):
    return 0
    
def test11_EstDansRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    if not est_dans_royaume(creer_carte(creer_archer()),P):
        return False
    retirer_carte_royaume(creer_carte(creer_archer()),P)
    return not est_dans_royaume(creer_carte(creer_archer()),P)

###CIMETIERE

#Le cimetière est vide quand on le crée, on le remplit dans le main du programme

#creer_cimetiere: int -> int
#creer le cimetière d’un joueur en in/out
def creer_cimetiere(j):
    return 0


#placer_dans_cimetiere: carte x cimetiere -> int
#Place la carte c dans le cimetière cim, en in/out
#renvoie le cimetière
def placer_dans_cimetiere(c,cim):
    return 0

def test10_PlacerdansCimetiere():
    P= creer_cimetiere(1)
    placer_dans_cimetiere(creer_carte(creer_archer()),P)
    return est_dans_cimetiere(creer_carte(creer_archer()),P)


#est_dans_cimetiere:  carte -> bool
#renvoie true si la carte c est dans le cimetière
def est_dans_cimetiere(c):
    return 0

def test5_creerCimetiere():
    p=creer_cimetiere(1)
    return get_joueur(p) ==1
    

###UNITES

#creer_carte: unite -> carte
#creer une carte selon une unité u avec un état par défaut défensif
#type doit exister
def creer_carte(u):
    return 0

#get_position_carte: carte x cdb -> int
#Renvoie la position de la carte c sur le champ de bataille cdb 
def get_position_carte(c,cdb):
    return 0

#est_en_position_defensive: carte x cdb-> bool
#vérifie si une carte est en position défensive dans un cdb
#pré-condition : la carte doit être dans le cdb
#résultat : True si la carte est en position défensive, false sinon
def est_en_position_defensive(c):
    return 0

#mettre_en_offensive: carte  -> int
#met une carte c en état offensif en in/out
def mettre_en_offensif(c):
    return 0

#mettre_en_defensive: carte -> int
#met une carte c en état défensif in/out
def mettre_en_defensive(c):
    return 0

#get_attaque : unite -> int
# renvoie l’attaque d’une carte c
def get_attaque(c):
    return 0

#get_def_def : unite -> int
# renvoie la défense defensive d’une carte c 
def get_def_def(c):
    return 0

#get_def_off : unite -> int
# renvoie la valeur de la défense offensive d’une carte c 
def get_def_off(c):
    return 0




##ARCHER

#Creer_Archer: Int -> unite
# Renvoie une carte archer, avec son type, l’attaque, la défense en position défensive et offensive.
def creer_type_archer() :
    return 0
def test22_CreerArcher():
    C= creer_carte(creer_archer())
    return get_type_carte(C)=="archer"
    


#Portee_Archer: position -> positions atteignables
#Renvoie les postions atteignables par un archer sachant sa position p.
def portee_archer(p):
    return 0


##SOLDAT

#Creer_soldat: Int -> unite
#Renvoie une carte soldat, avec son type, l’attaque, la défense en position défensive et offensive.
def creer_soldat():
    return 0

def test22_CreerSoldat():
    C= creer_carte(creer_soldat())
    return get_type_carte(C)=="soldat"

#Portee_soldat: position -> positions atteignables
#Renvoie les positions atteignables par un soldat sachant sa position p.
def portee_soldat(p):
    return 0

##GARDE

#Creer_garde: Int -> unite
# Renvoie une carte garde, avec son type, l’ attaque, la défense en position défensive et offensive.
def creer_garde():
    return 0

def test22_CreerGarde():
    C=creer_carte(creer_garde())
    return get_type_carte(C)=="garde"

#Portee_garde: position -> positions atteignables
#Renvoie les postions atteignables par un garde sachant sa position p.
def portee_garde(p):
    return 0


##Roi1

#Creer_roi1: Int -> unite
# Renvoie une carte roi1, avec son type, l’ attaque, la défense en position défensive et offensive.
def creer_roi1() :
    return 0

def test22_CreerRoi1():
    C= creer_carte(creer_roi1())
    return get_type_carte(C)=="roi1"

#Portee_roi1: position -> positions atteignables
#Renvoie les postions atteignables par un roi1 sachant sa position p.
def portee_roi1 (p):
    return 0

##Roi2

#Creer_roi2: Int -> unite
# Renvoie une carte roi2, avec son type, l’ attaque, la défense en position défensive et offensive.
def creer_roi2() :
    return 0

#Portee_roi2: position -> positions atteignables
#Renvoie les postions atteignables par un roi2 sachant sa position p.
def portee_roi2 (p):
    return 0

def test22_CreerRoi2():
    C= creer_carte(creer_roi2())
    return get_type_carte(C)=="roi2"

#est_roi: carte -> bool
#renvoie True si la cart c est un roi
def est_roi(c):
    return 0
def test22_CreerRoi2():
    C= creer_carte(creer_roi2())
    return est_roi(C)

# COMBAT

#Touche: carte x carte -> bool
#Renvoie True si selon sa portée c_att touche c_def, on extrait le type
#de la carte attaquante et détermine la fonction de portee à utiliser en fonction
def touche(c_att,c2_def):
    return 0

def test23_touche():
    return 0
#attaquer: carte x carte  -> int
#La première carte c1 attaque la deuxième c2, on soustrait les points de défense  
#de la carte 2 avec les points d’attaque de la carte 1 les paramètres sont placés en in/out
#Ne pas oublier de vérifier si la carte attaqué et en position offensive ou défensive
def attaquer(c1,c2):
    return 0


def test24_attaquer():
    return 0

#Reinitialiser_carte: joueur -> int
#Remet la défense de toutes les cartes du champ de bataille et du royaume du #joueur j à leur état initiale. Peut les supprimer et les recréer par exemple. 
def reinitialiser_carte(j):
    return 0







