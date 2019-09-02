#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 09:57:47 2019

@author: emilhenningsen
"""



##### Error evaluation of peer selection models 

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
import scipy.stats
import time
import math  


# Data import
# SARD results
# all data errors
kkusard1 = pd.read_csv('KK_errors_alldata_1_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkusard2 = pd.read_csv('KK_errors_alldata_2_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkusard3 = pd.read_csv('KK_errors_alldata_3_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkusard4 = pd.read_csv('KK_errors_alldata_4_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkusard5 = pd.read_csv('KK_errors_alldata_5_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})


# global errors
kkgsard1 = pd.read_csv('KK_errors_globaldata_1_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkgsard2 = pd.read_csv('KK_errors_globaldata_2_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkgsard3 = pd.read_csv('KK_errors_globaldata_3_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkgsard4 = pd.read_csv('KK_errors_globaldata_4_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkgsard5 = pd.read_csv('KK_errors_globaldata_5_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})


# global errors
kkesard1 = pd.read_csv('KK_errors_eudata_1_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkesard2 = pd.read_csv('KK_errors_eudata_2_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkesard3 = pd.read_csv('KK_errors_eudata_3_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkesard4 = pd.read_csv('KK_errors_eudata_4_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
kkesard5 = pd.read_csv('KK_errors_eudata_5_7.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

#### industry based SARD

# Data import
# SARD results
# all data errors

indusard1 = pd.read_csv('ind_errorsall_1.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                           'GICS_SECTOR': str})
indusard2 = pd.read_csv('ind_errorsall_2.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indusard3 = pd.read_csv('ind_errorsall_3.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indusard4 = pd.read_csv('ind_errorsall_4.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indusard5 = pd.read_csv('ind_errorsall_5.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

# global errors
indgsard1 = pd.read_csv('ind_errorsglobal_1.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indgsard2 = pd.read_csv('ind_errorsglobal_2.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indgsard3 = pd.read_csv('ind_errorsglobal_3.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indgsard4 = pd.read_csv('ind_errorsglobal_4.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indgsard5 = pd.read_csv('ind_errorsglobal_5.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

# eu errors
indeusard1 = pd.read_csv('ind_errorseu_1.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indeusard2 = pd.read_csv('ind_errorseu_2.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indeusard3 = pd.read_csv('ind_errorseu_3.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indeusard4 = pd.read_csv('ind_errorseu_4.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})
indeusard5 = pd.read_csv('ind_errorseu_5.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})


# Benchmark results
usindustry_benchmark = pd.read_csv('all__errors_benchmark_R10E6.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

gindustry_benchmark = pd.read_csv('global__errors_benchmark_R10E6.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

euindustry_benchmark = pd.read_csv('eu__errors_benchmark_R10E6.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int, 'SAMPLE_ID' : str, 
                                                           'INDEXID' : str, 'CISO' : str, 'SIZEINDEX' : str,
                                                  'GICS_SECTOR': str})

# Creating new industry benchmark errors aligned with SARD output
bcols = ['SAMPLE_ID', 'CISO', 'GICS_SECTOR', 'SIZEINDEX', 'MERGE_ID', 'GVKEY',
       'VALUE_YEAR', 'PE_error', 'PB_error', 'EVSALES_error','EVEBIT_error']
us_benchmark_1 = usindustry_benchmark[bcols].copy()
g_benchmark_1 = gindustry_benchmark[bcols].copy()
e_benchmark_1 = euindustry_benchmark[bcols].copy()


############ Evaluation of errors
### Traditional SARD model
print('Error evaluation traditional SARD model')
# 1. Step: error overview
# setting up error sample identifer
# all firms sample errors
kkusard1['SAMPLE_ID'] = 'SARD1'
kkusard2['SAMPLE_ID'] = 'SARD2'
kkusard3['SAMPLE_ID'] = 'SARD3'
kkusard4['SAMPLE_ID'] = 'SARD4'
kkusard5['SAMPLE_ID'] = 'SARD5'
us_benchmark_1['SAMPLE_ID'] = 'Benchmark'

# global sample errors
kkgsard1['SAMPLE_ID'] = 'SARD1'
kkgsard2['SAMPLE_ID'] = 'SARD2'
kkgsard3['SAMPLE_ID'] = 'SARD3'
kkgsard4['SAMPLE_ID'] = 'SARD4'
kkgsard5['SAMPLE_ID'] = 'SARD5'
g_benchmark_1['SAMPLE_ID'] = 'Benchmark'

# global sample errors
kkesard1['SAMPLE_ID'] = 'SARD1'
kkesard2['SAMPLE_ID'] = 'SARD2'
kkesard3['SAMPLE_ID'] = 'SARD3'
kkesard4['SAMPLE_ID'] = 'SARD4'
kkesard5['SAMPLE_ID'] = 'SARD5'
e_benchmark_1['SAMPLE_ID'] = 'Benchmark'

# creating the total dataset with all company-year observation 
# us sample errors
udfs = [kkusard1,kkusard2,kkusard3,kkusard4,kkusard5]
tkkusard = us_benchmark_1.append(udfs, ignore_index=True)
# global sample errors
gdfs = [kkgsard1,kkgsard2,kkgsard3,kkgsard4,kkgsard5]
tkkgsard = g_benchmark_1.append(gdfs, ignore_index=True)
# global sample errors
edfs = [kkesard1,kkesard2,kkesard3,kkesard4,kkesard5]
tkkesard = e_benchmark_1.append(edfs, ignore_index=True)

eve = 'EVEBIT_error'

# All data
# EVEBIT
# IND
uevediff01 = us_benchmark_1[eve] - kkusard1[eve]
uevediff02 = us_benchmark_1[eve] - kkusard2[eve]
uevediff03 = us_benchmark_1[eve] - kkusard3[eve]
uevediff04 = us_benchmark_1[eve] - kkusard4[eve]
uevediff05 = us_benchmark_1[eve] - kkusard5[eve]
    
#SARD1
uevediff10 = kkusard1[eve] - us_benchmark_1[eve]
uevediff12 = kkusard1[eve] - kkusard2[eve]
uevediff13 = kkusard1[eve] - kkusard3[eve]
uevediff14 = kkusard1[eve] - kkusard4[eve]
uevediff15 = kkusard1[eve] - kkusard5[eve]
    
# SARD2
uevediff20 = kkusard2[eve] - us_benchmark_1[eve]
uevediff21 = kkusard2[eve] - kkusard1[eve]
uevediff23 = kkusard2[eve] - kkusard3[eve]
uevediff24 = kkusard2[eve] - kkusard4[eve]
uevediff25 = kkusard2[eve] - kkusard5[eve]

# SARD3
uevediff30 = kkusard3[eve] - us_benchmark_1[eve]
uevediff32 = kkusard3[eve] - kkusard2[eve]
uevediff31 = kkusard3[eve] - kkusard1[eve]
uevediff34 = kkusard3[eve] - kkusard4[eve]
uevediff35 = kkusard3[eve] - kkusard5[eve]
    
# SARD4
uevediff40 = kkusard4[eve] - us_benchmark_1[eve]
uevediff42 = kkusard4[eve] - kkusard2[eve]
uevediff43 = kkusard4[eve] - kkusard3[eve]
uevediff41 = kkusard4[eve] - kkusard1[eve]
uevediff45 = kkusard4[eve] - kkusard5[eve]
 
# SARD5
uevediff50 = kkusard5[eve] - us_benchmark_1[eve]
uevediff52 = kkusard5[eve] - kkusard2[eve]
uevediff53 = kkusard5[eve] - kkusard3[eve]
uevediff54 = kkusard5[eve] - kkusard4[eve]
uevediff51 = kkusard5[eve] - kkusard1[eve]
    
uevediffs = [
         uevediff01, uevediff02, uevediff03, uevediff04, uevediff05, 
         uevediff10, uevediff12, uevediff13, uevediff14, uevediff15, 
         uevediff20, uevediff21, uevediff23, uevediff24, uevediff25, 
         uevediff30, uevediff31, uevediff32, uevediff34, uevediff35, 
         uevediff40, uevediff41, uevediff42, uevediff43, uevediff45, 
         uevediff50, uevediff51, uevediff52, uevediff53, uevediff54, 
         ]
uevediffs_index = [
         'uevediff01', 'uevediff02', 'uevediff03', 'uevediff04', 'uevediff05', 
         'uevediff10', 'uevediff12', 'uevediff13', 'uevediff14', 'uevediff15', 
         'uevediff20', 'uevediff21', 'uevediff23', 'uevediff24', 'uevediff25', 
         'uevediff30', 'uevediff31', 'uevediff32', 'uevediff34', 'uevediff35', 
         'uevediff40', 'uevediff41', 'uevediff42', 'uevediff43', 'uevediff45', 
         'uevediff50', 'uevediff51', 'uevediff52', 'uevediff53', 'uevediff54', 
         ]

# Global data
# EVEBIT
# IND
gevediff01 = g_benchmark_1[eve] - kkgsard1[eve]
gevediff02 = g_benchmark_1[eve] - kkgsard2[eve]
gevediff03 = g_benchmark_1[eve] - kkgsard3[eve]
gevediff04 = g_benchmark_1[eve] - kkgsard4[eve]
gevediff05 = g_benchmark_1[eve] - kkgsard5[eve]

#SARD1
gevediff10 = kkgsard1[eve] - g_benchmark_1[eve]
gevediff12 = kkgsard1[eve] - kkgsard2[eve]
gevediff13 = kkgsard1[eve] - kkgsard3[eve]
gevediff14 = kkgsard1[eve] - kkgsard4[eve]
gevediff15 = kkgsard1[eve] - kkgsard5[eve]

# SARD2
gevediff20 = kkgsard2[eve] - g_benchmark_1[eve]
gevediff21 = kkgsard2[eve] - kkgsard1[eve]
gevediff23 = kkgsard2[eve] - kkgsard3[eve]
gevediff24 = kkgsard2[eve] - kkgsard4[eve]
gevediff25 = kkgsard2[eve] - kkgsard5[eve]

# SARD3
gevediff30 = kkgsard3[eve] - g_benchmark_1[eve]
gevediff32 = kkgsard3[eve] - kkgsard2[eve]
gevediff31 = kkgsard3[eve] - kkgsard1[eve]
gevediff34 = kkgsard3[eve] - kkgsard4[eve]
gevediff35 = kkgsard3[eve] - kkgsard5[eve]

# SARD4
gevediff40 = kkgsard4[eve] - g_benchmark_1[eve]
gevediff42 = kkgsard4[eve] - kkgsard2[eve]
gevediff43 = kkgsard4[eve] - kkgsard3[eve]
gevediff41 = kkgsard4[eve] - kkgsard1[eve]
gevediff45 = kkgsard4[eve] - kkgsard5[eve]
    
# SARD5
gevediff50 = kkgsard5[eve] - g_benchmark_1[eve]
gevediff52 = kkgsard5[eve] - kkgsard2[eve]
gevediff53 = kkgsard5[eve] - kkgsard3[eve]
gevediff54 = kkgsard5[eve] - kkgsard4[eve]
gevediff51 = kkgsard5[eve] - kkgsard1[eve]

gevediffs = [
         gevediff01, gevediff02, gevediff03, gevediff04, gevediff05, 
         gevediff10, gevediff12, gevediff13, gevediff14, gevediff15, 
         gevediff20, gevediff21, gevediff23, gevediff24, gevediff25, 
         gevediff30, gevediff31, gevediff32, gevediff34, gevediff35,
         gevediff40, gevediff41, gevediff42, gevediff43, gevediff45, 
         gevediff50, gevediff51, gevediff52, gevediff53, gevediff54, 
         ]

gevediffs_index = [
         'gevediff01', 'gevediff02', 'gevediff03', 'gevediff04', 'gevediff05', 
         'gevediff10', 'gevediff12', 'gevediff13', 'gevediff14', 'gevediff15', 
         'gevediff20', 'gevediff21', 'gevediff23', 'gevediff24', 'gevediff25', 
         'gevediff30', 'gevediff31', 'gevediff32', 'gevediff34', 'gevediff35',
         'gevediff40', 'gevediff41', 'gevediff42', 'gevediff43', 'gevediff45', 
         'gevediff50', 'gevediff51', 'gevediff52', 'gevediff53', 'gevediff54', 
         ]

# EU data
# EVEBIT
# IND
eevediff01 = e_benchmark_1[eve] - kkesard1[eve]
eevediff02 = e_benchmark_1[eve] - kkesard2[eve]
eevediff03 = e_benchmark_1[eve] - kkesard3[eve]
eevediff04 = e_benchmark_1[eve] - kkesard4[eve]
eevediff05 = e_benchmark_1[eve] - kkesard5[eve]

#SARD1
eevediff10 = kkesard1[eve] - e_benchmark_1[eve]
eevediff12 = kkesard1[eve] - kkesard2[eve]
eevediff13 = kkesard1[eve] - kkesard3[eve]
eevediff14 = kkesard1[eve] - kkesard4[eve]
eevediff15 = kkesard1[eve] - kkesard5[eve]

# SARD2
eevediff20 = kkesard2[eve] - e_benchmark_1[eve]
eevediff21 = kkesard2[eve] - kkesard1[eve]
eevediff23 = kkesard2[eve] - kkesard3[eve]
eevediff24 = kkesard2[eve] - kkesard4[eve]
eevediff25 = kkesard2[eve] - kkesard5[eve]

# SARD3
eevediff30 = kkesard3[eve] - e_benchmark_1[eve]
eevediff32 = kkesard3[eve] - kkesard2[eve]
eevediff31 = kkesard3[eve] - kkesard1[eve]
eevediff34 = kkesard3[eve] - kkesard4[eve]
eevediff35 = kkesard3[eve] - kkesard5[eve]

# SARD4
eevediff40 = kkesard4[eve] - e_benchmark_1[eve]
eevediff42 = kkesard4[eve] - kkesard2[eve]
eevediff43 = kkesard4[eve] - kkesard3[eve]
eevediff41 = kkesard4[eve] - kkesard1[eve]
eevediff45 = kkesard4[eve] - kkesard5[eve]
    
# SARD5
eevediff50 = kkesard5[eve] - e_benchmark_1[eve]
eevediff52 = kkesard5[eve] - kkesard2[eve]
eevediff53 = kkesard5[eve] - kkesard3[eve]
eevediff54 = kkesard5[eve] - kkesard4[eve]
eevediff51 = kkesard5[eve] - kkesard1[eve]

eevediffs = [
         eevediff01, eevediff02, eevediff03, eevediff04, eevediff05, 
         eevediff10, eevediff12, eevediff13, eevediff14, eevediff15, 
         eevediff20, eevediff21, eevediff23, eevediff24, eevediff25, 
         eevediff30, eevediff31, eevediff32, eevediff34, eevediff35,
         eevediff40, eevediff41, eevediff42, eevediff43, eevediff45, 
         eevediff50, eevediff51, eevediff52, eevediff53, eevediff54, 
         ]

eevediffs_index = [
         'eevediff01', 'eevediff02', 'eevediff03', 'eevediff04', 'eevediff05', 
         'eevediff10', 'eevediff12', 'eevediff13', 'eevediff14', 'eevediff15', 
         'eevediff20', 'eevediff21', 'eevediff23', 'eevediff24', 'eevediff25', 
         'eevediff30', 'eevediff31', 'eevediff32', 'eevediff34', 'eevediff35',
         'eevediff40', 'eevediff41', 'eevediff42', 'eevediff43', 'eevediff45', 
         'eevediff50', 'eevediff51', 'eevediff52', 'eevediff53', 'eevediff54', 
         ]



# distribution

sevebit = uevediff51

#evebit
qqplot(sevebit, line='s',color='lightblue', label='Pairwise errors - QQ plot')
plt.tight_layout()
plt.savefig('qq_plots_all_evebit51.png')
plt.show()

print('JB test for normality')
print(stats.jarque_bera(sevebit))

# evebit
sns.distplot(sevebit, hist=True, kde=True, 
             bins=140, color = 'red', 
             hist_kws={'edgecolor':'pink'},
             kde_kws={'linewidth': 1})
plt.tight_layout()
plt.savefig('dist_plots_all_evebit51.png')
plt.show()

#### sub plot attempt

fig, axs = plt.subplots(2, sharex=False, sharey=False, figsize=(11,11))

g1 = qqplot(sevebit, line='s', color='lightblue', ax=axs[0])

g2 = sns.distplot(sevebit, hist=True, kde=True, 
             bins=140, color = 'red', 
             hist_kws={'edgecolor':'pink'},
             kde_kws={'linewidth': 1},
             ax=axs[1])

plt.show()

del (fig, axs, sevebit)

# hypothesis testing   
# I test on the various selection models within us and global sample.
# I look into the whether the difference between the paired errors for each model is higher/lower than the former.
# Systematic approach

# Test matrix
# above diagonal wilcoxon
# below whitney

#        0      1     2       3     4       5
#       IND   SARD1  SARD2  SARD3  SARD4   SARD5

#0 IND          x      x     x       x       x     
 
#1 SARD1   x           x     x       x       x

#2 SARD2   x    x            x       x       x

#3 SARD3   x    x      x             x       x 

#4 SARD4   x    x      x     x               x  

#5 SARD5   x    x      x     x       x  

# Non parametic tests

#The Wilcoxon signed-rank test tests the null hypothesis that two related paired samples come from the same distribution.
#In particular, it tests whether the distribution of the differences x - y is symmetric about zero.
#It is a non-parametric version of the paired T-test.

# source: statistics for business and economics by Newbold, Carson and Thorne
# p. 624-626

# critical values
# 1.645 at 0.05
# 1.930 at 0.025
# 2.36 at 0.01

# input data consists of the pairwise difference between models

#IND
#01, 02, 03, 04, 05 denote benchmark vs. all SARD models
# SARD1
#10, 12, 13, 14, 15 denote SARD1 vs. SARD models and benchmark 
# and vice versa
# all denoted diff...

####### Function to conduct wilcoxon signed rank test for greater and lesser respectively
# n will be corrected so that I only look at the non-zero pairwise differences

# E(T) = mu_T = n(n+1) / 4
# Var(T) = sigma_T^2 = (n(n+1)(2n+1)) / 24

# (T - E(T)) / sigma < -z_a

def wtest_greater(x):
    E_t = (len(x[x != 0]) * (len(x[x != 0]) + 1)) / 4 # expected value of length of non-zero differences
    sigma_t = math.sqrt((len(x[x != 0]) * (len(x[x != 0]) +1) * ((2*len(x[x != 0]) + 1))) / 24) # variance 
    x = x.replace(0, np.nan).copy() # zero differences are removed from the smaple
    x_sign = np.sign(x).copy() # signs to conduct the signed rank
    ax = abs(x).copy() # absolute differences
    sr_x = ax.rank(method='average',ascending=True) * x_sign # ranking of abs difference
    wg = sr_x[sr_x > 0].sum().copy() # investigating greater (i.e. postive differences) in the sample
    zg = (wg - E_t) / sigma_t # Z value for t-test
    p_val = scipy.stats.norm.sf(abs(zg))*2 #two-sided
    return wg, zg, p_val


# loop over the series of pairwise differences for the specific multiple selection models:

# greater hypothesis test -> the positive differences are larger than the negative differences 
# --> the median error of the i'th selection model is larger than the j'th selection model 
# (i.e. pair diff model_i - model_j)

## All
# EVEBIT

Ws = []
Zs = []
p_vals = []

alpha = 0.05

i = 0

for s in uevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(uevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    wg, zg, p_val = wtest_greater(s)
    print('Statistics=%.3f, z-test=%.3f ,p=%.3f' % (wg, zg, p_val))
    if p_val > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different centrality of error (reject H0)')
    # appending results to the stored data
    Ws.append(wg)
    Zs.append(zg)
    p_vals.append(p_val)
    i = i + 1

# Summary of the greater than one-sided Wilcoxon test
ueve_great_pair_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': uevediffs_index,
     'W_TEST' : Ws,
     'Z_TEST' : Zs,
     'P_VAL' : p_vals
  })   
    
del s, p_vals, Ws, Zs
    
ueve_great_pair_diff_eval['SIG90'] = 1.645
ueve_great_pair_diff_eval['SIG95'] = 1.960
ueve_great_pair_diff_eval['SIG98'] = 2.326
ueve_great_pair_diff_eval['SIGN'] = np.sign(ueve_great_pair_diff_eval.Z_TEST).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (ueve_great_pair_diff_eval['SIGN'] == -1) & (ueve_great_pair_diff_eval['P_VAL'] < 0.01),
    (ueve_great_pair_diff_eval['SIGN'] == -1) & (ueve_great_pair_diff_eval['P_VAL'] > 0.01) & (ueve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (ueve_great_pair_diff_eval['SIGN'] == -1) & (ueve_great_pair_diff_eval['P_VAL'] > 0.05),
    (ueve_great_pair_diff_eval['SIGN'] == 1) & (ueve_great_pair_diff_eval['P_VAL'] < 0.01),
    (ueve_great_pair_diff_eval['SIGN'] == 1) & (ueve_great_pair_diff_eval['P_VAL'] > 0.01) & (ueve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (ueve_great_pair_diff_eval['SIGN'] == 1) & (ueve_great_pair_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

ueve_great_pair_diff_eval['HMAP_ID'] = np.select(conditions, choices)

# Global
Ws = []
Zs = []
p_vals = []

alpha = 0.05

i = 0

for s in gevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(gevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    wg, zg, p_val = wtest_greater(s)
    print('Statistics=%.3f, z-test=%.3f ,p=%.3f' % (wg, zg, p_val))
    if p_val > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different centrality of error (reject H0)')
    # appending results to the stored data
    Ws.append(wg)
    Zs.append(zg)
    p_vals.append(p_val)
    i = i + 1

# Summary of the greater than one-sided Wilcoxon test
geve_great_pair_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': gevediffs_index,
     'W_TEST' : Ws,
     'Z_TEST' : Zs,
     'P_VAL' : p_vals
  })   
    
del s, p_vals, Ws, Zs
    
geve_great_pair_diff_eval['SIG90'] = 1.645
geve_great_pair_diff_eval['SIG95'] = 1.960
geve_great_pair_diff_eval['SIG98'] = 2.326
geve_great_pair_diff_eval['SIGN'] = np.sign(geve_great_pair_diff_eval.Z_TEST).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (geve_great_pair_diff_eval['SIGN'] == -1) & (geve_great_pair_diff_eval['P_VAL'] < 0.01),
    (geve_great_pair_diff_eval['SIGN'] == -1) & (geve_great_pair_diff_eval['P_VAL'] > 0.01) & (geve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (geve_great_pair_diff_eval['SIGN'] == -1) & (geve_great_pair_diff_eval['P_VAL'] > 0.05),
    (geve_great_pair_diff_eval['SIGN'] == 1) & (geve_great_pair_diff_eval['P_VAL'] < 0.01),
    (geve_great_pair_diff_eval['SIGN'] == 1) & (geve_great_pair_diff_eval['P_VAL'] > 0.01) & (geve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (geve_great_pair_diff_eval['SIGN'] == 1) & (geve_great_pair_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

geve_great_pair_diff_eval['HMAP_ID'] = np.select(conditions, choices)


# EU data
Ws = []
Zs = []
p_vals = []

alpha = 0.05

i = 0

for s in eevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(eevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    wg, zg, p_val = wtest_greater(s)
    print('Statistics=%.3f, z-test=%.3f ,p=%.3f' % (wg, zg, p_val))
    if p_val > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different centrality of error (reject H0)')
    # appending results to the stored data
    Ws.append(wg)
    Zs.append(zg)
    p_vals.append(p_val)
    i = i + 1

# Summary of the greater than one-sided Wilcoxon test
eeve_great_pair_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': eevediffs_index,
     'W_TEST' : Ws,
     'Z_TEST' : Zs,
     'P_VAL' : p_vals
  })   
    
del s, p_vals, Ws, Zs
    
eeve_great_pair_diff_eval['SIG90'] = 1.645
eeve_great_pair_diff_eval['SIG95'] = 1.960
eeve_great_pair_diff_eval['SIG98'] = 2.326
eeve_great_pair_diff_eval['SIGN'] = np.sign(eeve_great_pair_diff_eval.Z_TEST).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (eeve_great_pair_diff_eval['SIGN'] == -1) & (eeve_great_pair_diff_eval['P_VAL'] < 0.01),
    (eeve_great_pair_diff_eval['SIGN'] == -1) & (eeve_great_pair_diff_eval['P_VAL'] > 0.01) & (eeve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (eeve_great_pair_diff_eval['SIGN'] == -1) & (eeve_great_pair_diff_eval['P_VAL'] > 0.05),
    (eeve_great_pair_diff_eval['SIGN'] == 1) & (eeve_great_pair_diff_eval['P_VAL'] < 0.01),
    (eeve_great_pair_diff_eval['SIGN'] == 1) & (eeve_great_pair_diff_eval['P_VAL'] > 0.01) & (eeve_great_pair_diff_eval['P_VAL'] < 0.05) ,
    (eeve_great_pair_diff_eval['SIGN'] == 1) & (eeve_great_pair_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

eeve_great_pair_diff_eval['HMAP_ID'] = np.select(conditions, choices)



# t-test of mean pairwise differences
# if we consider the pairwise difference vector it is generally skewed with fat tails (i.e. outliers)
# however, due to the central limit theorem the distirbution of the mean will be approximately normally distiributed 
# through the central limit theorem
# p. 387-390

# Two means, dependent samples, known population variances

# H_0 : mu_x - mu_y = 0 or mu_x - mu_y <= 0
# H1 : mu_x - mu_y > 0

# interpretation: H0 acceptance --> no difference between model performance on the pairwise difference estimation errors
# H1 indicates that the prior model (x) is less accurate than the newer model (y)

# decision rule
# reject H0 if
# d_bar / (s_d / sqrt(n)) > t_n-1,a

# critical values
# 1.645 at 0.05 (10%)
# 1.930 at 0.025 (5%)
# 2.36 at 0.01 (1%)

def diff_pair_means(x):
    d_bar = x.mean()
    sd = x.std()
    n = math.sqrt(len(x))
    t = d_bar / (sd / n)
    p_valx = stats.t.sf(np.abs(t), len(x)-1)*2 # two-sided
    return t, p_valx


# All

ts = []
p_vals2 = []

alpha = 0.05

i = 0

for s in uevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(uevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    t, p_valx = diff_pair_means(s)
    print('Statistics=%.3f, p=%.3f' % (t, p_valx))
    if p_valx > alpha:
        print('Same mean (fail to reject H0)')
    else:
        print('Mean difference is different from zero (reject H0)')
    # appending results to the stored data
    ts.append(t)
    p_vals2.append(p_valx)
    i = i + 1

del s

# Summary of the different mean t-test (H0 mean of matched pairs not different from zero i.e. no difference among models)
ueve_mean_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': uevediffs_index,
     'TEST_SIZE' : ts,
     'P_VAL' : p_vals2
  })   

ueve_mean_diff_eval['SIG90'] = 1.645
ueve_mean_diff_eval['SIG95'] = 1.960
ueve_mean_diff_eval['SIG98'] = 2.326
ueve_mean_diff_eval['SIGN'] = np.sign(ueve_mean_diff_eval.TEST_SIZE).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (ueve_mean_diff_eval['SIGN'] == -1) & (ueve_mean_diff_eval['P_VAL'] < 0.01),
    (ueve_mean_diff_eval['SIGN'] == -1) & (ueve_mean_diff_eval['P_VAL'] > 0.01) & (ueve_mean_diff_eval['P_VAL'] < 0.05) ,
    (ueve_mean_diff_eval['SIGN'] == -1) & (ueve_mean_diff_eval['P_VAL'] > 0.05),
    (ueve_mean_diff_eval['SIGN'] == 1) & (ueve_mean_diff_eval['P_VAL'] < 0.01),
    (ueve_mean_diff_eval['SIGN'] == 1) & (ueve_mean_diff_eval['P_VAL'] > 0.01) & (ueve_mean_diff_eval['P_VAL'] < 0.05) ,
    (ueve_mean_diff_eval['SIGN'] == 1) & (ueve_mean_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

ueve_mean_diff_eval['HMAP_ID'] = np.select(conditions, choices)


# Global

ts = []
p_vals2 = []

alpha = 0.05

i = 0

for s in gevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(gevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    t, p_valx = diff_pair_means(s)
    print('Statistics=%.3f, p=%.3f' % (t, p_valx))
    if p_valx > alpha:
        print('Same mean (fail to reject H0)')
    else:
        print('Mean difference is different from zero (reject H0)')
    # appending results to the stored data
    ts.append(t)
    p_vals2.append(p_valx)
    i = i + 1

del s

# Summary of the different mean t-test (H0 mean of matched pairs not different from zero i.e. no difference among models)
geve_mean_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': gevediffs_index,
     'TEST_SIZE' : ts,
     'P_VAL' : p_vals2
  })   

geve_mean_diff_eval['SIG90'] = 1.645
geve_mean_diff_eval['SIG95'] = 1.960
geve_mean_diff_eval['SIG98'] = 2.326
geve_mean_diff_eval['SIGN'] = np.sign(geve_mean_diff_eval.TEST_SIZE).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (geve_mean_diff_eval['SIGN'] == -1) & (geve_mean_diff_eval['P_VAL'] < 0.01),
    (geve_mean_diff_eval['SIGN'] == -1) & (geve_mean_diff_eval['P_VAL'] > 0.01) & (geve_mean_diff_eval['P_VAL'] < 0.05) ,
    (geve_mean_diff_eval['SIGN'] == -1) & (geve_mean_diff_eval['P_VAL'] > 0.05),
    (geve_mean_diff_eval['SIGN'] == 1) & (geve_mean_diff_eval['P_VAL'] < 0.01),
    (geve_mean_diff_eval['SIGN'] == 1) & (geve_mean_diff_eval['P_VAL'] > 0.01) & (geve_mean_diff_eval['P_VAL'] < 0.05) ,
    (geve_mean_diff_eval['SIGN'] == 1) & (geve_mean_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

geve_mean_diff_eval['HMAP_ID'] = np.select(conditions, choices)

# EU data

ts = []
p_vals2 = []

alpha = 0.05

i = 0

for s in eevediffs:
    # printing the error eval conducted
    print('Pairwise difference analyzed and tested: ')
    print(eevediffs_index[i])
    # performing the greater than wilcoxon test as defined above
    t, p_valx = diff_pair_means(s)
    print('Statistics=%.3f, p=%.3f' % (t, p_valx))
    if p_valx > alpha:
        print('Same mean (fail to reject H0)')
    else:
        print('Mean difference is different from zero (reject H0)')
    # appending results to the stored data
    ts.append(t)
    p_vals2.append(p_valx)
    i = i + 1

del s

# Summary of the different mean t-test (H0 mean of matched pairs not different from zero i.e. no difference among models)
eeve_mean_diff_eval = pd.DataFrame(
    {'MODELVSMODEL': eevediffs_index,
     'TEST_SIZE' : ts,
     'P_VAL' : p_vals2
  })   

eeve_mean_diff_eval['SIG90'] = 1.645
eeve_mean_diff_eval['SIG95'] = 1.960
eeve_mean_diff_eval['SIG98'] = 2.326
eeve_mean_diff_eval['SIGN'] = np.sign(eeve_mean_diff_eval.TEST_SIZE).copy()

# creating new column with input data for heatmaps
# setting up condition boudary
conditions = [
    (eeve_mean_diff_eval['SIGN'] == -1) & (eeve_mean_diff_eval['P_VAL'] < 0.01),
    (eeve_mean_diff_eval['SIGN'] == -1) & (eeve_mean_diff_eval['P_VAL'] > 0.01) & (eeve_mean_diff_eval['P_VAL'] < 0.05) ,
    (eeve_mean_diff_eval['SIGN'] == -1) & (eeve_mean_diff_eval['P_VAL'] > 0.05),
    (eeve_mean_diff_eval['SIGN'] == 1) & (eeve_mean_diff_eval['P_VAL'] < 0.01),
    (eeve_mean_diff_eval['SIGN'] == 1) & (eeve_mean_diff_eval['P_VAL'] > 0.01) & (eeve_mean_diff_eval['P_VAL'] < 0.05) ,
    (eeve_mean_diff_eval['SIGN'] == 1) & (eeve_mean_diff_eval['P_VAL'] > 0.05)]
# choices matching the conditions
choices = [-2, -1 , 0, 2, 1, 0]

eeve_mean_diff_eval['HMAP_ID'] = np.select(conditions, choices)


# deleting individual diffs
del [
     uevediff01, uevediff02, uevediff03, uevediff04, uevediff05, 
     uevediff10, uevediff12, uevediff13, uevediff14, uevediff15, 
     uevediff20, uevediff21, uevediff23, uevediff24, uevediff25, 
     uevediff30, uevediff31, uevediff32, uevediff34, uevediff35, 
     uevediff40, uevediff41, uevediff42, uevediff43, uevediff45, 
     uevediff50, uevediff51, uevediff52, uevediff53, uevediff54, 
     ]


# deleting individual diffs
del [
     gevediff01, gevediff02, gevediff03, gevediff04, gevediff05, 
     gevediff10, gevediff12, gevediff13, gevediff14, gevediff15, 
     gevediff20, gevediff21, gevediff23, gevediff24, gevediff25, 
     gevediff30, gevediff31, gevediff32, gevediff34, gevediff35, 
     gevediff40, gevediff41, gevediff42, gevediff43, gevediff45, 
     gevediff50, gevediff51, gevediff52, gevediff53, gevediff54, 
     ]

# deleting individual diffs
del [
     eevediff01, eevediff02, eevediff03, eevediff04, eevediff05, 
     eevediff10, eevediff12, eevediff13, eevediff14, eevediff15, 
     eevediff20, eevediff21, eevediff23, eevediff24, eevediff25, 
     eevediff30, eevediff31, eevediff32, eevediff34, eevediff35, 
     eevediff40, eevediff41, eevediff42, eevediff43, eevediff45, 
     eevediff50, eevediff51, eevediff52, eevediff53, eevediff54, 
     ]

# constructing output dataframe
# wilcoxon test
# All
uweve01 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff01'].HMAP_ID.item()
uweve02 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff02'].HMAP_ID.item()
uweve03 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff03'].HMAP_ID.item()
uweve04 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff04'].HMAP_ID.item()
uweve05 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff05'].HMAP_ID.item()

uweve10 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff10'].HMAP_ID.item()
uweve12 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff12'].HMAP_ID.item()
uweve13 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff13'].HMAP_ID.item()
uweve14 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff14'].HMAP_ID.item()
uweve15 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff15'].HMAP_ID.item()

uweve20 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff20'].HMAP_ID.item()
uweve21 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff21'].HMAP_ID.item()
uweve23 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff23'].HMAP_ID.item()
uweve24 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff24'].HMAP_ID.item()
uweve25 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff25'].HMAP_ID.item()

uweve30 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff30'].HMAP_ID.item()
uweve32 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff32'].HMAP_ID.item()
uweve31 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff31'].HMAP_ID.item()
uweve34 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff34'].HMAP_ID.item()
uweve35 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff35'].HMAP_ID.item()

uweve40 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff40'].HMAP_ID.item()
uweve42 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff42'].HMAP_ID.item()
uweve43 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff43'].HMAP_ID.item()
uweve41 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff41'].HMAP_ID.item()
uweve45 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff45'].HMAP_ID.item()

uweve50 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff50'].HMAP_ID.item()
uweve52 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff52'].HMAP_ID.item()
uweve53 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff53'].HMAP_ID.item()
uweve54 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff54'].HMAP_ID.item()
uweve51 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff51'].HMAP_ID.item()

# Global
gweve01 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff01'].HMAP_ID.item()
gweve02 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff02'].HMAP_ID.item()
gweve03 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff03'].HMAP_ID.item()
gweve04 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff04'].HMAP_ID.item()
gweve05 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff05'].HMAP_ID.item()

gweve10 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff10'].HMAP_ID.item()
gweve12 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff12'].HMAP_ID.item()
gweve13 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff13'].HMAP_ID.item()
gweve14 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff14'].HMAP_ID.item()
gweve15 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff15'].HMAP_ID.item()

gweve20 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff20'].HMAP_ID.item()
gweve21 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff21'].HMAP_ID.item()
gweve23 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff23'].HMAP_ID.item()
gweve24 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff24'].HMAP_ID.item()
gweve25 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff25'].HMAP_ID.item()

gweve30 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff30'].HMAP_ID.item()
gweve32 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff32'].HMAP_ID.item()
gweve31 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff31'].HMAP_ID.item()
gweve34 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff34'].HMAP_ID.item()
gweve35 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff35'].HMAP_ID.item()

gweve40 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff40'].HMAP_ID.item()
gweve42 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff42'].HMAP_ID.item()
gweve43 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff43'].HMAP_ID.item()
gweve41 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff41'].HMAP_ID.item()
gweve45 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff45'].HMAP_ID.item()

gweve50 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff50'].HMAP_ID.item()
gweve52 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff52'].HMAP_ID.item()
gweve53 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff53'].HMAP_ID.item()
gweve54 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff54'].HMAP_ID.item()
gweve51 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff51'].HMAP_ID.item()

# EU
eweve01 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff01'].HMAP_ID.item()
eweve02 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff02'].HMAP_ID.item()
eweve03 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff03'].HMAP_ID.item()
eweve04 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff04'].HMAP_ID.item()
eweve05 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff05'].HMAP_ID.item()

eweve10 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff10'].HMAP_ID.item()
eweve12 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff12'].HMAP_ID.item()
eweve13 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff13'].HMAP_ID.item()
eweve14 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff14'].HMAP_ID.item()
eweve15 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff15'].HMAP_ID.item()

eweve20 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff20'].HMAP_ID.item()
eweve21 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff21'].HMAP_ID.item()
eweve23 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff23'].HMAP_ID.item()
eweve24 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff24'].HMAP_ID.item()
eweve25 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff25'].HMAP_ID.item()

eweve30 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff30'].HMAP_ID.item()
eweve32 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff32'].HMAP_ID.item()
eweve31 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff31'].HMAP_ID.item()
eweve34 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff34'].HMAP_ID.item()
eweve35 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff35'].HMAP_ID.item()

eweve40 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff40'].HMAP_ID.item()
eweve42 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff42'].HMAP_ID.item()
eweve43 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff43'].HMAP_ID.item()
eweve41 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff41'].HMAP_ID.item()
eweve45 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff45'].HMAP_ID.item()

eweve50 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff50'].HMAP_ID.item()
eweve52 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff52'].HMAP_ID.item()
eweve53 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff53'].HMAP_ID.item()
eweve54 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff54'].HMAP_ID.item()
eweve51 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff51'].HMAP_ID.item()

# t-tests
# ALL

uteve01 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff01'].HMAP_ID.item()
uteve02 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff02'].HMAP_ID.item()
uteve03 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff03'].HMAP_ID.item()
uteve04 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff04'].HMAP_ID.item()
uteve05 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff05'].HMAP_ID.item()

uteve10 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff10'].HMAP_ID.item()
uteve12 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff12'].HMAP_ID.item()
uteve13 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff13'].HMAP_ID.item()
uteve14 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff14'].HMAP_ID.item()
uteve15 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff15'].HMAP_ID.item()

uteve20 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff20'].HMAP_ID.item()
uteve21 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff21'].HMAP_ID.item()
uteve23 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff23'].HMAP_ID.item()
uteve24 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff24'].HMAP_ID.item()
uteve25 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff25'].HMAP_ID.item()

uteve30 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff30'].HMAP_ID.item()
uteve32 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff32'].HMAP_ID.item()
uteve31 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff31'].HMAP_ID.item()
uteve34 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff34'].HMAP_ID.item()
uteve35 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff35'].HMAP_ID.item()

uteve40 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff40'].HMAP_ID.item()
uteve42 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff42'].HMAP_ID.item()
uteve43 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff43'].HMAP_ID.item()
uteve41 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff41'].HMAP_ID.item()
uteve45 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff45'].HMAP_ID.item()

uteve50 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff50'].HMAP_ID.item()
uteve52 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff52'].HMAP_ID.item()
uteve53 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff53'].HMAP_ID.item()
uteve54 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff54'].HMAP_ID.item()
uteve51 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff51'].HMAP_ID.item()

# Global
gteve01 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff01'].HMAP_ID.item()
gteve02 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff02'].HMAP_ID.item()
gteve03 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff03'].HMAP_ID.item()
gteve04 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff04'].HMAP_ID.item()
gteve05 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff05'].HMAP_ID.item()

gteve10 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff10'].HMAP_ID.item()
gteve12 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff12'].HMAP_ID.item()
gteve13 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff13'].HMAP_ID.item()
gteve14 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff14'].HMAP_ID.item()
gteve15 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff15'].HMAP_ID.item()

gteve20 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff20'].HMAP_ID.item()
gteve21 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff21'].HMAP_ID.item()
gteve23 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff23'].HMAP_ID.item()
gteve24 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff24'].HMAP_ID.item()
gteve25 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff25'].HMAP_ID.item()

gteve30 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff30'].HMAP_ID.item()
gteve32 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff32'].HMAP_ID.item()
gteve31 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff31'].HMAP_ID.item()
gteve34 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff34'].HMAP_ID.item()
gteve35 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff35'].HMAP_ID.item()

gteve40 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff40'].HMAP_ID.item()
gteve42 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff42'].HMAP_ID.item()
gteve43 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff43'].HMAP_ID.item()
gteve41 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff41'].HMAP_ID.item()
gteve45 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff45'].HMAP_ID.item()

gteve50 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff50'].HMAP_ID.item()
gteve52 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff52'].HMAP_ID.item()
gteve53 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff53'].HMAP_ID.item()
gteve54 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff54'].HMAP_ID.item()
gteve51 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff51'].HMAP_ID.item()

# EU
eteve01 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff01'].HMAP_ID.item()
eteve02 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff02'].HMAP_ID.item()
eteve03 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff03'].HMAP_ID.item()
eteve04 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff04'].HMAP_ID.item()
eteve05 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff05'].HMAP_ID.item()

eteve10 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff10'].HMAP_ID.item()
eteve12 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff12'].HMAP_ID.item()
eteve13 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff13'].HMAP_ID.item()
eteve14 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff14'].HMAP_ID.item()
eteve15 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff15'].HMAP_ID.item()

eteve20 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff20'].HMAP_ID.item()
eteve21 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff21'].HMAP_ID.item()
eteve23 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff23'].HMAP_ID.item()
eteve24 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff24'].HMAP_ID.item()
eteve25 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff25'].HMAP_ID.item()

eteve30 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff30'].HMAP_ID.item()
eteve32 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff32'].HMAP_ID.item()
eteve31 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff31'].HMAP_ID.item()
eteve34 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff34'].HMAP_ID.item()
eteve35 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff35'].HMAP_ID.item()

eteve40 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff40'].HMAP_ID.item()
eteve42 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff42'].HMAP_ID.item()
eteve43 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff43'].HMAP_ID.item()
eteve41 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff41'].HMAP_ID.item()
eteve45 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff45'].HMAP_ID.item()

eteve50 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff50'].HMAP_ID.item()
eteve52 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff52'].HMAP_ID.item()
eteve53 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff53'].HMAP_ID.item()
eteve54 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff54'].HMAP_ID.item()
eteve51 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff51'].HMAP_ID.item()


# setting up data for heatmaps
# EV/EBIT

# all

uevehmdata = {'Benchmark':[None, uweve01, uweve02, uweve03, uweve04, uweve05,], 
             'SARD1':[uteve10, None, uweve12, uweve13, uweve14, uweve15, ], 
             'SARD2':[uteve20, uteve21, None, uweve23, uweve24, uweve25, ], 
             'SARD3':[uteve30, uteve31, uteve32, None, uweve34, uweve35,],
             'SARD4':[uteve40, uteve41, uteve42, uteve43, None, uweve45, ], 
             'SARD5':[uteve50, uteve51, uteve52, uteve53, uteve54, None, ],
              }

uevehm_df = pd.DataFrame(uevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(1)

# global

gevehmdata = {'Benchmark':[None, gweve01, gweve02, gweve03, gweve04, gweve05,], 
             'SARD1':[gteve10, None, gweve12, gweve13, gweve14, gweve15, ], 
             'SARD2':[gteve20, gteve21, None, gweve23, gweve24, gweve25, ], 
             'SARD3':[gteve30, gteve31, gteve32, None, gweve34, gweve35,],
             'SARD4':[gteve40, gteve41, gteve42, gteve43, None, gweve45, ], 
             'SARD5':[gteve50, gteve51, gteve52, gteve53, gteve54, None, ],
              }

gevehm_df = pd.DataFrame(gevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(1)

#EU

eevehmdata = {'Benchmark':[None, eweve01, eweve02, eweve03, eweve04, eweve05,], 
             'SARD1':[eteve10, None, eweve12, eweve13, eweve14, eweve15, ], 
             'SARD2':[eteve20, eteve21, None, eweve23, eweve24, eweve25, ], 
             'SARD3':[eteve30, eteve31, eteve32, None, eweve34, eweve35,],
             'SARD4':[eteve40, eteve41, eteve42, eteve43, None, eweve45, ], 
             'SARD5':[eteve50, eteve51, eteve52, eteve53, eteve54, None, ],
              }

eevehm_df = pd.DataFrame(eevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(1)




# Subplot of significance matrices
# color palette
color_palette = sns.diverging_palette(10, 240, sep=90, n=5)

## color palette
#color_palette = sns.diverging_palette(10, 240, sep=90, n=5)

# subplot attempt heatmaps 2
fig, axs = plt.subplots(1, 3, sharex='col', sharey='row', figsize=(9,9))

#EV/EBIT
# all
g1 = sns.heatmap(eevehm_df,cmap=color_palette,cbar=False,linewidths=.1 ,linecolor = 'whitesmoke',
                 vmin=-2, vmax=2, square=True, ax=axs[0])
g1.set_ylabel('')
g1.set_xlabel('')


# global
g2 = sns.heatmap(gevehm_df,cmap=color_palette,cbar=False,linewidths=.1 ,linecolor = 'whitesmoke',
                 vmin=-2, vmax=2, square=True, ax=axs[1])
g2.set_ylabel('')
g2.set_xlabel('')

# eu
g3 = sns.heatmap(uevehm_df,cmap=color_palette,cbar=False,linewidths=.1 ,linecolor = 'whitesmoke',
                 vmin=-2, vmax=2, square=True, ax=axs[2])
g3.set_ylabel('')
g3.set_xlabel('')



g1.set_title('A: EU firms', fontweight='bold')
g2.set_title('B: Global firms (excl. US)', fontweight='bold')
g3.set_title('C: All firms', fontweight='bold')

# print and storage figure
#fig.subplots_adjust(left=0.15, bottom=0, right=1, top=1)
#plt.tight_layout()
plt.savefig('evebit_newsignificance_sign_matrix_simpmodels.png')
plt.show()



del (eteve01, eteve02, eteve03, eteve04, eteve05,
     eteve10, eteve12, eteve13, eteve14, eteve15,
     eteve21, eteve20, eteve23, eteve24, eteve25,
     eteve31, eteve32, eteve30, eteve34, eteve35,
     eteve41, eteve42, eteve43, eteve40, eteve45,
     eteve51, eteve52, eteve53, eteve50, eteve54,
     
     uteve01, uteve02, uteve03, uteve04, uteve05,
     uteve10, uteve12, uteve13, uteve14, uteve15,
     uteve21, uteve20, uteve23, uteve24, uteve25,
     uteve31, uteve32, uteve30, uteve34, uteve35,
     uteve41, uteve42, uteve43, uteve40, uteve45,
     uteve51, uteve52, uteve53, uteve50, uteve54,
     
     gteve01, gteve02, gteve03, gteve04, gteve05,
     gteve10, gteve12, gteve13, gteve14, gteve15,
     gteve21, gteve20, gteve23, gteve24, gteve25,
     gteve31, gteve32, gteve30, gteve34, gteve35,
     gteve41, gteve42, gteve43, gteve40, gteve45,
     gteve51, gteve52, gteve53, gteve50, gteve54,
     
     )

del (eweve01, eweve02, eweve03, eweve04, eweve05,
     eweve10, eweve12, eweve13, eweve14, eweve15,
     eweve21, eweve20, eweve23, eweve24, eweve25,
     eweve31, eweve32, eweve30, eweve34, eweve35,
     eweve41, eweve42, eweve43, eweve40, eweve45,
     eweve51, eweve52, eweve53, eweve50, eweve54,
     
     uweve01, uweve02, uweve03, uweve04, uweve05,
     uweve10, uweve12, uweve13, uweve14, uweve15,
     uweve21, uweve20, uweve23, uweve24, uweve25,
     uweve31, uweve32, uweve30, uweve34, uweve35,
     uweve41, uweve42, uweve43, uweve40, uweve45,
     uweve51, uweve52, uweve53, uweve50, uweve54,
     
     gweve01, gweve02, gweve03, gweve04, gweve05,
     gweve10, gweve12, gweve13, gweve14, gweve15,
     gweve21, gweve20, gweve23, gweve24, gweve25,
     gweve31, gweve32, gweve30, gweve34, gweve35,
     gweve41, gweve42, gweve43, gweve40, gweve45,
     gweve51, gweve52, gweve53, gweve50, gweve54,
     
     )


# constructing output dataframe
# wilcoxon test
# All
uweve01 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff01'].Z_TEST.item()
uweve02 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff02'].Z_TEST.item()
uweve03 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff03'].Z_TEST.item()
uweve04 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff04'].Z_TEST.item()
uweve05 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff05'].Z_TEST.item()

uweve10 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff10'].Z_TEST.item()
uweve12 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff12'].Z_TEST.item()
uweve13 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff13'].Z_TEST.item()
uweve14 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff14'].Z_TEST.item()
uweve15 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff15'].Z_TEST.item()

uweve20 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff20'].Z_TEST.item()
uweve21 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff21'].Z_TEST.item()
uweve23 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff23'].Z_TEST.item()
uweve24 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff24'].Z_TEST.item()
uweve25 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff25'].Z_TEST.item()

uweve30 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff30'].Z_TEST.item()
uweve32 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff32'].Z_TEST.item()
uweve31 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff31'].Z_TEST.item()
uweve34 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff34'].Z_TEST.item()
uweve35 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff35'].Z_TEST.item()

uweve40 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff40'].Z_TEST.item()
uweve42 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff42'].Z_TEST.item()
uweve43 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff43'].Z_TEST.item()
uweve41 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff41'].Z_TEST.item()
uweve45 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff45'].Z_TEST.item()

uweve50 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff50'].Z_TEST.item()
uweve52 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff52'].Z_TEST.item()
uweve53 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff53'].Z_TEST.item()
uweve54 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff54'].Z_TEST.item()
uweve51 = ueve_great_pair_diff_eval.loc[ueve_great_pair_diff_eval['MODELVSMODEL']=='uevediff51'].Z_TEST.item()

# Global
gweve01 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff01'].Z_TEST.item()
gweve02 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff02'].Z_TEST.item()
gweve03 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff03'].Z_TEST.item()
gweve04 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff04'].Z_TEST.item()
gweve05 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff05'].Z_TEST.item()

gweve10 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff10'].Z_TEST.item()
gweve12 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff12'].Z_TEST.item()
gweve13 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff13'].Z_TEST.item()
gweve14 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff14'].Z_TEST.item()
gweve15 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff15'].Z_TEST.item()

gweve20 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff20'].Z_TEST.item()
gweve21 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff21'].Z_TEST.item()
gweve23 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff23'].Z_TEST.item()
gweve24 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff24'].Z_TEST.item()
gweve25 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff25'].Z_TEST.item()

gweve30 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff30'].Z_TEST.item()
gweve32 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff32'].Z_TEST.item()
gweve31 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff31'].Z_TEST.item()
gweve34 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff34'].Z_TEST.item()
gweve35 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff35'].Z_TEST.item()

gweve40 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff40'].Z_TEST.item()
gweve42 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff42'].Z_TEST.item()
gweve43 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff43'].Z_TEST.item()
gweve41 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff41'].Z_TEST.item()
gweve45 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff45'].Z_TEST.item()

gweve50 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff50'].Z_TEST.item()
gweve52 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff52'].Z_TEST.item()
gweve53 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff53'].Z_TEST.item()
gweve54 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff54'].Z_TEST.item()
gweve51 = geve_great_pair_diff_eval.loc[geve_great_pair_diff_eval['MODELVSMODEL']=='gevediff51'].Z_TEST.item()

# EU
eweve01 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff01'].Z_TEST.item()
eweve02 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff02'].Z_TEST.item()
eweve03 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff03'].Z_TEST.item()
eweve04 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff04'].Z_TEST.item()
eweve05 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff05'].Z_TEST.item()

eweve10 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff10'].Z_TEST.item()
eweve12 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff12'].Z_TEST.item()
eweve13 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff13'].Z_TEST.item()
eweve14 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff14'].Z_TEST.item()
eweve15 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff15'].Z_TEST.item()

eweve20 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff20'].Z_TEST.item()
eweve21 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff21'].Z_TEST.item()
eweve23 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff23'].Z_TEST.item()
eweve24 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff24'].Z_TEST.item()
eweve25 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff25'].Z_TEST.item()

eweve30 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff30'].Z_TEST.item()
eweve32 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff32'].Z_TEST.item()
eweve31 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff31'].Z_TEST.item()
eweve34 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff34'].Z_TEST.item()
eweve35 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff35'].Z_TEST.item()

eweve40 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff40'].Z_TEST.item()
eweve42 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff42'].Z_TEST.item()
eweve43 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff43'].Z_TEST.item()
eweve41 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff41'].Z_TEST.item()
eweve45 = eeve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff45'].Z_TEST.item()

eweve50 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff50'].Z_TEST.item()
eweve52 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff52'].Z_TEST.item()
eweve53 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff53'].Z_TEST.item()
eweve54 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff54'].Z_TEST.item()
eweve51 = geve_great_pair_diff_eval.loc[eeve_great_pair_diff_eval['MODELVSMODEL']=='eevediff51'].Z_TEST.item()

# t-tests
# ALL

uteve01 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff01'].TEST_SIZE.item()
uteve02 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff02'].TEST_SIZE.item()
uteve03 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff03'].TEST_SIZE.item()
uteve04 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff04'].TEST_SIZE.item()
uteve05 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff05'].TEST_SIZE.item()

uteve10 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff10'].TEST_SIZE.item()
uteve12 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff12'].TEST_SIZE.item()
uteve13 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff13'].TEST_SIZE.item()
uteve14 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff14'].TEST_SIZE.item()
uteve15 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff15'].TEST_SIZE.item()

uteve20 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff20'].TEST_SIZE.item()
uteve21 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff21'].TEST_SIZE.item()
uteve23 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff23'].TEST_SIZE.item()
uteve24 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff24'].TEST_SIZE.item()
uteve25 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff25'].TEST_SIZE.item()

uteve30 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff30'].TEST_SIZE.item()
uteve32 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff32'].TEST_SIZE.item()
uteve31 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff31'].TEST_SIZE.item()
uteve34 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff34'].TEST_SIZE.item()
uteve35 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff35'].TEST_SIZE.item()

uteve40 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff40'].TEST_SIZE.item()
uteve42 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff42'].TEST_SIZE.item()
uteve43 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff43'].TEST_SIZE.item()
uteve41 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff41'].TEST_SIZE.item()
uteve45 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff45'].TEST_SIZE.item()

uteve50 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff50'].TEST_SIZE.item()
uteve52 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff52'].TEST_SIZE.item()
uteve53 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff53'].TEST_SIZE.item()
uteve54 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff54'].TEST_SIZE.item()
uteve51 = ueve_mean_diff_eval.loc[ueve_mean_diff_eval['MODELVSMODEL']=='uevediff51'].TEST_SIZE.item()

# Global
gteve01 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff01'].TEST_SIZE.item()
gteve02 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff02'].TEST_SIZE.item()
gteve03 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff03'].TEST_SIZE.item()
gteve04 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff04'].TEST_SIZE.item()
gteve05 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff05'].TEST_SIZE.item()

gteve10 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff10'].TEST_SIZE.item()
gteve12 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff12'].TEST_SIZE.item()
gteve13 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff13'].TEST_SIZE.item()
gteve14 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff14'].TEST_SIZE.item()
gteve15 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff15'].TEST_SIZE.item()

gteve20 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff20'].TEST_SIZE.item()
gteve21 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff21'].TEST_SIZE.item()
gteve23 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff23'].TEST_SIZE.item()
gteve24 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff24'].TEST_SIZE.item()
gteve25 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff25'].TEST_SIZE.item()

gteve30 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff30'].TEST_SIZE.item()
gteve32 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff32'].TEST_SIZE.item()
gteve31 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff31'].TEST_SIZE.item()
gteve34 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff34'].TEST_SIZE.item()
gteve35 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff35'].TEST_SIZE.item()

gteve40 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff40'].TEST_SIZE.item()
gteve42 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff42'].TEST_SIZE.item()
gteve43 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff43'].TEST_SIZE.item()
gteve41 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff41'].TEST_SIZE.item()
gteve45 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff45'].TEST_SIZE.item()

gteve50 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff50'].TEST_SIZE.item()
gteve52 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff52'].TEST_SIZE.item()
gteve53 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff53'].TEST_SIZE.item()
gteve54 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff54'].TEST_SIZE.item()
gteve51 = geve_mean_diff_eval.loc[geve_mean_diff_eval['MODELVSMODEL']=='gevediff51'].TEST_SIZE.item()

# EU
eteve01 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff01'].TEST_SIZE.item()
eteve02 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff02'].TEST_SIZE.item()
eteve03 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff03'].TEST_SIZE.item()
eteve04 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff04'].TEST_SIZE.item()
eteve05 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff05'].TEST_SIZE.item()

eteve10 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff10'].TEST_SIZE.item()
eteve12 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff12'].TEST_SIZE.item()
eteve13 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff13'].TEST_SIZE.item()
eteve14 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff14'].TEST_SIZE.item()
eteve15 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff15'].TEST_SIZE.item()

eteve20 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff20'].TEST_SIZE.item()
eteve21 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff21'].TEST_SIZE.item()
eteve23 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff23'].TEST_SIZE.item()
eteve24 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff24'].TEST_SIZE.item()
eteve25 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff25'].TEST_SIZE.item()

eteve30 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff30'].TEST_SIZE.item()
eteve32 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff32'].TEST_SIZE.item()
eteve31 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff31'].TEST_SIZE.item()
eteve34 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff34'].TEST_SIZE.item()
eteve35 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff35'].TEST_SIZE.item()

eteve40 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff40'].TEST_SIZE.item()
eteve42 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff42'].TEST_SIZE.item()
eteve43 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff43'].TEST_SIZE.item()
eteve41 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff41'].TEST_SIZE.item()
eteve45 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff45'].TEST_SIZE.item()

eteve50 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff50'].TEST_SIZE.item()
eteve52 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff52'].TEST_SIZE.item()
eteve53 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff53'].TEST_SIZE.item()
eteve54 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff54'].TEST_SIZE.item()
eteve51 = eeve_mean_diff_eval.loc[eeve_mean_diff_eval['MODELVSMODEL']=='eevediff51'].TEST_SIZE.item()

# setting up data for significance test tables
# EV/EBIT


# all

uevehmdata = {'Benchmark':[None, uweve01, uweve02, uweve03, uweve04, uweve05,], 
             'SARD1':[uteve10, None, uweve12, uweve13, uweve14, uweve15, ], 
             'SARD2':[uteve20, uteve21, None, uweve23, uweve24, uweve25, ], 
             'SARD3':[uteve30, uteve31, uteve32, None, uweve34, uweve35,],
             'SARD4':[uteve40, uteve41, uteve42, uteve43, None, uweve45, ], 
             'SARD5':[uteve50, uteve51, uteve52, uteve53, uteve54, None, ],
              }

uevehm_df = pd.DataFrame(uevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(3)

# global

gevehmdata = {'Benchmark':[None, gweve01, gweve02, gweve03, gweve04, gweve05,], 
             'SARD1':[gteve10, None, gweve12, gweve13, gweve14, gweve15, ], 
             'SARD2':[gteve20, gteve21, None, gweve23, gweve24, gweve25, ], 
             'SARD3':[gteve30, gteve31, gteve32, None, gweve34, gweve35,],
             'SARD4':[gteve40, gteve41, gteve42, gteve43, None, gweve45, ], 
             'SARD5':[gteve50, gteve51, gteve52, gteve53, gteve54, None, ],
              }

gevehm_df = pd.DataFrame(gevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(3)

#EU

eevehmdata = {'Benchmark':[None, eweve01, eweve02, eweve03, eweve04, eweve05,], 
             'SARD1':[eteve10, None, eweve12, eweve13, eweve14, eweve15, ], 
             'SARD2':[eteve20, eteve21, None, eweve23, eweve24, eweve25, ], 
             'SARD3':[eteve30, eteve31, eteve32, None, eweve34, eweve35,],
             'SARD4':[eteve40, eteve41, eteve42, eteve43, None, eweve45, ], 
             'SARD5':[eteve50, eteve51, eteve52, eteve53, eteve54, None, ],
              }

eevehm_df = pd.DataFrame(eevehmdata, index =['Benchmark', 
                                           'SARD1', 'SARD2', 'SARD3','SARD4','SARD5',
                                           ]).round(3)



eve_test_results = eevehm_df.append([gevehm_df, uevehm_df], ignore_index=False).copy()

print(eve_test_results)

# extracting latex output
with open('test_results_evebit.tex','w') as tf:
    tf.write(eve_test_results.to_latex())
    
del (eteve01, eteve02, eteve03, eteve04, eteve05,
     eteve10, eteve12, eteve13, eteve14, eteve15,
     eteve21, eteve20, eteve23, eteve24, eteve25,
     eteve31, eteve32, eteve30, eteve34, eteve35,
     eteve41, eteve42, eteve43, eteve40, eteve45,
     eteve51, eteve52, eteve53, eteve50, eteve54,
     
     uteve01, uteve02, uteve03, uteve04, uteve05,
     uteve10, uteve12, uteve13, uteve14, uteve15,
     uteve21, uteve20, uteve23, uteve24, uteve25,
     uteve31, uteve32, uteve30, uteve34, uteve35,
     uteve41, uteve42, uteve43, uteve40, uteve45,
     uteve51, uteve52, uteve53, uteve50, uteve54,
     
     gteve01, gteve02, gteve03, gteve04, gteve05,
     gteve10, gteve12, gteve13, gteve14, gteve15,
     gteve21, gteve20, gteve23, gteve24, gteve25,
     gteve31, gteve32, gteve30, gteve34, gteve35,
     gteve41, gteve42, gteve43, gteve40, gteve45,
     gteve51, gteve52, gteve53, gteve50, gteve54,
     
     )

del (eweve01, eweve02, eweve03, eweve04, eweve05,
     eweve10, eweve12, eweve13, eweve14, eweve15,
     eweve21, eweve20, eweve23, eweve24, eweve25,
     eweve31, eweve32, eweve30, eweve34, eweve35,
     eweve41, eweve42, eweve43, eweve40, eweve45,
     eweve51, eweve52, eweve53, eweve50, eweve54,
     
     uweve01, uweve02, uweve03, uweve04, uweve05,
     uweve10, uweve12, uweve13, uweve14, uweve15,
     uweve21, uweve20, uweve23, uweve24, uweve25,
     uweve31, uweve32, uweve30, uweve34, uweve35,
     uweve41, uweve42, uweve43, uweve40, uweve45,
     uweve51, uweve52, uweve53, uweve50, uweve54,
     
     gweve01, gweve02, gweve03, gweve04, gweve05,
     gweve10, gweve12, gweve13, gweve14, gweve15,
     gweve21, gweve20, gweve23, gweve24, gweve25,
     gweve31, gweve32, gweve30, gweve34, gweve35,
     gweve41, gweve42, gweve43, gweve40, gweve45,
     gweve51, gweve52, gweve53, gweve50, gweve54,
     
     )

    
    
    





