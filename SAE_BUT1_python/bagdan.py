#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''jeu au tour par tour dont le but du jeu est
d’occuper la plus grande aire coloriée avec sa couleur. '''

# Imports ---------------------------------------------------------------------
from upemtk import *
from time import *
from math import pi
from math import sqrt
# Fonctions -------------------------------------------------------------------
def distance(lst1, lst2):
    """
    Calcule la distance entre deux points, représentés par des
    listes de type [x, y](potientiellement plus de données dans la liste
    ne dérange pas mais elles ne seront pas utilisées)
    >>> distance([100, 300],[100, 300])
    0
    >>> distance([100, 300],[110, 300])
    10
    >>> distance([100, 300],[10, 400])
    135
    >>> distance([10, 400],[100, 300])
    135
    """
        
    x1 = lst1[0]
    y1 = lst1[1]
    x2 = lst2[0]
    y2 = lst2[1]
    
    if x1>x2:
        disctancex = x1-x2
    else:
        disctancex = x2-x1
    if y1>y2:
        disctancey = y1-y2
    else:
        disctancey = y2-y1
        
    distance = int(round(sqrt(disctancex**2 + disctancey**2)))
    return distance

def point_place(x, y, couleur, sauvegarde):
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

def division_cercle(x, y, sauvegarde, couleur):
    """
    Si les coordonnées du point(x, y) sont dans l'une des boules
    ennemies dans la sauvegarde, divise cette boule et renvoie True
    """
    for elt in sauvegarde:
        if distance([x, y], elt)<50 and couleur != elt[4]:
            r = elt[2]
            r2 = int(round(sqrt((x - elt[0])*2))) + int(round((y - elt[1])*2)) #r2 represente aussi la distance entre le centre du cercle de base et les coordonées x1 et y1 du clic 
            if r2 < r :
                x = elt[0]
                y = elt[1]
                r1=r-r2
                hypo=int(round(sqrt(r1*2+r2*2)))
                cos = r2 / hypo
                sin = r1 / hypo

                if x1 > x and y1 > y :
                    x2 = x - (r1 * cos)
                    y2 = y - (r1 * sin)

                elif x1 < x and y1 < y :
                    x2 = x + (r1 * cos)
                    y2 = y + (r1 * sin)

                elif x1 > x and y1 < y :
                    x2 = x - (r1 * cos)
                    y2 = y + (r1 * sin) 
    
                elif x1 < x and y1 > y :
                    x2 = x + (r1 * cos)
                    y2 = y - (r1 * sin)
                
                cerlce(elt[0], elt[1], 50, remplissage='white')
                sauvegarde.remove(elt)
                cercle(x1, y1, r1, remplissage=couleur)
                sauvegarde.append([x1, y1, r1, int(round(pi*(r1*r1))), couleur])
                cercle(x2, y2, r2, remplissage=couleur)
                sauvegarde.append([x2, y2, r2, int(round(pi*(r2*r2))), couleur])
                return True
    return False

#Programme principal ---------------------------------------------------------------------            
if __name__ == '__main__':
    #Demande à l'utilisateur de ses préférences
    nombre_tour = int(input("Combien de tours souhaitez vous ? (un clic, un tour): "))
    temps_dispo = int(input("Combien de temps souhaitez vous pour jouer ? (en secondes): "))

    #Création de la fenetre et d'un message pour attendre le lancement du jeu
    cree_fenetre(800,600)
    rectangle(0, 0, 800, 50, remplissage="purple")
    texte(400, 20,"Batailles des boules", ancrage="center")
    txt = texte(400, 300, "READY?", taille="50", police="Monaco", ancrage="center")
    attente_clic()
    efface(txt)

    #Initialisation de variables
    txt = 0
    sauvegarde=[[0, 0, 0, 0, "red"], [0, 0, 0, 0, "blue"]]
    surface_totale_blue=0
    surface_totale_red=0


    #Début de la boucle du jeu 
    while nombre_tour>=1:
        now = time()
        max_delay = now + temps_dispo
        
        if nombre_tour%2==0: #Chaque joueur joue un tour sur deux
            txt2 = texte(540, 0, "joueur des boules rouges")

            #Prise en compte du clic de l'utilisateur et initialisation de variables selon ce clic
            evenement = attente_clic()
            couleur = "red"
            x = evenement[0]
            y = evenement[1]
            
            #effacement des textes qui peuvent gêner
            efface(txt)
            efface(txt2)

            '''if division_cercle(x, y, couleur, sauvegarde) == True:
                nombre_tour -= 1
                continue'''
            
            #Teste et passe au prochain tour si le temps est dépassé ou si le point est mal placé
            if time() > max_delay or point_place(x, y, couleur, sauvegarde) == True:
                txt = texte(0, 0, "tour passé")
                nombre_tour -= 1
                sauvegarde.append([0, 0, 0, 0, couleur])
                continue
            
            #Sinon, création d'une nouvelle boule selon le point
            cercle(x, y, 50, remplissage=couleur)
            sauvegarde.append([x, y, 50, int(round(pi*(50*50))), couleur])
            nombre_tour -= 1
            
        else:
            txt2 = texte(540, 0, "joueur des boules bleues")
            
            #Prise en compte du clic de l'utilisateur et initialisation de variables selon ce clic
            evenement = attente_clic()
            couleur = "blue"
            x = evenement[0]
            y = evenement[1]
            
            #effacement des textes qui peuvent gêner
            efface(txt)
            efface(txt2)

            '''if division_cercle(x, y, couleur, sauvegarde) == True:
                nombre_tour -= 1
                continue'''
            
            #Teste et passe au prochain tour si le temps est dépassé ou si le point est mal placé
            if time() > max_delay or point_place(x, y, couleur, sauvegarde) == True:
                txt = texte(0, 0, "tour passé")
                nombre_tour -= 1
                sauvegarde.append([0, 0, 0, 0, couleur])
                continue
            
            #Sinon, création d'une nouvelle boule selon le point
            cercle(x, y, 50, remplissage=couleur)
            sauvegarde.append([x, y, 50, int(round(pi*(50*50))), couleur])
            nombre_tour -= 1

        mise_a_jour()

    #Lorsque le compteur atteint 0, Fin de la boucle    
    #Après la fin de la boucle, calcul des surface remplies 
    for i in range(len(sauvegarde)):
        if sauvegarde[i][4] == 'red':
            surface_totale_red += sauvegarde[i][3]
        if sauvegarde[i][4] == 'blue':
             surface_totale_blue += sauvegarde[i][3]

    #Temps de répit pour que l'utilisateur voit le résultat final puis effacage de la fenêtre
    sleep(3)
    efface_tout()

    #Calcul et affichage du gagnant 
    if surface_totale_blue<surface_totale_red:
        texte(400, 300, "LE JOUEUR DES BOULES ROUGES A GAGNÉ", taille="30", police="Monaco", ancrage="center")
    elif surface_totale_blue==surface_totale_red:
        texte(400, 300, "ÉGALITÉ", taille="100", police="Monaco", ancrage="center")
    else:
        texte(400, 300, "LE JOUEUR DES BOULES BLEUES A GAGNÉ", taille="30", police="Monaco", ancrage="center")
    mise_a_jour()

    #Temps de répit puis fermeture de la fenêtre au clic de l'utilisateur
    sleep(2)
    attente_clic()
    ferme_fenetre()
