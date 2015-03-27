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

from debugGenerator import Generation

#Génère des noms de potentiel
def nomPotentiel(jt,c):
    res="Phi"
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
    c = Counter(list(chain(*jt.edges())))
    return c.most_common(1)[0][0]

#Initialisation des potentiels de séparateurs

#Découpe les arcs en liste de couples
def couples_cliques(iterable, taille, format=iter):
    it = iter(iterable)
    while True:
        yield format(chain((it.next(),), islice(it, taille - 1)))

#Retourne le nom du séparateur entre deux cliques a et b d'un arbre de jonction jt
def nom_separateur(jt, ca, cb):    
    res="Psi"
    for n in list(jt.clique(ca)):
        res += str(n)+"_"
    res+= "--"
    for n in list(jt.clique(cb)):
        res += str(n)+"_"
    return res
                    
#Absorption
#Renvoie la liste des voisins de la clique c
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
    
#Absorption
def absorption(bn,jt, rac):
    neigh = lsneighbors(jt)
    ls = jt.ids() #liste contenant tous les noeuds qui n'ont pas encore envoyé leur message
    
    
    while len(ls) != 1:
        suppr = []
        for i in ls:
            nomess = lInterm(neigh[i],ls) #Ce sont les voisins de i qui n'ont pas envoyé leur message
            if(len(nomess) == 1 and i != rac):
                print("Envoi du message de "+nomPotentiel(jt,i)+" à "+nomPotentiel(jt,nomess[0]))
                print("Marginalisation de "+nom_separateur(jt, i, nomess[0])+" selon "+nomPotentiel(jt,i))
                print("Multiplication de "+nomPotentiel(jt,nomess[0])+" par "+ nom_separateur(jt, i, nomess[0])+"\n")
                suppr.append(i)
        
        for i in suppr:
            ls.remove(i)

#Diffusion
"""def diffusion(bn,jt,rac):"""

    
    
#Reçoit un réseau bayésien et des évidences et calcule la probabilité des targets
def metaCode(bn,evs,t,generator):
    ie = gum.LazyPropagation(bn)
    jt = ie.junctionTree()
  

    print("###################################")
    print("##### Creation des potentiels #####")
    print("###################################")
   
    for c in jt.ids() :
        res = "Création du potentiel : "+nomPotentiel(jt,c)
                print(res)    
    
    ids = nomPotentielEvs(bn,evs)
    for i in ids:
        print("Création du potentiel : Ev_"+str(i))
    
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
    rac = cliqueRacine(jt)
    absorption(bn,jt,rac)
    
def ajouteFlag(jt,default):
    fl={}
    for i in jt.ids():
        fl[i]=default
    return fl
    
    
def pitibn():
    bn=gum.BayesNet()
    a,b,c,d,e=[bn.add(gum.LabelizedVariable(s,s,2)) for s in 'abcde']
    bn.addArc(a,b)
    bn.addArc(a,c)
    bn.addArc(b,d)
    bn.addArc(c,d)
    bn.addArc(e,c)

    bn.generateCPTs()
    return bn
    
#bn = gum.loadBN("C:/Users/Marvin/Desktop/Informatique/Projet PIMA/testMetaBaysGen/BNs/asia.bif")
#target = ["dypsonae?","bronchitis?"]
#evs = {"smoking?":[1,0]}

#bn=pitibn()
#target = []
#evs= {}
generator=DebugGeneration()
bn = gum.loadBN("/home/ubuntu/Documents/BNS/asia.bif")
target = []
evs = {}

ie=gum.LazyPropagation(bn)
jt = ie.junctionTree()
metaCode(bn,evs, target,generator)
showBN(bn,size="3")
showJT(bn,size="3")