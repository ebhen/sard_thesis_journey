#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:44:39 2019

@author: emilhenningsen
"""
  
import pandas as pd
import numpy as np
import time

# timer for loop action
start_action = time.time()

# Assumption median of the difference between RDQ and DATADATE in the US is assumed to be present for global companies as well
# import of RDQ medians for all years from US sample

rdq_19 = pd.read_csv('rdq_ratio_19.csv')
rdq_18 = pd.read_csv('rdq_ratio_18.csv')
rdq_17 = pd.read_csv('rdq_ratio_17.csv')
rdq_16 = pd.read_csv('rdq_ratio_16.csv')
rdq_15 = pd.read_csv('rdq_ratio_15.csv')
rdq_14 = pd.read_csv('rdq_ratio_14.csv')
rdq_13 = pd.read_csv('rdq_ratio_13.csv')
rdq_12 = pd.read_csv('rdq_ratio_12.csv')
rdq_11 = pd.read_csv('rdq_ratio_11.csv')
rdq_10 = pd.read_csv('rdq_ratio_10.csv')
rdq_09 = pd.read_csv('rdq_ratio_09.csv')
rdq_08 = pd.read_csv('rdq_ratio_08.csv')
rdq_07 = pd.read_csv('rdq_ratio_07.csv')
rdq_06 = pd.read_csv('rdq_ratio_06.csv')
rdq_05 = pd.read_csv('rdq_ratio_05.csv')
rdq_04 = pd.read_csv('rdq_ratio_04.csv')
rdq_03 = pd.read_csv('rdq_ratio_03.csv')
rdq_02 = pd.read_csv('rdq_ratio_02.csv')
rdq_01 = pd.read_csv('rdq_ratio_01.csv')
rdq_00 = pd.read_csv('rdq_ratio_00.csv')

# Creating the US RDQ total dataframe
# creating the total dataset with all company-year observation 
rdqs = [rdq_19.iloc[1],rdq_18.iloc[1],rdq_17.iloc[1],rdq_16.iloc[1],
        rdq_15.iloc[1],rdq_14.iloc[1],rdq_13.iloc[1],rdq_12.iloc[1],
        rdq_11.iloc[1],rdq_10.iloc[1],rdq_09.iloc[1],rdq_08.iloc[1],
            rdq_07.iloc[1],rdq_06.iloc[1],rdq_05.iloc[1],rdq_04.iloc[1],
            rdq_03.iloc[1],rdq_02.iloc[1],rdq_01.iloc[1]]
# calculating the median days delta for publication
rdqmedians = pd.DataFrame(rdq_00.iloc[1].append(rdqs, ignore_index=True))
rdqmedians['new_col'] = rdqmedians[1].astype(str).str[0:2]
rdqmedians['new_col'] = rdqmedians['new_col'].astype(int)
PB_DELTA_median = rdqmedians.new_col.median().astype(int)
PB_DELTA_median = pd.Timedelta(PB_DELTA_median,unit='D')

del (rdq_19,rdq_18,rdq_17,rdq_16,rdq_15,rdq_14,rdq_13,rdq_12,rdq_11,rdq_10,
     rdq_09,rdq_08,rdq_07,rdq_06,rdq_05,rdq_04,rdq_03,rdq_02,rdq_01,rdq_00,rdqs,
     rdqmedians)

# 1. step: import of data from Compustat and excel files and subsetting of data

# fundamentals
global_fundq = pd.read_csv('oecd_gq_period.csv', dtype={'conm': str, 'gvkey': str, 'isin': str,
                                                                   'loc': str, 'acctstdq': str, 'curcdq': str,})

global_funda = pd.read_csv('oecd_ga_period.csv', dtype={'conm': str, 'gvkey': str, 'isin': str,
                                                                   'loc': str, 'acctstdq': str, 'curcdq': str,} )

### FYI
# Global data because of OECD country filtering 
# before 2.312.539 global obs in period
# after 1.052.895 us global in period

# currencies
trans_rates = pd.read_csv('translation_rates_period.csv' )

us_rates = pd.read_csv('usd_rates.csv' )

# industry data
gics_index_data = pd.read_csv('global_company_GICS.csv', dtype={'conm': str, 'gvkey': str, 'ggroup': str,
                                                                   'gind': str, 'gsector': str, 'gsubind': str,} )

## sort on date and company name
global_fundq = global_fundq.sort_values(['conm','datadate'])

#### renaming columns
## Column names will be used throughout all data imported
column_names = {'conm':'NAME','isin':'ISIN','cusip':'CUSIP','rdq':'PUBL_DATE',
             'gvkey':'GVKEY','fyearq':'FYEARQ', 'fyr' : 'FYEAR_END','datafqtr':'FQYEAR','datacqtr':'DATA_QUARTER',
             'datadate':'DATE','acctstdq':'ACC_STD' ,'curcdq':'CURR', 'saleq':'SALESQ', 
             'oiadpq':'OIADPQ','ibq':'IBQ' ,'dlttq':'DLTTQ','dlcq':'DLCQ', 'cheq':'CHEQ', 
             'ceqq':'CEQQ','oancfy':'OANCFY','fincfy':'FINCFY','ivncfy':'IVNCFY','ggroup':'GGROUP', 
             'gind' : 'GIND', 'gsector' : 'G_SECTOR','gsubind' : 'G_SUBIND','prccd':'PRICE_CLOSE',
             'cshoc':'NSHARES','cshpria':'NSHARES2','curcdd':'CURR_STOCK','fromcurd':'FROMCURD' ,'tocurd':'TOCURD', 'exratd':'EXRATD','Company_FIC':'CISO',
             'Company_Name':'NAME','Index Name':'IND_NAME','Major Index Description':'MAJOR_IND_DESC',
             'iid':'ISSUE_ID','ajexdi':'ADJ_FACTOR','prcstd':'PSTATUS_CODE','qunit':'QUNIT', 'loc':'LOC'}

# Renaming both global_fundq, global comp ind and us_rdq
global_fundq.rename(columns = column_names,inplace=True)
gics_index_data.rename(columns = column_names,inplace=True)

# Global data preparation
global_fundq['DATE'] = pd.to_datetime(global_fundq['DATE']) 

# Calculating artificial publication date based on median from US
# global data doesn't have the date value rdq. Instead, I apply the median of time delta
# between rdq (public) and balance date from US companies as proxy for the publication for global companies 
# ASSUMPTION: publication procedure is more or less identical in all companies
# ading new column artificial publication date based on balance sheet date and PB_delta
global_fundq['ART_PUBL_DATE'] = global_fundq['DATE'] + PB_DELTA_median

##################################################### Data import finished!
###### Setting up financial statements


input_data = { 
            'SHEET_YEAR':[ 
                            '18',  '16', '15', '14',
                          '13', '12', '11', '10', '09',
                          '08', '07', '06', '05', '04',
                          '03', '02', '01', '00'], 
        
        
            'VALUE_DATE':[ 
                            '2018-03-31',  '2016-03-31', '2015-03-31', '2014-03-31',
                          '2013-03-31', '2012-03-31', '2011-03-31', '2010-03-31', '2009-03-31',
                          '2008-03-31', '2007-03-31', '2006-03-31', '2005-03-31', '2004-03-31',
                          '2003-03-31', '2002-03-31', '2001-03-31', '2000-03-31'], 

             'START_DATE1':[
                            '2017-03-31',  '2015-03-31', '2014-03-31', '2013-03-31',
                          '2012-03-31', '2011-03-31', '2010-03-31', '2009-03-31', '2008-03-31',
                          '2007-03-31', '2006-03-31', '2005-03-31', '2004-03-31', 
                          '2003-03-31',
                          '2002-03-31', '2001-03-31', '2000-03-31', '1999-03-31',], 
                            
                            
             'START_DATE2':[
                            '2017-01-01',  '2015-01-01', '2014-01-01', '2013-01-31',
                          '2012-01-01', '2011-01-01', '2010-01-01', '2009-01-01', '2008-01-01',
                          '2007-01-01', '2006-01-01', '2005-01-01', '2004-01-01',
                          '2003-01-01', 
                          '2002-01-01', '2001-01-01', '2000-01-01', '1999-01-01'], 
                            
             'END_DATE':[
                            '2017-12-31',  '2015-12-31', '2014-12-31', '2013-12-31',
                          '2012-12-31', '2011-12-31', '2010-12-31', '2009-12-31', '2008-12-31',
                          '2007-12-31', '2006-12-31', '2005-12-31', '2004-12-31', 
                          '2003-12-31',
                          '2002-12-31', '2001-12-31', '2000-12-31', '1999-12-31'],
             
              }

dates = pd.DataFrame(input_data)

def convertTuple(tup):
    str = ''.join(tup)
    return str
    

#### iterate over rows in inout data
for index, row in dates.iterrows():
    sheet_year = row['SHEET_YEAR']
    end_date = row['VALUE_DATE']
    start_date = row['START_DATE1']
    start_date2 = row['START_DATE2'] 
    end_date2 = row['END_DATE']
    
    sheet_year = convertTuple(sheet_year)
    end_date = convertTuple(end_date)
    start_date = convertTuple(start_date)
    end_date2 = convertTuple(end_date2)
    start_date2 = convertTuple(start_date2)
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    start_date2 = pd.to_datetime(start_date2)
    end_date2 = pd.to_datetime(end_date2)
    
    print(sheet_year)

    ## first, select approriate time id and start/end dates for the financial statements
    #sheet_year = input('Set time for later excel output of cleaned data (e.g 17): ')
    #
    ### second, we prompt to select the time of valuation 
    #valuation_date = input('Enter the time of valuation (e.g 2017-03-31): ')
    #
    ### third, we prompt to select the time of valuation 
    #last_day_of_trading = input('Enter the time of last_day_of_trading (e.g 2018-03-29): ')
    #
    ## time of valutaion 
    ### prompt ehich will be tapped 'in the code' 
    #### recent 12 months from valuation
    #start_date = input('Start date for recent period for valuation: ')
    #start_date = pd.to_datetime(start_date)
    #end_date = input('End date for recent period for valuation (always march 31st): ')
    #end_date = pd.to_datetime(end_date)
    #### recent calender year 
    #start_date2 = input('Start date for calender period of valuation (i.e. calender year): ')
    #start_date2 = pd.to_datetime(start_date2)
    #end_date2 = input('End date for calender period of valuation (i.e. calender year): ')
    #end_date2 = pd.to_datetime(end_date2)
    ## OBS! This has to be tapped in every run

    # YEAR-MONTH-DAY
    # datetime formating
    valuation_date = pd.to_datetime(end_date)

    ## overview of dates for all annual data sets
    #Last day of trading    valuation date    Start_date2   End_date2   Start_date 
    #2019-03-29              2019-03-31       2018-01-01   2018-12-31   2018-03-31 
    #2018-03-29              2018-03-31       2017-01-01   2017-12-31   2017-03-31
    #2017-03-31              2017-03-31       2016-01-01   2016-12-31   2016-03-31
    #2016-03-31              2016-03-31       2015-01-01   2015-12-31   2015-03-31
    #2015-03-31              2015-03-31       2014-01-01   2014-12-31   2014-03-31
    #2014-03-31              2014-03-31       2013-01-01   2013-12-31   2013-03-31
    #2013-03-28              2013-03-31       2012-01-01   2012-12-31   2012-03-31
    #2012-03-30              2012-03-31       2011-01-01   2011-12-31   2011-03-31
    #2011-03-31              2011-03-31       2010-01-01   2010-12-31   2010-03-31
    #2010-03-31              2010-03-31       2009-01-01   2009-12-31   2009-03-31
    #2009-03-31              2009-03-31       2008-01-01   2008-12-31   2008-03-31
    #2008-03-31              2008-03-31       2007-01-01   2007-12-31   2007-03-31
    #2007-03-30              2007-03-31       2006-01-01   2006-12-31   2006-03-31
    #2006-03-31              2006-03-31       2005-01-01   2005-12-31   2005-03-31
    #2005-03-31              2005-03-31       2004-01-01   2004-12-31   2004-03-31
    #2004-03-31              2004-03-31       2003-01-01   2003-12-31   2003-03-31
    #2003-03-31              2003-03-31       2002-01-01   2002-12-31   2002-03-31
    #2002-03-28              2002-03-31       2001-01-01   2001-12-31   2001-03-31
    #2001-03-30              2001-03-31       2000-01-01   2000-12-31   2000-03-31
    #2000-03-30              2000-03-31       1999-01-01   1999-12-31   2000-03-31

    ### OBS!! notice that we change 2018, 2013, 2012 and 2007 with alternartive dates.
    # this is due to the fact that these fall on weekends. Thus, we change to the recent workday prior to the 31st.

    # Assumption median of the difference between RDQ and DATADATE in the US is assumed to be present for global companies as well
    # import of RDQ medians for all years from US sample

    # we conduct valuation at march 31 every year. Because we utilize both market prices, accoutning figures 
    # and varying currency amounts, we set up two time defintions; the time horizon of the recent 12 month from valuation
    # and the financial year in which we construct and clean data. 
    # since the latest possible quarter reported for the current financial year will march the prior year
    # the period for currencies should contain the full prior calender year plus the first quarter of the year analyzed (i.e. march 31st)

    # add valutaion dates accordingly
    mask = (global_fundq['ART_PUBL_DATE'] > start_date) & (global_fundq['ART_PUBL_DATE'] <= end_date)

    global_fundq_subset = global_fundq.loc[mask].copy()
    print(len(global_fundq_subset))
    
    initial_length = len(global_fundq_subset)

    # removing NaNs 
    temp_count1 = len(global_fundq_subset) -  len(global_fundq_subset.dropna(subset=['ISIN', 'ACC_STD', 'NAME','CURR']))
    global_fundq_subset = global_fundq_subset.dropna(subset=['ISIN', 'ACC_STD', 'NAME','CURR']).copy()
    print('removing missing on ISIN, ACC_STD, NAME and CURR before loop. Data removed:')
    print(len(global_fundq_subset))

    # 2. step: currency translation of quarterly fundamentals
    # global data is denoted in the reported local currencies. Thus, we need to translate amounts into USD
    # rename columns
    trans_rates.rename(columns = column_names,inplace=True)

    # updating to datetime formatting
    trans_rates['DATE'] = pd.to_datetime(trans_rates['DATE']) 

    # add valuations dates accordingly in mask2
    mask2 = (trans_rates['DATE'] > start_date2) & (trans_rates['DATE'] <= end_date) # notice we combine start2 and end1

    # subset through mask2
    trans_rates_subset = trans_rates.loc[mask2].copy()

    ### Translation of currencies through obtained exchange rates
    # in order to obtain final USD amounts, we need to calculate to GBP from all local curr (translation rate)
    # hereafter we find the corresponding rate in USD
    # this is done for the merge for currency data and fundamental data, the date and currency will all be unique for every instance

    ## currency data

    # temp for exchange rate used in translation from GBP to local currency
    EXRATD_temp = trans_rates_subset['EXRATD'].copy()

    # translation rate into reference rate GBP
    trans_rates_subset.loc[:,'TRANSLATION'] = (1/EXRATD_temp)

    ## setting up the currency identifier which locates both time and currency
    # date identifier
    DATE_temp = trans_rates_subset['DATE'].astype(str).copy()
    # currency identifier
    TOCURD_temp = trans_rates_subset['TOCURD'].copy()
    # creating the currency identifer combining date and to currency denotion
    trans_rates_subset.loc[:,'CURR_identifier'] = DATE_temp +''+ TOCURD_temp
    
    # dropping date column since we won't use this anymore
    trans_rates_subset = trans_rates_subset.drop(['DATE'],axis=1)
    
    ## Fundamental data 
    
    # date identifier
    qDATE_temp = global_fundq_subset['DATE'].astype(str).copy()
    # currency identifer
    qTOCURD_temp = global_fundq_subset['CURR'].copy()
    # creating the currency identifer combining date and to currency denotion
    global_fundq_subset.loc[:,'CURR_identifier'] = qDATE_temp +''+ qTOCURD_temp
    
    ## merging currency and fundamental data
    # because of the currency mapper we're now able to merge the two datasets and calculate GBP amounts
    global_fundq_subset_curr_trans = pd.merge(global_fundq_subset,trans_rates_subset, 
                                              on='CURR_identifier', how='left').copy()
    
    # dropping unneccesary columns we only need the calculated translation 
    global_fundq_subset_curr_trans = global_fundq_subset_curr_trans.drop(
            ['FROMCURD', 'TOCURD', 'EXRATD','CURR_identifier'],axis=1)
    
    # setting up copy for further calculations
    global_fundq_subset_gbp = global_fundq_subset_curr_trans.copy()
    
    # using translation to get to GBP amounts
    global_fundq_subset_gbp.SALESQ = global_fundq_subset_gbp.SALESQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.OIADPQ = global_fundq_subset_gbp.OIADPQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.DLTTQ = global_fundq_subset_gbp.DLTTQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.DLCQ = global_fundq_subset_gbp.DLCQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.CHEQ = global_fundq_subset_gbp.CHEQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.IBQ = global_fundq_subset_gbp.IBQ * global_fundq_subset_gbp.TRANSLATION
    global_fundq_subset_gbp.CEQQ = global_fundq_subset_gbp.CEQQ * global_fundq_subset_gbp.TRANSLATION
    
    # dropping former local denottion and the translation rate
    global_fundq_subset_gbp = global_fundq_subset_gbp.drop(['CURR', 'TRANSLATION'],axis=1)
    
    # delete forms 
    del (DATE_temp,EXRATD_temp,TOCURD_temp,qDATE_temp,qTOCURD_temp)
    
    #### Final translation into USD amounts
    # From the gbp amounts we use the tocurd filter in the SQL to attain usd/gbp exchange rates
    # from here we calculate the usd amounts through the EXRATD imported from WRDS
    
    # rename columns accordingly
    us_rates.rename(columns = column_names,inplace=True)
    
    # transforming to date time format
    us_rates['DATE'] = pd.to_datetime(us_rates['DATE']) 
    
    # mask for subsets
    mask3 = (us_rates['DATE'] > start_date2) & (us_rates['DATE'] <= end_date)
    
    # subsetting for period analyzed
    data_curr_usd_subset = us_rates.loc[mask3].copy()
    
    # Merging fundamentals denoted in GBP with the USD rates in order to obtain USD amounts
    global_fundq_subset_usd_trans = pd.merge(global_fundq_subset_gbp,data_curr_usd_subset,
                                             on='DATE', how='left')
    
    # setting up subset for usd amounts
    global_fundq_subset_usd = global_fundq_subset_usd_trans.copy()
    
    # calculating usd amounts from exchange rates imported
    global_fundq_subset_usd.SALESQ = global_fundq_subset_usd.SALESQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.OIADPQ = global_fundq_subset_usd.OIADPQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.DLTTQ = global_fundq_subset_usd.DLTTQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.DLCQ = global_fundq_subset_usd.DLCQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.CHEQ = global_fundq_subset_usd.CHEQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.IBQ = global_fundq_subset_usd.IBQ * global_fundq_subset_usd.EXRATD
    global_fundq_subset_usd.CEQQ = global_fundq_subset_usd.CEQQ * global_fundq_subset_usd.EXRATD
    
    # dropping fromcurd gbp and the exchange rate from the working dataset
    global_fundq_subset_usd = global_fundq_subset_usd.drop(
            ['FROMCURD', 'EXRATD'],axis=1)
    
    # renaming TOCURD which was USD to CURR as currencies are now all usd amounts
    global_fundq_subset_usd.rename(columns={'TOCURD': 'CURR'}, inplace=True)
    
    print("Currency translation for quarterly data finished!")
    print(len(global_fundq_subset_usd))
    
    # removing data that are significantly small
    global_fundq_subset_usd['CRITERIA1'] = np.where(global_fundq_subset_usd['SALESQ']<0,1,0 )
    
    global_fundq_subset_usd['CRITERIA2'] = np.where(global_fundq_subset_usd['SALESQ'].isnull(),0,1)

    global_fundq_subset_usd['SALES_CRITERIA'] = global_fundq_subset_usd['CRITERIA1'] + global_fundq_subset_usd['CRITERIA2']

    # remove 2 i.e only low levels of sales, not being NaNs
    
    global_fundq_subset_usd['CRITERIA3'] = np.where(global_fundq_subset_usd['CEQQ']<0,1,0 )

    global_fundq_subset_usd['CRITERIA4'] = np.where(global_fundq_subset_usd['CEQQ'].isnull(),0,1)

    global_fundq_subset_usd['EQUITY_CRITERIA'] = global_fundq_subset_usd['CRITERIA3'] + global_fundq_subset_usd['CRITERIA4']

    # remove 2 i.e only low levels of sales, not being NaNs
    
    cond1 = global_fundq_subset_usd['SALES_CRITERIA'] != 2
    cond2 = global_fundq_subset_usd['EQUITY_CRITERIA'] != 2
    
    # Data removed due to restrictions on sales and equity
    temp_count2 = len(global_fundq_subset_usd)-len(global_fundq_subset_usd[cond1 & cond2])
    print(len(global_fundq_subset_usd)-len(global_fundq_subset_usd[cond1 & cond2]))
    
    global_fundq_subset_usd = global_fundq_subset_usd[cond1 & cond2].copy()
    print(len(global_fundq_subset_usd))
    
    ####################################### BREAK #################################
            
    # 3. step: data cleaning and NaN handling
    # final calculation of trailing financial statement
    
    # second, I look into the instances of quarters in the subset because of the publ date
    # counting number of instances of company quarters (some less, some more than 4!!)
    # unique company list to perform loops
    companies = list(global_fundq_subset_usd.GVKEY.unique())
    
    # I investigate potential discrepancies in regard to the estimated publication date through a counter of earnings instances
    ## counting n rows for every GVKEY
    qinstance_count = []
    
    for i in companies:
        qinstance_count.append(global_fundq_subset_usd.loc[global_fundq_subset_usd['GVKEY']==i].GVKEY.count())
        
    # combining the mapping with original data before removal
    gvkeyq_instance_overview = pd.DataFrame(
        {'GVKEY': companies,
         'QCOUNT': qinstance_count,
        })
    
    # delete forms    
    del i
    
    # merging the counter with the sub fundamentals
    global_fundq_subset_usd = pd.merge(global_fundq_subset_usd,gvkeyq_instance_overview, on='GVKEY', how='left')
    # number of instances with too many obs
    print('Cases of skewed quarter data with dupes...')
    print(global_fundq_subset_usd.QCOUNT.value_counts())
    
    global_fundq_subset_usd = global_fundq_subset_usd.sort_values(['NAME','FQYEAR']).copy()
    
    # initial loop to remove dupes. I have no other identifer than FQYEAR from COMPUSTAT. Dupes lead to removal where the first obs is kept.
    # additionally I consider instances in which the publication date overlaps with my time measure, but shouldn't be
    # included in the 4 most recent quarters. Thus, I eliminate the first row (i.e. the most not recent)
    # I only perform loops on companies with financial year end not following the calendar year 
    
    company_specific = pd.DataFrame()
    cleaned_company = pd.DataFrame()
    globalfundq_nd = pd.DataFrame()
    
    for i in companies:
        company_specific = global_fundq_subset_usd.loc[global_fundq_subset_usd['GVKEY']==i].copy()
        if company_specific.QCOUNT.value_counts().idxmax() > 4: 
            if company_specific.FYEAR_END.value_counts().idxmax() != 12:
                cleaned_company = company_specific.iloc[1:].copy()
                globalfundq_nd = globalfundq_nd.append(cleaned_company, ignore_index=True)
            else: 
                globalfundq_nd = globalfundq_nd.append(company_specific, ignore_index=True)
        else:
            globalfundq_nd = globalfundq_nd.append(company_specific, ignore_index=True)
                
    del (company_specific,cleaned_company,companies,qinstance_count,gvkeyq_instance_overview)
    
    # dropping prior qcount in usfundq_nd
    globalfundq_nd = globalfundq_nd.drop(['QCOUNT'],axis=1).copy()
    
    # dupes quarters removal
    temp_count3 = len(global_fundq_subset_usd) - len(globalfundq_nd)
    print(temp_count3)
    
    # unique company list to perform loops
    companies = list(globalfundq_nd.GVKEY.unique())
    
    ## counting n rows for every GVKEY
    qinstance_count = []
    
    for i in companies:
        qinstance_count.append(globalfundq_nd.loc[globalfundq_nd['GVKEY']==i].GVKEY.count())
        
    # combining the mapping with original data before removal
    gvkeyq_instance_overview = pd.DataFrame(
        {'GVKEY': companies,
         'QCOUNT': qinstance_count,
        })
    
    # delete forms    
    del i
    
    # merge the second counter with the sub fundamentals
    globalfundq_nd2 = pd.merge(globalfundq_nd,gvkeyq_instance_overview, on='GVKEY', how='left').copy()
    
    # delete forms 
    del (qinstance_count,
         gvkeyq_instance_overview,companies)
    
    
    ### Filters for data cleaning, dropping obs with insufficient quarter data
    ### additionally I consider instances in which the publication date overlaps with my time measure, but shouldn't be
    ### included in the 4 most recent quarters. Thus, I eliminate the first row (i.e. the most not recent)
    ### I only perform loops on companies with financial year end not following the calendar year 
    #
    #globalfundq_nd = global_fundq_subset_usd[global_fundq_subset_usd.QCOUNT == 4].copy()
    #print(len(globalfundq_nd))
    #print('dropping obs with insufficient quarter data')
    #temp_count2 = len(global_fundq_subset_usd) - len(globalfundq_nd)
    #print(len(global_fundq_subset_usd) - len(globalfundq_nd))
    
    print(globalfundq_nd2.QCOUNT.value_counts())
    print(len(globalfundq_nd2))
    
    pre_trail = len(globalfundq_nd2)
    
    del globalfundq_nd
    
    # Calculating artificial financial statements at valuation through quarterly data
    # for all companies with sufficient amount of QCOUNT, I now sum the four quarters into the trailing financial statement for the period
    
    # unique company list to perform loops
    companies = list(globalfundq_nd2.GVKEY.unique())
    
    # empty lists before loops
    salesq_aggregate = [] #sales
    oiadpq_aggregate = [] #Operating Income Before Depreciation - Quarterly
    dlttq_aggregate = [] #Long term debt
    dlcq_aggregate = [] #Debt in Current Liabilities
    cheq_aggregate = [] #Cash and Short-Term Investments
    ibq_aggregate = [] #Net income
    ceqq_aggregate = [] #book value of equity
    acc_standard = [] #accounting standard
    company_name = [] #name
    reported_currency = [] #reported currency
    financial_year_end = [] # financial year end
    isins = [] #Global specific, US use CUSIP
    locs = [] # headquarter of company
    
    for i in companies: 
        print(i)
        if  globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].QCOUNT.value_counts().idxmax() == 4:
            # the income statement figures is the sum of the year to date q items
            salesq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].SALESQ.sum(skipna=False))
            oiadpq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].OIADPQ.sum(skipna=False))
            ibq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].IBQ.sum(skipna=False))
            # the balance sheet and cash items is the figure from the most recent quarter at valuation
            dlttq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].DLTTQ.iloc[[3]].item())
            dlcq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].DLCQ.iloc[[3]].item())
            cheq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].CHEQ.iloc[[3]].item())
            ceqq_aggregate.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].CEQQ.iloc[[3]].item())
            acc_standard.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].ACC_STD.value_counts().idxmax())
            company_name.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].NAME.value_counts().idxmax())
            reported_currency.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].CURR.value_counts().idxmax())
            isins.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].ISIN.value_counts().idxmax())
            locs.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].LOC.value_counts().idxmax())
            financial_year_end.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].FYEAR_END.value_counts().idxmax())
        else:
            salesq_aggregate.append(None)
            oiadpq_aggregate.append(None)
            dlttq_aggregate.append(None)
            dlcq_aggregate.append(None)
            cheq_aggregate.append(None)
            ibq_aggregate.append(None)
            ceqq_aggregate.append(None)
            acc_standard.append(None)
            company_name.append(None)
            reported_currency.append(None)
            isins.append(None)
            locs.append(None)
            financial_year_end.append(globalfundq_nd2.loc[globalfundq_nd2['GVKEY']==i].FYEAR_END.value_counts().idxmax())
    
    
    
    global_fundacalc = pd.DataFrame(
        {'GVKEY': companies,
         'NAME' : company_name,
         'COUNTRY_ORIGIN' : locs,
         'ISIN' : isins,
         'ACC_STD' : acc_standard,
         'FYEAR_END' : financial_year_end,
         'CURR' : reported_currency,
         'SALES': salesq_aggregate,
         'OIADP': oiadpq_aggregate,
         'IB': ibq_aggregate,
         'DLTT': dlttq_aggregate,
         'DLC': dlcq_aggregate,
         'CHE': cheq_aggregate,
         'CEQ': ceqq_aggregate,
      })
    
    print('First artificial trailing financial statements at valuation finished!')
    
    print('Data reduction because of trailing financial statements:')
    
    print(len(globalfundq_nd2)-len(global_fundacalc))
    
    post_trail = len(global_fundacalc)
    
    trail_reduction = len(globalfundq_nd2)-len(global_fundacalc)
    
    # delete forms
    # lists from loops
    del (salesq_aggregate, oiadpq_aggregate, ibq_aggregate,dlttq_aggregate,dlcq_aggregate,cheq_aggregate,ceqq_aggregate,
    companies)
    
    # NaN handling using FUNDA 
    # FYR definition from COMPUSTAT    
    #This identifies the month in which a company ends its fiscal year. 
    #It consists of a 2-character numeric code for the month. 
    #If a fiscal year ends on day 1-14, the FYR contains a code for the prior month. 
    #If a fiscal year ends on or after the 15th, the FYR contains a code for the current month.   
    
    # Renaming as A for annual data
    ## GVKEY remains identical to quarterly data
    column_names2 = {'conm':'A_NAME','isin':'A_ISIN','cusip':'A_CUSIP','loc':'A_LOC',
                 'gvkey':'GVKEY','fyear':'AFYEAR', 'fyr':'AFYEAR_END',
                 'datadate':'ADATE','acctstd':'AACC_STD' ,'curcd':'ACURR', 'sale':'ASALES', 
                 'oiadp':'AOIADP', 'ib':'AIB','dltt':'ADLTT',
                 'dlc':'ADLC', 'che':'ACHE','ceq':'ACEQ',}
    
    global_funda.rename(columns = column_names2,inplace=True)
    
    # preparing annual dataset for calc of fyear statement
    
    # datetime formatting
    global_funda['ADATE'] = pd.to_datetime(global_funda['ADATE']) 
    
    # add balance dates accordingly
    mask4 = (global_funda['ADATE'] > start_date2) & (global_funda['ADATE'] <= end_date2) # notice that we use the calender year dates as predefined earlier
    
    # subsetting with mask4
    global_funda_subset = global_funda.loc[mask4].copy()
    
    # sort data on company name and accouting standard
    global_funda_subset = global_funda_subset.sort_values(['A_NAME','AACC_STD']).copy()
    print('Duplicated annual companies')
    print(global_funda_subset['GVKEY'].duplicated().sum())
    # in the case of duplicated observations I remove these and keep the first obs
    global_funda_subset = global_funda_subset.drop_duplicates(subset=['GVKEY'],keep='first').copy()
    
    # Before we uitlize annual data to impute NaNs, we transform local currencies into USD amounts
    # the procedure follows the one already completed for quarterly data
    
    # Setting up annual fundamental data identifier
    # unique date identifier
    aDATE_temp = global_funda_subset['ADATE'].astype(str).copy()
    # unique TOCURD identifier
    aTOCURD_temp = global_funda_subset['ACURR'].copy()
    # unique mapping of currency and date identifiers
    global_funda_subset.loc[:,'CURR_identifier'] = aDATE_temp +''+ aTOCURD_temp
    
    ## merging currency and fundamental data
    global_funda_subset_curr_trans = pd.merge(global_funda_subset,trans_rates_subset, 
                                              on='CURR_identifier', how='left').copy()
    # dropping unneccesary columns we only need the calculated translation 
    global_funda_subset_curr_trans = global_funda_subset_curr_trans.drop(
            ['FROMCURD', 'TOCURD', 'EXRATD','CURR_identifier'],axis=1)
    
    # setting up copy named GBP for further calculations
    global_funda_subset_gbp = global_funda_subset_curr_trans.copy()
    
    # using translation to get to GBP amounts
    global_funda_subset_gbp.ASALES = global_funda_subset_gbp.ASALES * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.AOIADP = global_funda_subset_gbp.AOIADP * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.ADLTT = global_funda_subset_gbp.ADLTT * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.ADLC = global_funda_subset_gbp.ADLC * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.ACHE = global_funda_subset_gbp.ACHE * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.ACEQ = global_funda_subset_gbp.ACEQ * global_funda_subset_gbp.TRANSLATION
    global_funda_subset_gbp.AIB = global_funda_subset_gbp.AIB * global_funda_subset_gbp.TRANSLATION
    
    # dropping translation and the local currency denotion
    global_funda_subset_gbp = global_funda_subset_gbp.drop(['ACURR', 'TRANSLATION'],axis=1)
    
    # From GBP to USD
    # merging currency and fundamental data
    # renaming date column in usd currency sub before merge
    adata_curr_usd_subset = data_curr_usd_subset.copy()
    adata_curr_usd_subset.rename(columns={'DATE': 'ADATE'}, inplace=True)
    
    # transforming to datetime format for ADATE
    global_funda_subset_gbp['ADATE'] = pd.to_datetime(global_funda_subset_gbp['ADATE']) 
    
    # merging gbp amounts subset with usd currency rates
    global_funda_subset_usd_trans = pd.merge(global_funda_subset_gbp,adata_curr_usd_subset,
                                             on='ADATE', how='left')
    
    # setting up subset for usd amounts
    global_funda_subset_usd = global_funda_subset_usd_trans.copy()
    
    # calculating usd amounts from exchange rates imported
    global_funda_subset_usd.ASALES = global_funda_subset_usd.ASALES * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.AOIADP = global_funda_subset_usd.AOIADP * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.ADLTT = global_funda_subset_usd.ADLTT * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.ADLC = global_funda_subset_usd.ADLC * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.ACHE = global_funda_subset_usd.ACHE * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.ACEQ = global_funda_subset_usd.ACEQ * global_funda_subset_usd.EXRATD
    global_funda_subset_usd.AIB = global_funda_subset_usd.AIB * global_funda_subset_usd.EXRATD
    
    # dropping fromcurd gbp and the exchange rate from the working dataset
    global_funda_subset_usd = global_funda_subset_usd.drop(
            ['FROMCURD', 'EXRATD'],axis=1)
    
    # renaming TOCURD which was USD to CURR as currencies are now all usd amounts
    global_funda_subset_usd.rename(columns={'TOCURD': 'ACURR'}, inplace=True)
    
    print("Currency translation of annual data finished!")
    print("Move on to data cleaning through annual dataset")
    
    # I merge annual and art financial statement data in order to replace the missing artificial acc figures under certain criteria
    merged_qa = pd.merge(global_fundacalc,global_funda_subset_usd, on='GVKEY', how='left')
    
    # looping through data and replacing trailing financial statements with numbers from annual database when certain criteria is met
    # FYEAR_END == AFYEAR_END 12 
    # additionally I impute missing data on the companies with year end 6 month prior to december (6,7,8,9,10,11)
    
    # I set up new dataframe combining the variables: GVKEY, NAME, CUSIP/ISIN, ACC_STD, 
    # CURR, SALES, OIADPQ, DLTTQ, DLCQ, CHEQ, FINCF, IVNCF and OANCF
    
    # I split the merged data set in order to populate data for companies with varying financial end dates
    
    # mask5 denotes the end month
    mask5 = [6,7,8,9,10,11]  # 6 month prior to december (6,7,8,9,10,11)
    
    # creating merged prior 6 month to december 
    merged_67891011 = merged_qa.loc[merged_qa['FYEAR_END'].isin(mask5)]
    
    # creating merged with all the other end month
    ## mask6 denotes the month not present in mask5
    mask6 = [5,4,3,2,1,12] 
    
    # creating merged prior 6 month to december 
    merged_12 = merged_qa.loc[merged_qa['FYEAR_END'].isin(mask6)]
    
    # unique company list to perform loops
    companies_12 = list(merged_12.GVKEY.unique())
    # unique company list to perform loops
    companies_67891011 = list(merged_67891011.GVKEY.unique())
    
    print("Cleaning merged_12 subset...")
    
    ## lists for looped data population
    asales = [] # sales
    aoiadp = [] # operating income before dep
    adltt = [] # long term debt
    adlc = [] # debt in current liabilities
    ache = [] # Cash and short term investments
    aib = [] # Net income
    aceq = [] # book value of equity
    aacc_standard = [] # acc standard
    acompany_name = [] # company name
    areported_currency = [] # reported currency
    aisin = [] #Global specific, US use CUSIP
    alocs = [] # Country of origin
    afyear_end = [] # financial year end id
    
    # Looping through merged data imputing annual data on the financial statements with year end december 31st
    ## criteria is financial year end decemeber 31 (i.e. calender year)
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            acompany_name.append(merged_12.loc[merged_12['GVKEY']==i].A_NAME.item())
        else:
            acompany_name.append(merged_12.loc[merged_12['GVKEY']==i].NAME.item())        
    del i
    
    print("Finished first!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aisin.append(merged_12.loc[merged_12['GVKEY']==i].A_ISIN.item())
        else:
            aisin.append(merged_12.loc[merged_12['GVKEY']==i].ISIN.item())  
    del i
    
    print("Finished second!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aacc_standard.append(merged_12.loc[merged_12['GVKEY']==i].AACC_STD.item())
        else:
            aacc_standard.append(merged_12.loc[merged_12['GVKEY']==i].ACC_STD.item())   
    del i
    
    print("Finished third!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            areported_currency.append(merged_12.loc[merged_12['GVKEY']==i].ACURR.item())
        else:
            areported_currency.append(merged_12.loc[merged_12['GVKEY']==i].CURR.item())       
    del i
    
    print("Finished fourth!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            asales.append(merged_12.loc[merged_12['GVKEY']==i].ASALES.item())
        else:
            asales.append(merged_12.loc[merged_12['GVKEY']==i].SALES.item())          
    del i
    
    print("Finished 5th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aoiadp.append(merged_12.loc[merged_12['GVKEY']==i].AOIADP.item())
        else:
            aoiadp.append(merged_12.loc[merged_12['GVKEY']==i].OIADP.item()) 
    del i
    
    print("Finished 6th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            adltt.append(merged_12.loc[merged_12['GVKEY']==i].ADLTT.item())
        else:
            adltt.append(merged_12.loc[merged_12['GVKEY']==i].DLTT.item())
    del i
    
    print("Finished 7th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            adlc.append(merged_12.loc[merged_12['GVKEY']==i].ADLC.item())
        else:
            adlc.append(merged_12.loc[merged_12['GVKEY']==i].DLC.item())
    del i
    
    print("Finished 8th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            ache.append(merged_12.loc[merged_12['GVKEY']==i].ACHE.item())
        else:
            ache.append(merged_12.loc[merged_12['GVKEY']==i].CHE.item())        
    del i
    
    print("Finished 9th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aib.append(merged_12.loc[merged_12['GVKEY']==i].AIB.item())
        else:
            aib.append(merged_12.loc[merged_12['GVKEY']==i].IB.item())       
    del i
    
    print("Finished 10th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aceq.append(merged_12.loc[merged_12['GVKEY']==i].ACEQ.item())
        else:
            aceq.append(merged_12.loc[merged_12['GVKEY']==i].CEQ.item())
    del i
    
    print("Finished 11th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            alocs.append(merged_12.loc[merged_12['GVKEY']==i].A_LOC.item())
        else:
            alocs.append(merged_12.loc[merged_12['GVKEY']==i].COUNTRY_ORIGIN.item())
    del i
    
    print("Finished 12th!")
    
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            afyear_end.append(merged_12.loc[merged_12['GVKEY']==i].AFYEAR_END.item())
        else:
            afyear_end.append(merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item())              
    del i
    
    print("Finished 13th!")
    
    # Next, I add the industry data from the imported industry identifier file
    
    aggroup = []
    agind = []
    agsector = []
    agsubind = []
    
    for i in companies_12:
        aggroup.append(gics_index_data.loc[gics_index_data['GVKEY']==i].GGROUP.item())
        agind.append(gics_index_data.loc[gics_index_data['GVKEY']==i].GIND.item())
        agsector.append(gics_index_data.loc[gics_index_data['GVKEY']==i].G_SECTOR.item())
        agsubind.append(gics_index_data.loc[gics_index_data['GVKEY']==i].G_SUBIND.item())
        
    del i
    
    # wrapping up loops in one final dataframe 
    ## will be named artificial financial statement
    global_fundacalc_12 = pd.DataFrame(
        {'GVKEY': companies_12,
         'NAME' : acompany_name,
         'COUNTRY_ORIGIN' : alocs,
         'ISIN' : aisin,
         'ACC_STD' : aacc_standard,
         'FYEAR_END' : afyear_end,
         'CURR' : areported_currency,
         'GGROUP' : aggroup,
         'GIND' : agind,
         'G_SECTOR' : agsector,
         'G_SUBIND' : agsubind,
         'SALES': asales,
         'OIADP': aoiadp,
         'IB': aib,
         'DLTT': adltt,
         'DLC': adlc,
         'CHE': ache,
         'CEQ':aceq,
    
      })
    
    del [acompany_name,aisin,aacc_standard,areported_currency,aggroup,agind,agsector,agsubind,asales,aoiadp,
    aib,adltt,adlc,ache,aceq, alocs,afyear_end,merged_12,companies_12]
    
    print("Cleaning merged_67891011 subset...")
    
    ## lists for looped data population
    asales = [] # sales
    aoiadp = [] # operating income before dep
    adltt = [] # long term debt
    adlc = [] # debt in current liabilities
    ache = [] # Cash and short term investments
    aib = [] # Net income
    aceq = [] # book value of equity
    aacc_standard = [] # acc standard
    acompany_name = [] # company name
    areported_currency = [] # reported currency
    aisin = [] #Global specific, US use CUSIP
    afyear_end = [] # financial year end information
    alocs = [] # Country of origin
    
    # company name NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].NAME.item()):
            acompany_name.append(merged_67891011.loc[merged_67891011['GVKEY']==i].A_NAME.item())
        else:
            acompany_name.append(merged_67891011.loc[merged_67891011['GVKEY']==i].NAME.item())
                
    print("Finished first!")
    
    del i
    
    # CUSIP/ISIN NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].ISIN.item()):
            aisin.append(merged_67891011.loc[merged_67891011['GVKEY']==i].A_ISIN.item())
        else:
            aisin.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ISIN.item())
                
    print("Finished second!")
    
    del i
    
    # Accoutning standard NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].ACC_STD.item()):
            aacc_standard.append(merged_67891011.loc[merged_67891011['GVKEY']==i].AACC_STD.item())
        else:
            aacc_standard.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ACC_STD.item())
                
    print("Finished third!")
    
    del i
    
    # Currency NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].CURR.item()):
            areported_currency.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ACURR.item())
        else:
            areported_currency.append(merged_67891011.loc[merged_67891011['GVKEY']==i].CURR.item())
                
    print("Finished fourth!")
    
    del i
    
    # Sales NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].SALES.item()):
            asales.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ASALES.item())
        else:
            asales.append(merged_67891011.loc[merged_67891011['GVKEY']==i].SALES.item())
    
    print("Finished fifth!")
    
    del i
    
    # OIADP NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].OIADP.item()):
            aoiadp.append(merged_67891011.loc[merged_67891011['GVKEY']==i].AOIADP.item())
        else:
            aoiadp.append(merged_67891011.loc[merged_67891011['GVKEY']==i].OIADP.item())
    
    print("Finished sixth!")
    
    del i
    
    # DLTT NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].DLTT.item()):
            adltt.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ADLTT.item())
        else:
            adltt.append(merged_67891011.loc[merged_67891011['GVKEY']==i].DLTT.item())
                
    print("Finished seventh!")
    
    del i
    
    # DLC NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].DLC.item()):
            adlc.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ADLC.item())
        else:
            adlc.append(merged_67891011.loc[merged_67891011['GVKEY']==i].DLC.item())
    
    print("Finished eight!")
    
    del i
    
    # CHE NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].CHE.item()):
            ache.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ACHE.item())
        else:
            ache.append(merged_67891011.loc[merged_67891011['GVKEY']==i].CHE.item())
    
    print("Finished ninth!")
    
    del i
    
    # IB NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].IB.item()):
            aib.append(merged_67891011.loc[merged_67891011['GVKEY']==i].AIB.item())
        else:
            aib.append(merged_67891011.loc[merged_67891011['GVKEY']==i].IB.item())
    
    print("Finished tenth!")
    
    del i
    
    # CEQ NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].CEQ.item()):
            aceq.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ACEQ.item())
        else:
            aceq.append(merged_67891011.loc[merged_67891011['GVKEY']==i].CEQ.item())
    
    print("Finished 11th!")
    
    del i
    
    # OANCFY NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].COUNTRY_ORIGIN.item()):
            alocs.append(merged_67891011.loc[merged_67891011['GVKEY']==i].A_LOC.item())
        else:
            alocs.append(merged_67891011.loc[merged_67891011['GVKEY']==i].COUNTRY_ORIGIN.item())
    
    print("Finished 12th!")
    
    del i
    
    # FYEAR NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].FYEAR_END.item()):
            afyear_end.append(merged_67891011.loc[merged_67891011['GVKEY']==i].AFYEAR_END.item())
        else:
            afyear_end.append(merged_67891011.loc[merged_67891011['GVKEY']==i].FYEAR_END.item())
    
    print("Finished 13th!")
    
    del i
    
    ## Finally, I loop over industry information for all companies in the list
    aggroup = []
    agind = []
    agsector = []
    agsubind = []
    
    for i in companies_67891011:
        aggroup.append(gics_index_data.loc[gics_index_data['GVKEY']==i].GGROUP.item())
        agind.append(gics_index_data.loc[gics_index_data['GVKEY']==i].GIND.item())
        agsector.append(gics_index_data.loc[gics_index_data['GVKEY']==i].G_SECTOR.item())
        agsubind.append(gics_index_data.loc[gics_index_data['GVKEY']==i].G_SUBIND.item())
        
    del i
        
    # wrapping up loops in one final dataframe 
    ## will be named artificial financial statement
    global_fundacalc_67891011 = pd.DataFrame(
        {'GVKEY': companies_67891011,
         'NAME' : acompany_name,
         'COUNTRY_ORIGIN' : alocs,
         'ISIN' : aisin,
         'ACC_STD' : aacc_standard,
         'FYEAR_END' : afyear_end,
         'CURR' : areported_currency,
         'GGROUP' : aggroup,
         'GIND' : agind,
         'G_SECTOR' : agsector,
         'G_SUBIND' : agsubind,
         'SALES': asales,
         'OIADP': aoiadp,
         'IB': aib,
         'DLTT': adltt,
         'DLC': adlc,
         'CHE': ache,
         'CEQ':aceq,
      })
    
    del [acompany_name,aisin,aacc_standard,areported_currency,aggroup,agind,agsector,agsubind,asales,aoiadp,
    aib,adltt,adlc,ache,aceq,afyear_end, alocs,merged_67891011,companies_67891011]
    
    # finally, I can combine the two dataframes of cleaned data
    global_fundacalc2 = global_fundacalc_12.append(global_fundacalc_67891011, ignore_index=True).copy()
    print('Test whether the length of cleaned data articulates with origin: ')
    print(len(global_fundacalc2)==len(global_fundacalc)) ; print('If true, first test okay!')
    print(len(global_fundacalc2)==(len(global_fundacalc_12)+len(global_fundacalc_67891011))) ; print('If true, second test okay!')
    print('Total number of unique companies in trailing financial statements: ')
    print(global_fundacalc2.GVKEY.nunique())
    print("Total number of clean companies in sample before adding annual reports")  
    print(len(global_fundacalc.dropna()))
    print("Total number of clean companies in sample after dding annual reports")  
    print(len(global_fundacalc2.dropna()))
    print("Various financial year end in sample (cleaned)") 
    print(global_fundacalc2.FYEAR_END.value_counts())
    
    del [global_fundacalc_67891011,global_fundacalc_12]
    
    # rearranging columns
    column_names3 = ['GVKEY', 'NAME', 'COUNTRY_ORIGIN' ,'ISIN', 
                     'ACC_STD', 'FYEAR_END' ,'CURR', 'GGROUP', 'GIND',
           'G_SECTOR', 'G_SUBIND', 'SALES', 'OIADP', 'IB', 'DLTT', 'DLC', 'CHE',
           'CEQ']
    
    global_fundacalc2 = global_fundacalc2[column_names3].copy() # dropping unnessecary columns
    
    print('Firms retained because of Data cleaning technique:')
    print(len(global_fundacalc2.dropna()) - len(global_fundacalc.dropna()))
    
    data_clean = len(global_fundacalc2.dropna()) - len(global_fundacalc.dropna())
    
    print('Calculation of trailing financial statements and NaN handling finished! - market prices will be added through the preeliminary datahandling script')
    
    # annual cleaned dataset ready calculation and SARD algo
    print('Companies excluded because of data cleaning and NaN handling: ')
    temp_count4 = len(global_fundacalc2)-len(global_fundacalc2.dropna())
    print(len(global_fundacalc2)-len(global_fundacalc2.dropna()))
    global_fundaclean = global_fundacalc2.dropna().copy()
    
    print('Total companies in cleaned sample: ')
    print(len(global_fundaclean))
    print("Various financial year end in sample (cleaned)") 
    print(global_fundaclean.FYEAR_END.value_counts())
    print("Unique companies in sample (cleaned)") 
    print(global_fundaclean.GVKEY.nunique())
    print("Duplication check") 
    print(global_fundaclean.GVKEY.duplicated().sum())
    
    # final requirements for small companies
    global_fundaclean['SALES_CRITERIA'] = np.where(global_fundaclean['SALES']<0,1,0 )
    
    # remove 1 i.e only low levels of sales
    global_fundaclean['EQUITY_CRITERIA'] = np.where(global_fundaclean['CEQ']<0,1,0 )
    
    # remove 1 i.e only low levels of sales
    
    cond1 = global_fundaclean['SALES_CRITERIA'] != 1
    cond2 = global_fundaclean['EQUITY_CRITERIA'] != 1
    
    # Data removed due to restrictions on sales and equity
    print('Total data excluded because of data restrictions: ')
    restricttion = len(global_fundaclean)-len(global_fundaclean[cond1 & cond2]) + temp_count2
    print(len(global_fundaclean)-len(global_fundaclean[cond1 & cond2]) + temp_count2)
    
    global_fundaclean = global_fundaclean[cond1 & cond2].copy()
    
    global_fundaclean = global_fundaclean.drop(['SALES_CRITERIA', 'EQUITY_CRITERIA'],axis=1).copy()
    
    nans = temp_count1 + temp_count3 + temp_count4
    
    
    final = len(global_fundaclean)

    temp_index = ['INITIAL',
                    'NaNs',
                  'DATA_CLEAN',
                  'RESTRICTIONS1',
                  'TRAIL_REDUCTION',
                  'PRE_TRAIL',
                  'POST_TRAIL',
                  'FINAL']
    
    removal = [initial_length,
                nans, 
               data_clean,
               restricttion ,
               trail_reduction,
               pre_trail,
               post_trail,
               final
               ]
    
    data_elimination = pd.DataFrame(
        {'REASON': temp_index,
         'NUMBER' : removal,
 
          })
        
    # INITIAL - nans - restrict  - trail_reduct = final    
        
    print(data_elimination)
        
    print('Distribution of countries')    
    print(global_fundaclean.COUNTRY_ORIGIN.value_counts())
    
    print(global_fundaclean.GVKEY.duplicated().sum())
    
    global_fundaclean.rename(columns={'COUNTRY_ORIGIN': 'CISO'}, inplace=True)
    
    global_fundaclean.to_csv('new_oecd_gfundaclean2_'+sheet_year+'.csv',index=False)
    
    # dynamic naming
    data_elimination.to_csv('data_elimination2_'+sheet_year+'.csv',index=False)
    
    # INITIAL - nans - restrict  - trail_reduct = final    
    
    #end time for entire data script
    end_action = time.time()
    print('Time elapsed throughout total script')
    print((end_action - start_action)/60)
    print('Size of finalized data')
    print(global_fundaclean.shape)      


