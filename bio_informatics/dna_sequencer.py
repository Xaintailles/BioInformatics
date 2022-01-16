# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:59:47 2022

@author: Gebruiker
"""

import json
import sys
import os

class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        
    def sequence_type(self):
        
        test_rna = self.sequence.find('U') != -1 #RNA = A,U,C,G
        test_dna = self.sequence.find('T') != -1 #DNA = A,C,T,G
        
        if test_rna:
            return('rna')
        elif test_dna:
            return('dna')
        else:
            return('unknown')
        
    def translate(self):
        
        with open(os.path.join(sys.path[0], "dna_to_prot.json"), "r") as f:
            translation_json = json.load(f)
        
        test_not_unknown = self.sequence_type() != 'unknown'
        
        if test_not_unknown: 
            translation_dict = translation_json[self.sequence_type().lower()]
            return(translation_dict)
        else:
            return('sequence type unknown, cannot chose dict')
    
test = Sequence('AAACCC')

test.sequence_type()

test.translate()


