from fltk import *

class Case:
    """
    contenu d'une case:[colonne:int,ligne:int,couleur:ch,retourné:bool] ou None si rien
    retourné=True si la case est face visible False si on ne la voit pas
    """
    def __init__(self,colonne,ligne,col,retourné):
        self.colonne=colonne
        



class Plateau:
    """
    contenu d'un plateau:[[[None],[1,2,'rouge',True],[None]],[[3,2,'blue',False],[None]]] contient une liste de
    liste(ligne) dont les indices sont les colonnes, contenant des cases
    """
    def __init__(self,nb_colonne,nb_ligne,t=1024):
        self.colonne=nb_colonne
        self.ligne=nb_ligne
        self.nb_case=self.colonne*self.ligne
        #optionnel:pour l'affichage fltk
        self.taille_interface=t
        self.taille_case=t//max(self.colonne,self.ligne)
        
        self.plateau=[]
        
        for i in range(min(self.colonne,self.ligne)):
            plateau_temp=[]
            temp=None
            for j in range(max(self.colonne,self.ligne)):
                plateau_temp.append(temp)
                """temp+=self.taille_case"""
            self.plateau.append(plateau_temp)
        
    def affichage(self):
        for i in range(len(self.plateau)):
            print(self.plateau[i])
        """return self.plateau"""
            
    def créé_case(self,colonne,ligne,couleur,retourné=True):
        self.plateau[colonne][ligne]=[colonne,ligne,couleur,retourné]
        
       
       
       
P1=Plateau(5,5)
P1.créé_case(1,1,'Rouge',True)
print(P1.affichage())
