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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sys.path.append('../src')
import config as cfg 

def opn_drvr( main_pg=cfg.URL_MASTER ):
	"""input
	   main_pg: html of root page to scrape
	   drvr: Browser you want to use; Chrome() typical

	   output: 
	   Selenium webdriver
	   -----------------------------
	   + Opens the main/root page
	   + Returns a Selenium webdriver
	"""

	driver = webdriver.Chrome()

	driver.get( main_pg )

	return driver

def htmls_by_xpath( xp, driver ):
	"""input
	   xp: xpath containing
	   driver: Selenium webdriver object

	   output: 
	   list of htmls incl in xpath
	   -----------------------------
	   Returns list of htmls contained in a given xpath
	"""

	xp_els = driver.find_elements_by_xpath( xp )
	
	lst_els = []
	for el in xp_els:
		lst_els.append( el.get_attribute( 'href' ) )

	return lst_els

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















































