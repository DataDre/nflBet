import pandas as pd
import numpy as np

SEASON_START = 2011
SEASON_END = 2020
SEASONS = list( range( 2010, SEASON_END + 1 ) )

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

url_master = 'https://www.pro-football-reference.com/teams/'

TEAM_NAMES = { 'buf':'BILLS', 'mia':'DOLPHINS', 'nwe':'PATRIOTS', 'nyj':'JETS', 
		      'pit':'STEELERS', 'cle':'BROWNS', 'rav':'RAVENS', 'cin':'BENGALS',
		      'clt':'COLTS', 'oti':'TITANS', 'htx':'TEXANS', 'jax':'JAGS',
		      'kan':'CHIEFS', 'rai':'RAIDERS', 'sdg':'CHARGERS', 'den':'BRONCOS',
		      'was':'FOOTBALL_TEAM', 'nyg':'GIANTS', 'dal':'COWBOYS', 'phi':'EAGLES',
			  'gnb':'PACKERS', 'chi':'BEARS', 'min':'VIKINGS', 'det':'LIONS',
			  'nor':'SAINTS', 'tam':'BUCS', 'car':'PANTHERS', 'atl':'FALCONS',
			  'sea':'SEAHWAKS', 'ram':'RAMS', 'crd':'CARDINALS', 'sfo':'49ERS'
			 }