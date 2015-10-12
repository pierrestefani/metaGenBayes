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
import sys

languages = ["Debug", "pyAgrum", "numPy", "PHP", "javascript"]

if (len(sys.argv)<2):
  print("metaGenBayes.py configfile.yaml")
  sys.exit(0)

print("loading configuration in "+sys.argv[1])

request = cg.loadConfig(sys.argv[1])
bnpath = request['bayesnet']
arrayOfInstructions = Compiler.compil(gum.loadBN(bnpath), request['target'][:], request['evidence'])


if(request['language'].lower() == languages[1].lower()):
    from Generator.pyAgrumGenerator import pyAgrumGenerator
    generator = pyAgrumGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'], arrayOfInstructions, request['filename']+'.py', request['function'])
    print("Génération en pyAgrum effectuée, fichier "+request['filename']+'.py crée')


elif(request['language'].lower() == languages[2].lower()):
    from Generator.numpyGenerator import numpyGenerator
    generator= numpyGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'], arrayOfInstructions, request['filename']+'.py', request['function'])
    print("Génération numpy effectuée, fichier "+request['filename']+".py crée")

elif(request['language'].lower() == languages[3].lower()):
    from Generator.phpGenerator import phpGenerator
    generator = phpGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'], arrayOfInstructions, request['filename']+'.php', request['function'])
    print("Génération PHP effectuée, fichier "+request['filename']+".php crée")

elif(request['language'].lower() == languages[0].lower()):
    from Generator.debugGenerator import debugGenerator
    generator = debugGenerator()
    generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'], arrayOfInstructions, request['filename']+'.py', request['function'])
    print("Génération en mode debug effectuée, fichier "+request['filename']+'.py crée')

elif(request['language'].lower() == languages[4].lower()):
    from Generator.javascriptGenerator import javascriptGenerator
    generator = javascriptGenerator()
    print("Génération en javascript bientôt implémentée\n")
    #generator.genere(gum.loadBN(bnpath), request['target'][:], request['evidence'], arrayOfInstructions, request['filename']+'.js', request['function'])
    #print("Génération en mode debug effectuée, fichier "+request['filename']+'.py crée')

else:
    print("The language you ask for isn't valid. Languages that have been implemented so far:\n"+str(languages))
