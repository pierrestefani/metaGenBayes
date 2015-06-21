# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:26:43 2015

@author: Marvin
"""

'''Abstract class for the generators'''

class AbstractGenerator:
    def initCpts(self,bn):
        raise(NotImplemented)
    
    def creaPot(self,jt,c):
        raise(NotImplemented)
    
    def addVarPot(self,jt,c):
        raise(NotImplemented)
        
    def addSoftEvPot(self,evid,nompot,index,value):
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