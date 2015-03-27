# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:39:48 2015

@author: Marvin
"""


# API DE GENERATION DE CODE
class Generation:
    def __init__(this):
        this.NBOP=0
        
    def Marginalisation(this,cliq,var):
        raise(NotImplemented)

    def Multiplication(this,sep2,cliq,sep):
        raise(NotImplemented)
    
    def CreationPotentiel(this,jt,c):
        raise(NotImplemented)
        #"{0:5} {1}".format(NBOP,res)


class DebugGeneration(Generation):
    def Marginalisation(this,cliq,var):
        this.NBOP+=1
        print(str(this.NBOP)+"Marginalisation de "+cliq+" selon "+var)

    def Multiplication(this,sep2,cliq,sep):
        this.NBOP+=1
        print("MULT")
    
    def CreationPotentiel(this,jt,c):
        this.NBOP+=1
        res = "Creation du potentiel : "+nomPotentiel(jt,c)
        print(str(NBOP)+res)
        #"{0:5} {1}".format(NBOP,res)

    

#