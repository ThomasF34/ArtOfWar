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
	while !est_dans_main(carte_choisi) :
		carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 1")
		
	#On affiche le champ de bataille pour que le joueur connaisse les positions disponibles
	afficher_cdb(get_position_utilisable_cdb(get_cdb(joueur1)))
	case_choisi = input("Quelle case de la ligne de front ?" )
	while !est_position_utilisable(case_choisi):
		case_choisi = input("Quelle case de la ligne de front ?" )
	placer_cdb(carte_choisi, get_cdb(joueur1), case_choisi)
	retirer_de_main(carte_choisi, get_main(joueur1))
	#---
	
	#Le second joueur choisit une carte de sa main et la place sur sa ligne de front
	afficher_main(get_main(joueur2))
	carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 2")
	while !est_dans_main(carte_choisi) :
		carte_choisi = input("Choisir la carte à placer sur la ligne de front du joueur 2")
		
	afficher_cdb(get_position_utilisable_cdb(get_cdb(joueur2)))
	case_choisi = input("Quelle case de la ligne de front ?")
	while !est_position_utilisable(case_choisi) :
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
	while !est_dans_main(carte_choisi) :
		carte_choisi = input("Choisir la carte à placer en réserve du joueur 2")	
	placer_dans_reserve(carte_choisi, get_reserve(joueur2))
	retirer_de_main(carte_choisi, get_main(joueur2))
	#---
#Fin de la phase de mise en place


	joueur = 1 #Le joueur 1 commence le premier

 	
#début de la boucle de jeu
	while !fin() :

#Début de la phase conscription
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
			while !est_position_utilisable(get_cdb(joueur),case_choisi) : 
				case_choisi = input("Position choisie : ")
			derniere_carte_reserve = piocher_dans_reserve(get_reserve(joueur))
			placer_cdb(derniere_carte_reserve, get_cdb(joueur), case_choisi)
			#---
			
			#On choisit la carte de notre royaume et sa position sur le champ de bataille
			print("Quelle carte de votre royaume souhaitez vous placer sur le champ de bataille")
			afficher_royaume(get_royaume(joueur))
			
			carte_choisi = input("Carte choisie : ")
			while !est_dans_royaume(carte_choisi) : 
					carte_choisi = input("Carte choisie : ")
			print("A quelle position voulez-vous la placer ?")
			afficher_cdb(get_cdb(joueur))
			case_choisi = input("Position choisie : ")
			while !est_position_utilisable(case_choisi):
				case_choisi = input("Position choisie : ")
			placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)			
			retirer_du_royaume(get_royaume(joueur), carte_choisi)

		if get_nombre_carte_reserve(get_reserve(joueur))>1:
			#On choisit la carte de notre reserve et on indique la position à laquelle on souhaite la poser sur le champ de bataille
			print("Les deux premières cartes de votre réserve vont être placées sur le champ de bataille")
			afficher_reserve(get_reserve(joueur))
			
			case_choisi = input("A quelle position souhaitez vous placer la première carte de votre réserve ? : ")
			while !est_position_utilisable(case_choisi) :
				carte_choisi = input("A quelle position souhaitez vous placer la première carte de votre réserve ? : ")
			placer_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)
			
			case_choisi = input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : ")
			while !est_position_utilisable(case_choisi) :
				carte_choisi = input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : ")
			placer_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)
			
		else :
			print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
			print("Veuillez choisir la première carte de votre royaume que vous souhaitez placer sur le champ de bataille")
			afficher_royaume(get_royaume(joueur))
			
			carte_choisi = input("Carte choisie : ")
			while !est_dans_royaume(carte_choisi) : 
					carte_choisi = input("Carte choisie : ")
			print("A quelle position voulez-vous la placer ?")
			afficher_cdb(get_cdb(joueur))
			case_choisi = input("Position choisie : ")
			while !est_position_utilisable(case_choisi):
				case_choisi = input("Position choisie : ")
			placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)			
			retirer_du_royaume(get_royaume(joueur), carte_choisi)
			
			print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
			print("Veuillez choisir la deuxième carte de votre royaume que vous souhaitez placer sur le champ de bataille")
			afficher_royaume(get_royaume(joueur))
			
			carte_choisi = input("Carte choisie : ")
			while !est_dans_royaume(carte_choisi) : 
					carte_choisi = input("Carte choisie : ")
			print("A quelle position voulez-vous la placer ?")
			afficher_cdb(get_cdb(joueur))
			case_choisi = input("Position choisie : ")
			while !est_position_utilisable(case_choisi):
				case_choisi = input("Position choisie : ")
			placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)			
			retirer_du_royaume(get_royaume(joueur), carte_choisi)
		
#--- Fin de la phase de conscription
	
#Début de la phase de préparation
	mettre_en_position_def(get_cdb(joueur))
	placer_dans_main(piocher_carte(get_pioche(joueur)),get_main(joueur))
	
#---Fin de la phase de préparation

#Début de la phase d'action
	afficher_cdb(get_cdb(joueur))
	afficher_royaume(get_royaume(joueur))
	afficher_main(get_main(joueur))
	afficher_reserve(get_reserve(joueur))
	action = input("Que souhaitez vous faire ? /n (Action possible : -Ne rien faire (n) /n -Mettre en réserve (r) /n -Déployer unité (d) /n -Attaquer (a)")
	
	if action == "r" :
		afficher_main(get_main(joueur))
		carte_choisi = input("Quelle carte souhaitez vous envoyer en réserve ?")
			while !est_dans_main(carte_choisi):
				carte_choisi = input("Quelle carte souhaitez vous envoyer en réserve ?")
		placer_dans_reserve(carte_choisi, get_reserve(joueur))
		retirer_de_main(carte_choisi, get_main(joueur))
	
	
	if action == "d" :
		if !reserve_vide(get_reserve(joueur)):
			afficher_reserve(get_reserve(joueur))
			carte_choisi = piocher_dans_reserve(joueur)
			print("A quelle position souhaitez vous placer votre carte ??")
			afficher_cdb(get_cdb(joueur))
			case_choisi = input("Position choisie : ")
			while !est_position_utilisable(case_choisi):
				case_choisi = input("Position choisie : ")
			placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)			

		else :
			print("Vous n'avez plus de cartes en réserve, choisissez une carte de votre main")
			afficher_main(get_main(joueur))
			carte_choisi = input("Quelle carte souhaitez vous envoyer sur le champ de bataille?")
			while !est_dans_main(carte_choisi):
				carte_choisi = input("Quelle carte souhaitez vous envoyer sur le champ de bataille?")
			
			print("A quelle position voulez-vous la placer ?")
			afficher_cdb(get_cdb(joueur))
			case_choisi = input("Position choisie : ")
			while !est_position_utilisable(case_choisi):
				case_choisi = input("Position choisie : ")
			placer_cdb(carte_choisi,get_cdb(joueur), case_choisi)			
			retirer_de_main(get_main(joueur), carte_choisi)
	
	if action == "a" :
		if joueur == 1
			afficher_cdb(2)
			afficher_cdb(1)
		else :
			afficher_cdb(1)
			afficher_cdb(2)
		
		while :
			cible = input()
			
	If x==« ne rien faire »:
	If x==« attaquer»: 
	Afficher
	demande qui attaquer
	Pour chaque faire un combat unité vs unité et stock t
#---Fin de la phase d'action



#phase action



#phase de développement
	Y=Input(« voulez vous envoyer une carte dans le royaume? ») 
	If nombreCarte(joueur.getMain())==6 or Y==oui:
	AfficherMain(joueur.getMain())
	R=input (« quel cartes (indices de carte voulez vous env dans le royaume »)
	joueur.getRoyaume().AjouterCarteRoy(R)

	if joueur == 2 :
		joueur = 1
	else joueur = 2
#---Fin de la boucle de jeu


#Renvoie la première carte de la réserve
#prendCarteReserve : reserve => carte
def prendCarteReserve()


#Place une carte sur une place défini du champ de bataille
#placer_cdb : CDB x place x Carte
def placer_cdb()  


#Dans réserve on doit forcément prendre la première carte.



	
		

#mettre_en_reserve : carte x reserve -> reserve
#Met en réserve une carte c dans la reserve r
#resultat : la reserve à  laquelle on a ajouté la carte c
def mettre_en_reserve(c, r)

#deployer_unite : carte x champ_de_bataille x position-> champ_de_bataille
#Déploie une carte c sur le champ de bataille cdb à  la position p
#resultat : champ_de_bataille auquel on a ajouté c 
def deployer_unite(c, cdb, p)

#reserve_vide : joueur -> bool
#Indique si la réserve du joueur j est vide
def reserve_vide(j) 

#placer_dans_royaume : carte x royaume -> royaume
#Place une carte c dans le royaume r
def placer_dans_royaume(c, r)

#position_vide : position x champ_de_bataille -> bool
#Indique si la position p du champ_de_bataille cdb est vide
def position_vide(p, cdb)

#main_vide : main -> bool
#Indique si la main m est vide
def main_vide(m)

class Main :
	#Crée une main 
	def Main()
	
	#Indique si la main est vide
	def estVide()

	#Renvoi la main
	def getMain()
	def setMain()
	def getJoueur()
	def setJoueur()
class Royaume :
	#Crée un royaume contenant 9 Soldats, 6 Gardes et 5 Archers 
	def Royaume()

	#Indique si le Royaume est vide 
	def estVide()
	def getRoyaume()
	def setRoyaume()
	
	#Ajoute une carte c dans le royaume 
	def ajouterCarte(c)

	#Retire une carte c du royaume
	def retirerCarte(c)

	#Renvoi le joueur associé au royaume 
	def getJoueur()
	
	#Défini le joueur à qui appartient le royaume
	def setJoeur() 

class CDB :
	def CDB()
	def getCdb()
	def setCdb()
	def getJoueur()
	def setJoueur()
	
class Carte :
	def Carte()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	#Renvoi le type de la carte
	def getType()
	#position x type_carte -> positions
	#Renvoi selon une position c et un type de carte tc les positions atteignable
	def getPortee(p, tc)
	def setMain()
	def getMain() 

class Soldat :
	def Soldat()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	def getPosition()
	
	#getPortee : position -> positions
	#Renvoi selon la position du Roi les positions atteignables
	def getPortee()
	def setMain()
	def getMain()

class RoiJ1 :
	def RoiJ1()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	def getPosition()

	#getPortee : position -> positions
	#Renvoi selon la position du Roi les positions atteignables
	def getPortee()
	def setMain()
	def getMain()

class RoiJ2 :
	def RoiJ2()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	def getPosition()
	#getPortee : position -> positions
	#Renvoi selon la position du Roi les positions atteignables
	def getPortee()
	def setMain()
	def getMain()

	
class Archer :
	def Archer()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	def getPosition()

	#getPortee : position -> positions
	#Renvoi selon la position de l’archer les positions atteignables
	def getPortee()
	def setMain()
	def getMain()

class Garde :
	def Garde()
	def getDefenseDefensive()
	def getDefenseOffensive()
	def getAttaque()
	def getPosition()

	#getPortee : position -> positions
	#Renvoi selon la position du garde les positions atteignables
	def getPortee()
	def setMain()
	def getMain()


Quand on pioche c’est bien de montrer la carte qu’on a pioché
