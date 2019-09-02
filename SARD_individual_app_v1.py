#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:33:12 2019

@author: emilhenningsen
"""

### One firm SARD selection algorithm

##### SARD identifier 

import pandas as pd
import numpy as np
from scipy import stats
import scipy.stats
import time

# timer for loop action
start_action = time.time()

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


# Setting estimation peers input
estimation_peers = 7

# setting up data for our SARD program
setting_up_data = True

# counter check
counter = 0

while setting_up_data: 
    # Select the dataset for the current SARD analysis
    data_id = input('Select either global-, all-, eu- or US firms (global, all, eu, us): ')
    if data_id == 'us':
        X = us_companies.copy()
        counter = counter + 1
    elif data_id == 'global':
        X = global_companies.copy()
        counter = counter + 1
    elif data_id == 'all':
        X = total_data.copy()
        counter = counter + 1
    elif data_id == 'eu':
        X = eu_firms.copy()
        counter = counter + 1
    else:
        print('Please select one of the two options presented earlier')
        setting_up_data = False
        break
    # Select the variables of the SARD models
    parameters = input('Select a parameter from 1 to 5 to select the level of detail for the SARD model: ')
    # The decision boundary
    if parameters == '1':
        print('Select from the following: ')
        print('ROE, NET_DEBT_EBIT, MKT_CAP, IMPLIED_GROWTH, EBIT_margin')
        selection_parameter1 = input('Specify one selection variable: ')
        
        variables = ['NAME','GVKEY','VALUE_YEAR','G_SECTOR','CISO',
                     'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT',
              selection_parameter1
              ]
        
        rvariables = [selection_parameter1 
             ]
        
        counter = counter + 1
    elif parameters == '2':
        print('Select from the following: ')
        print('ROE, NET_DEBT_EBIT, MKT_CAP, IMPLIED_GROWTH, EBIT_margin')
        selection_parameter1 = input('Specify first selection variable: ')
        selection_parameter2 = input('Specify second selection variable: ')
        
        variables = ['NAME','GVKEY','VALUE_YEAR','G_SECTOR','CISO',
                     'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT',
              selection_parameter1, selection_parameter2
              ]
        
        rvariables = [selection_parameter1, selection_parameter2, 
             ]
        
        counter = counter + 1
    elif parameters == '3':
        print('Select from the following: ')
        print('ROE, NET_DEBT_EBIT, MKT_CAP, IMPLIED_GROWTH, EBIT_margin')
        selection_parameter1 = input('Specify first selection variable: ')
        selection_parameter2 = input('Specify second selection variable: ')
        selection_parameter3 = input('Specify third selection variable: ')
        
        
        variables = ['NAME','GVKEY','VALUE_YEAR','G_SECTOR','CISO',
                     'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT',
              selection_parameter1, selection_parameter2, selection_parameter3
              ]
        
        rvariables = [selection_parameter1, selection_parameter2, selection_parameter3,
             ]
        
        counter = counter + 1
    elif parameters == '4':
        print('Select from the following: ')
        print('ROE, NET_DEBT_EBIT, MKT_CAP, IMPLIED_GROWTH, EBIT_margin')
        selection_parameter1 = input('Specify first selection variable: ')
        selection_parameter2 = input('Specify second selection variable: ')
        selection_parameter3 = input('Specify third selection variable: ')
        selection_parameter4 = input('Specify fourth selection variable: ')
        
        variables = ['NAME','GVKEY','VALUE_YEAR','G_SECTOR','CISO',
                     'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT',
              selection_parameter1, selection_parameter2, selection_parameter3,
              selection_parameter4
              ]
        
        rvariables = [selection_parameter1, selection_parameter2, selection_parameter3,
              selection_parameter4
             ]
        
        counter = counter + 1
    elif parameters == '5':
        print('Select from the following: ')
        print('ROE, NET_DEBT_EBIT, MKT_CAP, IMPLIED_GROWTH, EBIT_margin')
        selection_parameter1 = input('Specify first selection variable: ')
        selection_parameter2 = input('Specify second selection variable: ')
        selection_parameter3 = input('Specify third selection variable: ')
        selection_parameter4 = input('Specify fourth selection variable: ')
        selection_parameter5 = input('Specify fifth selection variable: ')
        
        variables = ['NAME','GVKEY','VALUE_YEAR','G_SECTOR','CISO',
                     'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT',
              selection_parameter1, selection_parameter2, selection_parameter3,
              selection_parameter4, selection_parameter5
              ]
        
        rvariables = [selection_parameter1, selection_parameter2, selection_parameter3,
              selection_parameter4, selection_parameter5
              ]
        
        counter = counter + 1

    else:
        print('Plese select a parameter from 1 to 5')
        setting_up_data = False
        break
    # Select the variables of the SARD models
    year = input('Select a year for valuation ranging from 2000 to 2019: ')
    year = int(year)
    X = X.loc[X['VALUE_YEAR']==year].copy()
    # finalizing the data for SARD
    if counter == 2:
        X2 = X[variables].copy()
        del X
    else: 
        print('Setting up data failed - please correct the input')
    # Closing the program for data setting
    setting_up_data = False

# Ranking data for SARD algorithm
X2[rvariables] = X2[rvariables].rank(axis=0, method='dense', ascending=False)

# the selection of variables are dynamic in regard to the setting_up_data program
print('Overview of firms to conduct a valuation in the selected year: ')
print(list(X2.NAME))
value_firm = input('Please select a target firm to perform analysis: ')

vfirm = X2.loc[X2['NAME']==value_firm].copy()

# SARD selection algorithm based on input for year, variables and the designated target firm

if parameters == '1':
    # value firm specifics
    # setting up industry parameter
    cgics2 = vfirm.G_SECTOR.item()
    # setting up selection variables of target firm i
    z1_i = vfirm[[selection_parameter1]].copy() ; z1_i = float(z1_i.iloc[0])
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    # calculating the SARD score
    X2['Z1ij'] = abs(X2[[selection_parameter1]] - z1_i) 
    ##
    # SARD score is the sum of absolute distances for the selection variables
    X2['SARD_score'] = X2.Z1ij 
    # finding the peers based on the lowest SARD score given variables z
    temp_peers1 = X2.sort_values(['SARD_score']).copy()
    temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
    peers = temp_peers2.loc[temp_peers2['NAME'] !=  value_firm].copy()
    # estimating the multiples from the natural peers
    PEest = stats.hmean(peers.PE_RATIO,axis=0)
    PBest = stats.hmean(peers.PB_RATIO,axis=0)
    EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
    EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
elif parameters == '2':
    # value firm specifics
    # setting up industry parameter
    cgics2 = vfirm.G_SECTOR.item()
    # setting up selection variables of target firm i
    z1_i = vfirm[[selection_parameter1]].copy() ; z1_i = float(z1_i.iloc[0])
    z2_i = vfirm[[selection_parameter2]].copy() ; z2_i = float(z2_i.iloc[0])
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    # calculating the SARD score
    X2['Z1ij'] = abs(X2[[selection_parameter1]] - z1_i) 
    X2['Z2ij'] = abs(X2[[selection_parameter2]] - z2_i) 
    ##
    # SARD score is the sum of absolute distances for the selection variables
    X2['SARD_score'] =  X2.Z1ij + X2.Z2ij 
    # finding the peers based on the lowest SARD score given variables z
    temp_peers1 = X2.sort_values(['SARD_score']).copy()
    temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
    peers = temp_peers2.loc[temp_peers2['NAME'] !=  value_firm].copy()
    # estimating the multiples from the natural peers
    PEest = stats.hmean(peers.PE_RATIO,axis=0)
    PBest = stats.hmean(peers.PB_RATIO,axis=0)
    EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
    EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
    
elif parameters == '3':
    # value firm specifics
    # setting up industry parameter
    cgics2 = vfirm.G_SECTOR.item()
    # setting up selection variables of target firm i
    z1_i = vfirm[[selection_parameter1]].copy() ; z1_i = float(z1_i.iloc[0])
    z2_i = vfirm[[selection_parameter2]].copy() ; z2_i = float(z2_i.iloc[0])
    z3_i = vfirm[[selection_parameter3]].copy() ; z3_i = float(z3_i.iloc[0])
    ##
    ##
    ##
    ##
    ##
    ##
    ##
    # calculating the SARD score
    X2['Z1ij'] = abs(X2[[selection_parameter1]] - z1_i) 
    X2['Z2ij'] = abs(X2[[selection_parameter2]] - z2_i) 
    X2['Z3ij'] = abs(X2[[selection_parameter3]] - z3_i) 
    ##
    # SARD score is the sum of absolute distances for the selection variables
    X2['SARD_score'] =  X2.Z1ij + X2.Z2ij + X2.Z3ij 
    # finding the peers based on the lowest SARD score given variables z
    temp_peers1 = X2.sort_values(['SARD_score']).copy()
    temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
    peers = temp_peers2.loc[temp_peers2['NAME'] !=  value_firm].copy()
    # estimating the multiples from the natural peers
    PEest = stats.hmean(peers.PE_RATIO,axis=0)
    PBest = stats.hmean(peers.PB_RATIO,axis=0)
    EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
    EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
    
elif parameters == '4':
    # value firm specifics
    # setting up industry parameter
    cgics2 = vfirm.G_SECTOR.item()
    # setting up selection variables of target firm i
    z1_i = vfirm[[selection_parameter1]].copy() ; z1_i = float(z1_i.iloc[0])
    z2_i = vfirm[[selection_parameter2]].copy() ; z2_i = float(z2_i.iloc[0])
    z3_i = vfirm[[selection_parameter3]].copy() ; z3_i = float(z3_i.iloc[0])
    z4_i = vfirm[[selection_parameter4]].copy() ; z4_i = float(z4_i.iloc[0])
    ##
    ##
    ##
    ##
    ##
    ##
    # calculating the SARD score
    X2['Z1ij'] = abs(X2[[selection_parameter1]] - z1_i) 
    X2['Z2ij'] = abs(X2[[selection_parameter2]] - z2_i) 
    X2['Z3ij'] = abs(X2[[selection_parameter3]] - z3_i) 
    X2['Z4ij'] = abs(X2[[selection_parameter4]] - z4_i) 
    ##
    # SARD score is the sum of absolute distances for the selection variables
    X2['SARD_score'] =  X2.Z1ij + X2.Z2ij + X2.Z3ij + X2.Z4ij 
    # finding the peers based on the lowest SARD score given variables z
    temp_peers1 = X2.sort_values(['SARD_score']).copy()
    temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
    peers = temp_peers2.loc[temp_peers2['NAME'] !=  value_firm].copy()
    # estimating the multiples from the natural peers
    PEest = stats.hmean(peers.PE_RATIO,axis=0)
    PBest = stats.hmean(peers.PB_RATIO,axis=0)
    EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
    EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)

elif parameters == '5':
    # value firm specifics
    # setting up industry parameter
    cgics2 = vfirm.G_SECTOR.item()
    # setting up selection variables of target firm i
    z1_i = vfirm[[selection_parameter1]].copy() ; z1_i = float(z1_i.iloc[0])
    z2_i = vfirm[[selection_parameter2]].copy() ; z2_i = float(z2_i.iloc[0])
    z3_i = vfirm[[selection_parameter3]].copy() ; z3_i = float(z3_i.iloc[0])
    z4_i = vfirm[[selection_parameter4]].copy() ; z4_i = float(z4_i.iloc[0])
    z5_i = vfirm[[selection_parameter5]].copy() ; z5_i = float(z5_i.iloc[0])
    ##
    ##
    ##
    ##
    ##
    # calculating the SARD score
    X2['Z1ij'] = abs(X2[[selection_parameter1]] - z1_i) 
    X2['Z2ij'] = abs(X2[[selection_parameter2]] - z2_i) 
    X2['Z3ij'] = abs(X2[[selection_parameter3]] - z3_i) 
    X2['Z4ij'] = abs(X2[[selection_parameter4]] - z4_i) 
    X2['Z5ij'] = abs(X2[[selection_parameter5]] - z5_i) 
    ##
    # SARD score is the sum of absolute distances for the selection variables
    X2['SARD_score'] =  X2.Z1ij + X2.Z2ij + X2.Z3ij + X2.Z4ij + X2.Z5ij 
    # finding the peers based on the lowest SARD score given variables z
    temp_peers1 = X2.sort_values(['SARD_score']).copy()
    temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
    peers = temp_peers2.loc[temp_peers2['NAME'] !=  value_firm].copy()
    # estimating the multiples from the natural peers
    PEest = stats.hmean(peers.PE_RATIO,axis=0)
    PBest = stats.hmean(peers.PB_RATIO,axis=0)
    EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
    EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
    
else:
    print('Please select appropriate parameters to perform SARD selection!!')
    
# calculating absolute percentage errors 
PE_error = abs((PEest - vfirm.PE_RATIO) / vfirm.PE_RATIO)
PB_error  = abs((PBest - vfirm.PB_RATIO) / vfirm.PB_RATIO)
EVSALES_error = abs((EV_SALESest - vfirm.EV_SALES) / vfirm.EV_SALES)
EVEBIT_error  = abs((EV_EBITest - vfirm.EV_EBIT) / vfirm.EV_EBIT)


# creating dict in order to show GICS sectors on selection
gsec_dict = {'35':'Health Care', '15':'Materials', '45':'Information Technology', '20':'Industrials',
             '40':'Financials', '55':'Utilities', '10':'Energy', '25':'Consumer Discretionary', '30':'Consumer Staples', 
             '60':'Real Estate', '50':'Telecommuncation Services' }

peers['G_SECTOR'] = peers['G_SECTOR'].map(gsec_dict)

peers_extract = peers.drop(['GVKEY','VALUE_YEAR'],axis=1)

print('Natural peers found through the SARD model')
print(peers_extract)


print('SARD model selection variables: ')
print(rvariables)

print('Estimation errors incurred for four multiples through the SARD approach')
print('PE error')
print(PE_error)
print('PB error')
print(PB_error)
print('EVEBIT error')
print(EVEBIT_error)
print('EVSALES error')
print(EVSALES_error)





