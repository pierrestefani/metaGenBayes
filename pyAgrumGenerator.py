# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:10:26 2015

@author: Marvin
"""
import time

class pyAgrumGenerator:    
    def creaPot(self,nompot):
        return ("\t"+str(nompot)+"=gum.Potential()\n")
    
    def addVarPot(self,var,nompot):
        return("\t"+str(nompot)+".add(bn.variable("+str(var)+"))\n")
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return("\t"+str(nompot)+"[{'"+str(evid)+"':"+index+"}]="+value+"\n")
    
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
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("import pyAgrum as gum\n\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nameFunc+"(bn,evs):\n")
        stream.write("\tres = list()\n")
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(cur[1]))
            elif act == 'ADV':
                stream.write(self.addVarPot(cur[1],cur[2]))
            elif act == 'ASE':
                stream.write(self.addSoftEvPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(cur[1],cur[2]))
            elif act == 'MUL':
                stream.write(self.mulPotPot(cur[1],cur[2]))
            elif act == 'MAR':
                stream.write(self.margi(cur[1],cur[2]))
            elif act == 'NOR':
                stream.write(self.norm(cur[1]))
                stream.write("\tres.append("+str(cur[1])+")\n")
            elif act == 'FIL':
                stream.write(self.fill(cur[1],cur[2]))
                #if (cur[2] == 0):
                    #flux.write("\t"+str(cur[1])+"['])
        stream.write("\treturn res")

        stream.close()
        

