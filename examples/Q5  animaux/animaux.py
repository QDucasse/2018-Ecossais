# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import randint
import sys
# from dprint import dprint

class Animal():
    """
    Classe décrivant les comportement par défaut des animaux. Peut-être 
    utilisée en l'état ou sous classée pour définir des comportements de
    déplacement différents.
    """
    def __init__(self, abscisse, ordonnee, eco, capacite=20):
        """
        Crée un animal aux coordonnées désirées.
        
        Paramètres
        ----------
        abscisse, ordonnée: int
            Les coordonnées auxquelles l'animal sera créé.
            
        capacité: int
            niveau de santé maximal de l'animal. Vaut 10 par défaut.
        """
        
        self.__sante = randint(capacite//2, capacite)
        self._max = capacite
        self._eco = eco
        self.coords = abscisse, ordonnee

    def __str__(self):
        """
        Affiche l'état courant de l'animal.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        """
        return "%c : position (%i, %i) etat %i/%i"%(
            self.car(), self.x, self.y,
            self.sante, self._max
            )
    
    def car(self):
        """
        Renvoie l'identifiant de l'espèce de l'animal.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère représentant l'animal.
        """
        return 'A'    

    def manger(self):
        """
        L'animal perd un niveau de sante, puis se nourrit s'il se trouve
        sur une case de nourriture. Il affiche "Je meurs de faim" si sa
        sante est à 0.
        """
        self.sante -= 1
        if self.x%5==0 and self.y%5==0:
            self.sante = self._max
        if self.sante<0:
            print(str(self)+". Je meurs de faim")

    def bouger(self):
        """
        Mouvement aléatoire uniforme dans un rayon de trois cases autour
        de la position courante. Utilise l'accesseur coords.
        """
        self.coords = (self.x+randint(-3,3),
                       self.y+randint(-3,3))

    @property
    def coords(self):
        """
        coords: tuple
            Les coordonnées de l'animal sur le plateau de jeu
        """
        return self.__coords

    @property
    def x(self):
        """
        x: nombre entier
            Abscisse de l'animal
        """
        return self.coords[0]

    @property
    def y(self):
        """
        y: nombre entier
            Abscisse de l'animal
        """
        return self.coords[1]

    @coords.setter
    def coords(self, nouv_coords):
        """
        Met à jour les coordonnées de l'insecte.
        Garantit qu'elles arrivent dans la zone définie par
        l'écosystème self._eco.
    
        Paramètres
        ----------
        nouv_coords : tuple représentant les coordonnées auquelles 
                      l'Animal essaie de se rendre.
        """
        x, y = nouv_coords
        x = min(x, self._eco.dims[0]-1)
        x = max(x, 0)
        y = min(y, self._eco.dims[1]-1)
        y = max(y, 0)
        self.__coords = (x, y)

    @property
    def sante(self):
        """
        sante: float
            Le niveau de santé de l'animal. Si ce niveau arrive à 0 l'animal
            est marqué comme mort et sera retiré du plateau de jeu
        """
        return self.__sante
    
    @sante.setter
    def sante(self, value):
        """
        Met à jour le niveau de santé de l'Animal. Garantit que la valeur arrive 
        dans l'intervalle [0, self._max]. Met à 0 les valeurs négatives, ne
        fait rien pour les valeurs trop grandes.
        """
        if value <= self._max:
            self.__sante = value
        if value <= 0:  # <= car certaines cases enlèvent plus de 1 en santé
            value = 0   # ce qui gèrera les décès plus tard


class Fourmi(Animal):
    """
    Classe spécialisant Animal pour représenter une Fourmi.
    """
    def car(self):
        return 'F'
        
    def bouger(self):
        """
        Effectue un mouvement aléatoire (défini dans la superclasse) si 
        sante>=3. Essaye de se rapprocher d'une case vers une réserve de
        nourriture sinon.
        """
        if self.sante>=3:
            super().bouger()
        else:
            if self.x%5 == 1 or self.x%5 == 2:
                nx = self.x-1
            elif self.x%5==0:
                nx = self.x
            else:
                nx = self.x+1
            if self.y%5 == 1 or self.y%5 == 2:
                ny = self.y-1
            elif self.y%5==0:
                ny = self.y
            else:
                ny = self.y+1
            self.coords = (nx, ny)
    
class Cigale(Animal):
    def __init__(self, x, y, eco):      # *args, **kwargs):
        """Le constructeur de la classe Cigale.
        x, y : int

        Note : Les lignes commentées dans le code source sont des
        façons alternatives d'invoquer le constructeur de la
        classe-mère.
        """
        # super().__init__(*args, **kwargs)
        # super().__init__(args[0], args[1])
        super().__init__(x, y, eco)
        self.sante = self._max
    
    def car(self):
        return 'C'

    def bouger(self):
        """
        Probabilité 1/3 de danser, 1/3 de chanter, 1/3 d'avoir
        un comportement semblable à une Fourmi.
        """
        action = randint(3)
        if action == 1:
            print("Je danse")
        elif action == 2:
            print("Je chante")
        elif self.sante>=3:
            super().bouger()
        else:
            if self.x%5 == 1 or self.x%5 == 2:
                nx = self.x-1
            elif self.x%5==0:
                nx = self.x
            else:
                nx = self.x+1
            if self.y%5 == 1 or self.y%5 == 2:
                ny = self.y-1
            elif self.y%5==0:
                ny = self.y
            else:
                ny = self.y+1
            self.coords = (nx, ny)

