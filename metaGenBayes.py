# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:59:05 2015

@author: ubuntu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:38:51 2015

@author: pierre

YAML Config format : 
'language' : 'pyAgrum',
    'function' : 'getProbaForAsia',
    'filename':'asia',
    'bayesnet': 'asia.bif',
    'target': ['a','b','c'],
    'evidence': ['x','y','z']
"""

import pyAgrum as gum
import yaml
from Compiler import Compiler
import config as cg

languages = ["Debug", "pyAgrum", "numPy", "PHP"]

request = cg.loadConfig('testAsia.yaml')
bnpath = "BNs/"+request['bayesnet'] 
arrayOfInstructions = Compiler.compil(gum.loadBN(bnpath), request['target'][:], request['evidence'][0])


if(request['language'].lower() == languages[1].lower()):
    from Generator.pyAgrumGenerator import pyAgrumGenerator
    generator = pyAgrumGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'][0], arrayOfInstructions, request['filename']+'.py', request['function'])
    print("Génération en pyAgrum effectuée, fichier "+request['filename']+'.py crée')
    
    
elif(request['language'].lower() == languages[2].lower()):
    print("generation en numPy tbd")

elif(request['language'].lower() == languages[3].lower()):
    print("generation en php tbd")

elif(request['language'].lower() == languages[0].lower()):
    from Generator.debugGenerator import debugGenerator
    generator = debugGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'][0], arrayOfInstructions, request['filename']+'.py', request['function'])
    print("Génération en mode debug effectuée, fichier "+request['filename']+'.py crée')

else:
    print("The language you ask for isn't valid. Languages that have been implemented so far:\n"+str(languages))
