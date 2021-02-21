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
from collections import Counter, defaultdict, abc
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



def make_tbl_dict( driver, xp_k, xp_v ):
    
    key_lst = driver.text_by_xpath( xp_k )
    val_lst = driver.text_by_xpath( xp_v )
    
    return dict( zip( key_lst, val_lst ) )

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

def scrub( lst_to_scrub, keep_lst ):

    for lnk in lst_to_scrub:
    
        if any( word in lnk for word in keep_lst ):
            
            yield lnk

'''[TODO] make func to build data table; then make func to scrape table info'''
def scrape_data_links( driver, xp_sns, xp_wks_in_sn, xp_gms_in_wk, tst_toggle=None ):

    d = defaultdict( dict )
    
    #get list of season URLs
    driver.opn_webPg( cfg_glb.URL_MASTER )
    seasons_links = driver.htmls_by_xpath( xp_sns )
    seasons_links = sorted( list( scrub( seasons_links, cfg_glb.SEASONS ) ) )
    
    for ssn_link in seasons_links[ :tst_toggle ]:

        ssn = [ i for i in ssn_link.split( '/' ) if i in cfg_glb.SEASONS ][ 0 ]
        d[ ssn ]
        
        driver.opn_webPg( ssn_link )
        
        #get list of week URLs in the season
        weeks_links = driver.htmls_by_xpath( xp_wks_in_sn )
        
        i=1
        for wk_lnk in weeks_links[ :tst_toggle ]:
            
            #get list of game URLs in a given week
            driver.opn_webPg( wk_lnk )
            games_links = driver.htmls_by_xpath( xp_gms_in_wk )
            d[ ssn ].setdefault( 'Week ' + str( i ), {} )

            for g in range( 1, len( games_links )+1 ):
                
                d[ ssn ][ 'Week ' + str( i ) ].setdefault( 'Game ' + str( g ), { 'link' : games_links[ g-1 ] } )
                # d[ ssn ][ 'Week ' + str( i ) ].update( { 'Game ' + str( g ): games_links[ g-1 ] } )
            
            i+=1

    return d

def add_to_nested_key( source_d, info_d ):
    """
    input
    source_d: python dictionary to update
    info_d: python dictionary containing info to input into source_d

    output: 
    updated python dictionary: source_d
   -----------------------------
    Update source dictionary in-place with info from another dictionary
    with similar mapping
    """
    for k, v in info_d.items():

        if isinstance(v, abc.Mapping) and v:

            returned = add_to_nested_key(source_d.get(k, {}), v)
            source_d[ k ] = returned
        
        else:
            
            source_d[ k ] = info_d[ k ]
    
    return source_d

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

'''
def scrape_data( d, driver, xp_k, xp_v ):
    
    for k,v in d.items():
        
        if any( key.startswith('Game') for key in d[ k ] ):
#             print( v, '\n' )
            for k2,v2 in v.items():
                
                v[ k2 ] = hlp.make_tbl_dict( driver, xp_k, xp_v )
            
        elif isinstance( v, dict ):
            
            scrape_data( v, driver, xp_k, xp_v )
    
    return d

game_num=1
for link in bscr_links[:tst_toggle]:
    
    webScrpr.opn_webPg( link )
    
    #scrape Game Info table
    stats_dict[ season ][ cfg_glb.WEEKS_LBL[ i ] ]\
    [ 'Game '+str( game_num ) ][ 'gameInfo' ] = hlp.make_tbl_dict( 
                                                        driver=webScrpr, 
                                                        xp_k=xp_kGI, 
                                                        xp_v=xp_vGI 
                                                        )
    
    
    game_num+=1

# def find_key( d, k_to_find ):

#     for k,v in d.items():

#         if k == k_to_find:

#             return d

#         else: 
            
#             if isinstance( v, dict ):
                
#                 find_key( v, k_to_find )
            
#             else:
                
#                 print( 'Nested val not a dict!!!' )
#                 break


# def add_to_key( d_info, d_upd, k_upd, k_to_find ):
    
#     for k,v in d_info.items():
        
#         if isinstance( v, ( str, list ) ):

#             if isinstance( v, str ):

#                 v = list( v )

#             for i in range( 0, len( v ) ):

#                 d_upd[ season ][ week ][ game ].update( 'link': v[ i ] )
            
#         else:

#             add_to_key( v, d_upd, k_upd,  k_to_find )
    
#     return d_upd

'''













































