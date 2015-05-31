import pyAgrum as gum
import random
from Compiler import Compiler
random.seed()

NUMBER_OF_VALUES = 2
NUMBER_OF_NETWORKS = 15
NUMBER_OF_EVIDENCES_TESTED = 10
countNOBN = 0
countNOET = 0




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
        binEv = random.random()
        evs[bn.variable(randVar).name()] = [binEv, 1-binEv]
        i=i+1    
    return evs

def targetSelecter(bn, evs):
    res = list()
    possibleTargets = list()
    for i in bn.ids():
        if(bn.variable(i).name()) not in evs:
            possibleTargets.append(i)
    tarLength = random.randint(1, len(possibleTargets))
    cpt = 0
    while (cpt < tarLength):
        randVar = random.choice(possibleTargets)
        possibleTargets.remove(randVar)
        res.append(bn.variable(randVar).name())
        cpt = cpt + 1
    return res


while(countNOBN < NUMBER_OF_NETWORKS):
    bn = gum.BNGenerator().generate()
    
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
            resPyAgrumRef[t] = ie.posterior(bn.idFromName(t))
            
        '''pyAgrum generated version'''
        resPyAgrumGen = {}
        from Generator.pyAgrumGenerator import pyAgrumGenerator
        generator= pyAgrumGenerator()
        generator.genere(bn, targets, evs, comp, "pyAgrumGenerated____test.py", "getValue")
        from pyAgrumGenerated____test import getValue
        resPyAgrumGen = getValue(evs)
        for tar in resPyAgrumRef:
            i = 0
            bool_pyAg = False
            while (i < NUMBER_OF_VALUES):        
                if(abs(resPyAgrumRef.get(tar)[i] / resPyAgrumGen.get(tar)[i] -1)>0.00001):
                    bool_pyAg = True
                    print('ERROR @ target: '+tar+', value('+str(i)+' is:'+str(resPyAgrumGen.get(tar)[i])+', should be :'+str(resPyAgrumRef.get(tar)[i]))
                i = i+1
        if(bool_pyAg):
            specs = input("Error @ pyAgrumGenerated version, y/n for specs")
            if (specs == 'y'):
                print('countNOET : '+countNOET+'\ncountNOBN = '+countNOBN+'\nBayesian network : '+bn.ids()+'\nEvidences : '+evs+'\nTargets : '+targets)
        
        
        
        
        countNOET = countNOET + 1
    
    countNOBN = countNOBN + 1

                
            
        

