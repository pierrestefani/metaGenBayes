# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:21:42 2015

@author: ubuntu
"""

import pyAgrum as gum

class Compiler:
    
    def __init__(self):
        '''The compiler class will be an array of instructions '''        
        self.tab = []
        
    def createPotentialClique(self,cliq,varPot):
        self.tab.append(["CPO", cliq, varPot])
        
    def addVariablePotential(self,var,cliq):
        self.tab.append(["ADV", var, cliq])      
    
    def addSoftEvidencePotential(self,evid,cliq,index,value):
        '''Instructions to add soft evidences following this type of input : {'likelihood : [value, value2, ...]'}'''
        self.tab.append(["ASE", evid, cliq, index, value])
    
    def fillPotential(self, cliq, value):
        self.tab.append(["FIL", cliq, value])

    def multiplicationCPT(self, cliq, cpt, varPot):
        self.tab.append(["MUC", cliq, cpt, varPot])
        
    def multiplicationPotentials(self, cliq1, parcliq2, varPot1, varPot2):
        self.tab.append(["MUL", cliq1, parcliq2, varPot1, varPot2])
        
    def marginalisation(self, bn, cliq1, seloncliq2,varPot1,varPot2):
        self.tab.append(["MAR", bn, cliq1, seloncliq2,varPot1,varPot2])
       
    def normalisation(self, cliq, targ):
        self.tab.append(["NOR", cliq, targ])
        
    def getTab(self):
        return self.tab

compilator = Compiler()

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:50:21 2015

@author: Marvin
"""

from Compiler import Compiler

def labelPotential(jt,c):
    """Get the name of the potential for a clique c"""
    res="Phi"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res
    
def creationPotentialsAbsorp(bn, jt):
    """Fill the compiler array of instructions in order to create the potentials and add the corresponding variables"""
    for i in jt.ids():
        label = labelPotential(jt,i)
        compilator.createPotentialClique(label,list(jt.clique(i)))
        for j in jt.clique(i):
            compilator.addVariablePotential(str(j), label)
        compilator.fillPotential(label,1)

def initPotentialsAbsorp(bn,jt):
    """Instructions for the initialization of the potentials"""
    res = []    
    for i in bn.ids():
        cpt = 0
        for j in jt.ids():
            cpt += 1
            if(i in jt.clique(j)):
                b = 1
                for l in bn.parents(i):                  
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    compilator.multiplicationCPT(labelPotential(jt,j),str(i),list(jt.clique(j)))
                    break
    return res

def creaIniOnePotDif(bn, jt, ca, cb):
    """Create a potential (for ca) for the diffusion"""
    labelAbs = labelPotential(jt,ca)
    labelDif = labelAbs+"to"+labelPotential(jt,cb)
    varClique = list(jt.clique(ca))
    compilator.createPotentialClique(labelDif,varClique)
    for j in varClique:
        compilator.addVariablePotential(str(j), labelDif)
    compilator.fillPotential(labelDif,1)
    compilator.multiplicationPotentials(labelDif,labelAbs,varClique,varClique)

def creaIniOnePotTar(bn, jt, ca):
    """Create a potential which contains a target for the diffusion"""
    labelAbs = labelPotential(jt,ca)
    labelDif = labelAbs+"tar"
    varClique = list(jt.clique(ca))
    compilator.createPotentialClique(labelDif, varClique)
    for j in varClique:
        compilator.addVariablePotential(str(j), labelDif)
    compilator.fillPotential(labelDif,1)
    compilator.multiplicationPotentials(labelDif,labelAbs,varClique,varClique)
    
def creaIniPotentialsDiffu(bn, jt, diffu, cliquesTar, targets):
    """Create all potentials for the diffusion, we must call this function before the absorption, and after the initialization of absorption's potentials"""
    R = len(diffu)
    for i in range(R):
        creaIniOnePotDif(bn, jt, diffu[i][0], diffu[i][1])
    for i in cliquesTar.values():
        creaIniOnePotTar(bn, jt, i)
def labelPotentialEvs(bn, evs):
    """Returns a list of every nodes of the BN who contains an evidence"""
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append([i,bn.variable(i).name()])
    return res
    
def evsPotentials(bn, jt , evs, diffu):
    '''Instructions to create, fill and initialize the potentials of soft evidences'''
    res = [] 
    ids = labelPotentialEvs(bn, evs)
    for i in evs:
        num = bn.idFromName(i)
        compilator.createPotentialClique("EV_"+str(num),str(num))
        compilator.addVariablePotential(str(num), "EV_"+str(num))
        compilator.addSoftEvidencePotential(str(i), "EV_"+str(num), str(0), "evs.get("+str([num,i])+"[1])")
    for i in ids:
        for j in jt.ids():
            if (i[0] in jt.clique(j)):
                b = 1
                for l in bn.parents(i[0]):
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
#                    compilator.createPotentialClique("EV_"+str(i[0]),str(i[0]))
#                    compilator.addVariablePotential(str(i[0]), "EV_"+str(i[0]))
#                    cpt = 0
#                    compilator.addSoftEvidencePotential(str(i[1]), "EV_"+str(i[0]), str(cpt), "evs.get("+str(i)+"[1])")
                    varClique = list(jt.clique(j))
                    label = labelPotential(jt,j)
                    compilator.multiplicationPotentials(label,"EV_"+str(i[0]),varClique,[str(i[0])])
#                    for k in diffu:
#                        if(k[0] == j):
#                            compilator.multiplicationPotentials(label+"to"+labelPotential(jt,k[1]),"EV_"+str(i[0]),varClique,[str(i[0])])
    return res
def neighbors(jt,c):
    """List of all the direct neighbors of a clique c in a junction tree jt"""
    ls = jt.edges()
    res = []
    for i in ls:
        if(i[0] == c):
            res.append(i[1])
        if(i[1] == c):
            res.append(i[0])
    return res

def nbneighbors(jt,c):
    return len(neighbors(jt,c))

def isTarget(bn,jt,target,n):
    '''Verifies if a clique n contains a target'''
    for i in target:
        if(bn.idFromName(i) in jt.clique(n)):
            return i
    return -1
    
def mainClique(bn,jt,target):
    """Gives the main clique of a junction where the information will be focused"""
    maxi = -1 #count how many neighbors the clique with the most neighbours and having at least a target has
    for i in jt.ids():
        for j in target:
            if(bn.idFromName(j) in jt.clique(i)):
                if(nbneighbors(jt,i) > maxi):
                    maxi = nbneighbors(jt,i)
                    res = i
    return res
    
def parcours(bn, jt, targetmp, n, r, absorp, diffu, cliquesTar):
    """Returns two lists for the absorption and the diffusion of the information in the junction tree"""
    ls = neighbors(jt,n)
    intersection = False
    if(r in ls):
        ls.remove(r)
    if(len(ls) == 0):
        return False
    for i in ls:
            tarnow = isTarget(bn,jt,targetmp,i)
            if(tarnow != -1):
                cliquesTar[tarnow] = i
                targetmp.remove(tarnow)
            tv = parcours(bn, jt,targetmp,i,n, absorp, diffu, cliquesTar)
            tar = tv or (tarnow != -1)
            absorp.append([i,n])
            if(tar):
                diffu.insert(0,[n,i])
                intersection = True
    return tar or intersection

def labelSeparator(jt, ca, cb): 
    """Returns the separator's label between ca and cb"""
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "xx"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res

def AinterB(la,lb):
    """Returns the intersection between lists la and lb"""
    res = []    
    for i in la:
        if(i in lb):
            res.append(i)
    return res
    
def sendMessAbsorp(bn, jt, ca, cb):
    """Updates the compiler array with inscrutions to send the message (absorption) from ca to cb"""
    np = labelSeparator(jt, ca, cb)
    varNp = AinterB(list(jt.clique(ca)),list(jt.clique(cb))) 
    compilator.createPotentialClique(np,varNp)
    for i in varNp:
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(bn,np, labelPotential(jt,ca),list(varNp),list(jt.clique(ca)))
    compilator.multiplicationPotentials(labelPotential(jt,cb), np,list(jt.clique(cb)),list(varNp))

def collectAroundCliq(bn, jt, ca, index, diffu):
    """Updates the compiler array to collect informations arround the cliq ca. index is the index of ca in diffu and diffutmp is the list of the first element of all elements of diffu until index"""
    neigh = neighbors(jt, ca)
    neigh.remove(diffu[index][1]) #we delete the destination
    if(index > 0 and diffu[index-1][1] == ca):
        neigh.remove(diffu[index-1][0]) #we delete the neighbor who has already given information
    for i in neigh:
        if([i,ca] in diffu[:index-1]): #The potential is a "diffusion's potential"
            np = labelSeparator(jt, i, ca)+"dif"
            varNp = AinterB(list(jt.clique(i)),list(jt.clique(ca)))
            compilator.multiplicationPotentials(labelPotential(jt,ca)+"to"+labelPotential(jt,diffu[index][1]),np, list(jt.clique(ca)), list(varNp))
        else: #The potential is a "absorption's potential"
            np = labelSeparator(jt, i, ca)
            varNp = AinterB(list(jt.clique(i)),list(jt.clique(ca)))
            compilator.multiplicationPotentials(labelPotential(jt,ca)+"to"+labelPotential(jt,diffu[index][1]),np, list(jt.clique(ca)), list(varNp))
        

def sendMessDiffu(bn, jt, ca, cb, index, diffu, cliquesTar):
    """Updates the compiler array with instructions to send the message (diffusion) from ca to cb"""
    collectAroundCliq(bn, jt, ca, index, diffu)
    np = labelSeparator(jt, ca, cb)+"dif"
    varNp = AinterB(list(jt.clique(ca)),list(jt.clique(cb)))
    label = labelPotential(jt,ca)+"to"+labelPotential(jt,cb)
    compilator.createPotentialClique(np, varNp)
    for i in varNp:
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(bn, np, label, list(varNp), list(jt.clique(ca)))
    if(index < (len(diffu)-1) and diffu[index+1][0] == diffu[index][1]):
        compilator.multiplicationPotentials(labelPotential(jt,cb)+"to"+labelPotential(jt,diffu[index+1][1]), np, list(jt.clique(cb)), list(varNp))
    if(cb in cliquesTar.values()):
        compilator.multiplicationPotentials(labelPotential(jt,cb)+"tar", np, list(jt.clique(cb)), list(varNp))

def deleteTarMainCliq(bn, jt, targetmp, rac):
    for i in jt.clique(rac):
        for j in targetmp:
            if(bn.idFromName(j) == i):
                targetmp.remove(j)
                
def inference(bn, jt, absorp, diffu, targets, targetmp, cliquesTar): 
    """Considering the targets of a bn, inference does the absorption and the diffusion of the information"""
    for i in absorp:
        sendMessAbsorp(bn, jt, i[0], i[1])
    
    if(diffu):
        for i in range(len(diffu)):
            sendMessDiffu(bn, jt, diffu[i][0], diffu[i][1], i, diffu, cliquesTar)

        for i in targetmp:        #We collect around cliques which contains targets
            for j in diffu:
                x = bn.idFromName(i)
                if(x in jt.clique(j[1])):
                    neigh = neighbors(jt,j[1])
                    neigh.remove(j[0])
                    for l in neigh:
                        np = labelSeparator(jt, l, j[1])
                        varNp = AinterB(list(jt.clique(l)),list(jt.clique(j[1])))
                        compilator.multiplicationPotentials(labelPotential(jt,j[1])+"tar", np,list(jt.clique(j[1])),list(varNp))
    return diffu
    
def output(bn,jt,target,diffu, cliquesTar): 
    """Instructions for the last cliques to be normalized and return the results for respective targets"""    
    rac = mainClique(bn,jt,target)
    ls = list(target)
    #Targets who are still in the main clique
    for i in target:
        x = bn.idFromName(i)
        if(x in jt.clique(rac)):
            compilator.createPotentialClique("P_"+str(x),[str(x)])
            compilator.addVariablePotential(str(x), "P_"+str(x))
            compilator.marginalisation(bn,"P_"+str(x), labelPotential(jt,rac),[x],list(jt.clique(rac)))
            compilator.normalisation("P_"+str(x), bn.variable(x).name())
            ls.remove(i)
    #All the other targets
    for tar, cliq in cliquesTar.items():
        x = bn.idFromName(tar)
        compilator.createPotentialClique("P_"+str(x),[str(x)])
        compilator.addVariablePotential(str(x), "P_"+str(x))
        compilator.marginalisation(bn,"P_"+str(x), labelPotential(jt,cliq)+"tar",[x],list(jt.clique(cliq)))
        compilator.normalisation("P_"+str(x), bn.variable(x).name())
                
    
compilator=Compiler()
    
def compil(bn, targets, evs):
    """This function uses all the predefined functions above to fill the compiler array with instructions to get the targets of a bn according to evidences"""
    ie=gum.LazyPropagation(bn)
    jt = ie.junctionTree()
    absorp = [] #the list for the absorption
    diffu = [] #the list for the diffusion
    cliquesTar = {} #the dictionnary which contains the couples {target:clique}
    r = mainClique(bn, jt, targets)
    n = r
    targetmp1 = list(targets) #for parcours (this list is changed)
    deleteTarMainCliq(bn, jt, targetmp1, r)
    targetmp2 = list(targetmp1) #for inference (this list is not changed)
    parcours(bn, jt, targetmp1, n, r, absorp, diffu, cliquesTar)
    #Creation and initialization of potentials
    creationPotentialsAbsorp(bn, jt)
    initPotentialsAbsorp(bn, jt)
    evsPotentials(bn, jt, evs, diffu)
    creaIniPotentialsDiffu(bn, jt, diffu, cliquesTar, targets)
    
    #Absorption and diffusion
    inference(bn, jt, absorp, diffu, targets, targetmp2, cliquesTar)
    
    #Computing targets
    output(bn, jt, targets, diffu, cliquesTar)
    return compilator.getTab()

#Diffusion opé
    
    