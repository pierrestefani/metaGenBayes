# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:00:38 2015

@author: Marvin
"""


from Compiler.Compiler import compil
from Generator.pyAgrumGenerator import pyAgrumGenerator
import pyAgrum as gum


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

comp = compil(bn, targets[:], evs)
generator = pyAgrumGenerator()
generator.genere(bn, targets, evs, comp, "generated.py", "getValue")
from generated import getValue
getValue(bn,evs)

for i in getValue(bn,evs):
    print(i)

print("** Génération PHP **")
print("to be done")

