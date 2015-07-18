# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:24:36 2015

@author: Marvin
"""

import time

class phpGenerator:
    @classmethod
    def nameCpt(self, bn, var):
        parents = []
        for i in bn.parents(var):
            parents.append(str(i))
        parents = "_".join(parents)
        return "P"+str(var)+"sachant"+parents
        
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            res += "\t$"+phpGenerator.nameCpt(bn,i) +"= "+str(bn.cpt(i).tolist())+";\n"
        return res
    
    def creaPot(self,bn,nomPot,varPot):
        dim = ""
        #Create potential evidence (made by addSoftEvPot)
        if (nomPot[0:2] == "EV"):
            return ""
        #Create potential
        for i in varPot:
                dim = "array_fill(0,"+str(bn.variable(int(i)).domainSize())+","+dim
        if (nomPot[0:3] == "Phi"):
            return "\t$"+nomPot+"="+dim+"1.0"+")"*len(varPot)+";\n"
    
        return "\t$"+nomPot+"="+dim+"0.0"+")"*len(varPot)+";\n"
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return "\t$"+str(nompot)+"= $evs['"+str(evid)+"'];\n"
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        R = len(varPot)
        res = ""
        indexPot = ""
        indexCpt = ""
        cpt = phpGenerator.nameCpt(bn,int(var))
        
        for i in range(R):
            res += "\tfor($i"+str(i)+"=0;$i"+str(i)+"<"+str(bn.variable(varPot[i]).domainSize())+";$i"+str(i)+"++)\n"
            res += "\t"*(i+1)
            indexPot = "[$i"+str(i)+"]"+indexPot

        for i in bn.cpt(int(var)).var_names:
            id_var = bn.idFromName(i)
            indexCpt += "[$i"+str(varPot.index(id_var))+"]"
        
        res += "\t"+"$"+nompot+indexPot+" *= $"+str(cpt)+str(indexCpt)+";\n"
        return res
             
    def mulPotPot(self,bn,nompot1,nompot2,varPot1,varPot2):
        R = len(varPot1)
        res = ""
        indexPot1 = ""
        indexPot2 = ""
        for i in range(R):
            res += "\tfor($i"+str(i)+"=0;$i"+str(i)+"<"+str(bn.variable(varPot1[i]).domainSize())+";$i"+str(i)+"++)\n"
            res += "\t"*(i+1)
            indexPot1 = "[$i"+str(i)+"]"+indexPot1

        for i in varPot2:
            indexPot2 = "[$i"+str(varPot1.index(int(i)))+"]"+indexPot2
            
        res += "\t"+"$"+nompot1+indexPot1+" *= $"+nompot2+indexPot2+";\n"
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
            res += "\tfor($i"+str(i)+"=0;$i"+str(i)+"<"+str(bn.variable(varPot1[i]).domainSize())+";$i"+str(i)+"++)\n"
            res += "\t"*(i+1)
            indexPot1 = "[$i"+str(i)+"]"+indexPot1
            indexPot2[R2-1-varPot2.index(int(varPot1[i]))] = "[$i"+str(i)+"]"
            
        for j in range(R3):
            res += "\tfor($j"+str(j)+"=0;$j"+str(j)+"<"+str(bn.variable(varPot3[j]).domainSize())+";$j"+str(j)+"++)\n"
            res += "\t"*(j+i+2)
            indexPot2[R2-1-varPot2.index(int(varPot3[j]))] = "[$j"+str(j)+"]"
        indexPot2 = "".join(indexPot2)
        res += "\t$"+nompot1+indexPot1+" += $"+nompot2+indexPot2+";\n"
        return res
        
    def phpToPythonRes(self, evs, nameFunc):
        res = "echo(\"{\");\n"
        res += "$bb=0;\n"
        res += "foreach("+nameFunc+"(array(\n"
        lsEvs = []
        for name, val in evs.items():
            lsEvs.append("\t"*2+"\""+str(name)+"\"=>"+str(val))
        res += ",\n".join(lsEvs)
        res += "\n)) as $k=>$v) {\n"
        res += "\t"*2+"if($bb==1) echo(\",\");\n"
        res += "\t"*2+"$bb=1;"
        res += "\t"*2+"echo(\"'$k': [[\");\n"
        res += "\t"*2+"$b=0;\n"
        res += "\t"*2+"foreach($v as $val) {\n"
        res += "\t"*3+"if ($b==1) echo(\",\");\n"
        res += "\t"*3+"$b=1;\n"
        res += "\t"*3+"echo(\" \");\n"
        res += "\t"*3+"echo($val);\n"
        res += "\t"*2+"}\n"
        res += "\t"*2+"echo(\"]]\");\n"
        res += "}\n"
        res += "echo(\"}\");"
        return res
        
    def norm(self, nompot):
        res = "\t$sum=0.0;\n"      
        res += "\tfor($i0=0;$i0<count($"+nompot+");$i0++)\n"
        res += "\t\t$sum+=$"+nompot+"[$i0];\n"
        res += "\tfor($i0=0;$i0<count($"+nompot+");$i0++)\n"
        res += "\t\t$"+nompot+"[$i0]/=$sum;\n"
        return res
    def equa(self, nompot1, nompot2):
        return "\t$"+nompot1+" = $"+nompot2+";\n"
        
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc):
        stream = open(nameFile,'w')
        stream.write("<?php\n")
        stream.write("//This code was generated for php>5.6, compiled by Compiler.py and generated with phpGenerator.py.\n")
        stream.write("//It shouldn't be altered here\n")        
        stream.write("//Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"\n\n")
        stream.write("function "+nameFunc+"($evs) {\n")
        stream.write("\t$res=[];\n")
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
                stream.write("\t$res['"+cur[2]+"']=$"+str(cur[1])+";\n")
            elif act == 'EQU':
                stream.write(self.equa(cur[1],cur[2]))
        stream.write("\treturn $res;\n}\n")
        evsphp = []
        for i in evs:
            ev = "\t\""+str(i)+"\""+" => "+str(evs[i])
            evsphp.append(ev)
        stream.write(self.phpToPythonRes(evs, nameFunc))
#        stream.write("print_r(getValue(array(\n"+",\n".join(evsphp)+"\n)));\n")
        stream.close()