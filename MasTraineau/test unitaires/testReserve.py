def test10_PlacerdansReserve():
    P= creer_reserve(1)
    placer_dans_reserve(creer_carte(creer_archer()),P)
    return est_dans_reserve( creer_carte(creer_archer()),P)

def test11_EstDansreserve():
    P=creer_reserve(1)
    placer_dans_reserve(creer_carte(creer_archer()),P)
    if not est_dans_reserve(creer_carte(creer_archer()),P):
        return False
    retirer_de_reserve(creer_carte(creer_archer()),P)
    return not est_dans_reserve(creer_carte(creer_archer()),P)

def test19_get_nombre_carte_reserve():
    P=creer_reserve(1)
    i=1
    while i<10 :
        placer_dans_reserve(creer_carte(creer_archer()),P)
        if i!= get_nombre_carte_reserve(P):
            return False
        i+=1
        return True

def test5_creerReserve():
    p=creer_reserve(1)
    return get_joueur(p) ==1