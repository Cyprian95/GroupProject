#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Start CDS
File:doStartCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to process DNA sequence with restriciton enzyme ecoRI
--------------------------------------------------------------------------
from configFile import *
import re
"""

from configFile import *
import re

def doEcoRI(seq):
     """ Process Sequence with restriction enzyme EcoRi
     Input: input ecoRI from cofigfile 
     Output:Sequence """
     f = re.compile(r'' + ecoRI_forward + '')
     r = re.compile(r'' + ecoRI_reverse + '')
     seq = f.sub(ecoRI_forward[0] + ecoRI_char + \
                 ecoRI_forward[1:len(ecoRI_forward)], seq)
     seq = r.sub(ecoRI_reverse[0] + ecoRI_char + \
                 ecoRI_reverse[1:len(ecoRI_reverse)], seq)
     return seq
