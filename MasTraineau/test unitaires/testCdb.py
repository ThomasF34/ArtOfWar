def test14_PlacerdansCDb(position):
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P,position)
    return est_dans_cdb(creer_carte(creer_archer()),P)

def test11_EstDansCdb():
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P)
    if not est_dans_cdb(creer_carte(creer_archer()),P):
        return False
    retirer_cdb(creer_carte(creer_archer()),P)
    return not est_dans_cdb(creer_carte(creer_archer()),P)

def test15_positionVide(position):
    P=creer_cdb(1)
    if not position_vide(position,P):
        return false
    placer_cdb(creer_carte(creer_archer()),P,position)
    return position_vide((position,P))


def test16_retirerCDB(position):
    P= creer_cdb(1)
    placer_cdb(creer_carte(creer_archer()),P,position)
    retirer_cdb(position,P)
    return not est_dans_cdb(creer_carte(creer_archer()),P)

def test17_isfront(positionFront,positionarriere):
    P= creer_cdb(1)
    if not is_front(positionarriere,P):
        return false
    placer_cdb(creer_carte(creer_archer()),P,positionFront)
    return is_front(positionarriere,P)

def test18_MettreEnpositionDef():
    P= creer_cdb(1)
    C=creer_archer()
    placer_cdb(C,P,position)
    put_offensive(C)
    mettre_en_position_def(P)
    return est_en_position_defensive(C,P)

def test20_get_nombre_carte_cdb():
    P=creer_cdb(1)
    i=1
    while i<10 :
        placer_cdb(creer_carte(creer_archer()),P)
        if i != get_nombre_carte_cdb(P):
            return False
        i+=1
        return True
        
def test3_creerCdb():
    p=creer_cdb(1)
    return get_joueur(p) ==1