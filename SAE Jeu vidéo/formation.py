
from upemtk import *
from time import *

scorej1 = 500

cree_fenetre(400,400)
while True:
    evenement = donne_evenement()
    type_ev = type_evenement(evenement)

    if type_ev == 'Touche':
        nom_touche = touche(evenement)
        if nom_touche =='s':
            
            texte(0, 0, scorej1, couleur="red", tag="s1")
            
            
sleep(3) 
ferme_fenetre()