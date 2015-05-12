# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:00:38 2015

@author: Marvin
"""
"""FICHIER TEST"""
"""
import Compilator as compilator
from debugGenerator import debugGenerator
import pyAgrum as gum
import os
os.chdir("C:/Users/Marvin/Desktop/Informatique/Projet PIMA/testMetaBaysGen/Recent2")

bn = gum.loadBN("C:/Users/Marvin/Desktop/Informatique/Projet PIMA/testMetaBaysGen/BNs/Asia.bif")
target = ["bronchitis?","visit_to_Asia?"]
evs = {"smoking?":[1,0]}

comp = compilator.compil(bn, target, evs)
generator = debugGenerator()
generator.genere(comp, "test.py", "getValue")
"""

import metacode_compilation as compilator
from pyAgrumGenerator import pyAgrumGenerator
import pyAgrum as gum
#import os
#os.chdir("C:/Users/Marvin/Desktop/Informatique/Projet PIMA/testMetaBaysGen/Recent2")

bn=gum.BayesNet()
a,b,c,d,e=[bn.add(gum.LabelizedVariable(s,s,2)) for s in 'abcde']
bn.addArc(a,b)
bn.addArc(a,c)
bn.addArc(b,d)
bn.addArc(c,d)
bn.addArc(e,c)
bn.generateCPTs()

targets = ["d","a"]
evs = {"e":[1,0], "b":[0.25,0.75]}

print("** Version aGrUM **")
ie=gum.LazyPropagation(bn)
ie.setEvidence(evs)
ie.makeInference()
for t in targets:
    print(ie.posterior(bn.idFromName(t)))

print("** Génération pyAgrum **")
comp = compilator.compil(bn, targets[:], evs)
generator = pyAgrumGenerator()
generator.genere(comp, "generated.py", "getValue(bn)")

from generated import getValue
for i in getValue(bn):
    print(i)


print("** Génération PHP **")
print("to be done")
