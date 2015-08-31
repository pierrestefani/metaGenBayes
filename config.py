# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 20:03:54 2015

@author: phw
"""

import yaml

def testDoc2Vars():
  document = """
  # configuration file for metaGeneBayes (file.yaml)

  # specification for inference
  bayesnet: asia.bif

  evidence:
    - x: [2,5]    #soft evidence
    - y # : 2      hard evidence (number of modality)
    - z # 'label'  hard evidence (label)

  target:
    - a
    - b
    - c


  # specification for generation code
  language: php
  filename: asia
  function: getProbaForAsia
  header: |
    ######################################
    # @filename@
    # @generationdate@
    ######################################

  """
  print yaml.load(document)

def testVars2Doc():
  res={
    'language' : 'php',
    'function' : 'getProbaForAsia',
    'filename':'asia',
    'bayesnet': 'asia.bif',
    'target': ['a','b','c'],
    'evidence': ['x:[2,5]','y','z']
    }

  print yaml.dump(res)

def loadConfig(filename):
  print(filename)
  with open(filename, 'r') as f:
    doc = yaml.load(f)

    print("\n=========================\nValues in config file\n=========================")
    for k in doc:
      print("{0} : {1}".format(k,doc[k]))
    print("=========================\n\n\n")

  return doc

config=loadConfig('config.yaml')
print("Compiling {0} ({1}) in function {2} of file {3}".format(
  config['bayesnet'],
  config['language'],
  config['function'],
  config['filename']))
