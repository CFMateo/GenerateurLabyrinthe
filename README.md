L'algorithme se sert d'ensembles de numéros (dans le sens mathématique d'ensemble, c'est-à-dire une collection de nombres sans duplication).
On peut définir horiz comme l'ensemble de murs horizontaux (et respectivement verti comme l'ensemble de murs verticaux) qui n'ont pas été retirés par l'algorithme de création de labyrinthe.
L'information contenue dans ces ensembles peut être combinée avec les valeurs de nx et ny pour dessiner un labyrinthe en traçant une séquence horizontale de pixels pour chaque mur horizontal 
dont le numéro est toujours dans horiz et une séquence verticale de pixels pour chaque mur vertical dont le numéro est toujours dans verti.

L'algorithme considère que la grille est un espace initialement plein sauf pour une cellule choisie aléatoirement qui est vide (c'est la cavité initiale).
À chaque itération de l'algorithme une nouvelle cellule sera choisie aléatoirement parmi toutes les cellules voisines de la cavité (mais ne faisant pas partie de la cavité) et un des murs
(soit horizontal ou vertical) qui la sépare de la cavité sera retiré aléatoirement pour former une plus grande cavité (soit de l'ensemble horiz si c'est un mur horizontal ou de l'ensemble
verti si c'est un mur vertical). Ce processus est répété jusqu'à ce que toutes les cellules de la grille fassent partie de la cavité.

Le choix de la prochaine cellule à ajouter à la cavité peut se faire simplement en conservant en tout temps deux autres ensembles de numéros : cave et front. 
Ce sont des ensemble qui contiennent des numéros de cellules. L'ensemble cave est l'ensemble des cellules qui ont été mis dans la cavité par l'algorithme. 
L'ensemble front est l'ensemble des cellules qui sont voisines des cellules dans la cavité (mais pas dans la cavité). On peut maintenir à jour ces ensembles au fur et à mesure qu'on sélectionne
des nouvelles cellules à ajouter à la cavité. En effet si on a ajouté à la cavité la cellule aux coordonnées (x,y) contenue dans l'ensemble front, il faut ajouter les cellules voisines à (x,y)
horizontalement et verticalement (mais pas dans l'ensemble cave) à l'ensemble front et retirer la cellule (x,y) de l'ensemble front et ajouter la cellule (x,y) à l'ensemble cave. 
Remarquez qu'on doit retirer ou ajouter de ces ensembles le numéro des cellules.
