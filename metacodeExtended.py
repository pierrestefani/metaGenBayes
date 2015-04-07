# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:47:35 2015

@author: ubuntu
"""

from collections import Counter
from itertools import chain, islice


#Génère des noms de potentiel
def nomPotentiel(jt,c):
    res="Phi"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res
    
#Retourne le nom des potentiels associés aux évidences
def nomPotentielEvs(bn, evs):    
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append(i)
    return res
    
#Retourne la clique "racine" vers laquelle on fait converger l'information
def cliqueRacine(jt):
    c = Counter(list(chain(*jt.edges())))
    return c.most_common(1)[0][0]

#Découpe les arcs en liste de couples    
def couples_cliques(iterable, taille, format=iter):
    it = iter(iterable)
    while True:
        yield format(chain((it.next(),), islice(it, taille - 1)))
    
def neighbors(jt,c):
    ls = jt.edges()
    res = []
    for i in ls:
        if(i[0] == c):
            res.append(i[1])
        if(i[1] == c):
            res.append(i[0])
    return res

#Retourne le nombre de voisins de la clique c
def nbneighbors(jt,c):
        return len(neighbors(jt,c))


#Retourne le nom du séparateur entre deux cliques a et b d'un arbre de jonction jt
def nom_separateur(jt, ca, cb):    
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "--"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res


def idsOfTargets(bn, target):
    """Retourne les ids de chaque target donnée pour le réseau bayésien considéré"""
    res=list()
    for i in bn.ids():
        if (bn.variable(i).name() in target):
            res.append(i)
    return res


def cliquesOfTargets(jt,bn,target):
    """Retourne le couple [target, clique de la target considéré]"""
    res = []
    sel = []
    for c in jt.ids():
        for n in jt.clique(c):
            if (n in idsOfTargets(bn,target) and (n not in sel)):
                res.append([n,c])
                sel.append(n)
    return res


