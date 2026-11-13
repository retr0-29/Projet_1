from fltk import *


"""
contenu d'une case:[(colonne:int,ligne:int),couleur:ch,statut:bool,aspect:ch]
couleur:chaine de caractere representant une couleur ou None si existe pas
statut=True si la case est face visible False si on ne la voit pas None si elle n'existe pas
aspect: souris chat vide ou None
"""
        



class Plateau:
    """
    contenu d'un plateau:[[[(0,0),None,None,None],[(1,0),'rouge',True,'chat']]] contient une liste de
    liste(ligne) dont les indices sont les colonnes, contenant des cases
    """
    def __init__(self,nb_colonne,nb_ligne,t=1024):
        #taille globale du plateau
        self.colonne=nb_colonne
        self.ligne=nb_ligne
        self.nb_case=self.colonne*self.ligne
        #optionnel:pour l'affichage fltk
        self.taille_interface=t
        self.taille_case=t//max(self.colonne,self.ligne)
        
        #création du plateau
        self.plateau=[]
        
        for i in range(self.ligne):
            plateau_temp=[]
            for j in range(self.colonne):
                temp=[(j,i),None,None,None]
                plateau_temp.append(temp)
            self.plateau.append(plateau_temp)
        
    def affichage(self):
        for i in range(len(self.plateau)):
            print(self.plateau[i])
        
            
    def créé_case(self,colonne,ligne,couleur,statut=True,aspect='vide'):#optionnel:fonction général pour n'importe quel case(peut etre inutile)
        self.plateau[colonne][ligne]=[(colonne,ligne),couleur,statut,aspect]
        
    def changer_couleur(self,colonne:int,ligne:int,couleur:str):
        self.plateau[colonne][ligne][1]=couleur
        
    def changer_statut(self,colonne:int,ligne:int,statut:bool):
        self.plateau[colonne][ligne][2]=statut
        
    def changer_aspect(self,colonne:int,ligne:int,aspect:str):
        self.plateau[colonne][ligne][3]=aspect
        

P1=Plateau(5,5)
P1.créé_case(1,1,'Rouge',True,'souris')
P1.affichage()
