# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:10:26 2015

@author: Marvin
"""
import time

class pyAgrumGenerator:   
    @classmethod
    def nameCpt(self, bn, var):
        parents = ""
        for i in bn.parents(var):
            parents += str(i)
        parents = "_".join(parents)
        return "P"+str(var)+"sachant"+parents
             
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            res += "\tv"+str(i)+" = gum.LabelizedVariable('"+bn.variable(i).name()+"','"+bn.variable(i).name()+"',"+str(bn.variable(i).domainSize())+")\n"
        for i in bn.ids():
#            parents = ""
#            for j in bn.parents(i):
#                parents += str(bn.variable(j).name())
            nameCpt = pyAgrumGenerator.nameCpt(bn,i)
#            res += "\t"+str(bn.variable(i).name()).upper()+"sachant"+parents.upper() +"= gum.Potential()\n"
#            res += "\t"+str(bn.variable(i).name()).upper()+"sachant"+parents.upper()+".add(v"+str(i)+")\n"
            res += "\t"+nameCpt+"= gum.Potential()\n"
            res += "\t"+nameCpt+".add(v"+str(i)+")\n"
            for j in bn.parents(i):
#                res += "\t"+str(bn.variable(i).name()).upper()+"sachant"+parents.upper()+".add(v"+str(j)+")\n"
                res += "\t"+nameCpt+".add(v"+str(j)+")\n"
            res += "\t"+nameCpt+"[:] = np.array("+str(bn.cpt(i).tolist())+")\n"
        return res
    def creaPot(self,nompot,varPot):
        return ("\t"+str(nompot)+"=gum.Potential()\n")
        
    def addVarPot(self,var,nompot):
        return("\t"+str(nompot)+".add("+str(var)+")\n")
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return("\t"+str(nompot)+"[:]="+value+"\n")
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        R = len(varPot)
        res = ""
        indexPot = "}]"
        indexCpt = ""
        cpt = pyAgrumGenerator.nameCpt(bn,int(var))
        
        for i in range(R):
            res += "\tfor i"+str(i)+" in range("+nompot+".var_dims["+str(i)+"]):\n"
            res += "\t"*(i+1)
            indexPot = ",'"+bn.variable(varPot[i]).name()+"' : i"+str(i)+indexPot

        for i in bn.cpt(int(var)).var_names:
            id_var = bn.idFromName(i)
            indexCpt = indexCpt+"[i"+str(varPot.index(id_var))+"]"
        
        indexPot = indexPot[1:]
        res += "\t"*(R-2)+nompot+"[{"+indexPot+" *= "+str(cpt)+"[:]"+str(indexCpt)+"\n"
#        res = "\t"+nompot+".multiplicateBy("+cpt+")\n"
        return res
             
    def mulPotPot(self,nompot1,nompot2,varPot1,varPot2):
        return("\t"+str(nompot1)+".multiplicateBy("+str(nompot2)+")\n")
        
    def margi(self,bn,nompot1,nompot2,varPot1,varPot2):    
        return("\t"+str(nompot1)+".marginalize("+str(nompot2)+")\n")
        
    def norm(self, nompot):
        return("\t"+str(nompot)+".normalize()\n")
    
    def fill(self, pot, num):
        return("\t"+str(pot)+".fill("+str(num)+")\n")
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("import pyAgrum as gum\nimport numpy as np\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n")
        stream.write("def "+nameFunc+"(evs):\n")
        stream.write("\tres = {}\n")
        stream.write(self.initCpts(bn))
        for cur in comp:
            act = cur[0]
            if act == 'CPO':
                stream.write(self.creaPot(cur[1],cur[2]))
            elif act == 'ADV':
                stream.write(self.addVarPot('v'+cur[1],cur[2]))
            elif act == 'ASE':
                stream.write(self.addSoftEvPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MUC':
                stream.write(self.mulPotCpt(bn,cur[1],cur[2],cur[3]))
            elif act == 'MUL':
                stream.write(self.mulPotPot(cur[1],cur[2],cur[3],cur[4]))
            elif act == 'MAR':
                stream.write(self.margi(cur[1],cur[2],cur[3],cur[4],cur[5]))
            elif act == 'NOR':
                stream.write(self.norm(cur[1]))
                stream.write("\tres['"+cur[2]+"']=["+str(cur[1])+"[:]]\n")
            elif act == 'FIL':
                stream.write(self.fill(cur[1],cur[2]))
        stream.write("\treturn res")

        stream.close()
        

