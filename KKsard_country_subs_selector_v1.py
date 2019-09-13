#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:57:15 2019

@author: emilhenningsen
"""


##### SARD identifier 

import pandas as pd
import numpy as np
from scipy import stats
import scipy.stats
import time

# timer for loop action
start_action = time.time()


# Global data

total_data = pd.read_csv('wctd.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,  'CID':str, 'SAMPLE' : str, 'SAMPLE2' : str, 'INDEXID' : str,
                                               'ACC_STD': str, 'CISO': str, 'FYEAR_END': int,'NAME': str,
                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,'G_SUBIND': str,
                                                  } )

### country check

years = list(total_data.VALUE_YEAR.unique())
cisos = list(total_data.CISO.unique())

country = ()
year = ()
dummy = ()

countries = []
years_list = []
dummies = []

lens = ()
lens_list = []

for y in years:
    ts = total_data.loc[total_data['VALUE_YEAR']==y].copy()
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
with open('countrycount_overview.tex','w') as tf:
    tf.write(p_count_countries2.to_latex())
    
del (lens, lens_list, dummies, dummy, year, country, years, cisos,
     temp, countries)

# In sum I develop 5 SARD models each adding one additional selection parameter in the peer selector model

sard_cols1 = ['GVKEY','VALUE_YEAR',
              'G_SECTOR','INDEXID','SAMPLE','CISO',
              'ROE',
              'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']
sard_cols2 = ['GVKEY','VALUE_YEAR',
              'G_SECTOR','INDEXID','SAMPLE','CISO',
              'ROE','NET_DEBT_EBIT',
              'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']
sard_cols3 = ['GVKEY','VALUE_YEAR',
              'G_SECTOR','INDEXID','SAMPLE','CISO',
              'ROE','NET_DEBT_EBIT','MKT_CAP',
              'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']
sard_cols4 = ['GVKEY','VALUE_YEAR',
              'G_SECTOR','INDEXID','SAMPLE','CISO',
              'ROE','NET_DEBT_EBIT','MKT_CAP','IMPLIED_GROWTH',
              'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']
sard_cols5 = ['GVKEY','VALUE_YEAR',
              'G_SECTOR','INDEXID','SAMPLE','CISO',
              'ROE','NET_DEBT_EBIT','MKT_CAP','IMPLIED_GROWTH','EBIT_margin',
              'PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']

# Select the dataset for the current SARD analysis
X = total_data.copy()
# Select the variables of the SARD models
parameters = input('Select a parameter from 1 to 5 to select the level of detail for the SARD model: ')
# The decision boundary
if parameters == '1':
    variables = sard_cols1
elif parameters == '2':
    variables = sard_cols2
elif parameters == '3':
    variables = sard_cols3
elif parameters == '4':
    variables = sard_cols4
elif parameters == '5':
    variables = sard_cols5
else:
    print('Plese select a parameter from 1 to 5')
    
X2 = X[variables].copy()
  
countries = [ 'NLD', 'ESP', 'ITA', 'NOR', 'JPN', 'FIN', 'CHE',
             'AUS', 'SWE', 'BEL', 'USA', 'FRA', 'KOR', 'DNK',
             'DEU', 'GBR', ]
#NLD    20
#ESP    20
#ITA    20
#NOR    20
#JPN    20
#FIN    20
#CHE    20
#AUS    20
#SWE    20
#BEL    20
#USA    20
#FRA    20
#KOR    20
#DNK    20
#DEU    20
#GBR    20

# cols for ranking
cols1 = ['ROE',]
cols2 = ['ROE','NET_DEBT_EBIT']
cols3 = ['ROE','NET_DEBT_EBIT','MKT_CAP']
cols4 = ['ROE','NET_DEBT_EBIT','MKT_CAP','IMPLIED_GROWTH']
cols5 = ['ROE','NET_DEBT_EBIT','MKT_CAP','IMPLIED_GROWTH','EBIT_margin']

estimation_peers = input('Required number of peers to obtain multiple estimate (K&K benchmark at 6, for the algo select the number of peers + 1, i.e. 7 for 6 peers): ')
estimation_peers = int(estimation_peers)

for c in countries:
    # SARD algorithm dynamic
    # setup
    cs = X2.loc[X2['CISO']==c].copy() # ciso specific
    print(c)
    print(len(cs))
    # setting up loop list for years
    # list for looping
    years = list(cs.VALUE_YEAR.unique())
    # empty period specific dataframe
    ps = pd.DataFrame() # ps = period_specific
    temp_peers1 = pd.DataFrame()
    temp_peers2 = pd.DataFrame()
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

    # empty company identifer list for future analysi
    sGics = []

    # industry gics sector parameter
    cgics2 = ()

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

    # selection variables
    z1_i = () # ROE
    z2_i = () # Debt/EBIT
    z3_i = () # Size (MKT_CAP)
    z4_i = () # Implied growth
    z5_i = () # EBIT margin
    
    # Dynamic SARD algo dependent on the input:
    
    if len(cs.columns) == 11:
        for y in years:
            print(y)
            ps = (cs.loc[cs['VALUE_YEAR']==y]).copy()
            ps[cols1] = ps[cols1].rank(axis=0, method='dense', ascending=False)
            companies = list(ps.GVKEY.unique()) # for the inner loop
            print(len(companies))
            for i in companies: 
                # setting up industry parameter
                cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
                # setting up size parameter
                cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
                # setting up sample IDs
                sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
                # setting up CISO IDs
                ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
                # setting up selection variables of target firm i
                z1_i = (ps.loc[ps['GVKEY']==i].ROE.item())
                # calculating the SARD score
                ps['Z1ij'] = abs(ps['ROE'] - z1_i) 
                # SARD score is the sum of absolute distances for the selection variables
                ps['SARD_score'] = ps.Z1ij 
                # finding the peers based on the lowest SARD score given variables z
                temp_peers1 = ps.sort_values(['SARD_score']).copy()
                temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
                peers = temp_peers2.loc[temp_peers2['GVKEY'] !=  i].copy()
                # estimating the multiples from the natural peers
                PEest = stats.hmean(peers.PE_RATIO,axis=0)
                PBest = stats.hmean(peers.PB_RATIO,axis=0)
                EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
                EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
                # populating estimation lists
                sPE.append(PEest.item())
                sPB.append(PBest.item())
                sEVEBIT.append(EV_EBITest.item())
                sEVSALES.append(EV_SALESest.item())
                # identifeir population lists are also added
                sYear.append(y.item())
                sCompany.append(i)
                sGics.append(cgics2)
                sSizeid.append(cindex)
                sampleids.append(sampleid)
                ciso_ids.append(ciso_id)
    elif len(cs.columns) == 12:
        for y in years:
            print(y)
            ps = (cs.loc[cs['VALUE_YEAR']==y]).copy()
            ps[cols2] = ps[cols2].rank(axis=0, method='dense', ascending=False)
            companies = list(ps.GVKEY.unique()) # for the inner loop
            print(len(companies))
            for i in companies:
                # setting up industry parameter
                cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
                # setting up size parameter
                cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
                # setting up sample IDs
                sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
                # setting up CISO IDs
                ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
                # setting up selection variables of target firm i
                z1_i = (ps.loc[ps['GVKEY']==i].ROE.item())
                z2_i = (ps.loc[ps['GVKEY']==i].NET_DEBT_EBIT.item())
                # calculating the SARD score
                ps['Z1ij'] = abs(ps['ROE'] - z1_i) 
                ps['Z2ij'] = abs(ps['NET_DEBT_EBIT'] - z2_i) 
                # SARD score is the sum of absolute distances for the selection variables
                ps['SARD_score'] = ps.Z1ij + ps.Z2ij
                # ffinding the peers based on the lowest SARD score given variables z
                temp_peers1 = ps.sort_values(['SARD_score']).copy()
                temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
                peers = temp_peers2.loc[temp_peers2['GVKEY'] != i ].copy()
                # estimating the multiples from the natural peers
                PEest = stats.hmean(peers.PE_RATIO,axis=0)
                PBest = stats.hmean(peers.PB_RATIO,axis=0)
                EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
                EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
                # populating estimation lists
                sPE.append(PEest.item())
                sPB.append(PBest.item())
                sEVEBIT.append(EV_EBITest.item())
                sEVSALES.append(EV_SALESest.item())
                # identifier population lists are also added
                sYear.append(y.item())
                sCompany.append(i)
                sGics.append(cgics2)
                sSizeid.append(cindex)
                sampleids.append(sampleid)
                ciso_ids.append(ciso_id)
    elif len(cs.columns) == 13:
        for y in years:
            print(y)
            ps = (cs.loc[cs['VALUE_YEAR']==y]).copy()
            ps[cols3] = ps[cols3].rank(axis=0, method='dense', ascending=False)
            companies = list(ps.GVKEY.unique()) # for the inner loop
            print(len(companies))
            for i in companies:
                # setting up industry parameter
                cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
                # setting up size parameter
                cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
                # setting up sample IDs
                sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
                # setting up CISO IDs
                ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
                # setting up selection variables of target firm i
                z1_i = (ps.loc[ps['GVKEY']==i].ROE.item())
                z2_i = (ps.loc[ps['GVKEY']==i].NET_DEBT_EBIT.item())
                z3_i = (ps.loc[ps['GVKEY']==i].MKT_CAP.item())
                # calculating the SARD score
                ps['Z1ij'] = abs(ps['ROE'] - z1_i) 
                ps['Z2ij'] = abs(ps['NET_DEBT_EBIT'] - z2_i) 
                ps['Z3ij'] = abs(ps['MKT_CAP'] - z3_i) 
                # SARD score is the sum of absolute distances for the selection variables
                ps['SARD_score'] = ps.Z1ij + ps.Z2ij + ps.Z3ij
                # finding the peers based on the lowest SARD score given variables z
                temp_peers1 = ps.sort_values(['SARD_score']).copy()
                temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
                peers = temp_peers2.loc[temp_peers2['GVKEY'] != i ].copy()
                # estimating the multiples from the natural peers
                PEest = stats.hmean(peers.PE_RATIO,axis=0)
                PBest = stats.hmean(peers.PB_RATIO,axis=0)
                EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
                EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
                # populating estimation lists
                sPE.append(PEest.item())
                sPB.append(PBest.item())
                sEVEBIT.append(EV_EBITest.item())
                sEVSALES.append(EV_SALESest.item())
                # identifier population lists are also added
                sYear.append(y.item())
                sCompany.append(i)
                sGics.append(cgics2)
                sSizeid.append(cindex)
                sampleids.append(sampleid)
                ciso_ids.append(ciso_id)
    elif len(cs.columns) == 14:
        for y in years:
            print(y)
            ps = (cs.loc[cs['VALUE_YEAR']==y]).copy()
            ps[cols4] = ps[cols4].rank(axis=0, method='dense', ascending=False)
            companies = list(ps.GVKEY.unique()) # for the inner loop
            print(len(companies))
            for i in companies:
                # setting up industry parameter
                cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
                # setting up size parameter
                cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
                # setting up sample IDs
                sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
                # setting up CISO IDs
                ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
                # setting up selection variables of target firm i
                z1_i = (ps.loc[ps['GVKEY']==i].ROE.item())
                z2_i = (ps.loc[ps['GVKEY']==i].NET_DEBT_EBIT.item())
                z3_i = (ps.loc[ps['GVKEY']==i].MKT_CAP.item())
                z4_i = (ps.loc[ps['GVKEY']==i].IMPLIED_GROWTH.item())
                # calculating the SARD score
                ps['Z1ij'] = abs(ps['ROE'] - z1_i) 
                ps['Z2ij'] = abs(ps['NET_DEBT_EBIT'] - z2_i) 
                ps['Z3ij'] = abs(ps['MKT_CAP'] - z3_i) 
                ps['Z4ij'] = abs(ps['IMPLIED_GROWTH'] - z4_i) 
                # SARD score is the sum of absolute distances for the selection variables
                ps['SARD_score'] = ps.Z1ij + ps.Z2ij + ps.Z3ij + ps.Z4ij
                # finding the peers based on the lowest SARD score given variables z
                temp_peers1 = ps.sort_values(['SARD_score']).copy()
                temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
                peers = temp_peers2.loc[temp_peers2['GVKEY'] != i ].copy()
                # estimating the multiples from the natural peers
                PEest = stats.hmean(peers.PE_RATIO,axis=0)
                PBest = stats.hmean(peers.PB_RATIO,axis=0)
                EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
                EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
                # populating estimation lists
                sPE.append(PEest.item())
                sPB.append(PBest.item())
                sEVEBIT.append(EV_EBITest.item())
                sEVSALES.append(EV_SALESest.item())
                # identifier population lists are also added
                sYear.append(y.item())
                sCompany.append(i)
                sGics.append(cgics2)
                sSizeid.append(cindex)
                sampleids.append(sampleid)
                ciso_ids.append(ciso_id)
    elif len(X2.columns) == 15:
        for y in years:
            print(y)
            ps = (cs.loc[cs['VALUE_YEAR']==y]).copy()
            ps[cols5] = ps[cols5].rank(axis=0, method='dense', ascending=False)
            companies = list(ps.GVKEY.unique()) # for the inner loop
            print(len(companies))
            for i in companies:
                # setting up industry parameter
                cgics2 = (ps.loc[ps['GVKEY']==i].G_SECTOR.item())
                # setting up size parameter
                cindex = (ps.loc[ps['GVKEY']==i].INDEXID.item())
                # setting up sample IDs
                sampleid = (ps.loc[ps['GVKEY']==i].SAMPLE.item())
                # setting up CISO IDs
                ciso_id = (ps.loc[ps['GVKEY']==i].CISO.item())
                # setting up selection variables of target firm i
                z1_i = (ps.loc[ps['GVKEY']==i].ROE.item())
                z2_i = (ps.loc[ps['GVKEY']==i].NET_DEBT_EBIT.item())
                z3_i = (ps.loc[ps['GVKEY']==i].MKT_CAP.item())
                z4_i = (ps.loc[ps['GVKEY']==i].IMPLIED_GROWTH.item())
                z5_i = (ps.loc[ps['GVKEY']==i].EBIT_margin.item())
                # calculating the SARD score
                ps['Z1ij'] = abs(ps['ROE'] - z1_i) 
                ps['Z2ij'] = abs(ps['NET_DEBT_EBIT'] - z2_i) 
                ps['Z3ij'] = abs(ps['MKT_CAP'] - z3_i) 
                ps['Z4ij'] = abs(ps['IMPLIED_GROWTH'] - z4_i) 
                ps['Z5ij'] = abs(ps['EBIT_margin'] - z5_i) 
                # SARD score is the sum of absolute distances for the selection variables
                ps['SARD_score'] = ps.Z1ij + ps.Z2ij + ps.Z3ij + ps.Z4ij + ps.Z5ij
                # finding the peers based on the lowest SARD score given variables z
                temp_peers1 = ps.sort_values(['SARD_score']).copy()
                temp_peers2 = (temp_peers1.iloc[0:estimation_peers]).copy()
                peers = temp_peers2.loc[temp_peers2['GVKEY'] != i ].copy()
                # estimating the multiples from the natural peers
                PEest = stats.hmean(peers.PE_RATIO,axis=0)
                PBest = stats.hmean(peers.PB_RATIO,axis=0)
                EV_EBITest = stats.hmean(peers.EV_EBIT,axis=0)
                EV_SALESest = stats.hmean(peers.EV_SALES,axis=0)
                # populating estimation lists
                sPE.append(PEest.item())
                sPB.append(PBest.item())
                sEVEBIT.append(EV_EBITest.item())
                sEVSALES.append(EV_SALESest.item())
                # identifier population lists are also added
                sYear.append(y.item())
                sCompany.append(i)
                sGics.append(cgics2)
                sSizeid.append(cindex)
                sampleids.append(sampleid)
                ciso_ids.append(ciso_id)
    else:
        print('The data structure of the input is insufficient for the current algorithm')

    # storage of results and calculation of errors        
    # multiple error evaluation
    # store data to calculate errors
    estimations = pd.DataFrame(
            {'GVKEY': sCompany,
             'SAMPLE_ID' : sampleids,
             'CISO' : ciso_ids,
             'VALUE_YEAR' : sYear,
             'GICS_SECTOR' : sGics,
             'SIZEINDEX' : sSizeid,
             'EST_PE' : sPE,
             'EST_PB' : sPB,
             'EST_EVEBIT' : sEVEBIT,
             'EST_EVSALES' : sEVSALES,
                         })

    # realized 'true' values
    realized = X2[['GVKEY','VALUE_YEAR','PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT']].copy()
    
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
    
    # drop estimated and realized values
    errors = errors.drop(['PE_RATIO','PB_RATIO','EV_SALES','EV_EBIT','EST_PE','EST_PB','EST_EVEBIT',
                          'EST_EVSALES'],axis=1).copy()          

    print('Error measurements')
    print('PE')
    print('mean')
    print(errors.PE_error.mean())
    print('median')
    print(errors.PE_error.median())
    print('IQR')
    print(scipy.stats.iqr(errors.PE_error,axis=0))
    print('###########BREAK########')
    print('PB')
    print('mean')
    print(errors.PB_error.mean())
    print('median')
    print(errors.PB_error.median())
    print('IQR')
    print(scipy.stats.iqr(errors.PB_error,axis=0))
    print('###########BREAK########')
    print('EV_EBIT')
    print('mean')
    print(errors.EVEBIT_error.mean())
    print('median')
    print(errors.EVEBIT_error.median())
    print('IQR')
    print(scipy.stats.iqr(errors.EVEBIT_error,axis=0))
    print('###########BREAK########')
    print('EV_SALES')
    print('mean')
    print(errors.EVSALES_error.mean())
    print('median')
    print(errors.EVSALES_error.median())  
    print('IQR')
    print(scipy.stats.iqr(errors.EVSALES_error,axis=0))

    estimation_peers = str(estimation_peers)

    # writing CSV
    errors.to_csv('KKcountry_errors_'+c+'data_'+parameters+'_'+estimation_peers+'.csv',index=False)
    
    estimation_peers = int(estimation_peers)

