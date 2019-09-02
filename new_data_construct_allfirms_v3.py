#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:16:17 2019

@author: emilhenningsen
"""

import pandas as pd
import numpy as np
import time

# timer for loop action
start_action = time.time()

############## Setting required peers input
required_sector_peers = input('Enter the amount of peers sufficient (GSEC criteria benchmark at 16): ')
required_sector_peers = int(required_sector_peers)

############## import of data from WRDS and I/B/E/S

# IBES for USA
uibes_00 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=0)
uibes_01 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=1)
uibes_02 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=2)
uibes_03 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=3)
uibes_04 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=4)
uibes_05 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=5)
uibes_06 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=6)
uibes_07 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=7)
uibes_08 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=8)
uibes_09 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=9)
uibes_10 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=10)
uibes_11 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=11)
uibes_12 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=12)
uibes_13 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=13)
uibes_14 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=14)
uibes_15 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=15)
uibes_16 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=16)
uibes_17 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=17)
uibes_18 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=18)
uibes_19 = pd.read_excel('US_IBES_MKTCAP.xlsx',sheet_name=19)

# IBES for global
gibes_19 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=19)
gibes_18 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=18)
gibes_17 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=17)
gibes_16 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=16)
gibes_15 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=15)
gibes_14 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=14)
gibes_13 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=13)
gibes_12 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=12)
gibes_11 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=11)
gibes_10 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=10)
gibes_09 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=9)
gibes_08 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=8)
gibes_07 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=7)
gibes_06 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=6)
gibes_05 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=5)
gibes_04 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=4)
gibes_03 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=3)
gibes_02 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=2)
gibes_01 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=1)
gibes_00 = pd.read_excel('GLOBAL_IBES_MKTCAP4.xlsx',sheet_name=0)

# US data

ud_19 = pd.read_csv('new_oecd_usfundaclean_19.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_18 = pd.read_csv('new_oecd_usfundaclean_18.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_17 = pd.read_csv('new_oecd_usfundaclean_17.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_16 = pd.read_csv('new_oecd_usfundaclean_16.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_15 = pd.read_csv('new_oecd_usfundaclean_15.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_14 = pd.read_csv('new_oecd_usfundaclean_14.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_13 = pd.read_csv('new_oecd_usfundaclean_13.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_12 = pd.read_csv('new_oecd_usfundaclean_12.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_11 = pd.read_csv('new_oecd_usfundaclean_11.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_10 = pd.read_csv('new_oecd_usfundaclean_10.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_09 = pd.read_csv('new_oecd_usfundaclean_09.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_08 = pd.read_csv('new_oecd_usfundaclean_08.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_07 = pd.read_csv('new_oecd_usfundaclean_07.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_06 = pd.read_csv('new_oecd_usfundaclean_06.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_05 = pd.read_csv('new_oecd_usfundaclean_05.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_04 = pd.read_csv('new_oecd_usfundaclean_04.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_03 = pd.read_csv('new_oecd_usfundaclean_03.csv', dtype={'GVKEY': str,'VALUE_YEAR': int, 
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_02 = pd.read_csv('new_oecd_usfundaclean_02.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_01 = pd.read_csv('new_oecd_usfundaclean_01.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )
ud_00 = pd.read_csv('new_oecd_usfundaclean_00.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str} )

# global data

gd_19 = pd.read_csv('new_oecd_gfundaclean2_19.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_18 = pd.read_csv('new_oecd_gfundaclean2_18.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_17 = pd.read_csv('new_oecd_gfundaclean2_17.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_16 = pd.read_csv('new_oecd_gfundaclean2_16.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_15 = pd.read_csv('new_oecd_gfundaclean2_15.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_14 = pd.read_csv('new_oecd_gfundaclean2_14.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_13 = pd.read_csv('new_oecd_gfundaclean2_13.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_12 = pd.read_csv('new_oecd_gfundaclean2_12.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str })
gd_11 = pd.read_csv('new_oecd_gfundaclean2_11.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_10 = pd.read_csv('new_oecd_gfundaclean2_10.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_09 = pd.read_csv('new_oecd_gfundaclean2_09.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_08 = pd.read_csv('new_oecd_gfundaclean2_08.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_07 = pd.read_csv('new_oecd_gfundaclean2_07.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_06 = pd.read_csv('new_oecd_gfundaclean2_06.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_05 = pd.read_csv('new_oecd_gfundaclean2_05.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_04 = pd.read_csv('new_oecd_gfundaclean2_04.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_03 = pd.read_csv('new_oecd_gfundaclean2_03.csv', dtype={'GVKEY': str, 'VALUE_YEAR': int, 
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_02 = pd.read_csv('new_oecd_gfundaclean2_02.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_01 = pd.read_csv('new_oecd_gfundaclean2_01.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )
gd_00 = pd.read_csv('new_oecd_gfundaclean2_00.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
                                                  'G_SUBIND': str, 'CISO':str} )

###########################################################################


#import cleaning data frames to calculate total sum of data removed

print("Data import finished!")

# Creating identifier column for IBES
# US data
uibes_19['VALUE_YEAR'] = 2019
uibes_18['VALUE_YEAR'] = 2018
uibes_17['VALUE_YEAR'] = 2017
uibes_16['VALUE_YEAR'] = 2016
uibes_15['VALUE_YEAR'] = 2015
uibes_14['VALUE_YEAR'] = 2014
uibes_13['VALUE_YEAR'] = 2013
uibes_12['VALUE_YEAR'] = 2012
uibes_11['VALUE_YEAR'] = 2011
uibes_10['VALUE_YEAR'] = 2010
uibes_09['VALUE_YEAR'] = 2009
uibes_08['VALUE_YEAR'] = 2008
uibes_07['VALUE_YEAR'] = 2007
uibes_06['VALUE_YEAR'] = 2006
uibes_05['VALUE_YEAR'] = 2005
uibes_04['VALUE_YEAR'] = 2004
uibes_03['VALUE_YEAR'] = 2003
uibes_02['VALUE_YEAR'] = 2002
uibes_01['VALUE_YEAR'] = 2001
uibes_00['VALUE_YEAR'] = 2000

# Global data
# IBES
gibes_19['VALUE_YEAR'] = 2019
gibes_18['VALUE_YEAR'] = 2018
gibes_17['VALUE_YEAR'] = 2017
gibes_16['VALUE_YEAR'] = 2016
gibes_15['VALUE_YEAR'] = 2015
gibes_14['VALUE_YEAR'] = 2014
gibes_13['VALUE_YEAR'] = 2013
gibes_12['VALUE_YEAR'] = 2012
gibes_11['VALUE_YEAR'] = 2011
gibes_10['VALUE_YEAR'] = 2010
gibes_09['VALUE_YEAR'] = 2009
gibes_08['VALUE_YEAR'] = 2008
gibes_07['VALUE_YEAR'] = 2007
gibes_06['VALUE_YEAR'] = 2006
gibes_05['VALUE_YEAR'] = 2005
gibes_04['VALUE_YEAR'] = 2004
gibes_03['VALUE_YEAR'] = 2003
gibes_02['VALUE_YEAR'] = 2002
gibes_01['VALUE_YEAR'] = 2001
gibes_00['VALUE_YEAR'] = 2000

# Financial statements
gd_19['VALUE_YEAR'] = 2019
gd_18['VALUE_YEAR'] = 2018
gd_17['VALUE_YEAR'] = 2017
gd_16['VALUE_YEAR'] = 2016
gd_15['VALUE_YEAR'] = 2015
gd_14['VALUE_YEAR'] = 2014
gd_13['VALUE_YEAR'] = 2013
gd_12['VALUE_YEAR'] = 2012
gd_11['VALUE_YEAR'] = 2011
gd_10['VALUE_YEAR'] = 2010
gd_09['VALUE_YEAR'] = 2009
gd_08['VALUE_YEAR'] = 2008
gd_07['VALUE_YEAR'] = 2007
gd_06['VALUE_YEAR'] = 2006
gd_05['VALUE_YEAR'] = 2005
gd_04['VALUE_YEAR'] = 2004
gd_03['VALUE_YEAR'] = 2003
gd_02['VALUE_YEAR'] = 2002
gd_01['VALUE_YEAR'] = 2001
gd_00['VALUE_YEAR'] = 2000

# Creating the US IBES total dataframe
# creating the total dataset with all company-year observation 
uibesdfs = [
            uibes_01,uibes_02,uibes_03,uibes_04,uibes_05,uibes_06,
            uibes_07,uibes_08,
            uibes_09,uibes_10,uibes_11,uibes_12,uibes_13,uibes_14,uibes_15,
            uibes_16,uibes_17,uibes_18,uibes_19]
tuibes = uibes_00.append(uibesdfs, ignore_index=True)

# deleting forms
del [uibes_01,uibes_02,uibes_03,uibes_04,uibes_05,uibes_06,uibes_07,uibes_08,
            uibes_09,uibes_10,uibes_11,uibes_12,uibes_13,uibes_14,uibes_15,
            uibes_16,uibes_17,uibes_18,uibes_19,uibesdfs,uibes_00]

# Global sample IBES
gibesdfs = [gibes_01,gibes_02,gibes_03,gibes_04,gibes_05,gibes_06,gibes_07,gibes_08,
            gibes_09,gibes_10,gibes_11,gibes_12,gibes_13,gibes_14,gibes_15,
            gibes_16,gibes_17,gibes_18,gibes_19]
tgibes = gibes_00.append(gibesdfs, ignore_index=True)

# deleting forms
del [gibes_01,gibes_02,gibes_03,gibes_04,gibes_05,gibes_06,gibes_07,gibes_08,
            gibes_09,gibes_10,gibes_11,gibes_12,gibes_13,gibes_14,gibes_15,
            gibes_16,gibes_17,gibes_18,gibes_19,gibesdfs,gibes_00]

# 1. Inclusion of forward EPS to the trailing financial statements
# us sample
# cusips as identifiers
tuibes2 = tuibes.copy()
tuibes2['MKT_CAP'] = pd.to_numeric(tuibes2['MKT_CAP'],errors='coerce')
tuibes2['EPS12'] = pd.to_numeric(tuibes2['EPS12'],errors='coerce')
tuibes2['EPS24'] = pd.to_numeric(tuibes2['EPS24'],errors='coerce')

tuibes2['IMPLIED_GROWTH'] = (tuibes2['EPS24'] / tuibes2['EPS12']) - 1

print('Total NaNs in IMPLIED GROWTH for US companies in year y')
print(tuibes2.IMPLIED_GROWTH.isnull().sum())
print(tuibes2.IMPLIED_GROWTH.isnull().sum() / len(tuibes))


print('US IBES estimates cleaning done!')

# global sample
# cusips as identifiers
tgibes2 = tgibes.copy()
tgibes2['MKT_CAP'] = pd.to_numeric(tgibes2['MKT_CAP'],errors='coerce')
tgibes2['EPS12'] = pd.to_numeric(tgibes2['EPS12'],errors='coerce')
tgibes2['EPS24'] = pd.to_numeric(tgibes2['EPS24'],errors='coerce')

tgibes2['IMPLIED_GROWTH'] = (tgibes2['EPS24'] / tgibes2['EPS12']) - 1
print('Total NaNs in IMPLIED GROWTH for Global companies in year y')
print(tgibes2.IMPLIED_GROWTH.isnull().sum())
print(tgibes2.IMPLIED_GROWTH.isnull().sum() / len(tgibes))

# rearranging columns
ibes_ucols = ['CUSIP','VALUE_YEAR','IMPLIED_GROWTH'] # us cols
ibes_gcols = ['ISIN','VALUE_YEAR','IMPLIED_GROWTH', 'MKT_CAP'] # global cols
# rearraging colmuns
us_growth = tuibes2[ibes_ucols].copy()
global_growth = tgibes2[ibes_gcols].copy()

# delete forms
del (tgibes2,tuibes2)

############################## MOVE ON TO NEXT STEP

## 3. step: combining artificial financial statements and Implied Growth from IBES

# Creating the US artifical financial statements total dataframe
#all company-year observation 
usdfs = [ud_01,ud_02,ud_03,ud_04,ud_05,ud_06,ud_07,ud_08,
            ud_09,ud_10,ud_11,ud_12,ud_13,ud_14,ud_15,
            ud_16,ud_17,ud_18,ud_19,
            ]
ustfin = ud_00.append(usdfs, ignore_index=True)

# deleting forms
del [ud_01,ud_02,ud_03,ud_04,ud_05,ud_06,ud_07,ud_08,
            ud_09,ud_10,ud_11,ud_12,ud_13,ud_14,ud_15,
            ud_16,ud_17,ud_18,ud_19,usdfs,ud_00, 
            ]

# Global sample 
gdfs = [gd_01,gd_02,gd_03,gd_04,gd_05,gd_06,gd_07,gd_08,
            gd_09,gd_10,gd_11,gd_12,gd_13,gd_14,gd_15,
            gd_16,gd_17,gd_18,gd_19]
gtfin = gd_00.append(gdfs, ignore_index=True)

# deleting forms
del [gd_01,gd_02,gd_03,gd_04,gd_05,gd_06,gd_07,gd_08,
            gd_09,gd_10,gd_11,gd_12,gd_13,gd_14,gd_15,
            gd_16,gd_17,gd_18,gd_19,gdfs,gd_00]

# US data specific
## Add CISO, IND_NAME and MAJOR_IND_DESC to US data
## format indexid to str

# calculating market cap 
ustfin['MKT_CAP'] = ustfin.NSHARES2 * ustfin.PRICE2

# Global data specific, add index identifiers INDEXID

gtfin['INDEXID'] = 'OECD'

# merge statement for both global and us financial statements
# checking for duplicates in IBES
# creating identifier for growth estimates
us_growth['MERGE_ID'] = us_growth.VALUE_YEAR.astype(str) + us_growth.CUSIP
global_growth['MERGE_ID'] = global_growth.VALUE_YEAR.astype(str) + global_growth.ISIN
print('Duplicated rows for each company year obs:')
print('US:')
print(us_growth.MERGE_ID.duplicated().sum())
print('Global:')
print(global_growth.MERGE_ID.duplicated().sum())

# if duplicated on the merge ID, I sort and drop the dupes but the first obs:
global_growth = global_growth.sort_values(by='MERGE_ID').copy()
us_growth = us_growth.sort_values(by='MERGE_ID').copy()

# drop dupes
global_growth = global_growth.drop_duplicates(subset=['MERGE_ID'],keep='first').copy()
us_growth = us_growth.drop_duplicates(subset=['MERGE_ID'],keep='first').copy()

# the potential error when infinite operaters is treated as a NaN that will later be removed
us_growth = us_growth.replace([np.inf, -np.inf], np.nan).copy()
global_growth = global_growth.replace([np.inf, -np.inf], np.nan).copy()

# rearrange DFs
us_growth = pd.DataFrame(us_growth,columns=['MERGE_ID','IMPLIED_GROWTH']).copy()
global_growth = pd.DataFrame(global_growth,columns=['MERGE_ID','IMPLIED_GROWTH','MKT_CAP']).copy()

# creating identifer on financial statements
ustfin['MERGE_ID'] = ustfin.VALUE_YEAR.astype(str) + ustfin.CUSIP
gtfin['MERGE_ID'] = gtfin.VALUE_YEAR.astype(str) + gtfin.ISIN

# merge artificial financial statements and growth estimates
tdus = pd.merge(ustfin,us_growth, on='MERGE_ID', how='left')
tdg = pd.merge(gtfin,global_growth, on='MERGE_ID', how='left')

# data removed because of dupes in growth
print('USA')
print(len(tdus) - len(tdus.dropna()))
us_remove1 = len(tdus) - len(tdus.dropna())

print('OECD')
print(len(tdg) - len(tdg.dropna()))
g_remove1 = len(tdg) - len(tdg.dropna())

total_remove1 = us_remove1 + g_remove1

# dropping MERGE_ID columns
tdus = tdus.drop(columns=['MERGE_ID']).copy()
tdg = tdg.drop(columns=['MERGE_ID']).copy()

# dropping NaNs from implied growth
ctdus = tdus.dropna().copy() # cleaned total data usa
ctdg = tdg.dropna().copy() # cleaned total data global

## 3. step: constructing the data applied for SARD models through accounting information, industry groups and earnings history
# Adding origin sample name column
ctdus['SAMPLE'] = 'USA'
ctdg['SAMPLE'] = 'GLOBAL'

print('Grouping of DI and DS ---> IFRS and US GAAP accounting standard:')
print('US origin accounting standards:')
print(ctdus.ACC_STD.value_counts())
print('Global origin accounting standards:')
print(ctdg.ACC_STD.value_counts())

# Identifier column for subsets
ctdus['SAMPLE2'] = ctdus['SAMPLE'] + ctdus['ACC_STD']
ctdg['SAMPLE2'] = ctdg['SAMPLE'] + ctdg['ACC_STD']
# NB used in step 6 splitting the test samples into two

# rename ISIN and CUSIP codes to CID (company identifier)
ctdus.rename(columns = {'CUSIP':'CID'},inplace=True ) # US companues apply CUSIP
ctdg.rename(columns = {'ISIN':'CID'},inplace=True ) # Global companies apply ISIN

# ordering columns for global and us data
cols1 = ['GVKEY', 'NAME', 'CID' ,'SAMPLE', 'SAMPLE2','INDEXID',
        'CISO','VALUE_YEAR' ,'ACC_STD', 'FYEAR_END',
        'CURR', 'GGROUP', 'GIND',
       'G_SECTOR', 'G_SUBIND', 'SALES', 'OIADP', 'IB', 'DLTT', 'DLC', 'CHE',
       'CEQ','IMPLIED_GROWTH','MKT_CAP']

ctdus = ctdus[cols1].copy() # ordering of accounting numbers, identifiers and market prices
ctdg = ctdg[cols1].copy()

################# remove criteria for global data, S&P 1500 'Global' replication restruction
### In order to be included in the SP1500 index (i.e SP600 is the lower bound)
## require market cap of 450 mio. USD. This also adds to robustness of research

gyears = list(ctdg.VALUE_YEAR.unique())

for y in gyears:
    ctdg['MKT_CAP_FILTER'] = np.where(ctdg['MKT_CAP']<=20,1,0 )
    
# remove 2 i.e only low levels of sales, not being NaNs
# setting up filter
cond1 = ctdg['MKT_CAP_FILTER'] != 1
    
# Data removed due to restrictions on sales and equity
mkt_cap_rstrt = len(ctdg)-len(ctdg[cond1])
print(mkt_cap_rstrt)

ctdg2 = ctdg[cond1].copy()
print(len(ctdg2))

ctdg2 = ctdg2.drop(['MKT_CAP_FILTER'],axis=1).copy()
    

# appending global data to us data before new filtering of the SARD samples
ctd = ctdus.append(ctdg2, ignore_index=True).copy()

ctd['VALUE_YEAR'] = pd.to_numeric(ctd['VALUE_YEAR'])

## 4. step: format data and calculate variables and multiples
  
# calculating variables   
# net interest bearing debt
## long term debt (DLTT) + short term liabilities (DLC) - cash and short investments (CHE)
ctd['NIBD'] = ctd.DLTT + ctd.DLC - ctd.CHE

# calculating P/E ratio
ctd['PE_RATIO'] = ctd.MKT_CAP / ctd.IB

# calculating P/B ratio
ctd['PB_RATIO'] = ctd.MKT_CAP / ctd.CEQ

# EV multiples with sales and EBIT, where EBIT is approximated through OIADP
## EV is market cap plus NIBD
ctd['EV'] = ctd.MKT_CAP + ctd.NIBD

# calculating EV/SALES 
ctd['EV_SALES'] = ctd.EV / ctd.SALES

# calculating EV/SALES 
ctd['EV_EBIT'] = ctd.EV / ctd.OIADP

# calculating EBIT margin 
ctd['EBIT_margin'] = ctd.OIADP / ctd.SALES

# calculating Return on equity
ctd['ROE'] = ctd.IB / ctd.CEQ

# calculating Net debt (NIBD) / EBIT
ctd['NET_DEBT_EBIT'] = ctd.NIBD / ctd.OIADP

# 5. step: Data cleaning
# I exclude observations if companies do not achieve positive EBIT, book value of equity, net income, sales, market cap and EV

# I apply a for loop with these conditon to map and later eliminate observations
# removal criteria, checking for earnings (EBIT and net income), EV, Market Cap, positive sales and book value of equity
# i.e sales and equity are already corrected in the oecd sample, but not for the us
## 1 if true, 0 if not true
remove = []

for index, row in ctd.iterrows():
    if row.IB <= 0:
        remove.append(1)
    elif row.OIADP <= 0:
        remove.append(1)
    elif row.EV <= 0:
        remove.append(1)
    elif row.MKT_CAP <= 0:
        remove.append(1)
    elif row.SALES <= 0:
        remove.append(1)
    elif row.CEQ <= 0:
        remove.append(1)
    else:
        remove.append(0)
        
# adding remove to ctd
ctd['NEGATIVE'] = remove

## Second, I exclude companies with fewer than 5 instances within the sample period
## this is done in order to eliminate outliers with questionable data quality
## unique company list to perform loop
#companies = list(ctd.GVKEY.unique())
#
## population list
#earningshistory_instance = []
#
## looping through data and counting incidents of specific companies
#for c in companies:
#    earningshistory_instance.append(ctd.loc[ctd['GVKEY']==c].GVKEY.count())
#
#del c
#
## incident dataframe:
#dincidents = pd.DataFrame(
#    {'GVKEY': companies,
#     'INSTANCE_COUNT' : earningshistory_instance
#  })
#
## merging former and counter
#ctd = pd.merge(ctd,dincidents, on='GVKEY', how='left').copy()

# dropping remove negatives and dropping remove column
# dropping few instances on the counter column 
ctd2 = ctd.loc[ctd['NEGATIVE']==0].copy() # No negatives earnings, sales, book value of equity and EV
#ctd2 = ctd2.loc[ctd2['INSTANCE_COUNT'] >= 5].copy() # No companies with fewer obs than 5
# drop prior identifier columns
ctd2 = ctd2.drop(['NEGATIVE'],axis=1).copy()

print('Total company year observations in non negative sample:')
print(len(ctd2))
us_remove2 = len(ctd.loc[ctd['SAMPLE']=='USA'].copy()) - len(ctd2.loc[ctd2['SAMPLE']=='USA'].copy())
g_remove2 = len(ctd.loc[ctd['SAMPLE']=='GLOBAL'].copy()) - len(ctd2.loc[ctd2['SAMPLE']=='GLOBAL'].copy())
total_remove2 = us_remove2 + g_remove2
print('Total company year observations excluded from total sample because of negativity (and too few obs):')
print(len(ctd)-len(ctd2))
print(total_remove2 == (len(ctd)-len(ctd2)))

del [ibes_gcols, ibes_ucols,
     row, remove, index]

##### 6. step: dual listings
## I seek to accomondate the risk of dual listings in europe and US through the GVKEY and Year identifiers
## Thus, if firms that are dual listed have unique GVKEY these are still included in the sample. However, if not these are removed
## only TRANSOCEAN LTD are dual listed in the sample and removed from the sample. 
ctd2['TEST'] = ctd2.VALUE_YEAR.astype(str) + ctd2.GVKEY.astype(str)

dupes = ctd2.TEST.duplicated().sum()
print(dupes)

print(len(ctd2) - len(ctd2.drop_duplicates(subset='TEST', keep='first')))

ctd2 = ctd2.drop_duplicates(subset='TEST', keep='first')

ctd2 = ctd2.drop('TEST', axis=1).copy()

rus_clear = len(ctd2) - len(ctd2[ctd2.CISO != 'RUS'])
print(rus_clear)

ctd2 = ctd2[ctd2.CISO != 'RUS'].copy()

print(len(ctd2.loc[ctd2['CISO']=='GBR']))

# Sensata (183942') change CISO in 2019. I replace the USA to GBR
ctd2['CISO'] = np.where(ctd2['GVKEY'] == '183942', 'GBR', ctd2['CISO'])

print(len(ctd2.loc[ctd2['CISO']=='GBR']))

# 7. step: winsorize data for all years. I winsorize at 1 and 99 in each sample year
# in order to handle outliers in regard to the estimated multiples, I winsorize the multiples on 0.5% and 99.5%  
import scipy.stats
# columns to winsorize
multiples = ['PE_RATIO','PB_RATIO', 'EV_SALES','EV_EBIT']
# creating year list to perform loops for both global and us data
years = list(ctd2.VALUE_YEAR.unique()) 

# Total data sample winsorize
ps = pd.DataFrame() 
wctd = pd.DataFrame()

for y in years:
    print(y)
    ps = (ctd2.loc[ctd2['VALUE_YEAR']==y]).copy()
    print(ps.PE_RATIO.mean())
    print(ps.PB_RATIO.mean())
    print(ps.EV_EBIT.mean())
    print(ps.EV_SALES.mean())
    ps[multiples] = scipy.stats.mstats.winsorize(ps[multiples], limits = 0.01)
    print(ps.PE_RATIO.mean())
    print(ps.PB_RATIO.mean())
    print(ps.EV_EBIT.mean())
    print(ps.EV_SALES.mean())
    wctd = wctd.append(ps,ignore_index=True)

## Creating the global sample (excl. US)
# denoted by g
    
gwtd = wctd.loc[wctd['SAMPLE']=='GLOBAL'].copy()
print(gwtd.CISO.value_counts())

# us sample denoted by u
uwtd = wctd.loc[wctd['SAMPLE']=='USA'].copy()
print(uwtd.CISO.value_counts())

# creating eu countries data from the global data set
    
print(gwtd.CISO.unique())    

# europe firm sample
eu_filter = gwtd['CISO'].isin([
        'GBR', 'ITA', 'ESP' ,'FRA', 'DEU', 'FIN' ,'NLD','SWE', 'AUT', 'BEL',
 'PRT', 'DNK', 'HUN', 'CZE', 'POL', 'GRC', 'LUX'
 ]) 
    
asiap_filter = gwtd['CISO'].isin([
        'JPN', 'KOR', 'AUS'
 ]) 


anglosaxon_filter1 = gwtd['CISO'].isin([
         'GBR', 
 ]) 
    


# euro data construction
euwtd = gwtd[eu_filter].copy()

# asia pacific data construction
asiapwtd = gwtd[asiap_filter].copy()

# anglo saxon data construction
anglsaxwtd = uwtd.append(gwtd[anglosaxon_filter1].copy()).copy()

# EU + US  data construction
euuswtd = uwtd.append(gwtd[eu_filter].copy()).copy()

#################################### break #################

print('Three final samples ready for analysis:')
print('COMBINED DATA, ALL FIRMS')
print(wctd.shape)
print('GLOBAL')
print(gwtd.shape)
print('USA')
print(uwtd.shape)
print('EU')
print(euwtd.shape)

print('ASIA')
print(asiapwtd.shape)
print('anglo saxon')
print(anglsaxwtd.shape)
print('EU + USA')
print(euuswtd.shape)

### creating data for industry based selection models
# here, we count yearly industry sectors
# I apply a level-up randomnized algorithm. The cutoff is ot 16 peers in GSECTOR as a baseline. 
# This is done through a counter of the instances for each indivdiual sector (G2) each year for both US and Global
# creating year list to perform loops for both global, us and all data

ayears = list(wctd.VALUE_YEAR.unique()) ;  print(list(ayears))
uyears = list(uwtd.VALUE_YEAR.unique()) ;  print(list(uyears))
gyears = list(gwtd.VALUE_YEAR.unique()) ;  print(list(gyears))
euyears = list(euwtd.VALUE_YEAR.unique()) ;  print(list(euyears))

asiap_years = list(asiapwtd.VALUE_YEAR.unique()) ;  print(list(asiap_years))

anglsax_years = list(anglsaxwtd.VALUE_YEAR.unique()) ;  print(list(anglsax_years))

euus_years = list(euuswtd.VALUE_YEAR.unique()) ;  print(list(euus_years))

print('Checking for consistence in years lists:')
print(len(uyears) == len(gyears)) 
print(len(ayears) == len(gyears))
print(len(ayears) == len(uyears))
print(len(euyears) == len(uyears))
print(len(euyears) == len(gyears))
print(len(euyears) == len(ayears))

## counting n rows for every GICS2
agsecinstance_count = [] # All firms
ugsecinstance_count = [] # US
ggsecinstance_count = [] # Global
eugsecinstance_count = [] # EU

asiapgsecinstance_count = [] # asia pacific
anglsaxgsecinstance_count = [] # anglo saxon
euusgsecinstance_count = [] # EU + US


## counting n years the counting
ayear_id = [] # All firms
uyear_id = [] # US
gyear_id = [] # Global
euyear_id = [] # EU

asiapyear_id = [] # asia pacific
anglsaxyear_id = [] # anglo saxon
euusyear_id = [] # EU + US

## Industry identifier
asec_identifier = [] # All firms
usec_identifier = [] # US
gsec_identifier = [] # Global
eusec_identifier = [] # EU

asiapsec_identifier = [] # asia pacific
anglsaxsec_identifier = [] # anglo saxon
euussec_identifier = [] # EU + US

# all firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for a in ayears: # outer loop
    print(a)
    ps = (wctd.loc[wctd['VALUE_YEAR']==a]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        ayear_id.append(a)
        asec_identifier.append(g)
        agsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [a,g,ayears,gics2s, ps]

# industry count dataframe
agcount_overview = pd.DataFrame(
    {'G_SECTOR': asec_identifier,
     'VALUE_YEAR' : ayear_id,
     'GSECTOR_COUNT' : agsecinstance_count
  })

agcount_overview['G_SECTOR_ID'] = agcount_overview.VALUE_YEAR.astype(str) +''+ agcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
agcount_overview = agcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

# US sample

# clear period specific
ps = pd.DataFrame()

for u in uyears: # outer loop
    print(u)
    ps = (uwtd.loc[uwtd['VALUE_YEAR']==u]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        uyear_id.append(u)
        usec_identifier.append(g)
        ugsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [u,g,uyears,gics2s, ps]

# industry count dataframe
ugcount_overview = pd.DataFrame(
    {'G_SECTOR': usec_identifier,
     'VALUE_YEAR' : uyear_id,
     'GSECTOR_COUNT' : ugsecinstance_count
  })

ugcount_overview['G_SECTOR_ID'] = ugcount_overview.VALUE_YEAR.astype(str) +''+ ugcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
ugcount_overview = ugcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

# Global sample

# clear period specific
ps = pd.DataFrame()

for gy in gyears:
    print(gy)
    ps = (gwtd.loc[gwtd['VALUE_YEAR']==gy]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s:
        gyear_id.append(gy)
        gsec_identifier.append(g)
        ggsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# industry count dataframe
ggcount_overview = pd.DataFrame(
    {'G_SECTOR': gsec_identifier,
     'VALUE_YEAR' : gyear_id,
     'GSECTOR_COUNT' : ggsecinstance_count
  })
    
ggcount_overview['G_SECTOR_ID'] = ggcount_overview.VALUE_YEAR.astype(str) +''+ ggcount_overview.G_SECTOR.astype(str)
# drop gsector and year
ggcount_overview = ggcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

# EU firms

# clear period specific
ps = pd.DataFrame()

for eu in euyears: # outer loop
    print(eu)
    ps = (euwtd.loc[euwtd['VALUE_YEAR']==eu]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        euyear_id.append(eu)
        eusec_identifier.append(g)
        eugsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [eu,g,euyears,gics2s, ps]

# industry count dataframe
eugcount_overview = pd.DataFrame(
    {'G_SECTOR': eusec_identifier,
     'VALUE_YEAR' : euyear_id,
     'GSECTOR_COUNT' : eugsecinstance_count
  })

eugcount_overview['G_SECTOR_ID'] = eugcount_overview.VALUE_YEAR.astype(str) +''+ eugcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
eugcount_overview = eugcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del [gsec_identifier,gyear_id,ggsecinstance_count,gyears,gy,
     usec_identifier,uyear_id,ugsecinstance_count, ayear_id, euyear_id,
     eugsecinstance_count,
     asec_identifier,agsecinstance_count] 

# Asia pacific firms

# clear period specific
ps = pd.DataFrame()

for au in asiap_years: # outer loop
    print(au)
    ps = (asiapwtd.loc[asiapwtd['VALUE_YEAR']==au]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        asiapyear_id.append(au)
        asiapsec_identifier.append(g)
        asiapgsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [au,g,asiap_years,gics2s, ps]

# industry count dataframe
asiapgcount_overview = pd.DataFrame(
    {'G_SECTOR': asiapsec_identifier,
     'VALUE_YEAR' : asiapyear_id,
     'GSECTOR_COUNT' : asiapgsecinstance_count
  })

asiapgcount_overview['G_SECTOR_ID'] = asiapgcount_overview.VALUE_YEAR.astype(str) +''+ asiapgcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
asiapgcount_overview = asiapgcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()


# Anglo saxon
# clear period specific
ps = pd.DataFrame()

for ang in anglsax_years: # outer loop
    print(ang)
    ps = (anglsaxwtd.loc[anglsaxwtd['VALUE_YEAR']==ang]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        anglsaxyear_id.append(ang)
        anglsaxsec_identifier.append(g)
        anglsaxgsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [ang,g,anglsax_years,gics2s, ps]

# industry count dataframe
anglsaxgcount_overview = pd.DataFrame(
    {'G_SECTOR': anglsaxsec_identifier,
     'VALUE_YEAR' : anglsaxyear_id,
     'GSECTOR_COUNT' : anglsaxgsecinstance_count
  })

anglsaxgcount_overview['G_SECTOR_ID'] = anglsaxgcount_overview.VALUE_YEAR.astype(str) +''+ anglsaxgcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
anglsaxgcount_overview = anglsaxgcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

# EU + USA
# clear period specific
ps = pd.DataFrame()

for euus in euus_years: # outer loop
    print(euus)
    ps = (euuswtd.loc[euuswtd['VALUE_YEAR']==euus]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        euusyear_id.append(euus)
        euussec_identifier.append(g)
        euusgsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [euus,g,euus_years,gics2s, ps]

# industry count dataframe
euusgcount_overview = pd.DataFrame(
    {'G_SECTOR': euussec_identifier,
     'VALUE_YEAR' : euusyear_id,
     'GSECTOR_COUNT' : euusgsecinstance_count
  })

euusgcount_overview['G_SECTOR_ID'] = euusgcount_overview.VALUE_YEAR.astype(str) +''+ euusgcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
euusgcount_overview = euusgcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del [anglsaxsec_identifier,anglsaxyear_id,anglsaxgsecinstance_count,
     euussec_identifier,euusyear_id,euusgsecinstance_count,
     asiapsec_identifier,asiapyear_id,asiapgsecinstance_count] 

# creating identifier on the origin
wctd['G_SECTOR_ID'] = wctd.VALUE_YEAR.astype(str) + wctd.G_SECTOR.astype(str)
uwtd['G_SECTOR_ID'] = uwtd.VALUE_YEAR.astype(str) + uwtd.G_SECTOR.astype(str)
gwtd['G_SECTOR_ID'] = gwtd.VALUE_YEAR.astype(str) + gwtd.G_SECTOR.astype(str)
euwtd['G_SECTOR_ID'] = euwtd.VALUE_YEAR.astype(str) + euwtd.G_SECTOR.astype(str)

asiapwtd['G_SECTOR_ID'] = asiapwtd.VALUE_YEAR.astype(str) + asiapwtd.G_SECTOR.astype(str)
anglsaxwtd['G_SECTOR_ID'] = anglsaxwtd.VALUE_YEAR.astype(str) + anglsaxwtd.G_SECTOR.astype(str)
euuswtd['G_SECTOR_ID'] = euuswtd.VALUE_YEAR.astype(str) + euuswtd.G_SECTOR.astype(str)


# merge statement
indwctd = pd.merge(wctd,agcount_overview, on='G_SECTOR_ID', how='left').copy()
induwtd = pd.merge(uwtd,ugcount_overview, on='G_SECTOR_ID', how='left').copy()
indgwtd = pd.merge(gwtd,ggcount_overview, on='G_SECTOR_ID', how='left').copy()
indeuwtd = pd.merge(euwtd,eugcount_overview, on='G_SECTOR_ID', how='left').copy()

indasiapwtd = pd.merge(asiapwtd,asiapgcount_overview, on='G_SECTOR_ID', how='left').copy()
indanglsaxwtd = pd.merge(anglsaxwtd,anglsaxgcount_overview, on='G_SECTOR_ID', how='left').copy()
indeuuswtd = pd.merge(euuswtd,euusgcount_overview, on='G_SECTOR_ID', how='left').copy()


# subsetting data in order to locate sufficient peers
indwctd = indwctd.loc[indwctd['GSECTOR_COUNT']>required_sector_peers].copy()
induwtd = induwtd.loc[induwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indgwtd = indgwtd.loc[indgwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indeuwtd = indeuwtd.loc[indeuwtd['GSECTOR_COUNT']>required_sector_peers].copy()

indasiapwtd = indasiapwtd.loc[indasiapwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indanglsaxwtd = indanglsaxwtd.loc[indanglsaxwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indeuuswtd = indeuuswtd.loc[indeuuswtd['GSECTOR_COUNT']>required_sector_peers].copy()


print('Data eliminated because of insufficient GICS sector peers:')
print('All firms:')
print(len(wctd)-len(indwctd))
ind_remove1 = len(wctd)-len(indwctd)
print('USA firms:')
print(len(uwtd)-len(induwtd))
ind_remove2 = len(uwtd)-len(induwtd)
print('GLOBAL firms:')
print(len(gwtd)-len(indgwtd))
ind_remove3 = len(gwtd)-len(indgwtd)
print('EU firms:')
print(len(euwtd)-len(indeuwtd))
ind_remove4 = len(euwtd)-len(indeuwtd)
print('ASIAP firms:')
print(len(asiapwtd)-len(indasiapwtd))
ind_remove5 = len(asiapwtd)-len(indasiapwtd)

print('Three final industry samples ready for industry-based selection models :')
print('COMBINED DATA, ALL FIRMS')
print(indwctd.shape)
print('USA')
print(induwtd.shape)
print('GLOBAL')
print(indgwtd.shape)
print('EU')
print(indeuwtd.shape)
print('ASIA PACIFIC')
print(indasiapwtd.shape)
print('ANGLO SAXON (UK + US)')
print(indanglsaxwtd.shape)
print('EU + US')
print(indeuuswtd.shape)

# 10. step: descriptive statistics
variables = ['ROE','NET_DEBT_EBIT','MKT_CAP','IMPLIED_GROWTH','EBIT_margin',
                 'EV_EBIT','EV_SALES','PE_RATIO','PB_RATIO']
# calculating mean, median and iqr for variables
from scipy.stats import iqr

# all firms, total sample
all_means = indwctd[variables].mean()
all_median = indwctd[variables].median()
all_iqr = scipy.stats.iqr(indwctd[variables],axis=0)
# storage of descriptive results
all_desc = pd.DataFrame(
    {'MEAN': all_means,
     'MEDIAN' : all_median,
     'IQR' : all_iqr, 
  }).round(3)
    
del [all_means,all_iqr,all_median]

# global sample
global_means = indgwtd[variables].mean()
global_median = indgwtd[variables].median()
global_iqr = scipy.stats.iqr(indgwtd[variables],axis=0)
# storage of descriptive results
global_desc = pd.DataFrame(
    {'MEAN': global_means,
     'MEDIAN' : global_median,
     'IQR' : global_iqr, 
  }).round(3)

del [global_means,global_iqr,global_median]

# us sample
us_means = induwtd[variables].mean()
us_median = induwtd[variables].median()
us_iqr = scipy.stats.iqr(induwtd[variables],axis=0)
# storage of descriptive results
us_desc = pd.DataFrame(
    {'MEAN': us_means,
     'MEDIAN' : us_median,
     'IQR' : us_iqr, 
  }).round(3)
    
del [us_means,us_iqr,us_median]

# us sample
eu_means = indeuwtd[variables].mean()
eu_median = indeuwtd[variables].median()
eu_iqr = scipy.stats.iqr(indeuwtd[variables],axis=0)
# storage of descriptive results
eu_desc = pd.DataFrame(
    {'MEAN': eu_means,
     'MEDIAN' : eu_median,
     'IQR' : eu_iqr, 
  }).round(3)
    
del [eu_means,eu_iqr,eu_median]

print('US')
print(us_desc)
print('Global')
print(global_desc)
print('all')
print(all_desc)
print('EU')
print(eu_desc)

# saving descriptive statistics as latex file

with open('us_desc2.tex','w') as tf:
    tf.write(us_desc.to_latex())

with open('global_desc2.tex','w') as tf:
    tf.write(global_desc.to_latex())
    
with open('total_desc.tex','w') as tf:
    tf.write(all_desc.to_latex())
    
with open('eu_desc.tex','w') as tf:
    tf.write(eu_desc.to_latex())

# IFRS adoption
cisos = list(wctd.CISO.unique())
print(cisos)

#['USA', 'GBR', 'ITA', 'CHE', 'ESP', 'FRA', 'DEU', 'FIN', 'NLD', 'JPN', 'SWE', 
# 'AUT', 'BEL', 'PRT', 'AUS', 'MEX', 'KOR', 'DNK', 'HUN', 'NOR', 'CZE', 'POL', 
# 'GRC', 'LUX', 'NZL', 'TUR', 'CAN',]

adopt = [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1]

ifrs_adopt = pd.DataFrame(
    {'COUNTRY': cisos,
     'ADOPTION' : adopt,
  })
    
# write to latex table:
with open('ifrs_adoption.tex','w') as tf:
    tf.write(ifrs_adopt.to_latex())

# writing data to csv ready for analysis
    
wctd.to_csv('wctd.csv',index=False)
uwtd.to_csv('uwtd.csv',index=False)
gwtd.to_csv('gwtd.csv',index=False)
euwtd.to_csv('euwtd.csv',index=False)

indwctd.to_csv('indwctd.csv',index=False)
induwtd.to_csv('induwtd.csv',index=False)
indgwtd.to_csv('indgwtd.csv',index=False)
indeuwtd.to_csv('indeuwtd.csv',index=False)

anglsaxwtd.to_csv('anglsaxwctd.csv',index=False)
asiapwtd.to_csv('asiapwtd.csv',index=False)
euuswtd.to_csv('euuswtd.csv',index=False)

indanglsaxwtd.to_csv('indanglsaxwtd.csv',index=False)
indasiapwtd.to_csv('indasiapwtd.csv',index=False)
indeuuswtd.to_csv('indeuuswtd.csv',index=False)

### country instances check

years = list(indwctd.VALUE_YEAR.unique())
cisos = list(indwctd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indwctd.loc[indwctd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 10:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    

temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

p_count_countries2 = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

#### store as latex
# write to latex table:
with open('countrycount_overview_induclean.tex','w') as tf:
    tf.write(p_count_countries2.to_latex())
    
del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, ts)


################ analysis of data removal troughout data process

# Global data because of OECD country filtering 
# before 2.312.539 global obs in period
# after 1.052.895 us global in period

#global data removal dfs

g_remove_00 = pd.read_csv('data_elimination2_00.csv' )

g_remove_00 = g_remove_00.set_index('REASON')

g_remove_00 = g_remove_00.T.copy()

g_remove_00['VALUE_YEAR'] = 2000

g_remove_01 = pd.read_csv('data_elimination2_01.csv' )

g_remove_01 = g_remove_01.set_index('REASON')

g_remove_01 = g_remove_01.T.copy()

g_remove_01['VALUE_YEAR'] = 2001

g_remove_02 = pd.read_csv('data_elimination2_02.csv' )

g_remove_02 = g_remove_02.set_index('REASON')

g_remove_02 = g_remove_02.T.copy()

g_remove_02['VALUE_YEAR'] = 2002

g_remove_03 = pd.read_csv('data_elimination2_03.csv' )

g_remove_03 = g_remove_03.set_index('REASON')

g_remove_03 = g_remove_03.T.copy()

g_remove_03['VALUE_YEAR'] = 2003

g_remove_04 = pd.read_csv('data_elimination2_04.csv' )

g_remove_04 = g_remove_04.set_index('REASON')

g_remove_04 = g_remove_04.T.copy()

g_remove_04['VALUE_YEAR'] = 2004

g_remove_05 = pd.read_csv('data_elimination2_05.csv' )

g_remove_05 = g_remove_05.set_index('REASON')

g_remove_05 = g_remove_05.T.copy()

g_remove_05['VALUE_YEAR'] = 2005

g_remove_06 = pd.read_csv('data_elimination2_06.csv' )

g_remove_06 = g_remove_06.set_index('REASON')

g_remove_06 = g_remove_06.T.copy()

g_remove_06['VALUE_YEAR'] = 2006

g_remove_07 = pd.read_csv('data_elimination2_07.csv' )

g_remove_07 = g_remove_07.set_index('REASON')

g_remove_07 = g_remove_07.T.copy()

g_remove_07['VALUE_YEAR'] = 2007

g_remove_08 = pd.read_csv('data_elimination2_08.csv' )

g_remove_08 = g_remove_08.set_index('REASON')

g_remove_08 = g_remove_08.T.copy()

g_remove_08['VALUE_YEAR'] = 2008

g_remove_09 = pd.read_csv('data_elimination2_09.csv' )

g_remove_09 = g_remove_09.set_index('REASON')

g_remove_09 = g_remove_09.T.copy()

g_remove_09['VALUE_YEAR'] = 2009

g_remove_10 = pd.read_csv('data_elimination2_10.csv' )

g_remove_10 = g_remove_10.set_index('REASON')

g_remove_10 = g_remove_10.T.copy()

g_remove_10['VALUE_YEAR'] = 2010

g_remove_11 = pd.read_csv('data_elimination2_11.csv' )

g_remove_11 = g_remove_11.set_index('REASON')

g_remove_11 = g_remove_11.T.copy()

g_remove_11['VALUE_YEAR'] = 2011

g_remove_12 = pd.read_csv('data_elimination2_12.csv' )

g_remove_12 = g_remove_12.set_index('REASON')

g_remove_12 = g_remove_12.T.copy()

g_remove_12['VALUE_YEAR'] = 2012

g_remove_13 = pd.read_csv('data_elimination2_13.csv' )

g_remove_13 = g_remove_13.set_index('REASON')

g_remove_13 = g_remove_13.T.copy()

g_remove_13['VALUE_YEAR'] = 2013

g_remove_14 = pd.read_csv('data_elimination2_14.csv' )

g_remove_14 = g_remove_14.set_index('REASON')

g_remove_14 = g_remove_14.T.copy()

g_remove_14['VALUE_YEAR'] = 2014

g_remove_15 = pd.read_csv('data_elimination2_15.csv' )

g_remove_15 = g_remove_15.set_index('REASON')

g_remove_15 = g_remove_15.T.copy()

g_remove_15['VALUE_YEAR'] = 2015

g_remove_16 = pd.read_csv('data_elimination2_16.csv' )

g_remove_16 = g_remove_16.set_index('REASON')

g_remove_16 = g_remove_16.T.copy()

g_remove_16['VALUE_YEAR'] = 2016

g_remove_17 = pd.read_csv('data_elimination2_17.csv' )

g_remove_17 = g_remove_17.set_index('REASON')

g_remove_17 = g_remove_17.T.copy()

g_remove_17['VALUE_YEAR'] = 2017

g_remove_18 = pd.read_csv('data_elimination2_18.csv' )

g_remove_18 = g_remove_18.set_index('REASON')

g_remove_18 = g_remove_18.T.copy()

g_remove_18['VALUE_YEAR'] = 2018

g_remove_19 = pd.read_csv('data_elimination2_19.csv' )

g_remove_19 = g_remove_19.set_index('REASON')

g_remove_19 = g_remove_19.T.copy()

g_remove_19['VALUE_YEAR'] = 2019

# trailing removal combined df

g_removedfs = [
            g_remove_01,g_remove_02,g_remove_03,g_remove_04,g_remove_05,g_remove_06,
            g_remove_07,g_remove_08,g_remove_09,g_remove_10,g_remove_11,g_remove_12,
            g_remove_13,g_remove_14,g_remove_15,g_remove_16,
            g_remove_17,g_remove_18,g_remove_19]

g_remove = g_remove_00.append(g_removedfs, ignore_index=True)

# INITIAL - nans - restrict  - trail_reduct - restrictions1 = final    

g_check = g_remove.INITIAL.sum() - g_remove.NaNs.sum() - g_remove.TRAIL_REDUCTION.sum() - g_remove.RESTRICTIONS1.sum()
print(g_check)
print(len(gtfin))

# deleting forms
del [
     g_remove_01,g_remove_02,g_remove_03,g_remove_04,g_remove_05,g_remove_06,
            g_remove_07,g_remove_08,g_remove_09,g_remove_10,g_remove_11,g_remove_12,
            g_remove_13,g_remove_14,g_remove_15,g_remove_16,
            g_remove_17,g_remove_18,g_remove_19
     ]


## US data because of SP1500 and filtering of these firms
## before 924.374 us obs in period
## after 179.764 us obs in period

# usa data removal dfs

u_remove_00 = pd.read_csv('us_data_elimination_00.csv' )

u_remove_00 = u_remove_00.set_index('REASON')

u_remove_00 = u_remove_00.T.copy()

u_remove_00['VALUE_YEAR'] = 2000

u_remove_01 = pd.read_csv('us_data_elimination_01.csv' )

u_remove_01 = u_remove_01.set_index('REASON')

u_remove_01 = u_remove_01.T.copy()

u_remove_01['VALUE_YEAR'] = 2001

u_remove_02 = pd.read_csv('us_data_elimination_02.csv' )

u_remove_02 = u_remove_02.set_index('REASON')

u_remove_02 = u_remove_02.T.copy()

u_remove_02['VALUE_YEAR'] = 2002

u_remove_03 = pd.read_csv('us_data_elimination_03.csv' )

u_remove_03 = u_remove_03.set_index('REASON')

u_remove_03 = u_remove_03.T.copy()

u_remove_03['VALUE_YEAR'] = 2003

u_remove_04 = pd.read_csv('us_data_elimination_04.csv' )

u_remove_04 = u_remove_04.set_index('REASON')

u_remove_04 = u_remove_04.T.copy()

u_remove_04['VALUE_YEAR'] = 2004

u_remove_05 = pd.read_csv('us_data_elimination_05.csv' )

u_remove_05 = u_remove_05.set_index('REASON')

u_remove_05 = u_remove_05.T.copy()

u_remove_05['VALUE_YEAR'] = 2005

u_remove_06 = pd.read_csv('us_data_elimination_06.csv' )

u_remove_06 = u_remove_06.set_index('REASON')

u_remove_06 = u_remove_06.T.copy()

u_remove_06['VALUE_YEAR'] = 2006

u_remove_07 = pd.read_csv('us_data_elimination_07.csv' )

u_remove_07 = u_remove_07.set_index('REASON')

u_remove_07 = u_remove_07.T.copy()

u_remove_07['VALUE_YEAR'] = 2007

u_remove_08 = pd.read_csv('us_data_elimination_08.csv' )

u_remove_08 = u_remove_08.set_index('REASON')

u_remove_08 = u_remove_08.T.copy()

u_remove_08['VALUE_YEAR'] = 2008

u_remove_09 = pd.read_csv('us_data_elimination_09.csv' )

u_remove_09 = u_remove_09.set_index('REASON')

u_remove_09 = u_remove_09.T.copy()

u_remove_09['VALUE_YEAR'] = 2009

u_remove_10 = pd.read_csv('us_data_elimination_10.csv' )

u_remove_10 = u_remove_10.set_index('REASON')

u_remove_10 = u_remove_10.T.copy()

u_remove_10['VALUE_YEAR'] = 2010

u_remove_11 = pd.read_csv('us_data_elimination_11.csv' )

u_remove_11 = u_remove_11.set_index('REASON')

u_remove_11 = u_remove_11.T.copy()

u_remove_11['VALUE_YEAR'] = 2011

u_remove_12 = pd.read_csv('us_data_elimination_12.csv' )

u_remove_12 = u_remove_12.set_index('REASON')

u_remove_12 = u_remove_12.T.copy()

u_remove_12['VALUE_YEAR'] = 2012

u_remove_13 = pd.read_csv('us_data_elimination_13.csv' )

u_remove_13 = u_remove_13.set_index('REASON')

u_remove_13 = u_remove_13.T.copy()

u_remove_13['VALUE_YEAR'] = 2013

u_remove_14 = pd.read_csv('us_data_elimination_14.csv' )

u_remove_14 = u_remove_14.set_index('REASON')

u_remove_14 = u_remove_14.T.copy()

u_remove_14['VALUE_YEAR'] = 2014

u_remove_15 = pd.read_csv('us_data_elimination_15.csv' )

u_remove_15 = u_remove_15.set_index('REASON')

u_remove_15 = u_remove_15.T.copy()

u_remove_15['VALUE_YEAR'] = 2015

u_remove_16 = pd.read_csv('us_data_elimination_16.csv' )

u_remove_16 = u_remove_16.set_index('REASON')

u_remove_16 = u_remove_16.T.copy()

u_remove_16['VALUE_YEAR'] = 2016

u_remove_17 = pd.read_csv('us_data_elimination_17.csv' )

u_remove_17 = u_remove_17.set_index('REASON')

u_remove_17 = u_remove_17.T.copy()

u_remove_17['VALUE_YEAR'] = 2017

u_remove_18 = pd.read_csv('us_data_elimination_18.csv' )

u_remove_18 = u_remove_18.set_index('REASON')

u_remove_18 = u_remove_18.T.copy()

u_remove_18['VALUE_YEAR'] = 2018

u_remove_19 = pd.read_csv('us_data_elimination_19.csv' )

u_remove_19 = u_remove_19.set_index('REASON')

u_remove_19 = u_remove_19.T.copy()

u_remove_19['VALUE_YEAR'] = 2019

# trailing removal combined df

u_removedfs = [
            u_remove_01,u_remove_02,u_remove_03,u_remove_04,u_remove_05,u_remove_06,
            u_remove_07,u_remove_08,u_remove_09,u_remove_10,u_remove_11,u_remove_12,
            u_remove_13,u_remove_14,u_remove_15,u_remove_16,
            u_remove_17,u_remove_18,u_remove_19
            ]

u_remove = u_remove_00.append(u_removedfs, ignore_index=True)

# deleting forms
del [
     u_remove_01,u_remove_02,u_remove_03,u_remove_04,u_remove_05,u_remove_06,
     u_remove_07,u_remove_08,u_remove_09,u_remove_10,u_remove_11,u_remove_12,
     u_remove_13,u_remove_14,u_remove_15,u_remove_16,
     u_remove_17,u_remove_18,u_remove_19
     ]


# INITIAL - nans - restrict  - trail_reduct = final    

u_check = u_remove.INITIAL.sum() - u_remove.NaNs.sum() - u_remove.TRAIL_REDUCTION.sum() 
print(u_check)
print(len(ustfin))


### overview of data removal
#start = 1052895
#
#check = g_remove.PRE_TRAIL.sum()
#
#NaNs = g_remove.NaNs.sum()
#
#TR = g_remove.TRAIL_REDUCTION.sum()
#
#restrict = g_remove.RESTRICTIONS1.sum()
#
#time_removal = start - check

### total input data 
total_check = len(ustfin) + len(gtfin)
print(total_check)
print(us_remove1) # IBES removal US
print(g_remove1) # IBES removal global

print(total_remove1) # total IBES removal
print(total_check - total_remove1) # total check ie. US and Global minus total remove

# global data market cap retriction
print(mkt_cap_rstrt)  # removal on global data

print(len(ctd) == (total_check - total_remove1 - mkt_cap_rstrt)) # test

print(len(ctd)) # cleaned total data after IBES removal

print(total_remove2) # mnegative earnings, book value of equity, EV, MKT cap, sales
# obs most are already included in the global sample
# country specific restriction 2 removal
print(us_remove2)
print(g_remove2)

# removal of dual listings and Russia CISO which is perceived as an outlier from initial restriction of OECD countries only
print(dupes) # presumed to be removal of dual listings
print(rus_clear) # one instance of a russian CISO (i.e. loc) in the global sample. ISIN of GB. removed because of country restriction

# cleaning articulate after NaNs and restrictions
print(len(ctd) - total_remove2 - dupes - rus_clear  == len(ctd2))
print(len(ctd2))

# for industry based comparisons, I apply the GICS 16 cleaning. these result in the following removal on various subsets:
print(ind_remove1) # all firms 
print(len(wctd)-ind_remove1) ; print(len(indwctd) == len(wctd)-ind_remove1)

print(ind_remove2) # us firms 
print(len(uwtd)-ind_remove1) ; print(len(induwtd) == len(uwtd)-ind_remove2)

print(ind_remove3) # global firms 
print(len(gwtd)-ind_remove1) ; print(len(indgwtd) == len(gwtd)-ind_remove3)

print(ind_remove4) # eu firms 
print(len(euwtd)-ind_remove4) ; print(len(indeuwtd) == len(euwtd)-ind_remove4)

print(ind_remove5) # asiap firms 
print(len(asiapwtd)-ind_remove5) ; print(len(indasiapwtd) == len(asiapwtd)-ind_remove5)


######################################### country specific for industry based models
### In order to test country specific performance, I need lists of country vectors for testing (i.e. I need to know whether some 
# instances are insufficient in order to run ind-based models)
## two samples: eu and global
### country check
#### global sample checl

years = list(indgwtd.VALUE_YEAR.unique())
cisos = list(indgwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indgwtd.loc[indgwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 10:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    

temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_global = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

#### store as latex
# write to latex table:
with open('indgwtd_countrycount_overview.tex','w') as tf:
    tf.write(count_countries_global.to_latex())
    
del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries)


#### europe sample checl

years = list(indeuwtd.VALUE_YEAR.unique())
cisos = list(indeuwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indeuwtd.loc[indeuwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 10:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    

temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_eu = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

#### store as latex
# write to latex table:
with open('indeuwtd_countrycount_overview.tex','w') as tf:
    tf.write(count_countries_eu.to_latex())
    
del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries)

############################################### break ######################################################
############ select countries in which I can apply the industry level up algo on country site

# AUS, JPN, KOR, CHE, FRA, DEU, GBR, DNK, BEL, SWE, NLD, FIN, NOR
auswtd = wctd.loc[wctd['CISO']=='AUS'].copy()
jpnwtd = wctd.loc[wctd['CISO']=='JPN'].copy()
korwtd = wctd.loc[wctd['CISO']=='KOR'].copy()
chewtd = wctd.loc[wctd['CISO']=='CHE'].copy()
frawtd = wctd.loc[wctd['CISO']=='FRA'].copy()
gbrwtd = wctd.loc[wctd['CISO']=='GBR'].copy()
gerwtd = wctd.loc[wctd['CISO']=='DEU'].copy()

dnkwtd = wctd.loc[wctd['CISO']=='DNK'].copy()
belwtd = wctd.loc[wctd['CISO']=='BEL'].copy()
swewtd = wctd.loc[wctd['CISO']=='SWE'].copy()
nldwtd = wctd.loc[wctd['CISO']=='NLD'].copy()
finwtd = wctd.loc[wctd['CISO']=='FIN'].copy()
norwtd = wctd.loc[wctd['CISO']=='NOR'].copy()

espwtd = wctd.loc[wctd['CISO']=='ESP'].copy()
itawtd = wctd.loc[wctd['CISO']=='ITA'].copy()


### years
ausyears = list(auswtd.VALUE_YEAR.unique()) ;  print(list(ausyears))
jpnyears = list(jpnwtd.VALUE_YEAR.unique()) ;  print(list(jpnyears))
koryears = list(korwtd.VALUE_YEAR.unique()) ;  print(list(koryears))
cheyears = list(chewtd.VALUE_YEAR.unique()) ;  print(list(cheyears))
frayears = list(frawtd.VALUE_YEAR.unique()) ;  print(list(frayears))
gbryears = list(gbrwtd.VALUE_YEAR.unique()) ;  print(list(gbryears))
geryears = list(gerwtd.VALUE_YEAR.unique()) ;  print(list(geryears))

dnkyears = list(dnkwtd.VALUE_YEAR.unique()) ;  print(list(dnkyears))
belyears = list(belwtd.VALUE_YEAR.unique()) ;  print(list(belyears))
sweyears = list(swewtd.VALUE_YEAR.unique()) ;  print(list(sweyears))
nldyears = list(nldwtd.VALUE_YEAR.unique()) ;  print(list(nldyears))
finyears = list(finwtd.VALUE_YEAR.unique()) ;  print(list(finyears))
noryears = list(norwtd.VALUE_YEAR.unique()) ;  print(list(noryears))

espyears = list(espwtd.VALUE_YEAR.unique()) ;  print(list(espyears))
itayears = list(itawtd.VALUE_YEAR.unique()) ;  print(list(itayears))

# australia

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in ausyears: # outer loop
    print(y)
    ps = (auswtd.loc[auswtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,ausyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
aus_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Japan

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in jpnyears: # outer loop
    print(y)
    ps = (jpnwtd.loc[jpnwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,jpnyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
jpn_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# KOrea

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in koryears: # outer loop
    print(y)
    ps = (korwtd.loc[korwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,koryears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
kor_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Switzerland

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in cheyears: # outer loop
    print(y)
    ps = (chewtd.loc[chewtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,cheyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
che_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# France

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in frayears: # outer loop
    print(y)
    ps = (frawtd.loc[frawtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,frayears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
fra_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Germany

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in geryears: # outer loop
    print(y)
    ps = (gerwtd.loc[gerwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,geryears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
ger_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Great britain

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in gbryears: # outer loop
    print(y)
    ps = (gbrwtd.loc[gbrwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,gbryears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
gbr_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Denmark

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in dnkyears: # outer loop
    print(y)
    ps = (dnkwtd.loc[dnkwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,dnkyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
dnk_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Sweden

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in sweyears: # outer loop
    print(y)
    ps = (swewtd.loc[swewtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,sweyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
swe_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Norway

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in noryears: # outer loop
    print(y)
    ps = (norwtd.loc[norwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,noryears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
nor_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Belgium

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in belyears: # outer loop
    print(y)
    ps = (belwtd.loc[belwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,belyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
bel_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

#  Finland

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in finyears: # outer loop
    print(y)
    ps = (finwtd.loc[finwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,finyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
fin_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

#  Netherlands

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in nldyears: # outer loop
    print(y)
    ps = (nldwtd.loc[nldwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,nldyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
nld_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Spain

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in espyears: # outer loop
    print(y)
    ps = (espwtd.loc[espwtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,espyears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
esp_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)

# Italy

## counting n rows for every GICS2
country_gsecinstance_count = [] 

## counting n years the counting
year_id = [] # year_id

## Industry identifier
country_sec_identifier = [] # All firms

# temporary dataframe for every year in order to validate the yearly count of industry groups
ps = pd.DataFrame()

for y in itayears: # outer loop
    print(y)
    ps = (itawtd.loc[itawtd['VALUE_YEAR']==y]).copy()
    gics2s = list(ps.G_SECTOR.unique())
    for g in gics2s: # inner loop
        year_id.append(y)
        country_sec_identifier.append(g)
        country_gsecinstance_count.append(ps.loc[ps['G_SECTOR']==g].G_SECTOR.count())

# delete iter
del [y,g,itayears,gics2s, ps]

# industry count dataframe
country_gcount_overview = pd.DataFrame(
    {'G_SECTOR': country_sec_identifier,
     'VALUE_YEAR' : year_id,
     'GSECTOR_COUNT' : country_gsecinstance_count
  })

country_gcount_overview['G_SECTOR_ID'] = country_gcount_overview.VALUE_YEAR.astype(str) +''+ country_gcount_overview.G_SECTOR.astype(str)
# drop gvkey and year
ita_gcount_overview = country_gcount_overview.drop(['G_SECTOR','VALUE_YEAR'],axis=1).copy()

del (country_gcount_overview, country_sec_identifier, year_id, country_gsecinstance_count)


### cleaning dataframes
# merge statement
indauswtd = pd.merge(auswtd,aus_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indjpnwtd = pd.merge(jpnwtd,jpn_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indkorwtd = pd.merge(korwtd,kor_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indchewtd = pd.merge(chewtd,che_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indfrawtd = pd.merge(frawtd,fra_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indgbrwtd = pd.merge(gbrwtd,gbr_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indgerwtd = pd.merge(gerwtd,ger_gcount_overview, on='G_SECTOR_ID', how='left').copy()

inddnkwtd = pd.merge(dnkwtd,dnk_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indbelwtd = pd.merge(belwtd,bel_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indswewtd = pd.merge(swewtd,swe_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indfinwtd = pd.merge(finwtd,fin_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indnorwtd = pd.merge(norwtd,nor_gcount_overview, on='G_SECTOR_ID', how='left').copy()
indnldwtd = pd.merge(nldwtd,nld_gcount_overview, on='G_SECTOR_ID', how='left').copy()

indespwtd = pd.merge(espwtd,nor_gcount_overview, on='G_SECTOR_ID', how='left').copy()
inditawtd = pd.merge(itawtd,nld_gcount_overview, on='G_SECTOR_ID', how='left').copy()

# subsetting data in order to locate sufficient peers
indauswtd = indauswtd.loc[indauswtd['GSECTOR_COUNT']>required_sector_peers].copy()
indjpnwtd = indjpnwtd.loc[indjpnwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indkorwtd = indkorwtd.loc[indkorwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indchewtd = indchewtd.loc[indchewtd['GSECTOR_COUNT']>required_sector_peers].copy()
indfrawtd = indfrawtd.loc[indfrawtd['GSECTOR_COUNT']>required_sector_peers].copy()
indgbrwtd = indgbrwtd.loc[indgbrwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indgerwtd = indgerwtd.loc[indgerwtd['GSECTOR_COUNT']>required_sector_peers].copy()

inddnkwtd = inddnkwtd.loc[inddnkwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indbelwtd = indbelwtd.loc[indbelwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indswewtd = indswewtd.loc[indswewtd['GSECTOR_COUNT']>required_sector_peers].copy()
indfinwtd = indfinwtd.loc[indfinwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indnorwtd = indnorwtd.loc[indnorwtd['GSECTOR_COUNT']>required_sector_peers].copy()
indnldwtd = indnldwtd.loc[indnldwtd['GSECTOR_COUNT']>required_sector_peers].copy()

inditawtd = inditawtd.loc[inditawtd['GSECTOR_COUNT']>required_sector_peers].copy()
indespwtd = indespwtd.loc[indespwtd['GSECTOR_COUNT']>required_sector_peers].copy()

print(indauswtd.VALUE_YEAR.nunique())
print(indjpnwtd.VALUE_YEAR.nunique())
print(indkorwtd.VALUE_YEAR.nunique())
print(indchewtd.VALUE_YEAR.nunique())
print(indfrawtd.VALUE_YEAR.nunique())
print(indgbrwtd.VALUE_YEAR.nunique())
print(indgerwtd.VALUE_YEAR.nunique())


print(inddnkwtd.VALUE_YEAR.nunique())
print(indbelwtd.VALUE_YEAR.nunique())
print(indswewtd.VALUE_YEAR.nunique())
print(indfinwtd.VALUE_YEAR.nunique())
print(indnorwtd.VALUE_YEAR.nunique())
print(indnldwtd.VALUE_YEAR.nunique())

print(indespwtd.VALUE_YEAR.nunique())
print(indespwtd.VALUE_YEAR.nunique())


print('Australia:')
print(len(auswtd)-len(indauswtd))
print('Japan:')
print(len(jpnwtd)-len(indjpnwtd))
print('South Korea:')
print(len(korwtd)-len(indkorwtd))
print('Switzerland:')
print(len(chewtd)-len(indchewtd))
print('France:')
print(len(frawtd)-len(indfrawtd))
print('Great britain:')
print(len(gbrwtd)-len(indgbrwtd))
print('Germany:')
print(len(gerwtd)-len(indgerwtd))

print('Denmark:')
print(len(dnkwtd)-len(inddnkwtd))
print('Sweden')
print(len(swewtd)-len(indswewtd))
print('Finland:')
print(len(finwtd)-len(indfinwtd))
print('Netherlands:')
print(len(nldwtd)-len(indnldwtd))
print('Norway:')
print(len(norwtd)-len(indnorwtd))
print('Netherlands:')
print(len(nldwtd)-len(indnldwtd))
print('Belgium:')
print(len(belwtd)-len(indbelwtd))

print('Spain:')
print(len(espwtd)-len(indespwtd))
print('Italy:')
print(len(itawtd)-len(inditawtd))

### looking through country specific instances after cleaning

# Austalia

years = list(indauswtd.VALUE_YEAR.unique())
cisos = list(indauswtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indauswtd.loc[indauswtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_aus = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )


# Japan 

years = list(indjpnwtd.VALUE_YEAR.unique())
cisos = list(indjpnwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indjpnwtd.loc[indjpnwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_jpn = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries,)

# KOrea

years = list(indkorwtd.VALUE_YEAR.unique())
cisos = list(indkorwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indkorwtd.loc[indkorwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_kor = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Switzerland

years = list(indchewtd.VALUE_YEAR.unique())
cisos = list(indchewtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indchewtd.loc[indchewtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_che = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# France

years = list(indfrawtd.VALUE_YEAR.unique())
cisos = list(indfrawtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indfrawtd.loc[indfrawtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_fra = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Germany

years = list(indgerwtd.VALUE_YEAR.unique())
cisos = list(indgerwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indgerwtd.loc[indgerwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_ger = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Great Britain

years = list(indgbrwtd.VALUE_YEAR.unique())
cisos = list(indgbrwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indgbrwtd.loc[indgbrwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_gbr = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )


# Denmark

years = list(inddnkwtd.VALUE_YEAR.unique())
cisos = list(inddnkwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = inddnkwtd.loc[inddnkwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_dnk = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Sweden

years = list(indswewtd.VALUE_YEAR.unique())
cisos = list(indswewtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indswewtd.loc[indswewtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_swe = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Norway

years = list(indnorwtd.VALUE_YEAR.unique())
cisos = list(indnorwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indnorwtd.loc[indnorwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_nor = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries,)

# Netherlands

years = list(indnldwtd.VALUE_YEAR.unique())
cisos = list(indnldwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indnldwtd.loc[indnldwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_nld = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

# Belgium

years = list(indbelwtd.VALUE_YEAR.unique())
cisos = list(indbelwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indbelwtd.loc[indbelwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_bel = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )


# Finland

years = list(indfinwtd.VALUE_YEAR.unique())
cisos = list(indfinwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indfinwtd.loc[indfinwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_fin = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries)


#Spain

years = list(indespwtd.VALUE_YEAR.unique())
cisos = list(indespwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = indespwtd.loc[indespwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_esp = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

#Italy

years = list(inditawtd.VALUE_YEAR.unique())
cisos = list(inditawtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = inditawtd.loc[inditawtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_ita = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )

#USA

years = list(induwtd.VALUE_YEAR.unique())
cisos = list(induwtd.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = induwtd.loc[induwtd['VALUE_YEAR']==y].copy()
    for c in cisos:
        cs = ts.loc[ts['CISO']==c].copy()
        country = c
        year = y
        lens = len(cs)
        if lens >= 7:
            dummy = 0
        else:
            dummy = 1
        # append
        countries.append(country)
        years_list.append(year)
        dummies.append(dummy)
        lens_list.append(lens)

count_countries = pd.DataFrame(
    {'COUNTRY': countries,
    'VALUE_YEAR' : years_list,
             'COUNT' : lens_list,
             'DUMMY' : dummies,
                         })
    
temp = count_countries.loc[count_countries['DUMMY']==0].copy()

print(temp.COUNTRY.value_counts())

##########

count_countries2 = count_countries.drop('DUMMY',axis=1)

count_countries_usa = count_countries2.pivot(index='COUNTRY', columns='VALUE_YEAR', values=['COUNT']).copy()

del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries, count_countries2, count_countries, )


#### combined df for country count
country_dfs = [count_countries_aus, count_countries_jpn, count_countries_kor,
               count_countries_che, count_countries_fra, count_countries_ger,
               
               count_countries_dnk, count_countries_fin, count_countries_bel,
               count_countries_nld, count_countries_swe, count_countries_nor,
               
               count_countries_esp, count_countries_ita, count_countries_usa
               
               ]

ind_countries_count = count_countries_gbr.append(country_dfs, ignore_index = False) 

del country_dfs

# countries can be analyzed through 2013-2019

with open('individual_countrycount_overview.tex','w') as tf:
    tf.write(ind_countries_count.to_latex())
    
    
#### industry data for algo on home countries
    
country_dfs = [
            indjpnwtd, indkorwtd, indchewtd, indgerwtd, 
            indfrawtd, indgbrwtd, indswewtd, indfinwtd,
               ]

indu_country_data = indauswtd.append(country_dfs, ignore_index = False).copy()

time_filter1 = indu_country_data['VALUE_YEAR'].isin([2014,
                                2015, 2016, 2017, 2018, 2019
]) 

indu_country_data2 = indu_country_data[time_filter1].copy()

indu_country_data2 = indu_country_data2.append(induwtd, ignore_index = False).copy()

indu_country_data2.to_csv('individual_country_data.csv',index=False)

indu_country_data3 = indu_country_data.append(induwtd, ignore_index = False)

indu_country_data3.to_csv('individual_country_data2.csv',index=False)


del (
     indauswtd, indjpnwtd, indkorwtd, indchewtd, indgerwtd, 
     indfrawtd, indbelwtd, inddnkwtd, indfinwtd, 
     indgbrwtd, indnorwtd, indswewtd, indnldwtd, 
     
     
     auswtd, jpnwtd, korwtd, chewtd, gerwtd, 
     frawtd, belwtd, dnkwtd, finwtd, 
     gbrwtd, norwtd, swewtd, nldwtd, 
     
     count_countries_aus, count_countries_jpn, count_countries_kor,
               count_countries_che, count_countries_fra, count_countries_ger,
               
               count_countries_dnk, count_countries_fin, count_countries_bel,
               count_countries_nld, count_countries_swe, count_countries_nor,
               
               count_countries_gbr, 
               
    aus_gcount_overview, fin_gcount_overview, bel_gcount_overview, che_gcount_overview,
    dnk_gcount_overview, fra_gcount_overview, gbr_gcount_overview, ger_gcount_overview,
    
    kor_gcount_overview, jpn_gcount_overview, nld_gcount_overview, nor_gcount_overview,
    swe_gcount_overview,
    
               
    country_dfs
     
     )

################################# Robustness check 1 
######### Size
## artificial S&P 1500

## S&P 600 (small): 450 mio. USD criteria
## S&P 400(mid): 1.600 mio. USD criteria
## S&P 500 (large): 8.200 mio. USD criteria

print(indwctd.MKT_CAP.describe())
print(indgwtd.MKT_CAP.describe())
print(indeuwtd.MKT_CAP.describe())

#print('Data eliminated because of insufficient GICS sector peers:')
#print('All firms:')
#print(len(wctd)-len(indwctd))
#ind_remove1 = len(wctd)-len(indwctd)
#print('USA firms:')
#print(len(uwtd)-len(induwtd))
#ind_remove2 = len(uwtd)-len(induwtd)
#print('GLOBAL firms:')
#print(len(gwtd)-len(indgwtd))
#ind_remove3 = len(gwtd)-len(indgwtd)
#print('EU firms:')
#print(len(euwtd)-len(indeuwtd))
#ind_remove4 = len(euwtd)-len(indeuwtd)

# All firm sample

years = list(indwctd.VALUE_YEAR.unique())

sp1500list = []
gvkeys = []
val_years = []

mkt_cap = ()

for y in years:
    print(y)
    ts = indwctd.loc[indwctd['VALUE_YEAR']==y].copy()
    companies = list(ts.GVKEY.unique())
    for c in companies:
        print(c)
        cs = ts.loc[ts['GVKEY']==c].copy()
        mkt_cap = cs.MKT_CAP.item()
        if  450 <= mkt_cap < 1600:
            sp1500list.append('SMALL')
        elif 1600 <= mkt_cap < 8200:
            sp1500list.append('MID')
        elif mkt_cap > 8200:
            sp1500list.append('LARGE')
        else:
            sp1500list.append('REST')
        gvkeys.append(c)
        val_years.append(y)
        
artsp_ids = pd.DataFrame(
        {'GVKEY': gvkeys,
         'VALUE_YEAR' : val_years,
         'ART_SP1500' : sp1500list,
      })

print(len(indwctd))

artsp_ids['MERGE_ID'] = artsp_ids.VALUE_YEAR.astype(str) + artsp_ids.GVKEY

artsp_ids = artsp_ids.drop(['GVKEY','VALUE_YEAR'],axis=1).copy()

indwctd['MERGE_ID'] = indwctd.VALUE_YEAR.astype(str) + indwctd.GVKEY

temp = pd.merge(indwctd,artsp_ids, on='MERGE_ID', how='left')

small_wctd = temp.loc[temp['ART_SP1500']=='SMALL'].copy()
print(len(small_wctd))
print(small_wctd.VALUE_YEAR.value_counts())
print(small_wctd.VALUE_YEAR.nunique())
print(small_wctd.CISO.value_counts())
mid_wctd = temp.loc[temp['ART_SP1500']=='MID'].copy()
print(len(mid_wctd))
print(mid_wctd.VALUE_YEAR.value_counts())
print(mid_wctd.VALUE_YEAR.nunique())
print(mid_wctd.CISO.value_counts())
large_wctd = temp.loc[temp['ART_SP1500']=='LARGE'].copy()
print(len(large_wctd))
print(large_wctd.VALUE_YEAR.value_counts())
print(large_wctd.VALUE_YEAR.nunique())
print(large_wctd.CISO.value_counts())

print(len(small_wctd)+len(mid_wctd)+len(large_wctd))
# number of firm-year obs eliminated due to sp 1500 artificial
print(len(indwctd) - (len(small_wctd)+len(mid_wctd)+len(large_wctd)))

print('SMALL')
print(small_wctd.MKT_CAP.describe())
# https://en.wikipedia.org/wiki/S%26P_600#cite_note-1
print('MID')
print(mid_wctd.MKT_CAP.describe())
# https://www.spice-indices.com/idpfiles/spice-assets/resources/public/documents/101753_111mktcaprange6openhitt.pdf
print('LARGE')
print(large_wctd.MKT_CAP.describe())
# https://us.spindices.com/documents/methodologies/methodology-sp-us-indices.pdf

small_wctd.to_csv('small_indwctd.csv',index=False)
mid_wctd.to_csv('mid_indwctd.csv',index=False)
large_wctd.to_csv('large_indwctd.csv',index=False)

index_data = small_wctd.append([mid_wctd, large_wctd], ignore_index = False).copy()

len(index_data)

index_data.to_csv('art_sp1500_data.csv',index=False)

all_size_data = temp.drop(['MERGE_ID'],axis=1).copy()

print(len(all_size_data))
print(len(all_size_data.ART_SP1500.unique()))
print(all_size_data.isnull().sum())

all_size_data.to_csv('all_size_data.csv',index=False)

del (sp1500list, years, gvkeys, mkt_cap, c, y, artsp_ids, temp)


# Global firm sample

years = list(indgwtd.VALUE_YEAR.unique())

sp1500list = []
gvkeys = []
val_years = []

mkt_cap = ()

for y in years:
    print(y)
    ts = indgwtd.loc[indgwtd['VALUE_YEAR']==y].copy()
    companies = list(ts.GVKEY.unique())
    for c in companies:
        print(c)
        cs = ts.loc[ts['GVKEY']==c].copy()
        mkt_cap = cs.MKT_CAP.item()
        if  450 <= mkt_cap < 1600:
            sp1500list.append('SMALL')
        elif 1600 <= mkt_cap < 8200:
            sp1500list.append('MID')
        elif mkt_cap > 8200:
            sp1500list.append('LARGE')
        else:
            sp1500list.append('REST')
        gvkeys.append(c)
        val_years.append(y)
        
artsp_ids = pd.DataFrame(
        {'GVKEY': gvkeys,
         'VALUE_YEAR' : val_years,
         'ART_SP1500' : sp1500list,
      })

print(len(indgwtd))

artsp_ids['MERGE_ID'] = artsp_ids.VALUE_YEAR.astype(str) + artsp_ids.GVKEY

artsp_ids = artsp_ids.drop(['GVKEY','VALUE_YEAR'],axis=1).copy()

indgwtd['MERGE_ID'] = indgwtd.VALUE_YEAR.astype(str) + indgwtd.GVKEY

temp = pd.merge(indgwtd,artsp_ids, on='MERGE_ID', how='left')


global_size_data = temp.drop(['MERGE_ID'],axis=1).copy()

print(len(global_size_data))
print(len(global_size_data.ART_SP1500.unique()))
print(global_size_data.isnull().sum())


global_size_data.to_csv('global_size_data.csv',index=False)

del (sp1500list, years, gvkeys, mkt_cap, c, y, artsp_ids, temp)

# Europ firm sample

years = list(indeuwtd.VALUE_YEAR.unique())

sp1500list = []
gvkeys = []
val_years = []

mkt_cap = ()

for y in years:
    print(y)
    ts = indeuwtd.loc[indeuwtd['VALUE_YEAR']==y].copy()
    companies = list(ts.GVKEY.unique())
    for c in companies:
        print(c)
        cs = ts.loc[ts['GVKEY']==c].copy()
        mkt_cap = cs.MKT_CAP.item()
        if  450 <= mkt_cap < 1600:
            sp1500list.append('SMALL')
        elif 1600 <= mkt_cap < 8200:
            sp1500list.append('MID')
        elif mkt_cap > 8200:
            sp1500list.append('LARGE')
        else:
            sp1500list.append('REST')
        gvkeys.append(c)
        val_years.append(y)
        
artsp_ids = pd.DataFrame(
        {'GVKEY': gvkeys,
         'VALUE_YEAR' : val_years,
         'ART_SP1500' : sp1500list,
      })

print(len(indeuwtd))

artsp_ids['MERGE_ID'] = artsp_ids.VALUE_YEAR.astype(str) + artsp_ids.GVKEY

artsp_ids = artsp_ids.drop(['GVKEY','VALUE_YEAR'],axis=1).copy()

indeuwtd['MERGE_ID'] = indeuwtd.VALUE_YEAR.astype(str) + indeuwtd.GVKEY

temp = pd.merge(indeuwtd,artsp_ids, on='MERGE_ID', how='left')

eu_size_data = temp.drop(['MERGE_ID'],axis=1).copy()

print(len(eu_size_data))
print(len(eu_size_data.ART_SP1500.unique()))
print(eu_size_data.isnull().sum())


rests_test = all_size_data.loc[all_size_data['ART_SP1500']=='REST'].copy()

print(rests_test.MKT_CAP.describe())
print(rests_test.CISO.value_counts())



eu_size_data.to_csv('eu_size_data.csv',index=False)

del (sp1500list, years, gvkeys, mkt_cap, c, y, artsp_ids, temp)

#end time for entire data script
end_action = time.time()
print('Time elapsed throughout total script')
print((end_action - start_action)/60)


