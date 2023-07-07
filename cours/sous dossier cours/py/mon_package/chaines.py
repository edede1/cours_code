def inverser_chaine(chaine):
  
    resultat = chaine[::-1]
    return resultat


def compter_mots(chaine):
  
    mots = chaine.split()
    nombre_mots = len(mots)
    return nombre_mots
