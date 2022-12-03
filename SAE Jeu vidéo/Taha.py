from upemtk import *
from time import *

while True:
    evenement = donne_evenement()
    type_ev = type_evenement(evenement)
    print(type_ev)
    pass

#Programme principal ---------------------------------------------------------------------            
    #Demande à l'utilisateur de ses préférences
nombre_tour = int(input("Combien de tours souhaitez vous ? (un clic, un tour): "))

#Création de la fenetre et d'un message pour attendre le lancement du jeu
cree_fenetre(800,600)
rectangle(0, 0, 800, 50, remplissage="purple")
texte(400, 20,"Batailles des boules", ancrage="center")
txt = texte(400, 300, "READY?", taille="50", police="Monaco", ancrage="center")
attente_clic()
efface(txt)
lst_j1 = []
lst_j2 = []
sauvegarde = []
def point_mal_place(x, y, couleur, sauvegarde):
    """
    Prends en paramètres les coordonnées d'un point et sa couleur,
    suivit d'une liste contenant aussi des points et différentes données,
    puis renvoie True si le point est mal placé, c'est-a-dire si
    il dépasse les limites ou si il est trop proche des autre points
    de couleurs différentes, renvoie False sinon.
    >>> point_place(100, 300, 'red', [[300, 295, 50, 7854, 'blue', '6']])
    False
    >>> point_place(100, 300, 'red', [[388, 295, 50, 7854, 'red', '6'], [100, 295, 50, 7854, 'blue', '5']])
    True
    """
    if y<100 or x<50 or y>550 or x>750:
            return True
        
    for elt in sauvegarde:
        if distance([x, y], elt)<100 and couleur != elt[4]:
            return True
        
    return False

while nombre_tour>=0:
    #Determine le tour du joueur 1
    if nombre_tour%2 ==0:
        
        couleur = "red"
        r = 50

        evenement = attente_clic()
        x1 = evenement[0]
        print(x1)
        y1 = evenement[1]
        print(y1)
        lst_j1.append([x1, y1])
        for element in lst_j1:
            if element not point_mal_place():
                cercle(x1, y1, r, remplissage=couleur)
                nombre_tour -= 1
        
    else:
        
        couleur = "green"
        r = 50


        evenement = attente_clic()
        x2 = evenement[0]
        print(x2)
        y2 = evenement[1]
        print(y2)
        lst_j2.append([x2, y2])
        cercle(x2, y2, r, remplissage=couleur)
        nombre_tour -= 1
        
        

        
print(lst_j1, lst_j2)      
sleep(1)
attente_clic()
ferme_fenetre()
    
    