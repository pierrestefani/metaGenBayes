# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:42:05 2015

@author: ubuntu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:24:09 2015

@author: Marvin
"""


import pyAgrum as gum
import gumLib.notebook as gnb

from collections import Counter
from itertools import chain, islice

#Génère des noms de potentiel
def nomPotentiel(jt,c):
    res="Phi_"
    for n in jt.clique(c):
        res += str(n)+"_"
    return res

#Ajoute les variables à leur potentiel respectif
def addVariables(jt):
    for c in jt.ids():
        for n in jt.clique(c):
            print("Ajout de la variable "+str(n)+" au potentiel " +nomPotentiel(jt,c))

#Initialisation des potentiels
def initPotentials(bn,jt):
    for i in bn.ids():
        for j in jt.ids():        
            if(i in jt.clique(j)):
                b = 1
                for l in bn.parents(i):                  
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    print("Multiplication du potentiel "+nomPotentiel(jt,j)+" par la cpt de la variable "+str(i))
                    break
                
#Retourne le nom des potentiels associés aux évidences
def nomPotentielEvs(bn, evs):    
    res=list()
    for i in bn.ids():
        if(evs.has_key(bn.variable(i).name())):
            res.append(i) 
    return res

#Affectation des évidences à un potentiel
def evsPotentials(bn, jt, ids):
    for i in ids:
        print(i)
        for j in jt.ids():
            if (i in jt.clique(j)):
                b = 1
                for l in bn.parents(i):
                    if(not(l in jt.clique(j))):
                        b = 0
                        break
                if(b == 1):
                    for index in enumerate(ids): 
                        print("Multiplication du potentiel Ev"+str(i)+" par la variable (évidence) "+str(i))
                        break
                
                
#Retourne la clique "racine" vers laquelle on fait converger l'information
def cliqueRacine(jt):
    c = Counter(list(itertools.chain(*jt.edges())))
    return c.most_common(1)[0][0]
    
"""def absorption(jt):
    for i in jt.ids():
        if()"""
        
#Initialisation des potentiels de séparateurs
def couples_cliques(iterable, taille, format=iter):
    """Découpe les arcs en liste de couples"""
    it = iter(iterable)
    while True:
        yield format(chain((it.next(),), islice(it, taille - 1)))

def nom_separateur(jt, ca, cb):
    """Retourne le nom du séparateur entre deux cliques a et b d'un arbre de jonction jt"""    
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "--"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res
                    
#Reçoit un réseau bayésien et des évidences et calcule la probabilité des targets
def metaCode(bn,evs,t):
    ie = gum.LazyPropagation(bn)
    jt = ie.junctionTree()
  

    print("###################################")
    print("##### Creation des potentiels #####")
    print("###################################")
        
    for c in jt.ids() :
        res = "Creation du potentiel : "+nomPotentiel(jt,c)
        print(res)
    
    
    ids = nomPotentielEvs(bn,evs)
    for i in ids:
        print("Création du potentiel : Ev"+str(i))
    
    print("##########################################################")
    print("##### Ajout des variables à leur potentiel respectif #####")
    print("##########################################################")
    addVariables(jt)
    for i in ids:
        print("Ajout de la variable "+str(i)+" au potentiel Ev"+str(i))
    print("#########################################")
    print("##### Initialisation des potentiels #####")
    print("#########################################")
    initPotentials(bn,jt)
    evsPotentials(bn,jt,ids) 
    
    print("######################################################")
    print("##### Création et Initialisation des Séparateurs #####")
    print("######################################################")
    #Création du potentiel séparateur
    for n in couples_cliques(jt.edges(), 1, list) :
        print("Création du potentiel "+nom_separateur(jt, n[0][0], n[0][1]))
    #Ajout des variables (ie : les variables dans le séparateur)
    for n in couples_cliques(jt.edges(), 1, list) :
        for c in n:
            for i in list(jt.clique(c[0]).intersection(jt.clique(c[1]))):
                print("Ajout de la variable "+str(i)+" au potentiel "+nom_separateur(jt, c[0], c[1]))

   
    print("#########################################")
    print("############# INFERENCE #################")
    print("#########################################")
    
    
bn = gum.loadBN("/home/ubuntu/Documents/BNS/asia.bif")
target = ["dypsonae?","bronchitis?"]
evs = {"smoking?":[1,0]}
ie=gum.LazyPropagation(bn)
jt = ie.junctionTree()
metaCode(bn,evs, target)
print(cliqueRacine(jt))
print(jt.clique(4))
jt.neighbors(4)
