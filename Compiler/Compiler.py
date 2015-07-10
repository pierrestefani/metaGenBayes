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
    
def creationPotentials(bn, jt, targets):
    """Fill the compiler array of instructions in order to create the potentials and add the corresponding variables"""
    res = []
    for i in jt.ids():
        label = labelPotential(jt,i)
        compilator.createPotentialClique(label,list(jt.clique(i)))
        compilator.createPotentialClique(label+"dif",list(jt.clique(i)))
        for j in jt.clique(i):
            compilator.addVariablePotential(str(j), label)
            compilator.addVariablePotential(str(j), label+"dif")
        compilator.fillPotential(label,1)
        compilator.fillPotential(label+"dif",1)
    
    rac = mainClique(bn,jt,targets)
    variables = list(jt.clique(rac))
    label1 = labelPotential(jt,rac)
    for i in neighbors(jt,rac):
        label2 = label1+"to"+labelPotential(jt,i)
        compilator.createPotentialClique(label2,variables)
        for j in jt.clique(rac):
            compilator.addVariablePotential(str(j), label2)
        compilator.fillPotential(label2,1)
    return res

def initPotentials(bn,jt):
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
    
def labelPotentialEvs(bn, evs):
    """Returns a list of every nodes of the BN who contains an evidence"""
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append([i,bn.variable(i).name()])
    return res
    
def evsPotentials(bn, jt , evs):
    '''Instructions to create, fill and initialize the potentials of soft evidences'''
    res = [] 
    ids = labelPotentialEvs(bn, evs)
    for i in ids:
        for j in jt.ids():
            if (i[0] in jt.clique(j)):
                b = 1
                for l in bn.parents(i[0]):
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    #index, enumerate... supprimés (résultats toujours corrects)
                    compilator.createPotentialClique("EV_"+str(i[0]),str(i[0]))
                    compilator.addVariablePotential(str(i[0]), "EV_"+str(i[0]))
                    cpt = 0
                    compilator.addSoftEvidencePotential(str(i[1]), "EV_"+str(i[0]), str(cpt), "evs.get("+str(i)+"[1])")
                    compilator.multiplicationPotentials(labelPotential(jt,j),"EV_"+str(i[0]),list(jt.clique(j)),[str(i[0])])
                    compilator.multiplicationPotentials(labelPotential(jt,j)+"dif","EV_"+str(i[0]),list(jt.clique(j)),[str(i[0])])
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
    
def parcours(bn, jt, targetmp, n, r, absorp, diffu):
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
                targetmp.remove(tarnow)
            tv = parcours(bn, jt,targetmp,i,n, absorp, diffu)
            
            tar = tv or (tarnow != -1)
            absorp.append([i,n])
            if(tar):
                diffu.insert(0,[n,i])
#                if(tarnow != -1):
#                    targetmp.remove(tarnow)
                intersection = True
    return tar or intersection

def labelSeparator(jt, ca, cb):    
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "xx"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res

def AinterB(la,lb):
    res = []    
    for i in la:
        if(i in lb):
            res.append(i)
    return res
    
def sendMessAbsor(bn, jt, ca, cb):
    """Updates the compiler array with inscrutions to send the message from ca to cb"""
    np = labelSeparator(jt, ca, cb)
    varNp = AinterB(list(jt.clique(ca)),list(jt.clique(cb))) 
    compilator.createPotentialClique(np,varNp)
    for i in varNp:
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(bn,np, labelPotential(jt,ca),list(varNp),list(jt.clique(ca)))
    compilator.multiplicationPotentials(labelPotential(jt,cb), np,list(jt.clique(cb)),list(varNp))

def sendMessAbsorToDiff(bn, jt, ca, cb):
    """Updates the compiler array with inscrutions to send the message from ca to cb"""
    np = labelSeparator(jt, ca, cb)+"dif"
    varNp = AinterB(list(jt.clique(ca)),list(jt.clique(cb))) 
    compilator.createPotentialClique(np,varNp)
    for i in varNp:
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(bn,np, labelPotential(jt,ca),list(varNp),list(jt.clique(ca)))
    compilator.multiplicationPotentials(labelPotential(jt,cb)+"dif", np,list(jt.clique(cb)),list(varNp))

def sendMessDiffu(bn, jt, ca, cb, rac):
    """Updates the compiler array with instructions for the diffusion"""
    np = labelSeparator(jt, ca, cb)+"dif"   #two different potential variables are used for absorption and diffusion in order to keep some of the results in certain nodes
    varNp = AinterB(list(jt.clique(ca)),list(jt.clique(cb)))    
    compilator.createPotentialClique(np,varNp)
    for i in varNp:
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(bn,np, labelPotential(jt,ca)+"dif",list(varNp),list(jt.clique(ca)))
    compilator.multiplicationPotentials(labelPotential(jt,cb)+"dif", np,list(jt.clique(cb)),list(varNp))

def inference(bn, jt, target,targetmp): 
    """Considering the targets of a bn, inference does the absorption and the diffusion of the information"""
    r = mainClique(bn, jt, target)
    label = labelPotential(jt,r)
    n = r
    absorp = []
    diffu = []
    neigh = neighbors(jt,r)
    targetmp = list(target)
    for i in jt.clique(r):
        for j in targetmp:
            if(bn.idFromName(j) == i):
                targetmp.remove(j)
    parcours(bn ,jt, targetmp, n, r, absorp, diffu)
    
                
    for i in neigh:
         compilator.multiplicationPotentials(label+"to"+labelPotential(jt,i), label,list(jt.clique(r)),list(jt.clique(r)))  
    for i in absorp:
        if(i[1] == r):
            np = labelSeparator(jt, i[0], i[1])
            varNp = AinterB(list(jt.clique(i[0])),list(jt.clique(i[1]))) 
            compilator.createPotentialClique(np,varNp)
            for v in varNp:
                compilator.addVariablePotential(str(v), np)
            compilator.marginalisation(bn,np, labelPotential(jt,i[0]),list(varNp),list(jt.clique(i[0])))
            for j in neigh:            
                if(j != i[0]):
                    compilator.multiplicationPotentials(label+"to"+labelPotential(jt,j), np,list(jt.clique(i[1])),list(varNp))
            compilator.multiplicationPotentials(label, np,list(jt.clique(r)),list(varNp))
        else:
            sendMessAbsor(bn, jt, i[0], i[1])
    
    if(diffu):
        for i in range(len(diffu)):
            if(diffu[i][0]==r):
                np = labelSeparator(jt, diffu[i][0], diffu[i][1])+"dif"
                varNp = AinterB(list(jt.clique(diffu[i][0])),list(jt.clique(diffu[i][1])))    
                compilator.createPotentialClique(np,varNp)
                for v in varNp:
                    compilator.addVariablePotential(str(v), np)
                compilator.marginalisation(bn,np, labelPotential(jt,diffu[i][0])+"to"+labelPotential(jt,diffu[i][1]),list(varNp),list(jt.clique(diffu[i][0])))
                compilator.multiplicationPotentials(labelPotential(jt,diffu[i][1])+"dif", np,list(jt.clique(diffu[i][1])),list(varNp))
            else:
                neigh = neighbors(jt,diffu[i][0])
                neigh.remove(diffu[i][1])
                if(diffu[i-1][1]==diffu[i][0]):
                    neigh.remove(diffu[i-1][0])
                for j in neigh:
#                    sendMessAbsorToDiff(bn,jt,j,diffu[i][0])
                    np = labelSeparator(jt, j, diffu[i][0])
                    varNp = AinterB(list(jt.clique(j)),list(jt.clique(diffu[i][0])))
                    compilator.multiplicationPotentials(labelPotential(jt,diffu[i][0])+"dif", np,list(jt.clique(diffu[i][0])),list(varNp))
                sendMessDiffu(bn, jt, diffu[i][0], diffu[i][1], r)
    return diffu
    
def output(bn,jt,target,diffu): 
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
    for i in ls:
        for j in diffu:
            x = bn.idFromName(i)
            if(x in jt.clique(j[1])):
                neigh = neighbors(jt,j[1])
                neigh.remove(j[0])
                for l in neigh:
                    np = labelSeparator(jt, l, j[1])
                    varNp = AinterB(list(jt.clique(j[1])),list(jt.clique(l)))
                    compilator.multiplicationPotentials(labelPotential(jt,j[1])+"dif", np,list(jt.clique(j[1])),list(varNp))
                compilator.createPotentialClique("P_"+str(x),[str(x)])
                compilator.addVariablePotential(str(x), "P_"+str(x))
                compilator.marginalisation(bn,"P_"+str(x), labelPotential(jt,j[1])+"dif",[x],list(jt.clique(j[1])))
                compilator.normalisation("P_"+str(x), bn.variable(x).name())
                break
                
    
compilator=Compiler()
    
def compil(bn,target,evs):
    """This function uses all the predefined functions above to fill the compiler array with instructions to get the targets of a bn according to evidences"""
    ie=gum.LazyPropagation(bn)
    jt = ie.junctionTree()
    #Creation des potentiels des cliques et ajout des variables à leur potentiel respectif.
    creationPotentials(bn, jt, target)

    #Initialisation des potentiels
    initPotentials(bn, jt)
    
    #Potentiel des évidences
    evsPotentials(bn,jt,evs)
                
    #Absorption et diffusion
    diffu = inference(bn, jt, target, target)
    
    #Calcul des targets
    output(bn,jt,target,diffu)

    return compilator.getTab()

#Diffusion opé
    
    