# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:51:16 2015

@author: Marvin
"""

import time
import numpy as np

class numpyGenerator:
    @classmethod
    def nameCpt(self, bn, var):
        parents = ""
        for i in bn.parents(var):
            parents += str(i)
        parents = "_".join(parents)
        return "P"+str(var)+"given"+parents
        
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            res += "\t"+numpyGenerator.nameCpt(bn,i) +"= "+str(bn.cpt(i).tolist())+"\n"
        return res
    
    def creaPot(self,bn,nomPot,varPot):
        #Create potential evidence (made by addSoftEvPot)
        if (nomPot[0:2] == "EV"):
            return ""
        
        #Create potential
        dim = []
        
        for i in varPot:
            dim += str(bn.variable(int(i)).domainSize())
        dim = ",".join(dim)
        if(nomPot[0:3] == "Phi"):    
            return "\t"+nomPot+"=np.ones(("+dim+"))\n"
        return "\t"+nomPot+"=np.zeros(("+dim+"))\n"

        
    def addSoftEvPot(self,evid,nompot,index,value):
        return "\t"+str(nompot)+"= evs.get('"+str(evid)+"')\n"
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        R = len(varPot)
        res = ""
        indexPot = ""
        indexCpt = ""
        cpt= numpyGenerator.nameCpt(bn,int(var))
        
        for i in range(R):
            res += "\tfor i"+str(i)+" in range("+str(bn.variable(varPot[i]).domainSize())+"):\n"
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
            res += "\tfor i"+str(i)+" in range("+str(bn.variable(varPot1[i]).domainSize())+"):\n"
            res += "\t"*(i+1)
            indexPot1 = "[i"+str(i)+"]"+indexPot1

        for i in varPot2:
            indexPot2 = "[i"+str(varPot1.index(int(i)))+"]"+indexPot2
            
        res += "\t"*(R-2)+nompot1+indexPot1+" *= "+nompot2+indexPot2+"\n"
        return res
        
    def margi(self, bn, nompot1,nompot2,varPot1,varPot2):
        res = ""
        R1 = len(varPot1)
        R2 = len(varPot2)
        indexPot1 = ""
        indexPot2 = ['*']*R2
        varPot3 = list(set(varPot2) - set(varPot1))
        R3 = len(varPot3)
        for i in range(R1):
            res += "\tfor i"+str(i)+" in range("+str(bn.variable(varPot1[i]).domainSize())+"):\n"
            res += "\t"*(i+1)
            indexPot1 = "[i"+str(i)+"]"+indexPot1
            indexPot2[R2-1-varPot2.index(int(varPot1[i]))] = "[i"+str(i)+"]"
            
        for j in range(R3):
            res += "\tfor j"+str(j)+" in range("+str(bn.variable(varPot2[j]).domainSize())+"):\n"
            res += "\t"*(j+i+2)
            indexPot2[R2-1-varPot2.index(int(varPot3[j]))] = "[j"+str(j)+"]"
        indexPot2 = "".join(indexPot2)
        res += "\t"+nompot1+indexPot1+" += "+nompot2+indexPot2+"\n"
        return res
        
    def norm(self, nompot):
        res = "\tsum = 0.0\n"        
        res += "\tfor i0 in range(len("+nompot+")):\n"
        res += "\t\tsum +="+nompot+"[i0]\n"
        res += "\tfor i0 in range(len("+nompot+")):\n"
        res += "\t\t"+nompot+"[i0]/=sum\n"
        return res
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for python (with the numpy package) use, compiled by Compiler.py and generated with numpyGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("\nimport numpy as np\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nameFunc+"(evs):\n")
        stream.write("\tres = {}\n")
        stream.write(self.initCpts(bn))
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(bn,cur[1],cur[2]))
            elif act == 'ASE':
                stream.write(self.addSoftEvPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(bn,cur[1],cur[2],cur[3]))
            elif act == 'MUL':
                stream.write(self.mulPotPot(bn,cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MAR':
                stream.write(self.margi(cur[1],cur[2],cur[3],cur[4],cur[5]))
            elif act == 'NOR':
                stream.write(self.norm(cur[1]))
                stream.write("\tres['"+cur[2]+"']=["+str(cur[1])+"[:]]\n")
        stream.write("\treturn res")

        stream.close()