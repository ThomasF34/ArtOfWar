def test10_PlacerdansRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    return est_dans_royaume(creer_carte(creer_archer()),P)

def test21_get_nombre_carte_royaume():
    P=creer_royaume(1)
    i=1
    while i<10 :
        placer_dans_royaume(creer_carte(creer_archer()),P)
        if i != get_nombre_carte_royaume(P):
            return False
        i+=1
        return True

def test10_retirerCarteRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    retirer_carte_royaume(t)
    return not est_dans_royaume(creer_carte(creer_archer()),P)

def test4_creerRoyaume():
    p=creer_royaume(1)
    return get_joueur(p) ==1
    
def test11_EstDansRoyaume():
    P= creer_royaume(1)
    placer_dans_royaume(creer_carte(creer_archer()),P)
    if not est_dans_royaume(creer_carte(creer_archer()),P):
        return False
    retirer_carte_royaume(creer_carte(creer_archer()),P)
    return not est_dans_royaume(creer_carte(creer_archer()),P)
