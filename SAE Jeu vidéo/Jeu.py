from upemtk import *
from matplotlib import *
from random import randint
import math

game_end=False
window_length=800
window_height=800
player_turn=1
game_round=0
verification=0
list_red=[]
list_blue=[]
player1 = {'id': 1, 'name': 'Player 1', 'color': 'blue'}
player2 = {'id': 2, 'name': 'Player 2', 'color': 'red'}

#Calculer les aires d'intersection
def Intersecting_Area(d, rad1, rad2):  
    rad1sqr = rad1 * rad1
    rad2sqr = rad2 * rad2

    if d == 0:
        if rad1>rad2:
            area=(math.pi * rad1**2)
        else:
            area=(math.pi * rad2**2)
        return area

    if d >= rad1+rad2:
        return 0
    
    if rad1==0 or rad2==0:
        return 0

    angle1 = (rad1sqr + (d * d) - rad2sqr) / (2 * rad1 * d)
    angle2 = (rad2sqr + (d * d) - rad1sqr) / (2 * rad2 * d)

    if ((angle1 < 1 and angle1 >= -1) or (angle2 < 1 and angle2 >= -1)):
        theta1 = (math.acos(angle1) * 2)
        theta2 = (math.acos(angle2) * 2)

        area1 = (0.5 * theta2 * rad2sqr) - (0.5 * rad2sqr * math.sin(theta2))
        area2 = (0.5 * theta1 * rad1sqr) - (0.5 * rad1sqr * math.sin(theta1))

        return area1 + area2

    return 0

#Calculer l'aire qu'occupe chaque couleur
def AreaOccupied(circle_list):
    total_area=0
    total_intersected_area=0

    for i in range(len(circle_list)-1):
        for j in range(len(circle_list)-i-1):
            rad1=circle_list[i][2]
            rad2=circle_list[j+i+1][2]
            total_intersected_area+=Intersecting_Area(
                math.dist([circle_list[i][0],circle_list[i][1]],[circle_list[j+i+1][0],circle_list[j+i+1][1]]),rad1 ,rad2)
    
    for i in range(len(circle_list)):
        total_area+= math.pi * circle_list[i][2] **2

    final_area=total_area-total_intersected_area
    
    return final_area

#tour du jouer, les actions qu'il peut faire
def Player_Turn(circle_list, enemy_circle_list, player_turn):
    
    verification=0

    if player_turn==1:
        player=player1
        other_player=player2
    else:
        player=player2
        other_player=player1

    rectangle(0,0,window_length,40,couleur='white', remplissage='white')
    rectangle(175,8,125,25,couleur=player['color'], remplissage=player['color'])
    texte(0,0,chaine=player['name'],ancrage='nw', police="Arial", taille=20)
    texte(200,0,chaine='Round:',ancrage='nw', police="Arial", taille=20)
    texte(300,0,chaine=game_round,ancrage='nw', police="Arial", taille=20)

    x1, y1, w = attente_clic()

    k=len(enemy_circle_list)-1
    while (k != -1):
        
        if math.dist(enemy_circle_list[k][0:2],[x1,y1])<160:
            verification=1

            if math.dist(enemy_circle_list[k][0:2],[x1,y1])<80:
                print(f'starting circle:{enemy_circle_list[k]}')

                rad_small=enemy_circle_list[k][2] - round(math.dist(enemy_circle_list[k][0:2],[x1,y1]),0)
                tag_circle=cercle(x1, y1, rad_small, couleur = other_player['color'], remplissage = other_player['color'])
                enemy_circle_list.append([x1,y1,rad_small,tag_circle])
                print(f'x:{x1}')
                print(f'y:{y1}')
                print(f'rad_small:{rad_small}')

                rad_medium= enemy_circle_list[k][2]-rad_small
                print(f'rad_medium:{rad_medium}')

                print('big cercle x', enemy_circle_list[k][0])
                if rad_medium>0:
                    x_medium= round(enemy_circle_list[k][0] + ((enemy_circle_list[k][0]-x1)*rad_small/rad_medium))
                
                    print('big cercle y', enemy_circle_list[k][1])
                
                    y_medium= round(enemy_circle_list[k][1] + ((enemy_circle_list[k][1]-y1)*rad_small/rad_medium))

                    print(f'x_medium:{x_medium}')
                    print(f'y_medium:{y_medium}')
                
                    tag_circle=cercle(x_medium, y_medium, rad_medium, couleur= other_player['color'], remplissage= other_player['color'])
                    circle_list.append([x_medium,y_medium,rad_medium,tag_circle])
                
                efface(enemy_circle_list[k][3])
                enemy_circle_list.pop(k)

        k-=1

    if verification==0:
        tag_circle=cercle(x1, y1, 80, couleur = player['color'] ,remplissage = player['color'])
        circle=[x1,y1,80,tag_circle]
        circle_list.append(circle)

    # while True:
    #     evenement = donne_evenement()
    #     type_ev = type_evenement(evenement)
    #     print(f'type_ev:{type_ev}')
    #     if type_ev == 'Touche':# and touche(evenement)=='s':
    #         print(f'Touche:{touche(evenement)}')
    #         blue_area=AreaOccupied(list_blue)
    #         red_area=AreaOccupied(circle_list)

    #         texte(150,200,chaine='Player 1 score:', ancrage='nw', police='Arial', taille=50)
    #         texte(150,200,chaine=blue_area, ancrage='nw', police='Arial', taille=50)

    #         texte(150,200,chaine='Player 2 score:', ancrage='nw', police='Arial', taille=50)
    #         texte(150,200,chaine=red_area, ancrage='nw', police='Arial', taille=50)

if __name__ == '__main__':
    cree_fenetre(window_height, window_length)
    while game_end==False:

        #changer les tours des joueurs
        if player_turn==1:
            Player_Turn(list_blue,list_red,player_turn)
            player_turn=2
        else:
            Player_Turn(list_red,list_blue,player_turn)
            player_turn=1

        mise_a_jour()
        game_round+=1
        if game_round==11:
            blue_area=AreaOccupied(list_blue)
            red_area=AreaOccupied(list_red)
            if red_area>blue_area:
                rectangle(0,0,window_length,window_height,couleur='white', remplissage='white')
                texte(150,200,chaine='Player 2 WINS',ancrage='nw', police='Arial', taille=50)
            else:
                rectangle(0,0,window_length,window_height,couleur='white', remplissage='white')
                texte(150,200,chaine='Player 1 WINS',ancrage='nw', police='Arial', taille=50)
            attente_clic()
            game_end=True

    ferme_fenetre()