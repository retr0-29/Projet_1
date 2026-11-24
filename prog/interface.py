# interface.py

from fltk import rectangle, texte, efface_tout
import constantes as C


def dessiner_fond():

    rectangle(
        0, 0,
        C.LARGEUR_FENETRE,
        C.HAUTEUR_FENETRE,
        couleur=C.COULEUR_FOND,
        remplissage=C.COULEUR_FOND
    )


def dessiner_bouton(zone, titre, couleur=None):

    x1, y1, x2, y2 = zone

    if couleur is None:
        couleur = C.COULEUR_BOUTON

    rectangle(
        x1, y1, x2, y2,
        couleur=couleur,
        remplissage=couleur,
        epaisseur=2
    )

    texte(
        (x1 + x2) // 2,
        (y1 + y2) // 2,
        titre,
        couleur=C.COULEUR_BOUTON_TEXTE,
        taille=22,
        ancrage="center"
    )


def point_dans_zone(x, y, zone):

    x1, y1, x2, y2 = zone

    return (
        x1 <= x <= x2
        and y1 <= y <= y2
    )


# MENU PRINCIPAL

def dessiner_menu():

    efface_tout()
    dessiner_fond()

    texte(
        550, 150,
        "CHATS ET SOURIS",
        couleur=C.COULEUR_TEXTE,
        taille=42,
        ancrage="center"
    )

    texte(
        550, 220,
        "Edition du plateau de jeu",
        couleur=C.COULEUR_TEXTE,
        taille=22,
        ancrage="center"
    )

    dessiner_bouton(
        C.BOUTON_EDITER_MENU,
        "EDITER UN PLATEAU"
    )

    dessiner_bouton(
        C.BOUTON_QUITTER_MENU,
        "QUITTER",
        "#B94747"
    )


# CHOIX DU NOMBRE DE COULEURS

def dessiner_choix_couleurs(nb_couleurs):

    efface_tout()
    dessiner_fond()

    texte(
        550, 140,
        "CHOIX DU NOMBRE DE COULEURS",
        couleur=C.COULEUR_TEXTE,
        taille=30,
        ancrage="center"
    )

    texte(
        550, 250,
        "Selectionnez le nombre de couleurs :",
        couleur=C.COULEUR_TEXTE,
        taille=20,
        ancrage="center"
    )

    dessiner_bouton(
        C.BOUTON_MOINS,
        "-"
    )

    texte(
        550, 417,
        str(nb_couleurs),
        couleur=C.COULEUR_TEXTE,
        taille=42,
        ancrage="center"
    )

    dessiner_bouton(
        C.BOUTON_PLUS,
        "+"
    )

    dessiner_bouton(
        C.BOUTON_VALIDER,
        "VALIDER"
    )

    dessiner_bouton(
        C.BOUTON_RETOUR_CHOIX,
        "RETOUR",
        "#777777"
    )


# CALCUL DE LA POSITION DES CARTES

def geometrie_grille(plateau):

    nb_colonnes = plateau.colonne
    nb_lignes = plateau.ligne

    cote_largeur = (
        C.LARGEUR_GRILLE_MAX
        - (nb_colonnes - 1) * C.ESPACE_CARTES
    ) // nb_colonnes

    cote_hauteur = (
        C.HAUTEUR_GRILLE_MAX
        - (nb_lignes - 1) * C.ESPACE_CARTES
    ) // nb_lignes

    cote = min(cote_largeur, cote_hauteur)

    largeur_totale = (
        nb_colonnes * cote
        + (nb_colonnes - 1) * C.ESPACE_CARTES
    )

    hauteur_totale = (
        nb_lignes * cote
        + (nb_lignes - 1) * C.ESPACE_CARTES
    )

    x0 = C.ZONE_GRILLE_X + (
        C.LARGEUR_GRILLE_MAX - largeur_totale
    ) // 2

    y0 = C.ZONE_GRILLE_Y + (
        C.HAUTEUR_GRILLE_MAX - hauteur_totale
    ) // 2

    return x0, y0, cote, C.ESPACE_CARTES


def position_case_depuis_clic(x, y, plateau):

    x0, y0, cote, espace = geometrie_grille(plateau)

    pas = cote + espace

    decalage_x = x - x0
    decalage_y = y - y0

    if decalage_x < 0 or decalage_y < 0:
        return None

    colonne = decalage_x // pas
    ligne = decalage_y // pas

    if colonne >= plateau.colonne or ligne >= plateau.ligne:
        return None

    position_x = decalage_x % pas
    position_y = decalage_y % pas

    # Le clic doit être dans la carte,
    # pas dans l'espace qui sépare deux cartes.

    if position_x >= cote or position_y >= cote:
        return None

    return colonne, ligne


# AFFICHAGE DU PLATEAU

def dessiner_plateau(plateau, selection=None):

    efface_tout()
    dessiner_fond()

    texte(
        550, 55,
        "EDITION DU PLATEAU",
        couleur=C.COULEUR_TEXTE,
        taille=32,
        ancrage="center"
    )

    x0, y0, cote, espace = geometrie_grille(plateau)

    for ligne in range(plateau.ligne):

        for colonne in range(plateau.colonne):

            case = plateau.plateau[ligne][colonne]

            couleur = case[1]
            statut = case[2]
            aspect = case[3]

            if couleur is None:
                couleur = "#DDDDDD"

            x1 = x0 + colonne * (cote + espace)
            y1 = y0 + ligne * (cote + espace)

            x2 = x1 + cote
            y2 = y1 + cote

            couleur_bordure = C.COULEUR_BORDURE
            epaisseur = 2

            # La carte sélectionnée est encadrée en noir.

            if selection == (colonne, ligne):
                couleur_bordure = C.COULEUR_SELECTION
                epaisseur = 5

            rectangle(
                x1, y1, x2, y2,
                couleur=couleur_bordure,
                remplissage=couleur,
                epaisseur=epaisseur
            )

            # Afficher le contenu uniquement si la carte est visible.

            if statut is True and aspect is not None:

                texte(
                    (x1 + x2) // 2,
                    (y1 + y2) // 2,
                    aspect.upper(),
                    couleur="#222222",
                    taille=15,
                    ancrage="center"
                )

    # Panneau d'informations

    rectangle(
        700, 140, 1070, 600,
        couleur="#BBBBBB",
        remplissage="#FFFFFF",
        epaisseur=2
    )

    texte(
        885, 180,
        "INFORMATIONS",
        couleur=C.COULEUR_TEXTE,
        taille=24,
        ancrage="center"
    )

    texte(
        730, 250,
        "Nombre de couleurs : " + str(plateau.colonne),
        couleur=C.COULEUR_TEXTE,
        taille=17
    )

    texte(
        730, 300,
        "Nombre de cartes : " + str(plateau.nb_case),
        couleur=C.COULEUR_TEXTE,
        taille=17
    )

    if selection is None:

        texte(
            730, 365,
            "Aucune carte selectionnee",
            couleur=C.COULEUR_TEXTE,
            taille=16
        )

    else:

        colonne, ligne = selection

        texte(
            730, 365,
            "Carte selectionnee :",
            couleur=C.COULEUR_TEXTE,
            taille=16
        )

        texte(
            730, 405,
            "Colonne : " + str(colonne),
            couleur=C.COULEUR_TEXTE,
            taille=16
        )

        texte(
            730, 445,
            "Ligne : " + str(ligne),
            couleur=C.COULEUR_TEXTE,
            taille=16
        )

    dessiner_bouton(
        C.BOUTON_RETOUR_PLATEAU,
        "RETOUR AU MENU",
        "#777777"
    )