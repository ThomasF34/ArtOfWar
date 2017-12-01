def test10_PlacerdansCimetiere():
    P= creer_cimetiere(1)
    placer_dans_cimetiere(creer_carte(creer_archer()),P)
    return est_dans_cimetiere(creer_carte(creer_archer()),P)

def test5_creerCimetiere():
    p=creer_cimetiere(1)
    return get_joueur(p) ==1