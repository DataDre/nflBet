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

class WebScraper( object ):
	"""
    Uses patient BGP (predicted in previous function), reg, meal, and insulin titration
    to recommend insulin tritration adjustments based on set of clinically derived rule.


    Methods:
    --------
    + replace_bgp_str       : converts string outputs from BGP predictions to BGPs
    + determine_dosage      : uses rules-based model to generate 
                              insulin recos (to be used as features for ML model)
    + aggregate_and_map     : aggregates the rules-based model recos and maps to 
                              proper mealtimes
    + generate_bgp_features : reads in patient logbooks with raw BG readings and 
                                  creates features for the ML model

    """
	def __init__( self, main_pg=cfg_glb.URL_MASTER ):
		self.main_pg = main_pg
		self.driver = webdriver.Chrome()
		# driver.get( self.main_pg )

	def opn_webPg( self, webPg ):
		"""input
		   main_pg: html of root page to scrape
		   drvr: Browser you want to use; Chrome() typical

		   output: 
		   Selenium webdriver
		   -----------------------------
		   + Opens the main/root page
		   + Returns a Selenium webdriver
		"""

		# driver = webdriver.Chrome()
		
		return self.driver.get( webPg )

		# return driver

	def back( self ):
		"""Go back"""
		return self.driver.back()

	def htmls_by_xpath( self, xp ):
		"""input
		   xp: xpath containing
		   
		   output: 
		   list of htmls incl in xpath
		   -----------------------------
		   Returns list of htmls contained in a given xpath
		"""

		xp_els = self.driver.find_elements_by_xpath( xp )
		
		els_list = []
		for el in xp_els:
			els_list.append( el.get_attribute( 'href' ) )

		return els_list

	def text_by_xpath( self, xp ):
		"""input
		   xp: xpath containing text to extract
		   
		   output: 
		   list of text incl in xpath
		   -----------------------------
		   Returns list of text contained in a given xpath
		"""
		xp_els = self.driver.find_elements_by_xpath( xp )

		els_list=[]
		for el in xp_els:

			 els_list.append( el.text )

		return els_list



# def opn_html( driver, html, ):
# 	"""input
# 	   driver: Selenium webdriver object
# 	   html: an html string
# 	   output: 
# 	   Selenium webdriver object
# 	   -----------------------------
# 	   Returns Selenium webdriver object of html input
# 	"""
	
# 	return driver.get( html )

"""
@click.command()
@click.argument('df_bgp_location', type=click.Path(exists=True) )
@click.argument('df_logbooks_location', type=click.Path(exists=True) )
@click.option('--save_results', '-s', help='True or False to save RBM results')
@click.option('--df_ftrs_filename', '-f', help='name of csv')
def main( df_bgp_location, df_logbooks_location, save_results, df_ftrs_filename ):
    Generates rules-based model predictions
    
    
    logger = logging.getLogger(__name__)
    
    webScrpr = WebScraper()
    

    webScrpr.opn_drvr()

	for season in range( cfg_glb.SEASON_START, cfg_glb.SEASON_END+1 ):

		logger.info('Obtaining list of {} Season, Week {} links'. format( , ) )
	    webScrpr.determine_dosage()

	    logger.info('Aggregating and mapping raw RBM predictions...')
	    webScrpr.aggregate_and_map()

	    logger.info('Generating hand-coded BGP features...')
	    webScrpr.generate_bgp_features()

    if save_results:
        df = webScrpr.df_ftrs
        if not os.path.exists(cfg_glbl.DF_OUTPATH+'/testing'):
            os.makedirs( cfg_glbl.DF_OUTPATH+'/testing' )
        hlp_mdl.save_obj( cfg_glbl.DF_OUTPATH+'/testing', df, df_ftrs_filename )
        df.to_csv( cfg_glbl.DF_OUTPATH+'/testing/'+df_ftrs_filename+'.csv', index=False )

    logger.info('Finished Feature Generation!')

    return

if __name__=='__main__':
    main()

"""











































