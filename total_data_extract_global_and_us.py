#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:15:51 2019

@author: emilhenningsen
"""

####### Total data extract from COMPUSTAT

import pandas as pd
import numpy as np
import time

import wrds
db = wrds.Connection()

# timer for loop action
start_action = time.time()

# Extracting total data on compustat for both quarterly and annual data
# SQL path
global_fundq = db.raw_sql("SELECT conm,isin,gvkey,loc,fyearq,fyr,datafqtr,datacqtr,datadate,acctstdq,curcdq,saleq,oiadpq,ibq,dlttq,dlcq,cheq,ceqq from compg.g_fundq where datadate between '1999-01-01' and '2019-03-31'")
print(len(global_fundq))

global_funda = db.raw_sql("SELECT conm,isin,gvkey,loc,fyear,fyr,datadate,acctstd,curcd,sale,oiadp,ib,dltt,dlc,che,ceq from compg.g_funda where datadate between '1999-01-01' and '2019-03-31'")    
print(len(global_funda))

global_fundq.to_csv('total_global_fundq_period.csv',index=False)
global_funda.to_csv('total_global_funda_period.csv',index=False)

temp = tuple(global_fundq.gvkey.unique().copy())
parm_ind = {'ID_GVKEY': temp }

# SQL path to industry groups 
global_comp_ind = db.raw_sql('SELECT conm,gvkey,ggroup,gind,gsector,gsubind from compg.g_company WHERE g_company.gvkey in %(ID_GVKEY)s', params=parm_ind)
global_comp_ind.to_csv('global_company_GICS.csv',index=False)

# create tuple of unique currencies in subset for import
currency = tuple(global_fundq.curcdq.unique())

# creating import parameter
parm_curr = {'ID_CURR': currency }

# sql import of currency data from compustat
data_curr = db.raw_sql('SELECT datadate,fromcurd,tocurd,exratd from compg.g_exrt_dly WHERE g_exrt_dly.tocurd in %(ID_CURR)s', params=parm_curr)

# Now importing USD exchange rates for the period
data_curr_usd = db.raw_sql("SELECT datadate,fromcurd,tocurd,exratd from compg.g_exrt_dly WHERE g_exrt_dly.tocurd in ('USD')")

data_curr.to_csv('exchange_rates_total.csv',index=False)
data_curr_usd.to_csv('usd_rates.csv',index=False)

##### All this data is applied on the Global trailing financial statement script

# Extracting total data on compustat
us_fundq = db.raw_sql("SELECT conm,cusip,gvkey,fyearq,fyr,datafqtr,datacqtr,rdq,datadate,acctstdq,curcdq,saleq,oiadpq,ibq,dlttq,dlcq,cheq,ceqq,oancfy,prccq,cshoq from compd.fundq where datadate between '1999-01-01' and '2019-03-31'")
print(len(us_fundq))
us_funda = db.raw_sql("SELECT conm,cusip,gvkey,fyear,fyr,datadate,acctstd,curcd,sale,oiadp,ib,dltt,dlc,che,ceq,prcc_c,prcc_f,csho from compd.funda where datadate between '1999-01-01' and '2019-03-31'")
print(len(us_funda))

us_fundq.to_csv('total_us_fundq_period.csv',index=False)
us_funda.to_csv('total_us_funda_period.csv',index=False)

# S&P 1500 constituents
SP_comp = db.raw_sql("select gvkey, iid, indexid, datadate "
           "from compd.spidx_cst "
           "where datadate in ('2005-03-31','2006-03-31','2007-03-30','2008-03-31','2009-03-31','2010-03-31',"
           "'2011-03-31','2012-03-30','2013-03-28','2014-03-31','2015-03-31','2016-03-31','2017-03-31','2018-03-29',"
           "'2019-03-29','2004-03-31','2003-03-31','2002-03-28','2001-03-30','2000-03-31','1999-03-31')") 

SP_comp.to_csv('total_sp1500_comp.csv',index=False)

# creating tuple of unique company gvkeys for further data entry
us_comp_list = tuple(SP_comp.gvkey.unique())
# creating parm for sql import
parm = {'ID_GVKEY': us_comp_list }
# Industry groups
us_comp_ind = db.raw_sql('SELECT conm,gvkey,ggroup,gind,gsector,gsubind from compd.company WHERE company.gvkey in %(ID_GVKEY)s', params=parm) # industry identifiers

us_comp_ind.to_csv('us_company_GICS.csv',index=False)
# marketprices for US firms at valuation dates
us_marketprices = db.raw_sql("select gvkey,cusip,conm,datadate,fyearq,fyr,datafqtr,datacqtr,prccq,cshoq "
           "from compd.fundq "
           "where datadate in ('2005-03-31','2006-03-31','2007-03-31','2008-03-31','2009-03-31','2010-03-31',"
           "'2011-03-31','2012-03-31','2013-03-31','2014-03-31','2015-03-31','2016-03-31','2017-03-31','2018-03-31',"
           "'2019-03-31','2004-03-31','2003-03-31','2002-03-31','2001-03-31','2000-03-31','1999-03-31')") 

us_marketprices.to_csv('us_marketprices.csv',index=False)

####### Global filters

# OECD countries in 2000

#Australia, June 7, 1971
#Austria, September 29, 1961
#Belgium, September 13, 1961
#Canada, April 10, 1961
#The Czech Republic, December 21, 1995
#Denmark, May 30, 1961
#Finland, January 28, 1969
#France, August 7, 1961
#Germany, September 27, 1961
#Greece, September 27, 1961
#Hungary, May 7, 1996
#Iceland, June 5, 1961
#Ireland, August 17, 1961
#Italy, March 29, 1962
#Japan, April 28, 1974
#Korea, December 12, 1996
#Luxembourg, December 7, 1961
#Mexico, May 18, 1994
#The Netherlands, November 13, 1961
#New Zealand, May 29, 1973
#Norway, July 4, 1961
#Poland, November 22, 1996
#Portugal, August 4, 1961
#Spain, August 3, 1961
#Sweden, September 28, 1961
#Switzerland, September 28, 1961
#Turkey, August 2, 1961
#The United Kingdom, May 2, 1961
#The United States of America, April 12, 1961

# AUS, AUT, BEL, CAN,  CZE, DNK, FIN, FRA, DEU, GRC, HUN, ISL
# IRL, ITA, JPN, KOR, LUX, MEX, NLD, NZL, NOR, POL, PRT, ESP, SWE, 
# CHE, TUR, GBR, USA

oecd_filter = global_fundq['loc'].isin([
         'AUS', 'AUT', 'BEL', 'CAN',  'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL'
 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'ESP', 'SWE', 
 'CHE', 'TUR', 'GBR', 
]) 

oecd_filter2 = global_funda['loc'].isin([
         'AUS', 'AUT', 'BEL', 'CAN',  'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL'
 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'ESP', 'SWE', 
 'CHE', 'TUR', 'GBR', 
]) 

oecd_gq = global_fundq[oecd_filter]
print(len(oecd_gq) )
print('Quarterly Global Data eliminated from OECD filter:')
print(len(global_fundq) - len(oecd_gq) )
oecd_ga = global_funda[oecd_filter2] 
print(len(oecd_ga))
print('Annual Global Data eliminated from OECD filter:')
print(len(global_funda) - len(oecd_ga) )

oecd_gq.to_csv('oecd_gq_period.csv',index=False)
oecd_ga.to_csv('oecd_ga_period.csv',index=False)

# Global data because of OECD country filtering 
# before 2.312.539 global obs in period
# after 1.052.895 us global in period

########## USA filters

us_comp_list = list(SP_comp.gvkey.unique())

sp1500_filter = us_fundq['gvkey'].isin(us_comp_list) 

sp1500_filter2 = us_funda['gvkey'].isin(us_comp_list) 

sp1500_usq = us_fundq[sp1500_filter]
len(sp1500_usq)
print('Quarterly US Data eliminated from SP filter:')
len(us_fundq) - len(sp1500_usq) 


sp1500_usa = us_funda[sp1500_filter2]
len(sp1500_usa)
print('Annual US Data eliminated from SP filter:')
len(us_funda) - len(sp1500_usa) 

sp1500_usq.to_csv('sp1500_usq_period.csv',index=False)
sp1500_usa.to_csv('sp1500_usa_period.csv',index=False)

# US data because of SP1500 and filtering of these firms
# before 924.374 us obs in period
# after 179.764 us obs in period

######################### currencies

#oecd_gq = pd.read_csv('oecd_gq_period.csv', dtype={'conm': str, 'gvkey': str, 'isin': str,
#                                                                   'loc': str, 'acctstdq': str, 'curcdq': str,})
#
#
#data_curr = pd.read_csv('exchange_rates_total.csv' )

currencies1 = list(oecd_gq.curcdq.unique())

transrate_filter = data_curr['tocurd'].isin(currencies1) 

oecd_data_curr = data_curr[transrate_filter]

oecd_data_curr.to_csv('translation_rates_period.csv',index=False)

########################## original raw global data

# 1. step: import of data for global indices for every year in order to create mapping system
# reading excel data collected from WRDS
# sheet year will be set to select the index constituents on the valuation date

global_data_index_99 = pd.read_excel('Global_indexes.xlsx',sheet_name='99')
global_data_index_00 = pd.read_excel('Global_indexes.xlsx',sheet_name='00')
global_data_index_01 = pd.read_excel('Global_indexes.xlsx',sheet_name='01')
global_data_index_02 = pd.read_excel('Global_indexes.xlsx',sheet_name='02')
global_data_index_03 = pd.read_excel('Global_indexes.xlsx',sheet_name='03')
global_data_index_04 = pd.read_excel('Global_indexes.xlsx',sheet_name='04')
global_data_index_05 = pd.read_excel('Global_indexes.xlsx',sheet_name='05')
global_data_index_06 = pd.read_excel('Global_indexes.xlsx',sheet_name='06')
global_data_index_07 = pd.read_excel('Global_indexes.xlsx',sheet_name='07')
global_data_index_08 = pd.read_excel('Global_indexes.xlsx',sheet_name='08')
global_data_index_09 = pd.read_excel('Global_indexes.xlsx',sheet_name='09')
global_data_index_10 = pd.read_excel('Global_indexes.xlsx',sheet_name='10')
global_data_index_11 = pd.read_excel('Global_indexes.xlsx',sheet_name='11')
global_data_index_12 = pd.read_excel('Global_indexes.xlsx',sheet_name='12')
global_data_index_13 = pd.read_excel('Global_indexes.xlsx',sheet_name='13')
global_data_index_14 = pd.read_excel('Global_indexes.xlsx',sheet_name='14')
global_data_index_15 = pd.read_excel('Global_indexes.xlsx',sheet_name='15')
global_data_index_16 = pd.read_excel('Global_indexes.xlsx',sheet_name='16')
global_data_index_17 = pd.read_excel('Global_indexes.xlsx',sheet_name='17')
global_data_index_18 = pd.read_excel('Global_indexes.xlsx',sheet_name='18')
global_data_index_19 = pd.read_excel('Global_indexes.xlsx',sheet_name='19')


global_data_index = global_data_index_99.append([ global_data_index_00, global_data_index_01,
                                                global_data_index_02, global_data_index_03, global_data_index_04,
                                                global_data_index_05, global_data_index_06, global_data_index_07,
                                                global_data_index_08, global_data_index_09, global_data_index_10,
                                                global_data_index_11, global_data_index_12, global_data_index_13,
                                                global_data_index_14, global_data_index_15, global_data_index_16,
                                                global_data_index_17, global_data_index_18, global_data_index_19,]
                                                                                        )

del (global_data_index_99, global_data_index_00, global_data_index_01,
      global_data_index_02, global_data_index_03, global_data_index_04,
     global_data_index_05, global_data_index_06, global_data_index_07,
     global_data_index_08, global_data_index_09, global_data_index_10,
     global_data_index_11, global_data_index_12, global_data_index_13,
     global_data_index_14, global_data_index_15, global_data_index_16,
     global_data_index_17, global_data_index_18, global_data_index_19 )


global_comp_list = list(global_data_index.ISIN.unique())

global_comp_filter = global_fundq['isin'].isin(global_comp_list) 

comps_global_fundq = global_fundq[global_comp_filter]

# Global data because of INDEX company filtering 
# before 2.312.539 global obs in period
# after 326.707 us global in period



