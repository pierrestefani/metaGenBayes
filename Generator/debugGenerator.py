# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:39:48 2015
@author: Marvin
"""
# Code generation API
from AbstractGenerator import AbstractGenerator
import time

class debugGenerator(AbstractGenerator):    
    def creaPot(self,nompot):
        return ("\tCreation de potentiel :" + str(nompot)+"\n")
    
    def addVarPot(self,var,nompot):
        return("\tAjout de la variable "+str(var)+" au potentiel "+str(nompot)+"\n")
        
    def mulPotCpt(self,nompot, var):
        return("\tMultiplication du potentiel "+str(nompot)+" par la cpt de la variable "+str(var)+"\n")
    
    def mulPotPot(self,nompot1,nompot2):
        return("\tMultiplication du potentiel "+str(nompot1)+" par le potentiel "+str(nompot2)+"\n")
        
    def margi(self,nompot1,nompot2):
        return("\tMarginalisation de "+str(nompot1)+ " par "+str(nompot2)+"\n")
        
    def norm(self, nompot):
        return("\tNormalisation de "+str(nompot)+"\n")
    
    def fill(self, pot, num): 
        return("\tFill"+str(num)+" de "+str(pot))
    
    def genere(self, comp, nomfichier, nomfonc):
        stream = open(nomfichier,'w')
        stream.write("'''This code was generated to debug (it lists all the instructions to do on the tree to calculate the value of targets), compiled by Compiler.py and generated with debugGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nomfonc+"():\n")
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(cur[1]))
            elif act == 'ADV':
                stream.write(self.addVarPot(cur[1],cur[2]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(cur[1],cur[2]))
            elif act == 'MUL':
                stream.write(self.mulPotPot(cur[1],cur[2]))
            elif act == 'MAR':
                stream.write(self.margi(cur[1],cur[2]))
            elif act == 'NOR':
                stream.write(self.norm(cur[1]))
            elif act == 'FIL':
                stream.write(self.fill(cur[1],cur[2]))
        stream.close()