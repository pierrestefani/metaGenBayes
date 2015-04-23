# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:10:26 2015

@author: Marvin
"""

class pyAgrumGenerator:    
    def creaPot(self,nompot):
        return ("\t"+str(nompot)+"=gum.Potential()\n")
    
    def addVarPot(self,var,nompot):
        return("\t"+str(nompot)+".add(bn.variable("+str(var)+"))\n")
        
    def mulPotCpt(self,nompot, var):
        return("\t"+str(nompot)+".multiplicateBy(bn.cpt("+str(var)+"))\n")
    
    def mulPotPot(self,nompot1,nompot2):
        return("\t"+str(nompot1)+".multiplicateBy("+str(nompot2)+")\n")
        
    def margi(self,nompot1,nompot2):
        return("\t"+str(nompot1)+".marginalize("+str(nompot2)+")\n")
        
    def norm(self, nompot):
        return("\t"+str(nompot)+".normalize()\n")
    
    def fill(self, pot, num): #??? Que fait fill dans inférence à la main ???
        return("\t"+str(pot)+".fill("+str(num)+")\n")
    
    def genere(self, comp, nomfichier, nomfonc):
        flux = open(nomfichier,'w')
        flux.write("import pyAgrum as gum\n\n")
        flux.write("def "+nomfonc+":\n")
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                flux.write(self.creaPot(cur[1]))
            elif act == 'ADV':
                flux.write(self.addVarPot(cur[1],cur[2]))
            elif act == 'MUC':
                flux.write(self.mulPotCpt(cur[1],cur[2]))
            elif act == 'MUL':
                flux.write(self.mulPotPot(cur[1],cur[2]))
            elif act == 'MAR':
                flux.write(self.margi(cur[1],cur[2]))
            elif act == 'NOR':
                flux.write(self.norm(cur[1]))
            elif act == 'FIL':
                flux.write(self.fill(cur[1],cur[2]))
        flux.close()
        

