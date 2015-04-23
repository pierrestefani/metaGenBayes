# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:26:43 2015

@author: Marvin
"""

class AbstractGenerator:
    def creaPot(self,jt,c):
        raise(NotImplemented)
    
    def addVarPot(self,jt,c):
        raise(NotImplemented)
        
    def mulPotCpt(self,sep2,cliq,sep):
        raise(NotImplemented)
    
    def mulPotPot(self,sep2,cliq,sep):
        raise(NotImplemented)
        
    def margi(self,cliq,var):
        raise(NotImplemented)
        
    def norm(self, pot):
        raise(NotImplemented)
    
    def fill(self, pot):
        raise NotImplemented
    
    def genere(prog, nomfichier, nomfonc):
        raise(NotImplemented)