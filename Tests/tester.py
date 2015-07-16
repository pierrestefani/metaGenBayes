# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import subprocess
import json

import pyAgrum as gum
import numpy as np

import random
random.seed()

from Compiler import Compiler
import Generator.numpyGenerator
import Generator.pyAgrumGenerator 
import Generator.phpGenerator




NUMBER_OF_NETWORKS = 15
NUMBER_OF_EVIDENCES_TESTED = 10
countNOBN = 0
countNOET = 0

resNumpyGen = {}
resPHPGen = {}
resPyAgrumGen = {}
error = True


#print(targets)
#print(evs)
#print(resPyAgrumRef)

def randomEvidenceGenerator(bn):
    '''randomEvidenceGenerator create a dictionaries of soft evidences to be used in the testing of metaGenBayes functions'''
    '''v1 : binary probabilities generated'''
    evs = {}
    nodeToEvs = list(bn.ids())
    print(nodeToEvs)
    evsLength = random.randint(1, len(bn.ids())/2)
    i = 0
    while (i < evsLength):
        randVar = random.choice(nodeToEvs)
        nodeToEvs.remove(randVar)
        evs[bn.variable(randVar).name()] = list(np.random.dirichlet(np.ones(bn.variable(randVar).domainSize()), size=1)[0])
        i=i+1    
    return evs

def targetSelecter(bn, evs):
    res = list()
    possibleTargets = list()
    for i in bn.ids():
        if(bn.variable(i).name()) not in evs:
            possibleTargets.append(i)
    tarLength = random.randint(1, len(possibleTargets)/2)
    cpt = 0
    while (cpt < tarLength):
        randVar = random.choice(possibleTargets)
        possibleTargets.remove(randVar)
        res.append(bn.variable(randVar).name())
        cpt = cpt + 1
    return res

def describeJunctionTree(bn, jt, target):
    res = ""
    for i in jt.ids():
        res += str(i)+"---------\n"
        for j in jt.clique(i):
            res += bn.variable(j).name()+"\n"
    res += "\n"+str(list(jt.edges()))
    res += "\nClique racine : "+str(Compiler.mainClique(bn, jt, target))
    return res

def errorMarginChecker(generated, reference, targets, epsilon):
    '''checks the deviation of thr generated results from a reference. If the deviation is > than epsilon, errorMarginChecker returns the boolean false'''
    print(reference)    
    for t in reference:
        i=0
        boolean = True
        while(i<bn.variable(bn.idFromName(t)).domainSize()):
            if(abs(reference.get(t)[i] - generated.get(t)[i])/reference.get(t)[i] >epsilon):
                boolean=False
                print("ERROR @ target "+t+", value "+str(i)+" is: "+str(generated.get(t)[i])+", should be "+str(reference.get(t)[i])+"\n")
                break
            i=i+1
    return boolean         

def errorWriter(language, filename):
     print("Error @ "+language+" version")
     target = open(filename, 'w')
     target.write('Bayesian network : '+str(bn.ids())+'\n')
     target.write('countNOET : '+str(countNOET)+'\ncountNOBN = '+str(countNOBN)+'\n')
     target.write('Evidences : '+str(evs)+'\nTargets : '+str(targets)+'\n')
     target.write('\n\nJunction Tree description : \n'+describeJunctionTree(bn, jt, targets))
     target.close()



while(countNOBN < NUMBER_OF_NETWORKS and error):
    bn = gum.BNGenerator().generate()
    bn.saveBIF('tester.bif')
    
    while(countNOET < NUMBER_OF_EVIDENCES_TESTED):
                
        evs = randomEvidenceGenerator(bn)
        targets = targetSelecter(bn, evs)
        comp = Compiler.compil(bn, targets[:], evs)
        
        '''pyAgrum reference version'''
        resPyAgrumRef= {}
        ie=gum.LazyPropagation(bn)
        ie.setEvidence(evs)
        ie.makeInference()
        jt = ie.junctionTree()
        for t in targets:
            resPyAgrumRef[t] = list(ie.posterior(bn.idFromName(t)))
            
        '''pyAgrum generated version'''
        resPyAgrumGen.clear()
        generator= Generator.pyAgrumGenerator.pyAgrumGenerator()
        generator.genere(bn, targets, evs, comp, "pyAgrumGenerated____test.py", "getValue")
        from pyAgrumGenerated____test import getValue
        resPyAgrumGen = getValue(evs)
        print('resPyAgrumRef : '+str(resPyAgrumRef))
        print('resPyAgrumGen : '+str(resPyAgrumGen))
        bool_pyAg = errorMarginChecker(resPyAgrumGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_pyAg)):
            print("ERROR")
            errorWriter('pyAgrum', 'errorPyAgrum.txt')
            error = False
            break
        
        '''numpy generated version'''
        resNumpyGen.clear()
        generator = Generator.numpyGenerator.numpyGenerator()
        generator.genere(bn, targets, evs, comp, "numpyGenerated____test.py", "getValueNP")
        from numpyGenerated____test import getValueNP
        resNumpyGen = getValueNP(evs)
        print("resNumpyGen : "+str(resNumpyGen))
        bool_numpy = errorMarginChecker(resNumpyGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_numpy)):
            print("ERROR")
            errorWriter('numpy', 'errorNumpy.txt')
            error = False
            break

        '''PHP generated version
        resPHPGen.clear()
        generator = Generator.phpGenerator.phpGenerator()
        generator.genere(bn, targets, evs, comp, "PHPGenerated____test.php", "getValuePHP")
        proc = subprocess.Popen("php PHPGenerated____test.php", shell = True, stdout = subprocess.PIPE)
        #print("resPHPGen : "+str(resPHPGen))
        bool_PHP = errorMarginChecker(resPHPGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_PHP)):
            print("ERROR")
            errorWriter('php', 'errorPHP.txt')
            error = False
            break
      '''
        
        os.system('rm pyAgrumGenerated____test.py')
        countNOET = countNOET + 1
    
    countNOBN = countNOBN + 1

                
            
        

