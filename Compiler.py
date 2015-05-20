# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:21:42 2015

@author: ubuntu
"""

class Compiler:
    
    def __init__(self):
        '''The compiler class will be an array of instructions '''        
        self.tab = []
        
    def createPotentialClique(self,cliq):
        self.tab.append(["CPO", cliq])
        
    def addVariablePotential(self,var,cliq):
        self.tab.append(["ADV", var, cliq])      
    
    def addSoftEvidencePotential(self,evid,cliq,index,value):
        '''Instructions to add soft evidences following this type of input : {'likelihood : [value, value2, ...]'}'''
        self.tab.append(["ASE", evid, cliq, index, value])
    
    def fillPotential(self, cliq, value):
        self.tab.append(["FIL", cliq, value])

    def multiplicationCPT(self, cliq, cpt):
        self.tab.append(["MUC", cliq, cpt])
        
    def multiplicationPotentials(self, cliq1, parcliq2):
        self.tab.append(["MUL", cliq1, parcliq2])
        
        
    def marginalisation(self, cliq1, seloncliq2):
        self.tab.append(["MAR", cliq1, seloncliq2])
       
    def normalisation(self, cliq):
        self.tab.append(["NOR", cliq])
        
    def getTab(self):
        return self.tab
    
    