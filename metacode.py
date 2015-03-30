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

import metacodeExtended as mce

from debugGenerator import CompilGeneration


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
                    print("Multiplication du potentiel "+mce.nomPotentiel(jt,j)+" par la cpt de la variable "+str(i))
                    break
                


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
def absorption(bn,jt, rac):
    neigh = mce.lsneighbors(jt)
    ls = jt.ids() #liste contenant tous les noeuds qui n'ont pas encore envoyé leur message
    
    
    while len(ls) != 1:
        suppr = []
        for i in ls:
            nomess = mce.lInterm(neigh[i],ls) #Ce sont les voisins de i qui n'ont pas envoyé leur message
            if(len(nomess) == 1 and i != rac):
                print("Envoi du message de "+mce.nomPotentiel(jt,i)+" à "+mce.nomPotentiel(jt,nomess[0]))
                print("Marginalisation de "+nom_separateur(jt, i, nomess[0])+" selon "+mce.nomPotentiel(jt,i))
                print("Multiplication de "+mce.nomPotentiel(jt,nomess[0])+" par "+ nom_separateur(jt, i, nomess[0])+"\n")
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
        generator.CreationPotentiel(jt,c)
        
    ids = mce.nomPotentielEvs(bn,evs)
    for i in ids:
        print("Création du potentiel : Ev_"+str(i))


    print("##########################################################")
    print("##### Ajout des variables à leur potentiel respectif #####")
    print("##########################################################")
    for c in jt.ids():
        for n in jt.clique(c):
            generator.AjoutVariablePotentiel(jt,c,n)
   
   
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
    for n in mce.couples_cliques(jt.edges(), 1, list) :
        print("Création du potentiel "+nom_separateur(jt, n[0][0], n[0][1]))
    #Ajout des variables (ie : les variables dans le séparateur)
    for n in mce.couples_cliques(jt.edges(), 1, list) :
        for c in n:
            for i in list(jt.clique(c[0]).intersection(jt.clique(c[1]))):
                print("Ajout de la variable "+str(i)+" au potentiel "+nom_separateur(jt, c[0], c[1]))

   
    print("#########################################")
    print("############# INFERENCE #################")
    print("#########################################")
    rac = mce.cliqueRacine(jt)
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
generator = CompilGeneration()
bn = gum.loadBN("/home/ubuntu/Documents/BNS/asia.bif")
target = []
evs = {"smoking?":[1,0]}

ie=gum.LazyPropagation(bn)
jt = ie.junctionTree()
metaCode(bn,evs, target,generator)
showBN(bn,size="3")
showJT(bn,size="3")