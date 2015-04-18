# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:39:48 2015

@author: Marvin
"""
import metacodeExtended as mce

# API DE GENERATION DE CODE
class Generation:
    def __init__(self):
        print("Je sais pas quoi mettre là dedans")
        
    def Marginalisation(self,cliq,var):
        raise(NotImplemented)

    def Multiplication(self,sep2,cliq,sep):
        raise(NotImplemented)
    
    def CreationPotentiel(self,jt,c):
        raise(NotImplemented)
        
    def AjoutVariablePotentiel(self,jt,c):
        raise(NotImplemented)


class CompilGeneration(Generation):
    def Marginalisation(self,cliq,var):
        print("Marginalisation de "+cliq+" selon "+var)

    def Multiplication(self,sep2,cliq,sep):
        print("MULT")
    
    def CreationPotentiel(self,jt,c):
        print("Creation du potentiel : "+ mce.nomPotentiel(jt,c))
    
    def AjoutVariablePotentiel(self,jt,c,var):
        print("Ajout de la variable "+str(var)+" au potentiel " +mce.nomPotentiel(jt,c))
    
    #def AjoutEvidencePotentiel(self,jt,c,)
    
    

    

#hiérarchiser, debug gen et pyAgrum gen