import time

def flatten(liste):
    '''Transforms multidimensional arrays into one'''
    for i in liste:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i

def makeIndexOutOfDict(dictionary, potSize):
    '''From a dictionary of indexes, lenghts, structured in the margi function,
    to the string uses in the potential index of the same function'''
    arr = list()
    size = potSize
    ind=0
    while(ind < len(dictionary)):
        for i in dictionary:
            if(dictionary.get(i)[0] == ind):
                size /= dictionary.get(i)[1]
                arr.append(str(i)+'*'+str(size))
                ind += 1
    return "+".join(arr)

class javascriptGenerator:
    @classmethod
    def nameCpt(self, bn, var):
        parents = []
        for i in bn.parents(var):
            parents.append(str(i))
        parents = "_".join(parents)
        return "P"+str(var)+"given"+parents
        
    def initCpts(self,bn):
        res = ""
        for i in bn.ids():
            res += "\t"+javascriptGenerator.nameCpt(bn,i) +"= new Float32Array("+str(list(flatten(bn.cpt(i).tolist())))+");\n"
        return res     
        
        
    def creaPot(self, bn, nomPot, varPot):
        dim = []
        res = ""
        for i in varPot:
            dim += str(bn.variable(int(i)).domainSize())
        dim = "*".join(dim)
        if(nomPot[0:3] == "Phi"):
            res += "\t"+nomPot+"= new Float32Array("+str(dim)+");\n"
            res += "\tfor(i=0;i<"+str(dim)+";i++)\n\t\t"+nomPot+"[i] = 1.0;\n"
        else:
            res += "\t"+nomPot+"= new Float32Array("+str(dim)+");\n"
            res += "\tfor(i=0;i<"+str(dim)+";i++)\n\t\t"+nomPot+"[i] = 0.0;\n"      
        return res
        
        
    def addSoftEvPot(self,evid,nompot,index,value):
        return "\t"+str(nompot)+"= new Float32Array(evs['"+str(evid)+"']);\n"        
        
    def mulPotCpt(self, bn, nompot, var, varPot):
        R = len(varPot)
        res = ""
        indexPotList = list()
        indexCptList = list()
        indexPot = "["
        indexCpt = "["
        cpt = javascriptGenerator.nameCpt(bn, int(var))
        sizePot = 1
        sizeCpt = 1
        for i in bn.cpt(int(var)).var_names:
            sizeCpt *= bn.variable(bn.idFromName(i)).domainSize()
        
        for i in range(R):
            res += "\tfor (i"+str(i)+"=0; i"+str(i)+"<"+str(bn.variable(varPot[i]).domainSize())+";i"+str(i)+"++){\n"
            res += "\t"*(i+1)
            indexPotList.append("i"+str(i)+"*"+str(sizePot))
            sizePot *= bn.variable(varPot[i]).domainSize()
        indexPot += "+".join(indexPotList)+"]"

        for i in bn.cpt(int(var)).var_names:
            id_var = bn.idFromName(i)
            sizeCpt /= bn.variable(varPot[varPot.index(id_var)]).domainSize()
            indexCptList.append("i"+str(varPot.index(id_var))+"*"+str(sizeCpt))
        indexCpt += "+".join(indexCptList)+"]"
        
        res += "\t"+nompot+indexPot+" *= "+str(cpt)+str(indexCpt)+";"+"}"*(R)+"\n"
        return res
        
    def mulPotPot(self,bn,nompot1,nompot2,varPot1,varPot2):
        R = len(varPot1)
        res = ""
        indexPot1List = list()
        indexPot2List = list()
        indexPot1 = "["
        indexPot2 = "["
        sizePot = 1
        for i in range(R):
            res += "\tfor (i"+str(i)+"=0; i"+str(i)+"<"+str(bn.variable(varPot1[i]).domainSize())+";i"+str(i)+"++){\n"
            res += "\t"*(i+1)
            indexPot1List.append("i"+str(i)+"*"+str(sizePot))
            sizePot *= bn.variable(varPot1[i]).domainSize()
        indexPot1 += "+".join(indexPot1List)+"]"
        sizePot = 1

        for i in varPot2:
            indexPot2List.append("i"+str(varPot1.index(int(i)))+"*"+str(sizePot))
            sizePot *= bn.variable(varPot1[varPot1.index(int(i))]).domainSize()
        indexPot2 += "+".join(indexPot2List)+"]"
            
        res += "\t"*(R-2)+nompot1+indexPot1+" *= "+nompot2+indexPot2+";"+"}"*(R)+"\n"
        return res
        
        
    def margi(self,bn,nompot1,nompot2,varPot1,varPot2):
        res = ""
        R1 = len(varPot1)
        R2 = len(varPot2)
        indexPot1 = "["
        indexPot2 = "["
        indexPot1List = list()
        indexPot2Dict = {}
        sizePot1=1
        sizePot2=1
        varPot3 = list(set(varPot2) - set(varPot1))
        R3 = len(varPot3)
        
        for i in range(R1):
            res += "\tfor (i"+str(i)+"=0;i"+str(i)+"<"+str(bn.variable(varPot1[i]).domainSize())+";i"+str(i)+"++){\n"
            res += "\t"*(i+1)
            indexPot1List.append("i"+str(i)+"*"+str(sizePot1))
            sizePot1 *= bn.variable(varPot1[i]).domainSize()
            indexPot2Dict['i'+str(i)] = [R2-1-varPot2.index(int(varPot1[i])), bn.variable(varPot2[varPot2.index(int(varPot1[i]))]).domainSize()]
            sizePot2 *= bn.variable(varPot2[varPot2.index(int(varPot1[i]))]).domainSize()
        indexPot1 += "+".join(indexPot1List)+"]"
        
        for j in range(R3):
            res += "\tfor (j"+str(j)+"=0;j"+str(j)+"<"+str(bn.variable(varPot3[j]).domainSize())+";j"+str(j)+"++){\n"
            res += "\t"*(j+i+2)
            indexPot2Dict['j'+str(j)] = [R2-1-varPot2.index(int(varPot3[j])), bn.variable(varPot3[j]).domainSize()]
            sizePot2 *= bn.variable(varPot3[j]).domainSize()
            
        indexPot2 += makeIndexOutOfDict(indexPot2Dict, sizePot2)
        res += "\t"+nompot1+indexPot1+" += "+nompot2+indexPot2+"];"+"}"*(R1+R3)+"\n"
        return res
        
    def norm(self, nompot):
        res = "\tsum = 0.0\n"        
        res += "\tfor (i0=0; i0 <"+nompot+".length;i0++){\n"
        res += "\t\tsum +="+nompot+"[i0];}\n"
        res += "\tfor (i0=0; i0 <"+nompot+".length;i0++){\n"
        res += "\t\t"+nompot+"[i0]/=sum;}\n"
        return res

    def genere(self, bn, targets, evs, comp, nameFile, nameFunc, header):
        stream = open(nameFile,'w')
        stream.write("//This code was generated for javascript use, compiled by Compiler.py and generated with javascriptGenerator.py.\n//It shouldn't be altered here'''\n")
        stream.write("//Generated on : "+time.strftime('%m/%d/%y %H:%M',time.localtime())+"\n\n\n")
        stream.write(header+"\n\n")
        stream.write("function "+nameFunc+"(evs) {\n")
        stream.write("\tres=[];\n")
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
                stream.write("\tres['"+cur[2]+"']="+str(cur[1])+";\n")
        stream.write("\treturn res;\n}\n")
        evsjs = []
        for i in evs:
            ev = "\t\""+str(i)+"\""+" : "+str(evs[i])
            evsjs.append(ev)
        
        stream.write("console.log("+nameFunc+"({\n"+",\n".join(evsjs)+"\n}));\n")
        stream.close()
        
