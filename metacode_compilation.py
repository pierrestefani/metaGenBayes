# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:50:21 2015

@author: Marvin
"""

import pyAgrum as gum
from Compiler import Compiler
#import metacodeExtended as mce

def labelPotential(jt,c):
    """Get the name of the potential for a clique c"""
    res="Phi"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res
    
def creationPotentials(jt):
    """Fill the compiler array of instructions in order to create the potentials and add the corresponding variables"""
    res = []
    for i in jt.ids():
        compilator.createPotentialClique(labelPotential(jt,i))
        for j in jt.clique(i):
            compilator.addVariablePotential(str(j), labelPotential(jt, i))
        compilator.fillPotential(labelPotential(jt,i),1)
    return res

def initPotentials(bn,jt):
    """Instructions for the initialization of the potentials"""
    res = []    
    for i in bn.ids():
        for j in jt.ids():        
            if(i in jt.clique(j)):
                b = 1
                for l in bn.parents(i):                  
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    compilator.multiplicationCPT(labelPotential(jt,j),str(i))
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
                    compilator.createPotentialClique("EV_"+str(i[0]))
                    compilator.addVariablePotential(str(i[0]), "EV_"+str(i[0]))
                    compilator.fillPotential("EV_"+str(i[0]),0)
                    cpt = 0
                    for v in evs.get(i[1]):
                        compilator.addSoftEvidencePotential(str(i[1]), "EV_"+str(i[0]), str(cpt), str(v))
                        cpt = cpt + 1
                    compilator.multiplicationPotentials(labelPotential(jt,j),"EV_"+str(i[0]))
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
            return True
    return False
    
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
    
def parcours(bn, jt, target, n, r, absorp, diffu):
    """Returns two lists fot he absoprtion and the diffusion of the information in the junction tree"""
    ls = neighbors(jt,n)
    if(r in ls):
        ls.remove(r)
    if(len(ls) == 0):
        return False
    for i in ls:
            tv = parcours(bn, jt,target,i,n, absorp, diffu)
            tar = tv or isTarget(bn,jt,target,i)
            absorp.append([i,n])
            if(tar):
                diffu.insert(0,[n,i])
    return tar

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
    compilator.createPotentialClique(np)
    for i in AinterB(jt.clique(ca), jt.clique(cb)):
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(np, labelPotential(jt,ca))
    compilator.multiplicationPotentials(labelPotential(jt,cb), np)

def sendMessDiffu(bn, jt, ca, cb):
    """Updates the compiler array with instructions for the diffusion"""
    np = labelSeparator(jt, ca, cb)+"dif"   #two different potential variables are used for absorption and diffusion in order to keep some of the results in certain nodes
    compilator.createPotentialClique(np)
    for i in AinterB(jt.clique(ca), jt.clique(cb)):
        compilator.addVariablePotential(str(i), np)
    compilator.marginalisation(np, labelPotential(jt,ca))
    compilator.multiplicationPotentials(labelPotential(jt,cb), np)

def inference(bn, jt, target): 
    """Considering the targets of a bn, inference does the absorption and the diffusion of the information"""
    r = mainClique(bn, jt, target)
    n = r
    absorp = []
    diffu = []
    parcours(bn ,jt, target, n, r, absorp, diffu)
    for i in absorp:
        sendMessAbsor(bn, jt, i[0], i[1])
    
    if(diffu):
        for i in diffu:
            sendMessDiffu(bn, jt, i[0], i[1])

    
def output(bn,jt,target): 
    """Instructions for the last cliques to be normalized and return the results for respective targets"""    
    rac = mainClique(bn,jt,target)
    ls = target
    #Targets who are still in the main clique
    for i in target:
        x = bn.idFromName(i)
        if(x in jt.clique(rac)):
            compilator.createPotentialClique("P_"+str(x))
            compilator.addVariablePotential(str(x), "P_"+str(x))
            compilator.marginalisation("P_"+str(x), labelPotential(jt,rac))
            compilator.normalisation("P_"+str(x))
            ls.remove(i)
            break
    #All the other targets
    for i in ls:
        for j in jt.ids():
            x = bn.idFromName(i)
            if(x in jt.clique(j)):
                compilator.createPotentialClique("P_"+str(x))
                compilator.addVariablePotential(str(x), "P_"+str(x))
                compilator.marginalisation("P_"+str(x), labelPotential(jt,j))
                compilator.normalisation("P_"+str(x))
                break
                
    
compilator=Compiler()
    
def compil(bn,target,evs):
    """This function uses all the predefined functions above to fill the compiler array with instructions to get the targets of a bn according to evidences"""
    ie=gum.LazyPropagation(bn)
    jt = ie.junctionTree()
    
    #Creation des potentiels des cliques et ajout des variables à leur potentiel respectif.
    creationPotentials(jt)

    #Initialisation des potentiels
    initPotentials(bn, jt)
    
    #Potentiel des évidences
    evsPotentials(bn,jt,evs)
                
    #Absorption et diffusion
    inference(bn, jt, target)
    
    #Calcul des targets
    output(bn,jt,target)

    return compilator.getTab()
    
    
    