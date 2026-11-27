from fltk import *
from classes import*

LARGEUR, HAUTEUR = 600, 700
COULEUR_FLTK = {VERT:'#39D98A', BLEU:'#398BFF', ORANGE:'#FF9F43', ROSE:'#F06BCB', GRIS:'#929BAA', MARRON:'#A66B45', ROUGE:'#FF4D5A'}
TAILLE = 100  # pixel par case

#Bouton de l'interface
BTN_EDITER = (200, 250, 400, 310)
BTN_QUITTER = (200, 340, 400, 400)
BTN_RETOUR = (20, 620, 180, 680)
BTN_N = {4: (60, 300, 200, 380), 5: (230, 300, 370, 380), 6: (400, 300, 540, 380)}

# renvoie le bouton touché
def dans_rect(x, y, r):          # r = (ax, ay, bx, by)
    return r[0] <= x <= r[2] and r[1] <= y <= r[3]


def bouton(r, libelle):
    rectangle(r[0], r[1], r[2], r[3], remplissage="#8B6DFF", epaisseur=2)
    texte((r[0]+r[2])//2, (r[1]+r[3])//2, libelle, ancrage="center", taille=20)


#dessine le menu
def dessine_menu():
    efface_tout()
    texte(300, 120, "CHATS ET SOURIS", ancrage="center", taille=32)
    bouton(BTN_EDITER, "Éditer un plateau")
    bouton(BTN_QUITTER, "Quitter")
    mise_a_jour()

#dessine les choix de grille
def dessine_choix():
    efface_tout()
    texte(300, 120, "Nombre de couleurs ?", ancrage="center", taille=32)
    bouton(BTN_N[4], "4")
    bouton(BTN_N[5], "5")
    bouton(BTN_N[6], "6")
    bouton(BTN_RETOUR, "retour")
    mise_a_jour()

#fonction qui dessine la grille
def dessine_grille(p, selection=None):
    efface_tout()
    for ligne in range(p.ligne):
        for colonne in range(p.colonne):
            x = colonne * TAILLE
            y = ligne * TAILLE
            rectangle(x, y, x + TAILLE, y + TAILLE, remplissage=COULEUR_FLTK[p.couleur_de(colonne, ligne)])
    
    if selection is not None:
        colonne, ligne = selection
        x = colonne * TAILLE
        y = ligne * TAILLE
        rectangle(x, y, x + TAILLE, y + TAILLE, couleur='#20283A', epaisseur=5)
    mise_a_jour()

cree_fenetre(LARGEUR, HAUTEUR)
ecran = 'menu'
dessine_menu()
selection = None

while True:
    ev = donne_ev()
    if type_ev(ev) == "Quitte":
        break

    if type_ev(ev) == "ClicGauche":
        x, y = abscisse(ev), ordonnee(ev)

        if ecran == 'menu':
            if dans_rect(x, y, BTN_EDITER):
                ecran = 'choix'
                dessine_choix()
            elif dans_rect(x, y, BTN_QUITTER):
                break

        elif ecran == 'choix':
            if dans_rect(x, y, BTN_RETOUR):
                ecran = 'menu'
                dessine_menu()
            else:
                for n in BTN_N:
                    if dans_rect(x, y, BTN_N[n]):
                        p = Plateau(n, n)
                        p.charger(n)
                        selection = None
                        ecran = 'grille'
                        dessine_grille(p, selection)

        elif ecran == 'grille':
            if dans_rect(x, y, BTN_RETOUR):
                ecran = 'menu'
                dessine_menu()
            else:
                taille = 600 // p.colonne
                colonne, ligne = x // taille, y // taille
                if p.dans_grille(colonne, ligne):
                    selection = (colonne, ligne)
                    dessine_grille(p, selection)
    mise_a_jour()
ferme_fenetre()
