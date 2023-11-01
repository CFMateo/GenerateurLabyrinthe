
from random import randint



def sequence(n):
    sequence = []
    for el in range(n):
        sequence.append(el)
    return sequence

#print(sequence(5)

def contient(tab,nombre):
    return nombre in tab

#print(contient([9,2,5], 4))


def ajouter(tab,nombre):
    if contient(tab,nombre):
        return tab
    else:
        tab.append(nombre)
        return tab

#print(ajouter([9,2,5], 2))
#print(ajouter([9,2,5], 4))


def retirer(tab,nombre):
    if contient(tab,nombre):
        tab.remove(nombre)
        return tab
    else:
        return tab
#print(retirer([9,2,5], 2))
#print(retirer([9,2,5], 4))



def voisins(x, y, largeur, hauteur):
    """
    Cette fonction prend la coordonnée (x,y) d'une cellule et 
    la taille d'une grille (largeur=nx et hauteur=ny) et retourne 
    un tableau contenant le numéro des cellules voisines. Par exemple :

    voisins(7, 2, 8, 4) = [15,22,31]

    """
    voisins = []

    coordoneesNord = [x, y-1]
    coordoneesEst = [x+1, y]
    coordoneesSud = [x, y+1]
    coordoneesOuest = [x-1, y]
    
    
    
    if 0 <= coordoneesNord[0] <= largeur-1 and 0 <= coordoneesNord[1] <= hauteur-1:
        voisinNord = (coordoneesNord[0] + coordoneesNord[1] * largeur) 
        voisins.append(voisinNord)

    if 0 <= coordoneesOuest[0] <= largeur-1 and 0 <= coordoneesOuest[1] <= hauteur-1:
        voisinOuest = (coordoneesOuest[0] + coordoneesOuest[1] * largeur)
        voisins.append(voisinOuest)
    
    
    if 0 <= coordoneesSud[0] <= largeur-1 and 0 <= coordoneesSud[1] <= hauteur-1:
        voisinSud = (coordoneesSud[0] + coordoneesSud[1] * largeur) 
        voisins.append(voisinSud)
    
    if 0 <= coordoneesEst[0] <= largeur-1 and 0 <= coordoneesEst[1] <= hauteur-1:
        voisinEst= (coordoneesEst[0] + coordoneesEst[1] * largeur) 
        voisins.append(voisinEst)
    

    return voisins

print(voisins(7, 2, 8, 4))





def laby(largeur,hauteur,dimension): #PAS OUBLIER LE PARAMETRE DIMENSION 
    """
    Cette procédure crée un labyrinthe aléatoire (largeur=nx et hauteur=ny) 
    et dessine ce labyrinthe dans la fenêtre de pixels en utilisant une grille 
    avec des cellules de dimension pixels de largeur et hauteur et des murs dont 
    l'épaisseur est 1 pixel. La valeur de dimension c'est le nombre de pixels entre 
    les lignes. Tous les paramètres sont des entiers >= 1. Le labyrinthe doit être noir sur fond blanc.

    set_screen_mode(10, 10)  # Crée une fenêtre de pixels 10x10

    for i in range(largeur):
        for j in range(hauteur):
            setPixel(i, j, "#FFF")
    
    """
    from random import randint

def laby(largeur, hauteur, dimension):
    """
    Crée un labyrinthe aléatoire (largeur=nx et hauteur=ny)
    et dessine le labyrinthe dans une fenêtre de pixels.
    """

    cellules_cavite = []
    frontiere = []
    
    murs_horizontaux = sequence(largeur * (hauteur + 1))
    murs_verticaux = sequence((largeur + 1) * hauteur)
    
   
    # On choisit aléatoirement la cavité initiale, en faisant en sorte que le numéro represente bien une cellule:
    caviteInit = 0
    while 0 <= caviteInit <= largeur - 1 or largeur * (hauteur + 1) - largeur - 1 <= caviteInit <= largeur * (hauteur + 1) - 1:
        caviteInit = randint(0, len(murs_horizontaux) - 1)
    ajouter(cellules_cavite, caviteInit)

    # Premier élement = x , deuxieme = y:
    coordonneCavite = [cellules_cavite[0] % largeur, cellules_cavite[0] // largeur]


    
    # On ajoute à la frontiere les voisins de la cavite initiale:
    frontiere = voisins(coordonneCavite[0], coordonneCavite[1], largeur, hauteur)
    
  

    while len(cellules_cavite) != largeur * hauteur:
        frontiere_aleatoire = frontiere[randint(0, len(frontiere) - 1)]
        x, y = frontiere_aleatoire % largeur, frontiere_aleatoire // largeur

        voisins_cavite = []

        if y > 0 and (x + (y - 1) * largeur) in cellules_cavite:
            voisins_cavite.append(x + (y - 1) * largeur)
        if y < hauteur - 1 and (x + (y + 1) * largeur) in cellules_cavite:
            voisins_cavite.append(x + (y + 1) * largeur)
        if x > 0 and (x - 1 + y * largeur) in cellules_cavite:
            voisins_cavite.append(x - 1 + y * largeur)
        if x < largeur - 1 and (x + 1 + y * largeur) in cellules_cavite:
            voisins_cavite.append(x + 1 + y * largeur)

        if voisins_cavite:
            voisin = voisins_cavite[randint(0, len(voisins_cavite) - 1)]

            if voisin == frontiere_aleatoire + 1:
                retirer(murs_verticaux, y * (largeur + 1) + x + 1)
            elif voisin == frontiere_aleatoire - 1:
                retirer(murs_verticaux, y * (largeur + 1) + x)
            elif voisin == frontiere_aleatoire + largeur:
                retirer(murs_horizontaux, (y + 1) * largeur + x)
            elif voisin == frontiere_aleatoire - largeur:
                retirer(murs_horizontaux, y * largeur + x)

            ajouter(cellules_cavite, frontiere_aleatoire)
            retirer(frontiere, frontiere_aleatoire)

            # Directions relatives des voisins
            voisins_relatifs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for voisin_x, voisin_y in voisins_relatifs:
                new_x, new_y = x + voisin_x, y + voisin_y
                new_cell = new_x + new_y * largeur

                # Vérification si la nouvelle cellule doit etre ajoutée a la fronti
                if 0 <= new_x < largeur and 0 <= new_y < hauteur and new_cell not in cellules_cavite and new_cell not in frontiere:
                    ajouter(frontiere, new_cell)


  

    print(murs_horizontaux,murs_verticaux)
    

   #Représentation du labyrinthe:
    setScreenMode((largeur*dimension)+1,(hauteur*dimension)+1)
    
    retirer(murs_horizontaux,0)
    print(murs_horizontaux[-1])
    retirer(murs_horizontaux,murs_horizontaux[-1])
    
    

    setScreenMode((largeur*dimension)+1,(hauteur*dimension)+1)

    for x in range(largeur*dimension):
        for y in range(hauteur*dimension):
            set_pixel(x,y,"#FFF")
        

    for y in range(hauteur):
        for x in range(largeur):
            # Murs murHorizontauxontaux:
            if contient(murs_horizontaux,x+y*largeur):
                for i in range(dimension):
                    set_pixel(x*dimension+i,y*dimension,"#000")

            # Murs murVerticauxcaux:
            if contient(murs_verticaux,x+y*(largeur+1)):
                for i in range(dimension):
                    set_pixel(x*dimension,y*dimension+i,"#000")

                    
                    
    

laby(8,4,10)