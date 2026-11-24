# evenements.py

from fltk import (
    cree_fenetre,
    ferme_fenetre,
    attend_ev,
    type_ev,
    abscisse,
    ordonnee,
    touche,
    mise_a_jour
)

import random

import constantes as C

from plateau import Plateau

from interface import (
    dessiner_menu,
    dessiner_choix_couleurs,
    dessiner_plateau,
    point_dans_zone,
    position_case_depuis_clic
)


def creer_plateau(nb_couleurs):

    plateau = Plateau(
        nb_couleurs,
        nb_couleurs
    )

    # Chaque couleur apparaît exactement
    # nb_couleurs fois dans la grille.

    liste_couleurs = []

    for couleur in C.COULEURS_CARTES[:nb_couleurs]:

        for i in range(nb_couleurs):
            liste_couleurs.append(couleur)

    random.shuffle(liste_couleurs)

    indice = 0

    for ligne in range(nb_couleurs):

        for colonne in range(nb_couleurs):

            couleur = liste_couleurs[indice]
            indice += 1

            plateau.changer_couleur(
                colonne,
                ligne,
                couleur
            )

            plateau.changer_statut(
                colonne,
                ligne,
                False
            )

            plateau.changer_aspect(
                colonne,
                ligne,
                None
            )

    return plateau


def lancer_interface():

    cree_fenetre(
        C.LARGEUR_FENETRE,
        C.HAUTEUR_FENETRE
    )

    page = "menu"

    nb_couleurs = C.NB_COULEURS_DEFAUT

    plateau = None
    selection = None

    continuer = True

    dessiner_menu()
    mise_a_jour()

    while continuer:

        evenement = attend_ev()
        type_evenement = type_ev(evenement)

        # Fermeture de la fenêtre

        if type_evenement == "Quitte":

            continuer = False

        # Gestion du clavier

        elif type_evenement == "Touche":

            touche_pressee = touche(evenement)

            if touche_pressee == "Escape":

                if page in ("plateau", "choix"):

                    page = "menu"
                    dessiner_menu()

                else:

                    continuer = False

        # Gestion des clics

        elif type_evenement == "ClicGauche":

            x = abscisse(evenement)
            y = ordonnee(evenement)

            # MENU PRINCIPAL

            if page == "menu":

                if point_dans_zone(
                    x, y, C.BOUTON_EDITER_MENU
                ):

                    page = "choix"

                    dessiner_choix_couleurs(
                        nb_couleurs
                    )

                elif point_dans_zone(
                    x, y, C.BOUTON_QUITTER_MENU
                ):

                    continuer = False

            # CHOIX DU NOMBRE DE COULEURS

            elif page == "choix":

                if point_dans_zone(
                    x, y, C.BOUTON_MOINS
                ):

                    nb_couleurs = max(
                        C.NB_COULEURS_MIN,
                        nb_couleurs - 1
                    )

                    dessiner_choix_couleurs(
                        nb_couleurs
                    )

                elif point_dans_zone(
                    x, y, C.BOUTON_PLUS
                ):

                    nb_couleurs = min(
                        C.NB_COULEURS_MAX,
                        nb_couleurs + 1
                    )

                    dessiner_choix_couleurs(
                        nb_couleurs
                    )

                elif point_dans_zone(
                    x, y, C.BOUTON_VALIDER
                ):

                    plateau = creer_plateau(
                        nb_couleurs
                    )

                    selection = None
                    page = "plateau"

                    dessiner_plateau(
                        plateau,
                        selection
                    )

                elif point_dans_zone(
                    x, y, C.BOUTON_RETOUR_CHOIX
                ):

                    page = "menu"
                    dessiner_menu()

            # PLATEAU

            elif page == "plateau":

                if point_dans_zone(
                    x, y, C.BOUTON_RETOUR_PLATEAU
                ):

                    page = "menu"
                    plateau = None
                    selection = None

                    dessiner_menu()

                else:

                    position = position_case_depuis_clic(
                        x, y, plateau
                    )

                    if position is not None:

                        selection = position

                        dessiner_plateau(
                            plateau,
                            selection
                        )

        mise_a_jour()

    ferme_fenetre()
    