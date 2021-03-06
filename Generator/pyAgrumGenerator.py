import time

class pyAgrumGenerator:   
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
            res += "\tv"+str(i)+" = gum.LabelizedVariable('"+bn.variable(i).name()+"','"+bn.variable(i).name()+"',"+str(bn.variable(i).domainSize())+")\n"
        for i in bn.ids():

            nameCpt = pyAgrumGenerator.nameCpt(bn,i)
            res += "\t"+nameCpt+" = gum.Potential()\n"
            res += "\t"+nameCpt+".add(v"+str(i)+")\n"
            ls = bn.cpt(i).var_names
            for j in reversed(ls[0:len(ls)-1]):
                res += "\t"+nameCpt+".add(v"+str(bn.idFromName(j))+")\n"
            res += "\t"+nameCpt+"[:] = np.array("+str(bn.cpt(i).tolist())+")\n"
        return res
        
    def creaPot(self,nompot,varPot):
        return ("\t"+str(nompot)+"=gum.Potential()\n")
        
    def addVarPot(self,var,nompot):
        return("\t"+str(nompot)+".add("+str(var)+")\n")
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return("\t"+str(nompot)+"[:]="+value+"\n")
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        cpt = pyAgrumGenerator.nameCpt(bn,int(var))
        res = "\t"+nompot+".multiplicateBy("+cpt+")\n"
        return res
             
    def mulPotPot(self,nompot1,nompot2,varPot1,varPot2):
        return("\t"+str(nompot1)+".multiplicateBy("+str(nompot2)+")\n")
        
    def margi(self,bn,nompot1,nompot2,varPot1,varPot2):    
        return("\t"+str(nompot1)+".marginalize("+str(nompot2)+")\n")
        
    def norm(self, nompot):
        return("\t"+str(nompot)+".normalize()\n")
    
    def fill(self, pot, num):
        return("\t"+str(pot)+".fill("+str(num)+")\n")
    
    def equa(self, nompot1, nompot2):
        return "\t"+nompot1+" = "+nompot2+"\n"
    
    def genere(self, bn, targets, evs, comp, nameFile, nameFunc, header):
        stream = open(nameFile,'w')
        stream.write("'''This code was generated for pyAgrum use, compiled by Compiler.py and generated with pyAgrumGenerator.py.\nIt shouldn't be altered here'''\n")
        stream.write("import pyAgrum as gum\nimport numpy as np\n")
        stream.write("'''Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"'''\n\n\n")
        stream.write(header+"\n\n")
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
                stream.write("\tres['"+cur[2]+"']=np.copy("+str(cur[1])+"[:])\n")
            elif act == 'FIL':
                stream.write(self.fill(cur[1],cur[2]))
            elif act == 'EQU':
                stream.write(self.equa(cur[1],cur[2]))
        stream.write("\treturn res")

        stream.close()
        

