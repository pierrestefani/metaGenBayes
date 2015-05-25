# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:10:26 2015

@author: Marvin
"""
import time
import numpy as np
import pyAgrum

class pyAgrumGenerator:                
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            res += "\tv"+str(i)+" = gum.LabelizedVariable('v"+str(i)+"','v"+str(i)+"',"+str(bn.variable(i).domainSize())+")\n"
            res += "\tcpt_v"+str(i)+" = "+str(bn.cpt(i).tolist())+"\n"
        return res
    def creaPot(self,nompot):
        return ("\t"+str(nompot)+"=gum.Potential()\n")
    #A changer
    def addVarPot(self,var,nompot):
        return("\t"+str(nompot)+".add("+str(var)+")\n")
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return("\t"+str(nompot)+"[{'"+str(evid)+"':"+index+"}]="+value+"\n")
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        #return("\t"+str(nompot)+".multiplicateBy(bn.cpt("+str(var)+"))\n")
        R = len(varPot)
        res = ""
        indexPot = "}]"
        indexCpt = ""
        value = bn.cpt(int(var))
        
        for i in range(R):
            res += "\tfor i"+str(i)+" in range("+nompot+".var_dims["+str(i)+"]):\n"
            res += "\t"*(i+1)
            indexPot = ",'v"+str(varPot[i])+"' : i"+str(i)+indexPot

        for i in bn.cpt(int(var)).var_names:
            id_var = bn.idFromName(i)
            indexCpt = indexCpt+"[i"+str(varPot.index(id_var))+"]"
        
        indexPot = indexPot[1:]
        res += "\t"*(R-2)+nompot+"[{"+indexPot+" = cpt_v"+str(var)+str(indexCpt)+"\n"
        return res
             
    def mulPotPot(self,nompot1,nompot2):
        return("\t"+str(nompot1)+".multiplicateBy("+str(nompot2)+")\n")
        
    def margi(self,nompot1,nompot2):
        return("\t"+str(nompot1)+".marginalize("+str(nompot2)+")\n")
        
    def norm(self, nompot):
        return("\t"+str(nompot)+".normalize()\n")
    
    def fill(self, pot, num):
        return("\t"+str(pot)+".fill("+str(num)+")\n")
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("import pyAgrum as gum\nfrom pyAgrum import Instantiation\nimport numpy as np\n\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nameFunc+"(bn,evs):\n")
        stream.write("\tres = list()\n")
        stream.write(self.initCpts(bn))
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(cur[1]))
            elif act == 'ADV':
                stream.write(self.addVarPot("v"+cur[1],cur[2]))
            elif act == 'ASE':
                stream.write(self.addSoftEvPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(bn,cur[1],cur[2],cur[3]))
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
        

