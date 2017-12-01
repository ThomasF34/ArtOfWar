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