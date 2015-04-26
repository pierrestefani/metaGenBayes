# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:21:42 2015

@author: ubuntu
"""

class Compilation:
    
    def __init__(self):
        '''La classe Compilation sera un tableau '''        
        self.tab = []
        
    def creerPotentielClique(self,cliq):
        self.tab.append(["CPO", cliq])
        
    def assigneVariablePotentiel(self,var,cliq):
        self.tab.append(["ADV", var, cliq])      
    
    def assigneSoftEvidencePotentiel(self,evid,cliq,index,value):
        '''Gère l'assignation d'évidences de type {'vraisemblance : [value, value2,...]}'''
        self.tab.append(["ASE", evid, cliq, index, value])
    
    def fillPotentiel(self, cliq, value):
        self.tab.append(["FIL", cliq, value])

    def multiplicationCPT(self, cliq, cpt):
        self.tab.append(["MUC", cliq, cpt])
        
    def multiplicationPotentiels(self, cliq1, parcliq2):
        self.tab.append(["MUL", cliq1, parcliq2])
        
        
    def marginalisation(self, cliq1, seloncliq2):
        self.tab.append(["MAR", cliq1, seloncliq2])
       
    def normalisation(self, cliq):
        self.tab.append(["NOR", cliq])
        
    def getTab(self):
        return self.tab
    
    