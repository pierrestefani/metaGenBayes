# -*- coding: utf-8 -*-

import sys; import os
sys.path.insert(0, os.path.abspath('..'))

import os
import subprocess
import pyAgrum as gum
import numpy as np
import random
import json
from Compiler import Compiler
random.seed()
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


def importOrReload(module_name, *names):
    import sys

    if module_name in sys.modules:
        reload(sys.modules[module_name])
    else:
        __import__(module_name, fromlist=names)

    for name in names:
        globals()[name] = getattr(sys.modules[module_name], name)



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

def errorMarginChecker(generated, reference, targets, epsilon):
    '''checks the deviation of thr generated results from a reference. If the deviation is > than epsilon, errorMarginChecker returns the boolean false'''
    for t in reference:
        i=0
        boolean = True
        while(i<bn.variable(bn.idFromName(t)).domainSize()):
            if(abs(reference.get(t)[i] - generated.get(t)[0][i])/reference.get(t)[i] >epsilon):
                boolean=False
                print("ERROR @ target "+t+", value "+str(i)+" is: "+str(generated.get(t)[0][i])+", should be "+str(reference.get(t)[i])+"\n")
                break
            i=i+1
    return boolean         



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
        for t in targets:
            resPyAgrumRef[t] = list(ie.posterior(bn.idFromName(t)))
            
        '''pyAgrum generated version'''
        resPyAgrumGen.clear()
        generator= Generator.pyAgrumGenerator.pyAgrumGenerator()
        generator.genere(bn, targets, evs, comp, "pyAgrumGenerated____test.py", "getValue")
        importOrReload("pyAgrumGenerated____test", "getValue")
        resPyAgrumGen = getValue(evs)
        print('resPyAgrumGen : '+str(resPyAgrumGen))
        print('resPyAgrumRef : '+str(resPyAgrumRef))
        bool_pyAg = errorMarginChecker(resPyAgrumGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_pyAg)):
            print("Error @ pyAgrumGenerated version")
            print('countNOET : '+str(countNOET)+'\ncountNOBN = '+str(countNOBN)+'\nBayesian network : '+str(bn.ids())+'\nEvidences : '+str(evs)+'\nTargets : '+str(targets))
            error = False
            break
        
        '''numpy generated version'''
        resNumpyGen.clear()
        generator = Generator.numpyGenerator.numpyGenerator()
        generator.genere(bn, targets, evs, comp, "numpyGenerated____test.py", "getValue")
        importOrReload('numpyGenerated____test', 'getValue')
        resNumpyGen = getValue(evs)
        print("resNumpyGen : "+str(resNumpyGen))
        bool_numpy = errorMarginChecker(resNumpyGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_numpy)):
            print("Error @ numpyGenerated version\n")
            print("countNOET : "+str(countNOET)+"\ncountNOBN : "+str(countNOBN)+"\nBayesian Network : "+str(bn.ids())+"\nEvidences : "+str(evs)+"\nTargets : "+str(targets))
            error = False
            break
        
        '''PHP generated version
        resPHPGen.clear()
        from Generator.phpGenerator import phpGenerator
        generator = phpGenerator()
        generator.genere(bn, targets, evs, comp, "PHPGenerated____test.php", "getValue")
        proc = subprocess.call(["php", "PHPGenerated____test.php"])
        resPHPGen = proc.stdout.read()
        #print("resPHPGen : "+str(resPHPGen))
        bool_PHP = errorMarginChecker(resPHPGen, resPyAgrumRef, targets, 0.1)
        if(not(bool_PHP)):
            specs = input("Error @ PHPGenerated version, y/n for specs")
            if (specs=='y'):
                print("countNOET : "+countNOET+"\countNOBN : "+countNOBN+"\nBayesian Network : "+bn.ids()+"\nEvidences : "+evs+"\nTargets : "+targets)
      '''
        
        os.system('rm pyAgrumGenerated____test.py')
        countNOET = countNOET + 1
    
    countNOBN = countNOBN + 1

                
            
        

