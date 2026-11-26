VERT = 'vert'
BLEU = 'bleu'
ORANGE = 'orange'
ROSE = 'rose'
GRIS = 'gris'
MARRON = 'marron'
ROUGE = 'rouge'

CHAT = 'chat'
SOURIS = 'souris'
VIDE = 'vide'

COULEURS = [VERT, BLEU, ORANGE, ROSE, GRIS, MARRON, ROUGE]


GRILLES = {
    4: [
        [ROUGE, ROUGE, ROUGE, VERT],
        [BLEU, ROUGE, VERT, VERT],
        [BLEU, BLEU, ORANGE, VERT],
        [BLEU, ORANGE, ORANGE, ORANGE],
    ],

    5: [
        [MARRON, MARRON, MARRON, MARRON, MARRON],
        [GRIS, GRIS, GRIS, GRIS, GRIS],
        [BLEU, BLEU, BLEU, BLEU, BLEU],
        [ROSE, ROSE, ROSE, ROSE, ROSE],
        [VERT, VERT, VERT, VERT, VERT],
    ],

    6: [
        [MARRON, MARRON, MARRON, MARRON, MARRON, MARRON],
        [GRIS, GRIS, GRIS, GRIS, GRIS, GRIS],
        [BLEU, BLEU, BLEU, BLEU, BLEU, BLEU],
        [ROSE, ROSE, ROSE, ROSE, ROSE, ROSE],
        [VERT, VERT, VERT, VERT, VERT, VERT],
        [ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE],
    ]
}



class Plateau:
    """
    Contenu d'un plateau : liste de lignes contenant des cases.
    Chaque case est représentée par :
    [(colonne, ligne), couleur, statut, aspect]
    """

    def __init__(self, n_colonne, n_ligne):

        # Taille globale du plateau
        self.colonne = n_colonne
        self.ligne = n_ligne
        self.nb_case = self.colonne * self.ligne

        # Création du plateau
        self.plateau = []
        for i in range(self.ligne):
            plateau_temp = []
            for j in range(self.colonne):
                temp = [(j, i), None, None, VIDE]
                plateau_temp.append(temp)
            self.plateau.append(plateau_temp)
    
#affiche la grille
    def affichage(self):
        for i in range(len(self.plateau)):
            print(self.plateau[i])

#verifie si la case est dans la grille
    def dans_grille(self, colonne, ligne):
        return 0 <= colonne < self.colonne and 0 <= ligne < self.ligne

# cree une case
    def cree_case(self, colonne, ligne, couleur, statut=True, aspect=VIDE):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        self.plateau[ligne][colonne] = [(colonne, ligne), None, statut, VIDE]
        self.changer_couleur(colonne, ligne, couleur)
        self.changer_aspect(colonne, ligne, aspect)

#change la couleur d'une case
    def changer_couleur(self, colonne: int, ligne: int, couleur: str):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        couleur = couleur.lower()

        if couleur in COULEURS:
            self.plateau[ligne][colonne][1] = couleur
        else:
            raise ValueError("Couleur invalide")

# regarde si la case est retournée
    def changer_statut(self, colonne: int, ligne: int, statut: bool):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        self.plateau[ligne][colonne][2] = statut

# modifie l'aspect de la case
    def changer_aspect(self, colonne: int, ligne: int, aspect: str):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        if aspect in [CHAT, SOURIS, VIDE]:
            self.plateau[ligne][colonne][3] = aspect
        else:
            raise ValueError("Aspect invalide")

# renvoie la couleur de la case
    def couleur_de(self, colonne, ligne):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        return self.plateau[ligne][colonne][1]
# renvoie l'aspect de la case
    def aspect_de(self, colonne, ligne):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")

        return self.plateau[ligne][colonne][3]
    
# charge des grilles pré-existantes
    def charger(self, n):
        if n not in GRILLES:
            raise ValueError("Grille inexistante")

        if self.colonne != n or self.ligne != n:
            raise ValueError("Dimensions incorrectes")

        for ligne in range(n):
            for colonne in range(n):
                couleur = GRILLES[n][ligne][colonne]
                self.changer_couleur(colonne, ligne, couleur)

# place un aspect sur la grille en verifiant qu'elle soit utilisée ou non
    def placer(self, colonne, ligne, aspect):
        if not self.dans_grille(colonne, ligne):
            raise IndexError("Case hors du plateau")
        
        if aspect == VIDE:
            self.changer_aspect(colonne, ligne, VIDE)
            return None
        
        for c in range(self.colonne):
            if c != colonne and self.aspect_de(c, ligne) == aspect:
                return "Il y a déjà un " + aspect + " sur cette ligne"
        
        for l in range(self.ligne):
            if l != ligne and self.aspect_de(colonne, l) == aspect:
                return "Il y a déjà un " + aspect + " sur cette colonne"
        
        for l in range(self.ligne):
            for c in range(self.colonne):
                if (c, l) != (colonne, ligne) and self.couleur_de(c, l) == self.couleur_de(colonne, ligne) and self.aspect_de(c, l) == aspect:
                    return "Il y a déjà un " + aspect + " de cette couleur"
        
        if aspect == CHAT:
            oppose = SOURIS
        else:
            oppose = CHAT

        for dl in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (dc, dl) != (0, 0):
                    c = colonne + dc
                    l = ligne + dl
                    if self.dans_grille(c, l) and self.couleur_de(c, l) == self.couleur_de(colonne, ligne) and self.aspect_de(c, l) == oppose:
                        return "Un " + oppose + " de même couleur est voisin"

        self.changer_aspect(colonne, ligne, aspect)
        return None


