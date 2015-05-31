# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:51:16 2015

@author: Marvin
"""

import time
import numpy as np

class numpyGenerator:                
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            parents = []
            for j in bn.parents(i):
                parents += str(j)
            parents = "_".join(parents)
            res += "\tP"+str(i)+"given"+parents +"= np.array("+str(bn.cpt(i).tolist())+")\n"
        return res
    
    def creaPot(self,bn,nomPot,varPot):
        #Create potential evidence
        if (nomPot[0:2] == "Ev"):
            return "\t"+nomPot+"=np.zeros(("+str(bn.variable(int(varPot[0])).domainSize())+"))\n"
        
        #Create potential
        dim = []
        
        for i in varPot:
            dim += str(bn.variable(int(i)).domainSize())
        dim = ",".join(dim)
        if(nomPot[0:3] == "Phi"):    
            return "\t"+nomPot+"=np.ones(("+dim+"))\n"
        return "\t"+nomPot+"=np.zeros(("+dim+"))\n"
             
#    def addVarPot(self,var,nompot):
#        return("\t"+str(nompot)+".add("+str(var)+")\n")
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return "\t"+str(nompot)+"= evs.get('"+str(evid)+"')\n"
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        R = len(varPot)
        res = ""
        indexPot = ""
        indexCpt = ""
        cpt = []
        for i in bn.parents(int(var)):
            cpt += str(i)
        cpt = "_".join(cpt)
        cpt ="P"+var+"given"+cpt
        
        for i in range(R):
            res += "\tfor i"+str(i)+" in range("+nompot+".shape["+str(i)+"]):\n"
            res += "\t"*(i+1)
            indexPot = "[i"+str(i)+"]"+indexPot

        for i in bn.cpt(int(var)).var_names:
            id_var = bn.idFromName(i)
            indexCpt += "[i"+str(varPot.index(id_var))+"]"
        
        res += "\t"*(R-2)+nompot+indexPot+" *= "+str(cpt)+str(indexCpt)+"\n"
        return res
             
    def mulPotPot(self,bn,nompot1,nompot2,varPot1,varPot2):
        R = len(varPot1)
        res = ""
        indexPot1 = ""
        indexPot2 = ""
        for i in range(R):
            res += "\tfor i"+str(i)+" in range("+nompot1+".shape["+str(i)+"]):\n"
            res += "\t"*(i+1)
            indexPot1 = "[i"+str(i)+"]"+indexPot1

        for i in varPot2:
            indexPot2 = "[i"+str(varPot1.index(int(i)))+"]"+indexPot2
            
        res += "\t"*(R-2)+nompot1+indexPot1+" *= "+nompot2+indexPot2+"\n"
        return res
        
    def margi(self,nompot1,nompot2,varPot1,varPot2):
        res = ""
        R1 = len(varPot1)
        R2 = len(varPot2)
        indexPot1 = ""
        indexPot2 = np.chararray(R2,itemsize=6)
        varPot3 = list(set(varPot2) - set(varPot1))
        R3 = len(varPot3)
        for i in range(R1):
            res += "\tfor i"+str(i)+" in range("+nompot1+".shape["+str(i)+"]):\n"
            res += "\t"*(i+1)
            indexPot1 = "[i"+str(i)+"]"+indexPot1
            indexPot2[R2-1-varPot2.index(int(varPot1[i]))] = "[i"+str(i)+"]"
            
        for j in range(R3):
            res += "\tfor j"+str(j)+" in range("+nompot2+".shape["+str(varPot2.index(int(varPot3[j])))+"]):\n"
            res += "\t"*(j+i+2)
            indexPot2[R2-1-varPot2.index(int(varPot3[j]))] = "[j"+str(j)+"]"
        indexPot2 = "".join(indexPot2)
        res += "\t"+nompot1+indexPot1+" += "+nompot2+indexPot2+"\n"
        return res
        
    def norm(self, nompot):
        res = "\tratio = "+str(nompot)+"[0]/"+str(nompot)+"[1]\n"
        res += "\t"+str(nompot)+"[0] = ratio/(ratio +1)\n"
        res += "\t"+str(nompot)+"[1] = 1/(ratio +1)\n"
        return res
    
#    def fill(self, pot, num):
#        return("\t"+str(pot)+".fill("+str(num)+")\n")
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for python (with the numpy package) use, compiled by Compiler.py and generated with numpyGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("\nimport numpy as np\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nameFunc+"(evs):\n")
        stream.write("\tres = list()\n")
        stream.write(self.initCpts(bn))
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(bn,cur[1],cur[2]))
#            elif act == 'ADV':
#                stream.write(self.addVarPot('v'+cur[1],cur[2]))
            elif act == 'ASE':
                stream.write(self.addSoftEvPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(bn,cur[1],cur[2],cur[3]))
            elif act == 'MUL':
                stream.write(self.mulPotPot(bn,cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MAR':
                stream.write(self.margi(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'NOR':
                stream.write(self.norm(cur[1]))
                stream.write("\tres.append("+str(cur[1])+")\n")
#            elif act == 'FIL':
#                stream.write(self.fill(cur[1],cur[2]))
                #if (cur[2] == 0):
                    #flux.write("\t"+str(cur[1])+"['])
        stream.write("\treturn res")

        stream.close()