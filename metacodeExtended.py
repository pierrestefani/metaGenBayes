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

""" CODE ABSORPTION LOURD TEMPORAIRE """

#Retourne l privé de m, on s'en servira pour avoir la liste des voisins d'un noeud qui ont envoyé leur message.
def lOum(l,m):
    res = []    
    for i in l:
        if (not(i in m)):
            res.append(i)
    return res
    
#Retourne l intersection m, on s'en servira pour avoir la liste des voisins d'un noeud qui n'ont pas envoyé leur message
def lInterm(l,m):
    res = []
    for i in l:
        if(i in l and i in m):
            res.append(i)
    return res
    
#Retoure la liste dont le i ème élément est la liste des voisins de la  ième clique    
def lsneighbors(jt):
    neigh = {} 
    for i in jt.ids():
        neigh[i]=neighbors(jt,i)
    return neigh
    

#Retourne la liste dont le i ème élément est le nombre de voisins de la i ème clique      
def lsnbneighbors(jt):
    return len(lsneighbors(jt))
    
"""FIN"""



