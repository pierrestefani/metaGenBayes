# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:39:59 2015

@author: ubuntu
"""

class Compilation:
    
    def __init__(self):
        '''La classe Compilation sera un tableau '''        
        self.tab = []
        
    def creerPotentielClique(self,cliq):
        self.tab.append(["CPC", cliq])
        
    def assigneVariablePotentiel(self,var,cliq):
        self.tab.append(["ADV", var, cliq])      
        
    def assigneEvidencePotentiel(self, evid, cliq):
        self.tab.append(["ADE", evid, cliq])
    

    #pour la cpt, Multiplication aussi : Multiplication du potentiel Phi16_17_29_33_ par la cpt de la variable 33
        
    def multiplicationPotentiels(self, cliq1, parcliq2):
        self.tab.append(["MUL", cliq1, parcliq2])
        
        
    def marginalisation(self, cliq1, seloncliq2):
        self.nb = self.nb + 1
        self.tab[self.nb] = ["MAR", cliq1, seloncliq2]
        
    def normalisation(self, cliq):
        self.nb = self.nb + 1
        self.tab[self.nb] = ["NOR", cliq]
        
    
         

''' Test ADV 
['ADV', 2, 'Phi2_3_'], ['ADV', 3, 'Phi2_3_'], ['ADV', 2, 'Phi2_6_7_'], ['ADV', 6, 'Phi2_6_7_'], ['ADV', 7, 'Phi2_6_7_'], ['ADV', 0, 'Phi0_1_'], 
['ADV', 1, 'Phi0_1_'], ['ADV', 1, 'Phi1_2_4_'], ['ADV', 2, 'Phi1_2_4_'], ['ADV', 4, 'Phi1_2_4_'], ['ADV', 2, 'Phi2_5_6_'], ['ADV', 5, 'Phi2_5_6_'], 
['ADV', 6, 'Phi2_5_6_'], ['ADV', 2, 'Phi2_4_5_'], ['ADV', 4, 'Phi2_4_5_'], ['ADV', 5, 'Phi2_4_5_']]         '''

''' Test MUL cpt
['MUL', 'Phi0_1_', 'par la cpt de la variable 0'], ['MUL', 'Phi0_1_', 'par la cpt de la variable 1'], ['MUL', 'Phi1_2_4_', 'par la cpt de la variable 2'],
 ['MUL', 'Phi2_3_', 'par la cpt de la variable 3'], ['MUL', 'Phi2_4_5_', 'par la cpt de la variable 4'], ['MUL', 'Phi2_5_6_', 'par la cpt de la variable 5'],
 ['MUL', 'Phi2_5_6_', 'par la cpt de la variable 6'], ['MUL', 'Phi2_6_7_', 'par la cpt de la variable 7']]  '''