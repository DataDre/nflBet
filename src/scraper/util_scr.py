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
from collections import defaultdict
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

def make_tbl_dict( driver, xp_k, xp_v ):
    
    key_lst = driver.text_by_xpath( xp_k )
    val_lst = driver.text_by_xpath( xp_v )
    
    return dict( zip( key_lst, val_lst ) )

def scrape_data( d, driver, xp_k, xp_v ):
    
    for k,v in d.items():
        
        if any( key.startswith('Game') for key in d[ k ] ):
#             print( v, '\n' )
            for k2,v2 in v.items():
                
                v[ k2 ] = hlp.make_tbl_dict( driver, xp_k, xp_v )
            
        elif isinstance( v, dict ):
            
            scrape_data( v, driver, xp_k, xp_v )
    
    return d

def build_stats_shell( d=defaultdict( dict ) ):
    
    for game in list( range( 1, 17 ) ):

        game = 'Game '+ str( game )

        for week in list( range( 1, 22 ) ):

            week = cfg_glb.WEEKS_LBL[ week ]

            for season in cfg_glb.SEASONS:

                d.setdefault(season, {})
                d[ season ].setdefault( week, {} )
                d[ season ][ week ].setdefault( game, {} )
                
                for tbl in cfg_glb.STATS_LV2:
                	
                	d[ season ][ week ][ game ].setdefault( tbl, {} )

    return d
















































