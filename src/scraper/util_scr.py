#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#-----------------------------------------------------------------------------------------#
#                                   BeGiN                                                 #
# Last Modified by <Andre Toujas> on 2018-Feb-08 at 22h00 MST                             #
# CC BY-NC-ND 'unknown'.0, <https://creativecommons.org/licenses/by-nc-nd/'unknown'.0/>.  #
#                                                                                         #
#   Version: SemVer 'low'.0.0                                                             #
#   Filename: util_scr.py                                                               #
#   Depends:                                        #
#-----------------------------------------------------------------------------------------#

'''
import sys
import pandas as pd
import numpy as np
import time
import dill 
from tqdm import tqdm
from collections import Counter
from itertools import chain
import operator
import click
import logging
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sys.path.append('../src')
import config as cfg_glb

# print('updated')

### How to recursively search through dictionaries:

def gen_dict_extract( var, key ):
    if isinstance( var, dict ):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance( v, ( dict, list ) ):
                yield from gen_dict_extract( v, key )
    elif isinstance( var, list ):
        for d in var:
            yield from gen_dict_extract( d, key )

def build_stats_dict( name_dict, key ):

	try:

		name_dict[ key ]

	except:

		name_dict[ key ] = {}

	return name_dict














































