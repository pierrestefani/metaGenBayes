# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:47:35 2015
@author: ubuntu
"""
import pyAgrum as gum
import gumLib.notebook as gnb
from collections import Counter
from itertools import chain, islice


def nomPotentiel(jt,c):
    '''Génère des noms de potentiel pour la clique c d'un arbre de jonction'''
    res="Phi"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res
    
def nomPotentielEvs(bn, evs):  
    '''Retourne le nom des potentiels associés aux évidences'''
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append(i)
    return res
    
    
def cliqueRacine(bn,jt,target):
    '''Retourne la clique "racine" vers laquelle on fait converger l'information'''
    maxi = -1 #contient le nombre de voisins de la clique contenant le plus de voisins et contenant au moins une target
    for i in jt.ids():
        for j in target:
            if(bn.idFromName(j) in jt.clique(i)):
                if(nbneighbors(jt,i) > maxi):
                    maxi = nbneighbors(jt,i)
                    res = i
    return res

  
def couples_cliques(iterable, taille, format=iter):
    '''Découpe les arcs en liste de couples  '''
    it = iter(iterable)
    while True:
        yield format(chain((it.next(),), islice(it, taille - 1)))
    
    
def neighbors(jt,c):
    '''Renvoie la liste des cliques voisines de la clique c dans l'arbre de jonction jt'''
    ls = jt.edges()
    res = []
    for i in ls:
        if(i[0] == c):
            res.append(i[1])
        if(i[1] == c):
            res.append(i[0])
    return res


def nbneighbors(jt,c):
    '''Retourne le nombre de voisins de la clique c'''
    return len(neighbors(jt,c))


def nom_separateur(jt, ca, cb):    
    '''Retourne le nom du séparateur entre deux cliques a et b d'un arbre de jonction jt'''
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "--"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res


def isTarget(bn,jt,target,n):
    '''Retourne vraie si il existe une target dans la clique n, faux sinon'''
    for i in target:
        if(bn.idFromName(i) in jt.clique(n)):
            return True
    return False