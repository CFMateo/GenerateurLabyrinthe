
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

    if 0 <= coordoneesEst[0] <= largeur-1 and 0 <= coordoneesEst[1] <= hauteur-1:
        voisinEst= (coordoneesEst[0] + coordoneesEst[1] * largeur) 
        voisins.append(voisinEst)
    
    if 0 <= coordoneesSud[0] <= largeur-1 and 0 <= coordoneesSud[1] <= hauteur-1:
        voisinSud = (coordoneesSud[0] + coordoneesSud[1] * largeur) 
        voisins.append(voisinSud)
    

    if 0 <= coordoneesOuest[0] <= largeur-1 and 0 <= coordoneesOuest[1] <= hauteur-1:
        voisinOuest = (coordoneesOuest[0] + coordoneesOuest[1] * largeur)
        voisins.append(voisinOuest)
    

    return voisins

#print(voisins(4, 3, 8, 4))




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
    celluleCavite = []
    frontiere = []
    mursCavite = []

    index = 0
   


    murHorizontaux = sequence(largeur*(hauteur+1))
    murVerticaux = sequence((largeur+1)*hauteur)
    #print(murHorizontaux)
    #print(murVerticaux)
    caviteInit = 0

    # Sélection aléatoire de la cavité initiale:
    while 0<=caviteInit<=largeur-1 or largeur*(hauteur+1)-largeur-1<=caviteInit<=largeur*(hauteur+1)-1:
        caviteInit = randint(0, len(murHorizontaux) - 1)
    ajouter(celluleCavite,caviteInit)
    

   

    while len(celluleCavite) != largeur*hauteur:
        mursVoisins = []

        coordonneCavite = [celluleCavite[index] % largeur, celluleCavite[index] // largeur]
        # Numeros frontieres a la cavité:
        voisinsCavite = voisins(coordonneCavite[0], coordonneCavite[1], largeur, hauteur)
        for el in voisinsCavite:
            ajouter(frontiere,el)
        for i in range(len(celluleCavite)):
            retirer(frontiere,celluleCavite[i])
            retirer(voisinsCavite)
        
        
        print("cavite=",celluleCavite,"////frontiere=",frontiere)

        # Choix aleatoire parmis les numéros de la frontiere:
        voisinAleatoire = frontiere[randint(0,len(frontiere)-1)]
        coordonneVoisin = [voisinAleatoire% largeur, voisinAleatoire// largeur]
        print(voisinAleatoire)

        # On detérmine tout les murs des membres de la cavité:
        mursCavite.append(coordonneCavite[0] + coordonneCavite[1] * largeur)  # Mur Nord
        mursCavite.append(1 + coordonneCavite[0] + coordonneCavite[1] * (largeur + 1))
        mursCavite.append(coordonneCavite[0] + (coordonneCavite[1] + 1) * largeur)
        mursCavite.append(coordonneCavite[0] + coordonneCavite[1] * (largeur + 1))
        print("mursCavite=",mursCavite)
        
        # On detérmine tout les murs des membres du voisin aléatoire:
        mursVoisins.append(coordonneVoisin[0] + coordonneVoisin[1] * largeur)
        mursVoisins.append(1 + coordonneVoisin[0] + coordonneVoisin[1] * (largeur + 1))
        mursVoisins.append(coordonneVoisin[0] + (coordonneVoisin[1] + 1) * largeur)
        mursVoisins.append(coordonneVoisin[0] + coordonneVoisin[1] * (largeur + 1))
        print("MURS VOSIINS=",mursVoisins)

        

        # On cherche un mur commun entre la cellule aléatoire voisine et la cavité:
        for i in range(len(mursVoisins)):
                    if mursVoisins[i] in mursCavite:
                        ajouter(celluleCavite,voisinAleatoire)
                        retirer(frontiere, voisinAleatoire)
                        retirer(mursCavite,mursVoisins[i])
                        if i % 2 == 0:
                            retirer(murHorizontaux, mursVoisins[i])
                            retirer(mursVoisins,mursVoisins[i])
                            break
                        else:
                            retirer(murVerticaux, mursVoisins[i])
                            retirer(mursVoisins,mursVoisins[i])
                            break
                            
                        
        #On ajoute les murs de la cellule voisine chosie a la cavité:
        mursCavite.extend(mursVoisins)
        #print(murHorizontaux,murVerticaux)
        index+=1
        print("CELLULE CAVITE =",celluleCavite,"FRONTIERE =",frontiere,"MURS CAVITE=",mursCavite,"MURS VOISINS=",mursVoisins)
        print(murHorizontaux,murVerticaux)
    """
    #Représentation du labyrinthe:
    setScreenMode(largeur*dimension,hauteur*dimension)

    for y in range(hauteur):
        for x in range(largeur):
            # Murs horizontaux:
            if contient(murHorizontaux,x+y*largeur):
                for i in range(dimension):
                    set_pixel(x*dimension+i,y*dimension,"#FFF")

            # Murs verticaux:
            if contient(murVerticaux,x+y*(largeur+1)):
                for i in range(dimension):
                    set_pixel(x*dimension,y*dimension+i,"#FFF   ")

    
        """



laby(8,4,10)




        






