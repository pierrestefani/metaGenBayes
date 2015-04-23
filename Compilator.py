# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:50:21 2015

@author: Marvin
"""

import pyAgrum as gum
#import metacodeExtended as mce

def nomPotentiel(jt,c):
    """Retourne le nom du potentiel de la clique c"""
    res="Phi"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res
    
def creationPotentiels(jt):
    """Renvoie la liste des actions à effecteur pour créer les potentiels des cliques et leur affecte leurs variables"""
    res = []
    for i in jt.ids():
        np = nomPotentiel(jt,i)
        res.append(["CPO",np])
        for j in jt.clique(i):
            res.append(["ADV",str(j), np])
        res.append(["FIL",np,1])
    return res

def initPotentiels(bn,jt):
    """Initialise les potentiels des cliques"""
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
                    res.append(["MUC",nomPotentiel(jt,j),str(i)])
                    break
    return res
    
def nomPotentielEvs(bn, evs):
    """Retourne la liste des noeuds du bn qui sont une évidence"""
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append(i)
    return res
    
def evsPotentiels(bn, jt , evs):
    res = [] 
    ids = nomPotentielEvs(bn, evs)
    for i in ids:
        for j in jt.ids():
            if (i in jt.clique(j)):
                b = 1
                for l in bn.parents(i):
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    for index in enumerate(ids): 
                        res.append(["CPO","EV_"+str(i)])
                        res.append(["ADV", str(i),"EV_"+str(i)])
                        res.append(["FIL",nomPotentiel(jt,j),0])
                        res.append(["MUL", nomPotentiel(jt,j),"EV_"+str(i)])
                    break
    return res

def neighbors(jt,c):
    """Retourne la liste des voisins de la clique c"""
    ls = jt.edges()
    res = []
    for i in ls:
        if(i[0] == c):
            res.append(i[1])
        if(i[1] == c):
            res.append(i[0])
    return res

def nbneighbors(jt,c):
    """Retourne le nombre de voisins de la clique c"""
    return len(neighbors(jt,c))

def isTarget(bn,jt,target,n):
    for i in target:
        if(bn.idFromName(i) in jt.clique(n)):
            return True
    return False
    
def cliqueRacine(bn,jt,target):
    """Retourne la clique "racine" vers laquelle on fait converger l'information"""
    maxi = -1 #contient le nombre de voisins de la clique contenant le plus de voisins et contenant au moins une target
    for i in jt.ids():
        for j in target:
            if(bn.idFromName(j) in jt.clique(i)):
                if(nbneighbors(jt,i) > maxi):
                    maxi = nbneighbors(jt,i)
                    res = i
    return res
    
def parcours(bn, jt, target, n, r, absorp, diffu):
    """Renvoie la liste à parcourir pour l'absorption et la diffusion"""
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

def nom_separateur(jt, ca, cb):    
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
    """Renvoie la liste des actions à effectuer pour envoyer le message de ca à cb"""
    np = nom_separateur(jt, ca, cb)    
    res = [["CPO",np]]
    for i in AinterB(jt.clique(ca), jt.clique(cb)):
        res.append(["ADV", str(i), np])
    res.append(["MAR",np,nomPotentiel(jt,ca)])
    res.append(["MUL", nomPotentiel(jt,cb), np])
    return res

def sendMessDiffu(bn, jt, ca, cb):
    """Renvoie la liste des actions à effectuer pour envoyer le message de ca à cb"""
    np = nom_separateur(jt, ca, cb)+"dif"   #le dif nous sert de '
    res = [["CPO",np]]
    for i in AinterB(jt.clique(ca), jt.clique(cb)):
        res.append(["ADV", str(i), np])
    res.append(["MAR",np,nomPotentiel(jt,ca)])
    res.append(["MUL", nomPotentiel(jt,cb), np])
    return res
    
def inference(bn, jt, target):
    res = []    
    r = cliqueRacine(bn, jt, target)
    n = r
    absorp = []
    diffu = []
    parcours(bn ,jt, target, n, r, absorp, diffu)
    for i in absorp:
        res.extend(sendMessAbsor(bn, jt, i[0], i[1]))
    
    if(diffu):
        for i in diffu:
            res.extend(sendMessDiffu(bn, jt, i[0], i[1]))
    return res
    
def cliqTarget(bn,jt,target): #implementation naïve
    """Renvoie la liste des cliques pour le calcul des targets"""    
    rac = cliqueRacine(bn,jt,target)
    ls = target
    res = []
    #On s'occupe des target qui sont dans la racine
    for i in target:
        x = bn.idFromName(i)
        if(x in jt.clique(rac)):
            res.append(["CPO","P_"+str(x)])
            res.append(["ADV",str(x),"P_"+str(x)])
            res.append(["MAR","P_"+str(x),str(nomPotentiel(jt,rac))])
            res.append(["NOR","P_"+str(x)])
            ls.remove(i)
            break
    #Puis on s'occupe des autres target
    for i in ls:
        for j in jt.ids():
            x = bn.idFromName(i)
            if(x in jt.clique(j)):
                res.append(["CPO","P_"+str(x)])
                res.append(["ADV",str(x),"P_"+str(x)])
                res.append(["MAR","P_"+str(x),str(nomPotentiel(jt,j))])
                res.append(["NOR","P_"+str(x)])
                break
    return res
                
    
    
def compil(bn,target,evs):
    """Retourne la liste des actions à effectuer jusqu'au calcul des targets"""
    res = []
    ie=gum.LazyPropagation(bn)
    jt = ie.junctionTree()
    
    #Creation des potentiels des cliques et ajout des variables à leur potentiel respectif.
    res.extend(creationPotentiels(jt))
    """ne pas oublier de fill pour PyAgrum, voir inférence à la main"""
    #Initialisation des potentiels
    res.extend(initPotentiels(bn, jt))
    
    #Potentiel des évidences
    res.extend(evsPotentiels(bn,jt,evs))
                
    #Absorption et diffusion
    res.extend(inference(bn, jt, target))
    
    #Calcul des targets
    res.extend(cliqTarget(bn,jt,target))

    return res
    
    
    