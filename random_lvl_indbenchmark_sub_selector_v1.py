#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:43:11 2019

@author: emilhenningsen
"""

##### Benchmark randomized level up algorithm

import pandas as pd
import numpy as np
from scipy import stats
import scipy.stats
import time

# timer for loop action
start_action = time.time()

# Setting required peers input
required_peers = input('Required number of peers in the random level up (Lee, Ma, Wang criteria benchmark at 10): ')
required_peers = int(required_peers)

# Setting estimation peers input
estimation_peers = input('Required number of peers to obtain multiple estimate (K&K benchmark at 6): ')
estimation_peers = int(estimation_peers)

print('FYI! the req peers are always n+1 larger than the estimation peers')

# benchmark results robustness tests
# US
#uindselection_R6E6 = pd.read_csv('us_ind_req6_est6.csv')
#uindselection_R7E6 = pd.read_csv('us_ind_req7_est6.csv')
#uindselection_R8E6 = pd.read_csv('us_ind_req8_est6.csv')
#uindselection_R9E6 = pd.read_csv('us_ind_req9_est6.csv')
#uindselection_R10E6 = pd.read_csv('us_ind_req10_est6.csv') # benchmark
#uindselection_R11E6 = pd.read_csv('us_ind_req11_est6.csv')
#uindselection_R12E6 = pd.read_csv('us_ind_req12_est6.csv')
#uindselection_R13E6 = pd.read_csv('us_ind_req13_est6.csv')
#uindselection_R14E6 = pd.read_csv('us_ind_req14_est6.csv')
#uindselection_R15E6 = pd.read_csv('us_ind_req15_est6.csv')
#uindselection_R16E6 = pd.read_csv('us_ind_req16_est6.csv')

# Global
#gindselection_R6E6 = pd.read_csv('global_ind_req6_est6.csv')
#gindselection_R7E6 = pd.read_csv('global_ind_req7_est6.csv')
#gindselection_R8E6 = pd.read_csv('global_ind_req8_est6.csv')
#gindselection_R9E6 = pd.read_csv('global_ind_req9_est6.csv')
#gindselection_R10E6 = pd.read_csv('global_ind_req10_est6.csv') # benchmark
#gindselection_R11E6 = pd.read_csv('global_ind_req11_est6.csv')
#gindselection_R12E6 = pd.read_csv('global_ind_req12_est6.csv')
#gindselection_R13E6 = pd.read_csv('global_ind_req13_est6.csv')
#gindselection_R14E6 = pd.read_csv('global_ind_req14_est6.csv')
#gindselection_R15E6 = pd.read_csv('global_ind_req15_est6.csv')
#gindselection_R16E6 = pd.read_csv('global_ind_req16_est6.csv')


# Data import
# Data import
# US data
us_companies = pd.read_csv('induwtd.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,  'CID':str, 'SAMPLE' : str, 'SAMPLE2' : str, 'INDEXID' : str,
                                               'ACC_STD': str, 'CISO': str, 'FYEAR_END': int,'NAME': str,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,'G_SUBIND': str,
                                                  } )
# Global data
global_companies = pd.read_csv('indgwtd.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,  'CID':str, 'SAMPLE' : str, 'SAMPLE2' : str, 'INDEXID' : str,
                                               'ACC_STD': str, 'CISO': str, 'FYEAR_END': int,'NAME': str,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,'G_SUBIND': str,
                                                  } )

total_data = pd.read_csv('indwctd.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,  'CID':str, 'SAMPLE' : str, 'SAMPLE2' : str, 'INDEXID' : str,
                                               'ACC_STD': str, 'CISO': str, 'FYEAR_END': int,'NAME': str,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,'G_SUBIND': str,
                                                  } )


eu_firms = pd.read_csv('indeuwtd.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,  'CID':str, 'SAMPLE' : str, 'SAMPLE2' : str, 'INDEXID' : str,
                                               'ACC_STD': str, 'CISO': str, 'FYEAR_END': int,'NAME': str,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,'G_SUBIND': str,
                                                  } )


# I create the benchmark randomized level up algorithm for both samples. I store the results in a vector of errors for later analysis.
cols = ['GVKEY', 'NAME', 'CID' , 'SAMPLE','INDEXID',
        'CISO', 'VALUE_YEAR' ,'ACC_STD', 'FYEAR_END',
        'CURR', 'G_SUBIND','GIND','GGROUP', 
       'G_SECTOR', 'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']

# setting the random state to be able to reproduce results
seed = 42
# I use pandas sample function which include a random number generator

# Select the dataset for the current SARD analysis
data_id = input('Select either global, us, all firms or eu firms (us, global, all or eu): ')
if data_id == 'us':
    X = us_companies.copy()
elif data_id == 'global':
    X = global_companies.copy()
elif data_id == 'all':
    X = total_data.copy()
elif data_id == 'eu':
    X = eu_firms.copy()
else:
    print('Please select one of the two options presented earlier')

X = X[cols].copy()
  
# empty period specific dataframe
ps = pd.DataFrame() # ps = period_specific

# industry parameters
cgics2 = () # sector
cgics4 = () # group
cgics6 = () # industry
cgics8 = () # sub-industry

# empty dataframes for the peers found through the level up method
temp_peers = pd.DataFrame() 
peers = pd.DataFrame()

# empty estimated multiples (i.e. items)
PEest = ()
PBest = ()
EV_SALESest = ()
EV_EBITest = ()

# empty estimation population lists
sPE = []
sPB = []
sEVEBIT = []
sEVSALES = []

# empty yearly estimation list for future analysis
sYear = []

# empty company identifer list for future analysis
sCompany = []

# empty GICS sector list for population. For further analysis:
sGics2 = []

# empty company size (index) identifer list for future analysis
sSizeid = []

# industry gics sector parameter
cindex = ()

# sample identifiers
sampleid = ()

# sample id lists
sampleids = []

# country id
ciso_id = ()

# country id list
ciso_ids = []

# dummy identifier showing at which GICS 'level' I'm able to locate sufficient amount of peers
sg2 = []
sg4 = []
sg6 = []
sg8 = []

# list of years for yearly loops
years = list(X.VALUE_YEAR.unique()) # outer loop

# list of companies is empty at origin and will be 'populated' in the inner loop
companies = []

for y in years:
    print(y)
    ps = (X.loc[X['VALUE_YEAR']==y]).copy()
    companies = list(ps.GVKEY.unique()) # for the inner loop
    print(len(companies))
    for i in companies:
        # industry parameter for the ith company
        cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
        cgics4 = (ps.loc[ps['GVKEY']==i].GGROUP.item())
        cgics6 = (ps.loc[ps['GVKEY']==i].GIND.item())
        cgics8 = (ps.loc[ps['GVKEY']==i].G_SUBIND.item())
        # setting up size parameter
        cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
        # setting up sample IDs
        sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
        # setting up CISO IDs
        ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
        # we start off in the highest detail level of industry - subind
        if len(ps.loc[ps['G_SUBIND']==cgics8]) - 1 >= required_peers:
            temp_peers = ps.loc[(ps['G_SUBIND'] == cgics8) & (ps['GVKEY'] != i)].copy() # the same gics8, no target firm
            peers = temp_peers.sample(n=estimation_peers, random_state=seed).copy() # randomly selected sub ind peers
            # estimating the multiples from the randomly selected industry peers
            PEest = stats.hmean(peers.PE_RATIO,axis=0)
            PBest = stats.hmean(peers.PB_RATIO,axis=0)
            EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
            EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
            # populating estimation lists
            sPE.append(PEest.item())
            sPB.append(PBest.item())
            sEVEBIT.append(EV_EBITest.item())
            sEVSALES.append(EV_SALESest.item())
            # identifier population lists are also added
            sYear.append(y.item())
            sCompany.append(i)
            sGics2.append(cgics2)
            sSizeid.append(cindex)
            sampleids.append(sampleid)
            ciso_ids.append(ciso_id)
            # dummies showing the size of selection at various industry levels
            sg2.append(1)
            sg4.append(1)
            sg6.append(1)
            sg8.append(1)
        # if not sufficient we move 'up' the GICS code in order to attain the comparable industry peers
        elif len(ps.loc[ps['GIND']==cgics6]) - 1 >= required_peers:
            temp_peers = ps.loc[(ps['GIND'] == cgics6) & (ps['GVKEY'] != i)].copy() # the same gics6, no target firm
            peers = temp_peers.sample(n=estimation_peers, random_state=seed).copy() # randomly selected ind peers
            # estimating the multiples from the randomly selected industry peers
            PEest = stats.hmean(peers.PE_RATIO,axis=0)
            PBest = stats.hmean(peers.PB_RATIO,axis=0)
            EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
            EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
            # populating estimation lists
            sPE.append(PEest.item())
            sPB.append(PBest.item())
            sEVEBIT.append(EV_EBITest.item())
            sEVSALES.append(EV_SALESest.item())
            # identifier population lists are also added
            sYear.append(y.item())
            sCompany.append(i)
            sGics2.append(cgics2)
            sSizeid.append(cindex)
            sampleids.append(sampleid)
            ciso_ids.append(ciso_id)
            # dummies showing the size of selection at various industry levels
            sg2.append(1)
            sg4.append(1)
            sg6.append(1)
            sg8.append(0)
        elif len(ps.loc[ps['GGROUP']==cgics4]) - 1 >= required_peers:
            temp_peers = ps.loc[(ps['GGROUP'] == cgics4) & (ps['GVKEY'] != i)].copy() # the same gics4, no target firm
            peers = temp_peers.sample(n=estimation_peers, random_state=seed).copy() # randomly selected GICS group peers
            # estimating the multiples from the randomly selected industry peers
            PEest = stats.hmean(peers.PE_RATIO,axis=0)
            PBest = stats.hmean(peers.PB_RATIO,axis=0)
            EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
            EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
            # populating estimation lists
            sPE.append(PEest.item())
            sPB.append(PBest.item())
            sEVEBIT.append(EV_EBITest.item())
            sEVSALES.append(EV_SALESest.item())
            # identifier population lists are also added
            sYear.append(y.item())
            sCompany.append(i)
            sGics2.append(cgics2)
            sSizeid.append(cindex)
            sampleids.append(sampleid)
            ciso_ids.append(ciso_id)
            # dummies showing the size of selection at various industry levels
            sg2.append(1)
            sg4.append(1)
            sg6.append(0)
            sg8.append(0)
        else:
            temp_peers = ps.loc[(ps['G_SECTOR'] == cgics2) & (ps['GVKEY'] != i)].copy() # the same gics2, no target firm
            peers = temp_peers.sample(n=estimation_peers, random_state=seed).copy() # randomly selected GICS sector peers
            # estimating the multiples from the randomly selected industry peers
            PEest = stats.hmean(peers.PE_RATIO,axis=0)
            PBest = stats.hmean(peers.PB_RATIO,axis=0)
            EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
            EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
            # populating estimation lists
            sPE.append(PEest.item())
            sPB.append(PBest.item())
            sEVEBIT.append(EV_EBITest.item())
            sEVSALES.append(EV_SALESest.item())
            # identifier population lists are also added
            sYear.append(y.item())
            sCompany.append(i)
            sGics2.append(cgics2)
            sSizeid.append(cindex)
            sampleids.append(sampleid)
            ciso_ids.append(ciso_id)
            # dummies showing the size of selection at various industry levels
            sg2.append(1)
            sg4.append(0)
            sg6.append(0)
            sg8.append(0)
            
print("Peers located and multiples estimated!")

# multiple error evaluation
# store data to calculate errors
estimations = pd.DataFrame(
    {'GVKEY': sCompany,
     'SAMPLE_ID' : sampleids,
     'CISO' : ciso_ids,
     'GICS_SECTOR': sGics2,
     'SIZEINDEX' : sSizeid,
          'GICS8_dummy' : sg8,
     'GICS6_dummy' : sg6,
     'GICS4_dummy': sg4,
     'GICS2_dummy': sg2,
     'VALUE_YEAR' : sYear,
     'EST_PE' : sPE,
     'EST_PB' : sPB,
     'EST_EVEBIT' : sEVEBIT,
     'EST_EVSALES' : sEVSALES,
  })
    
# realized 'true' values
realized = X[['GVKEY','VALUE_YEAR','PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']].copy()

# creating merge ID
realized['MERGE_ID'] = realized.VALUE_YEAR.astype(str) + realized.GVKEY.astype(str)
estimations['MERGE_ID'] = estimations.VALUE_YEAR.astype(str) + estimations.GVKEY.astype(str)
estimations = estimations.drop(['GVKEY','VALUE_YEAR'],axis=1).copy()
# merge dataframes
errors = pd.merge(estimations,realized,on='MERGE_ID',how='left').copy()

# calculating absolute percentage errors 
errors['PE_error'] = abs((errors.EST_PE - errors.PE_RATIO) / errors.PE_RATIO)
errors['PB_error']  = abs((errors.EST_PB - errors.PB_RATIO) / errors.PB_RATIO)
errors['EVSALES_error']  = abs((errors.EST_EVSALES - errors.EV_SALES) / errors.EV_SALES)
errors['EVEBIT_error']  = abs((errors.EST_EVEBIT - errors.EV_EBIT) / errors.EV_EBIT)

# identifier for GICS groups selection within SARD
# 1 GICS2 lvl
# 2 GICS4 lvl
# 3 GICS6 lvl
# 4 GICS8 lvl

errors['INDLVL_SELECT'] = (errors.GICS8_dummy + errors.GICS6_dummy + errors.GICS4_dummy + errors.GICS2_dummy)

# drop estimated and realized values
errors = errors.drop(['PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT','EST_PE','EST_PB','EST_EVEBIT',
            'EST_EVSALES'],axis=1).copy()

# storage of us industry estimation errors
benchmark_errors = errors.copy() 
# add back identifiers on the inputs for the selection algorithm
benchmark_errors['REQ_PEERS'] = required_peers
benchmark_errors['EST_PEERS'] = estimation_peers

# printing errors
print('PE')
print('mean')
print(benchmark_errors.PE_error.mean())
print('median')
print(benchmark_errors.PE_error.median())
print('IQR')
print(scipy.stats.iqr(benchmark_errors.PE_error,axis=0))
print('###########BREAK########')
print('PB')
print('mean')
print(benchmark_errors.PB_error.mean())
print('median')
print(benchmark_errors.PB_error.median())
print('IQR')
print(scipy.stats.iqr(benchmark_errors.PB_error,axis=0))
print('###########BREAK########')
print('EV_EBIT')
print('mean')
print(benchmark_errors.EVEBIT_error.mean())
print('median')
print(benchmark_errors.EVEBIT_error.median())
print('IQR')
print(scipy.stats.iqr(benchmark_errors.EVEBIT_error,axis=0))
print('###########BREAK########')
print('EV_SALES')
print('mean')
print(benchmark_errors.EVSALES_error.mean())
print('median')
print(benchmark_errors.EVSALES_error.median())  
print('IQR')
print(scipy.stats.iqr(benchmark_errors.EVSALES_error,axis=0))

# writing to csv
required_peers_id = str(required_peers)
estimation_peers_id = str(estimation_peers)

benchmark_errors.to_csv(''+data_id+'__errors_benchmark_R'+required_peers_id+'E'+estimation_peers_id+'.csv',index=False)

# industry selection summary
selections = pd.DataFrame(
    {'GVKEY': sCompany,
     'VALUE_YEAR' : sYear,
     'GICS2' : sg2,
     'GICS4' : sg4,
     'GICS6' : sg6,
     'GICS8' : sg8,
  })

# adding identifiers for the selection data
selections['REQ_PEERS'] = required_peers
selections['EST_PEERS'] = estimation_peers    

# calculate percentages and store results with the required number of peers
g8_ratio = selections.loc[selections['GICS8']==1].GICS8.count() / len(selections)
g6_ratio = selections.loc[selections['GICS6']==1].GICS8.count() / len(selections)
g4_ratio = selections.loc[selections['GICS4']==1].GICS8.count() / len(selections)
g2_ratio = selections.loc[selections['GICS2']==1].GICS8.count() / len(selections)

print(g8_ratio)
print(g6_ratio)
print(g4_ratio)
print(g2_ratio)


del [years,companies,EV_EBITest,EV_SALESest,PEest,PBest,ps,sCompany,sEVEBIT,sEVSALES,
     sPB,sPE,sYear,sg2,sg4,sg6,sg8,X,errors,peers,temp_peers,y,i,
     g8_ratio,g6_ratio,g4_ratio,g2_ratio,cgics2,cgics4,cgics6,cgics8, realized,estimations]
     
     
# writing to csv
selections.to_csv(''+data_id+'_ind_req'+required_peers_id+'_est'+estimation_peers_id+'.csv',index=False)


