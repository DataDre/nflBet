import pandas as pd
import numpy as np

SEASON_START = 2011
SEASON_END = 2020
URL_MASTER='https://www.pro-football-reference.com/years/'
""" url of root page you want to scrape """

SEASONS = [ str( i ) for i in list( range( SEASON_START, SEASON_END + 1 ) ) ]

######################################################
#############   GLOBAL VARIABLES: PATHS   ############
######################################################

DATA_INPATH = '../data/raw'

DF_OUTPATH = '../data/interim/dfs'
LST_OUTPATH = '../data/interim/lists'
DICT_OUTPATH = '../data/interim/dictionaries'
RESULTS_OUTPATH = '../data/processed'
MODEL_OUTPATH = '../models'
FIG_OUTPATH = '../reports/figures'

########################################################
#############   GLOBAL VARIABLES: GENERAL   ############
########################################################

TEAMS_AFC = [ 'buf', 'mia', 'nwe', 'nyj', 
		      'pit', 'cle', 'rav', 'cin',
		      'clt', 'oti', 'htx', 'jax',
		      'kan', 'rai', 'sdg', 'den'
		    ]

TEAMS_NFC = [ 'was', 'nyg', 'dal', 'phi',
			  'gnb', 'chi', 'min', 'det',
			  'nor', 'tam', 'car', 'atl',
			  'sea', 'ram', 'crd', 'sfo'
		    ]

TEAM_NAMES = { 'buf':'BILLS', 'mia':'DOLPHINS', 'nwe':'PATRIOTS', 'nyj':'JETS', 
		      'pit':'STEELERS', 'cle':'BROWNS', 'rav':'RAVENS', 'cin':'BENGALS',
		      'clt':'COLTS', 'oti':'TITANS', 'htx':'TEXANS', 'jax':'JAGS',
		      'kan':'CHIEFS', 'rai':'RAIDERS', 'sdg':'CHARGERS', 'den':'BRONCOS',
		      'was':'FOOTBALL_TEAM', 'nyg':'GIANTS', 'dal':'COWBOYS', 'phi':'EAGLES',
			  'gnb':'PACKERS', 'chi':'BEARS', 'min':'VIKINGS', 'det':'LIONS',
			  'nor':'SAINTS', 'tam':'BUCS', 'car':'PANTHERS', 'atl':'FALCONS',
			  'sea':'SEAHWAKS', 'ram':'RAMS', 'crd':'CARDINALS', 'sfo':'49ERS'
			 }

WEEKS_LBL = {
	  1: 'Week 1',
	  2: 'Week 2',
	  3: 'Week 3',
	  4: 'Week 4',
	  5: 'Week 5',
	  6: 'Week 6',
	  7: 'Week 7',
	  8: 'Week 8',
	  9: 'Week 9',
	 10: 'Week 10',
	 11: 'Week 11',
	 12: 'Week 12',
	 13: 'Week 13',
	 14: 'Week 14',
	 15: 'Week 15',
	 16: 'Week 16',
	 17: 'Week 17',
	 18: 'Wild Card',
	 19: 'Divisional',
	 20: 'Conf Champ',
	 21: 'Super Bowl'
 }

##########################
## SCRAPER ##
##########################

# STATS_LV1 = [ 'season', 'week', 'game' ]
STATS_LV2 = [ 'link', 'gameInfo', 'prr', 'def', 'st', 'prr_adv', 'def_adv' ]

# test = {'2011': { 
# 			'Week 1': { 
# 				'Game 1': {
# 					'Game_Info': {
# 						'Home Team': 'Packers',
# 					    'Away Team': 'Saints'
# 					    'Roof': 'outdoors', 
# 					    'Surface': 'grass',
# 					    'weather': '68 degrees',
# 					    'Line': 'Green Bay Packers -5.0',
# 					    'Pt_Total': 48.0 
# 						},
# 					'PRR': {
# 						'Player': { 
# 							'Drew Brees': {
# 								'Completions_pass': 32,
# 								'Attempts_pass': 49,
# 								'Yards_pass': 419,
# 								'TD_pass': 3
# 							},
# 							'Mark Ingram': {
# 								'Attempts_rush': 13,
# 								'Yards_rush': 40,
# 								'TD_rush': 0
# 								}
# 						}
# 					}	
# 				},
# 				'Game 2': {
# 					'Game_Info': {
# 						'Home Team': 'Packers',
# 					    'Away Team': 'Saints'
# 					    'Roof': 'outdoors', 
# 					    'Surface': 'grass',
# 					    'weather': '85 degrees',
# 					    'Line': 'Green Bay Packers -3.0',
# 					    'Pt_Total': 48.0 
# 						},
# 					'PRR': {
# 						'Player': { 
# 							'Drew Brees': {
# 								'Completions_pass': 45,
# 								'Attempts_pass': 60,
# 								'Yards_pass': 550,
# 								'TD_pass': 5
# 							},
# 							'Mark Ingram': {
# 								'Attempts_rush': 7,
# 								'Yards_rush': 75,
# 								'TD_rush': 2
# 								}
# 						}
# 					}	
# 				}
# 			}
# }


























