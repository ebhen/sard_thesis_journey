#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:32:07 2019

@author: emilhenningsen
"""


import pandas as pd
import numpy as np
import time

# timer for loop action
start_action = time.time()

### fundq
#### US data

# 1. step: import of data from Compustat and excel files and subsetting of data

# fundamentals
us_fundq = pd.read_csv('total_us_fundq_period.csv', dtype={'conm': str, 'gvkey': str, 'cusip': str,
                                                                   'loc': str, 'acctstdq': str, 'curcdq': str,})

us_funda = pd.read_csv('total_us_funda_period.csv', dtype={'conm': str, 'gvkey': str, 'cusip': str,
                                                                   'loc': str, 'acctstdq': str, 'curcdq': str,} )
# SP 1500 information
SP_comp_index = pd.read_csv('total_sp1500_comp.csv',  dtype={ 'gvkey': str, 'indexid': str,
                                                                  })

# industry information
us_comp_ind = pd.read_csv('us_company_GICS.csv', dtype={ 'gvkey': str, 'gind': str,
                                                        'ggroup': str, 'gsector': str,
                                                        'gsubind': str,
                                                                  } )

# Marketprices
us_marketprices = pd.read_csv('us_marketprices.csv', dtype={ 'gvkey': str}  )

#### renaming columns
column_names = {'conm':'NAME','isin':'ISIN','cusip':'CUSIP','rdq':'PUBL_DATE',
             'gvkey':'GVKEY','fyearq':'FYEARQ', 'fyr' : 'FYEAR_END','datafqtr':'FQYEAR','datacqtr':'DATA_QUARTER',
             'datadate':'DATE','acctstdq':'ACC_STD' ,'curcdq':'CURR', 'saleq':'SALESQ', 
             'oiadpq':'OIADPQ', 'dlttq':'DLTTQ','ibq':'IBQ','dlcq':'DLCQ', 
             'cheq':'CHEQ', 'ceqq':'CEQQ','oancfy':'OANCFY','fincfy':'FINCFY','ivncfy':'IVNCFY','ggroup':'GGROUP','gind':'GIND','gsector':'G_SECTOR','gsubind':'G_SUBIND',
             'prccq':'PRICE_CLOSE','cshoq':'NSHARES','curcdd':'CURR_STOCK','indexid':'INDEXID',
             'iid':'ISSUE_ID','ajexdi':'ADJ_FACTOR','prcstd':'PSTATUS_CODE'}

# renaming columns for further analysis 
us_fundq.rename(columns = column_names,inplace=True)
us_comp_ind.rename(columns = column_names,inplace=True)
SP_comp_index.rename(columns = column_names,inplace=True)
us_marketprices.rename(columns = column_names,inplace=True)


# Renaming as A for annual data
## GVKEY remains identical to quarterly data
column_names2 = {'conm':'A_NAME','isin':'A_ISIN','cusip':'A_CUSIP',
             'gvkey':'GVKEY','fyear':'AFYEAR', 'fyr':'AFYEAR_END',
             'datadate':'ADATE','acctstd':'AACC_STD' ,'curcd':'ACURR', 'sale':'ASALES', 
             'oiadp':'AOIADP', 'dltt':'ADLTT',
             'dlc':'ADLC', 'che':'ACHE','ib':'AIB','ceq':'ACEQ',
             'prcc_c':'APRICE_C','prcc_f':'APRICE_F','csho':'ANSHARES'}

# renaming annual data columns
us_funda.rename(columns = column_names2,inplace=True)

input_data = { 
            'SHEET_YEAR':[ '19',
                            '18', '17', '16', '15', '14',
                          '13', '12', '11', '10', '09',
                          '08', '07', '06', '05', '04',
                          '03', '02', '01', '00'], 
        
        
            'VALUE_DATE':[ '2019-03-31',
                            '2018-03-31', '2017-03-31', '2016-03-31', '2015-03-31', '2014-03-31',
                          '2013-03-31', '2012-03-31', '2011-03-31', '2010-03-31', '2009-03-31',
                          '2008-03-31', '2007-03-31', '2006-03-31', '2005-03-31', '2004-03-31',
                          '2003-03-31', '2002-03-31', '2001-03-31', '2000-03-31'], 

             'START_DATE1':[ '2018-03-31',
                            '2017-03-31', '2016-03-31', '2015-03-31', '2014-03-31', '2013-03-31',
                          '2012-03-31', '2011-03-31', '2010-03-31', '2009-03-31', '2008-03-31',
                          '2007-03-31', '2006-03-31', '2005-03-31', '2004-03-31', 
                          '2003-03-31',
                          '2002-03-31', '2001-03-31', '2000-03-31', '1999-03-31',], 
                            
                            
             'START_DATE2':[ '2018-01-01',
                            '2017-01-01', '2016-01-01', '2015-01-01', '2014-01-01', '2013-01-31',
                          '2012-01-01', '2011-01-01', '2010-01-01', '2009-01-01', '2008-01-01',
                          '2007-01-01', '2006-01-01', '2005-01-01', '2004-01-01',
                          '2003-01-01', 
                          '2002-01-01', '2001-01-01', '2000-01-01', '1999-01-01'], 
                            
             'END_DATE':[ '2018-12-31',
                            '2017-12-31', '2016-12-31', '2015-12-31', '2014-12-31', '2013-12-31',
                          '2012-12-31', '2011-12-31', '2010-12-31', '2009-12-31', '2008-12-31',
                          '2007-12-31', '2006-12-31', '2005-12-31', '2004-12-31', 
                          '2003-12-31',
                          '2002-12-31', '2001-12-31', '2000-12-31', '1999-12-31'],
                         
              'LAST_DAY_TRADE':[ '2019-03-29',
                            '2018-03-29', '2017-03-31', '2016-03-31', '2015-03-31', '2014-03-31',
                          '2013-03-28', '2012-03-30', '2011-03-31', '2010-03-31', '2009-03-31',
                          '2008-03-31', '2007-03-30', '2006-03-31', '2005-03-31', 
                          '2004-03-31',
                          '2003-03-31', '2002-03-28', '2001-03-30', '2000-03-31'],           
             
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
    last_trade_day = row['LAST_DAY_TRADE']
    
    sheet_year = convertTuple(sheet_year)
    end_date = convertTuple(end_date)
    start_date = convertTuple(start_date)
    end_date2 = convertTuple(end_date2)
    start_date2 = convertTuple(start_date2)
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    start_date2 = pd.to_datetime(start_date2)
    end_date2 = pd.to_datetime(end_date2)
    last_trade_day = pd.to_datetime(last_trade_day)
    
    print(sheet_year)

    #### preparing datasets for calc of fyear statement
    # datetime formatting
    us_fundq['DATE'] = pd.to_datetime(us_fundq['DATE']) 
    us_fundq['PUBL_DATE'] = pd.to_datetime(us_fundq['PUBL_DATE'])
    us_marketprices['DATE'] = pd.to_datetime(us_marketprices.DATE)

    # distinguish balance day and annoucement day to public
    ## assumption! rdq from COMPUSTAT equals the public date of acc information
    balance_date = us_fundq['DATE'].copy()
    public_date = us_fundq['PUBL_DATE'].copy()

    # Public to balance dates delta
    us_fundq['PB_DELTA'] = public_date - balance_date
    PB_DELTA_median = us_fundq['PB_DELTA'].median() # median for imputation of NaNs

    # imputing public to balance days median on missing data points
    # total number of misisng values for publication date
    print('percentage of misisng values for publication date')
    RDQ_ratio = (us_fundq['PUBL_DATE'].isnull().sum())/len(us_fundq.index)
    print(RDQ_ratio)

    comb = {'ID': ['RDQ_RATIO', 'RDQ_MEDIAN'],
        'OUTPUT': [RDQ_ratio, PB_DELTA_median] 
        }

    output = pd.DataFrame(comb).set_index('ID')

    # dynamic naming - ratio of missing RDQ in data
    #output.to_csv('rdq_ratio_'+sheet_year+'.csv',index=False)
    del [RDQ_ratio,output,comb]

    # ading new column artificial publication date based on balance sheet date and PB_delta
    us_fundq['ART_PUBL_DATE'] = us_fundq['DATE'] + PB_DELTA_median
    # replacing NaN in PUBL_DATE with the artificially estimation of publication date
    us_fundq['PUBL_DATE'].fillna(us_fundq['ART_PUBL_DATE'], inplace=True)
    
    #### Extracting the S&P 1500 companies at the date of valuation

    # datetime formating
    SP_comp_index['DATE'] = pd.to_datetime(SP_comp_index.DATE)
    # selecting the index constituents at the day of valuation
    temp1 = SP_comp_index.loc[SP_comp_index['DATE']==last_trade_day].copy()
    
    # SP firms at date
    firms = list(temp1.GVKEY.unique())

    # index identifiers on both SP1500 total and the subsets large, mid and small
    # 500 large cap set
    sp500comp = temp1.loc[temp1['INDEXID']=='500'].copy()
    # 400 mid cap set
    sp400comp = temp1.loc[temp1['INDEXID']=='400'].copy()
    # 600 small cap set
    sp600comp = temp1.loc[temp1['INDEXID']=='600'].copy()
    # appending all sub indexes into the S&P 1500 on the selected valuation date 
    sub_indexes = [sp400comp, sp600comp]
    # applying pandas append function for the mid and small cap companies
    sp1500comp = sp500comp.append(sub_indexes, ignore_index=True).copy()
    ## Adding sub index information
    sub_index_id = sp1500comp[['GVKEY','INDEXID']].copy()
    # removing dupes on the index information
    sub_index_id = sub_index_id.drop_duplicates(subset=['GVKEY'],keep='first')

    # deleting the import set and test1
    SP_datefilter1 = us_fundq['GVKEY'].isin(firms)
    SP_datefilter2 = us_funda['GVKEY'].isin(firms)
    SP_datefilter3 = us_comp_ind['GVKEY'].isin(firms)
    SP_datefilter4 = us_marketprices['GVKEY'].isin(firms)
    
    us_fundq2 = us_fundq[SP_datefilter1].copy()
    us_funda2 = us_funda[SP_datefilter2].copy()
    us_comp_ind2 = us_comp_ind[SP_datefilter3].copy()
    us_marketprices2 = us_marketprices[SP_datefilter4].copy()
    
    us_marketprices2.rename(columns = {'PRICE_CLOSE':'PRICE2'},inplace=True )
    us_marketprices2.rename(columns = {'NSHARES':'NSHARES2'},inplace=True )
    
    us_fundq2 = us_fundq2.sort_values(['NAME','DATE'])

    # time of valutaion
    ######### OBS ############
    ### first step: setting up dates accurately before subsetting
    # we conduct valuation at march 31 every year. Because we utilize both market prices, accoutning figures 
    # we set up two time defintions; the time horizon of the recent 12 month from valuation
    # and the recent financial year in which we construct and clean data. 
    print(us_fundq2['FYEAR_END'].value_counts())
    # march 31st is strategically selected since most of the companies have financial year end in december (i.e. december)
    # we apply the input dates to subset the fundq for the specific time of valuation
    mask = (us_fundq2['PUBL_DATE'] > start_date) & (us_fundq2['PUBL_DATE'] <= end_date)
    # subsetting with mask
    us_fundq_subset = us_fundq2.loc[mask].copy()
    
    initial_length = len(us_fundq_subset)
    
    print('Data import and subsetting finished!')

    # 2. step: data cleaning and NaN handling
    # final calculation of trailing financial statement

    ######## Assumption: US accounting standards prior to 2009 issue

    # Replacing null values with NaNs in us fundq subset (before 2009 US companies dont have acc in quarterly data)
    ## constructing corrected accounting standard column if valuation date before 2009-01-01
    ## imputing DS on all rows
    us_fundq_subset['ACC_STD_COR'] = np.where(us_fundq_subset['DATE'] <  pd.to_datetime('2009-01-01'), 'DS', 
                us_fundq_subset['ACC_STD'])

    ## dropping original ACC STD and replacing with correction
    us_fundq_subset = us_fundq_subset.drop(['ACC_STD'],axis=1)

    ## renaming back to ACC_STD
    us_fundq_subset.rename(columns={'ACC_STD_COR': 'ACC_STD'}, inplace=True)

    # second, I look into the instances of quarters in the subset because of the publ date
    # counting number of instances of company quarters (some less, some more than 4!!)
    # unique company list to perform loops
    companies = list(us_fundq_subset.GVKEY.unique())

    # I investigate potential discrepancies in regard to the estimated publication date through a counter of earnings instances
    ## counting n rows for every GVKEY
    qinstance_count = []
    
    for i in companies:
        qinstance_count.append(us_fundq_subset.loc[us_fundq_subset['GVKEY']==i].GVKEY.count())
    
    # combining the mapping with original data before removal
    gvkeyq_instance_overview = pd.DataFrame(
            {'GVKEY': companies,
             'QCOUNT': qinstance_count,
             })

    # delete forms    
    del i

    # merging the counter with the sub fundamentals
    us_fundq_subset2 = pd.merge(us_fundq_subset,gvkeyq_instance_overview, on='GVKEY', how='left')
    # number of instances with too many obs
    print('Cases of skewed quarter data with dupes...')
    print(us_fundq_subset2.QCOUNT.value_counts())

    us_fundq_subset2 = us_fundq_subset2.sort_values(['NAME','FQYEAR']).copy()

    # initial loop to remove dupes. I have no other identifer than FQYEAR from COMPUSTAT. Dupes lead to removal where the first obs is kept.
    # additionally I consider instances in which the publication date overlaps with my time measure, but shouldn't be
    # included in the 4 most recent quarters. Thus, I eliminate the first row (i.e. the most not recent)
    # I only perform loops on companies with financial year end not following the calendar year 

    company_specific = pd.DataFrame()
    cleaned_company = pd.DataFrame()
    usfundq_nd = pd.DataFrame()

    for i in companies:
        company_specific = us_fundq_subset2.loc[us_fundq_subset2['GVKEY']==i].copy()
        if len(company_specific) > 4: 
            if company_specific.FYEAR_END.value_counts().idxmax() != 12:
                cleaned_company = company_specific.iloc[1:].copy()
                usfundq_nd = usfundq_nd.append(cleaned_company, ignore_index=True)
            else: 
                usfundq_nd = usfundq_nd.append(company_specific, ignore_index=True)
        else:
            usfundq_nd = usfundq_nd.append(company_specific, ignore_index=True)
            
    del (company_specific,cleaned_company,companies,qinstance_count,gvkeyq_instance_overview)

    # dropping prior qcount in usfundq_nd
    usfundq_nd = usfundq_nd.drop(['QCOUNT'],axis=1).copy()
    
    # dupes quarters removal
    temp_count1 = len(us_fundq_subset2) - len(usfundq_nd)
    print(temp_count1)

    # counting the instances of GVKEY again after correction
    # same procedure as above with new input
    
    # unique company list to perform loops
    companies = list(usfundq_nd.GVKEY.unique())

    ## counting n rows for every GVKEY
    qinstance_count = []

    for i in companies:
        qinstance_count.append(usfundq_nd.loc[usfundq_nd['GVKEY']==i].GVKEY.count())
    
    # combining the mapping with original data before removal
    gvkeyq_instance_overview = pd.DataFrame(
            {'GVKEY': companies,
             'QCOUNT': qinstance_count,
             })

    # delete forms    
    del i

    # merge the second counter with the sub fundamentals
    usfundq_nd2 = pd.merge(usfundq_nd,gvkeyq_instance_overview, on='GVKEY', how='left').copy()

    # delete forms 
    del (qinstance_count,
         gvkeyq_instance_overview,companies)
    
    # Calculating artificial financial statements at valuation through quarterly data
    # for all companies with sufficient amount of QCOUNT, I now sum the four quarters into the trailing financial statement for the period

    # unique company list to perform loops
    companies = list(usfundq_nd2.GVKEY.unique())
    
    print(len(usfundq_nd2))
    
    pre_trail = len(usfundq_nd2)

    # empty lists before loops
    salesq_aggregate = [] #sales
    oiadpq_aggregate = [] #Operating Income Before Depreciation - Quarterly
    dlttq_aggregate = [] #Long term debt
    dlcq_aggregate = [] #Debt in Current Liabilities
    cheq_aggregate = [] #Cash and Short-Term Investments
    ibq_aggregate = [] #Net income
    ceqq_aggregate = [] #book value of equity
    price_close = [] # closing price of the most recent quarter
    nshares = [] # outstanding shares in the most recent quarter
    acc_standard = [] #accounting standard
    company_name = [] #name
    reported_currency = [] #reported currency
    financial_year_end = [] # financial year end
    cusip = [] #US specific, global use ISIN

    for i in companies: 
        if  usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].QCOUNT.value_counts().idxmax() == 4:
            # the income statement figures is the sum of the year to date q items
            salesq_aggregate.append(usfundq_nd2.loc[ usfundq_nd2['GVKEY']==i].SALESQ.sum(skipna=False))
            oiadpq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].OIADPQ.sum(skipna=False))
            ibq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].IBQ.sum(skipna=False))
            # the balance sheet and cash items is the figure from the most recent quarter at valuation
            dlttq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].DLTTQ.iloc[[3]].item())
            dlcq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].DLCQ.iloc[[3]].item())
            cheq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].CHEQ.iloc[[3]].item())
            ceqq_aggregate.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].CEQQ.iloc[[3]].item())
            price_close.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].PRICE_CLOSE.iloc[[3]].item())
            nshares.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].NSHARES.iloc[[3]].item())
            acc_standard.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].ACC_STD.value_counts().idxmax())
            company_name.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].NAME.value_counts().idxmax())
            reported_currency.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].CURR.value_counts().idxmax())
            cusip.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].CUSIP.value_counts().idxmax())
            financial_year_end.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].FYEAR_END.value_counts().idxmax())
        else:
            salesq_aggregate.append(None)
            oiadpq_aggregate.append(None)
            dlttq_aggregate.append(None)
            dlcq_aggregate.append(None)
            cheq_aggregate.append(None)
            ibq_aggregate.append(None)
            ceqq_aggregate.append(None)
            price_close.append(None)
            nshares.append(None)
            acc_standard.append(None)
            company_name.append(None)
            reported_currency.append(None)
            cusip.append(None)
            financial_year_end.append(usfundq_nd2.loc[usfundq_nd2['GVKEY']==i].FYEAR_END.value_counts().idxmax())

    us_fundacalc = pd.DataFrame(
    {'GVKEY': companies,
     'NAME' : company_name,
     'CUSIP' : cusip,
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
     'PRICE': price_close,
     'NSHARES': nshares,
                 })
        
    print('Data reduction because of trailing financial statements:')
    
    print(len(usfundq_nd2)-len(us_fundacalc))
    
    post_trail = len(us_fundacalc)
    
    trail_reduction = len(usfundq_nd2)-len(us_fundacalc)

    print('First artificial trailing financial statements at valuation finished!')
    # delete forms
    # lists from loops
    del (salesq_aggregate, oiadpq_aggregate, ibq_aggregate,dlttq_aggregate,dlcq_aggregate,cheq_aggregate,ceqq_aggregate,
         companies)
    del balance_date

    # Imputing NaNs data through FUNDA (Annual reports)

    ## FYR definition from COMPUSTAT    
    #This identifies the month in which a company ends its fiscal year. 
    #It consists of a 2-character numeric code for the month. 
    #If a fiscal year ends on day 1-14, the FYR contains a code for the prior month. 
    #If a fiscal year ends on or after the 15th, the FYR contains a code for the current month.    

    #preparing datasets before imputing of data from yearly database
    # us data publcation date 
    us_funda2['ADATE'] = pd.to_datetime(us_funda2['ADATE']) 

    # add balance dates accordingly
    mask2 = (us_funda2['ADATE'] > start_date2) & (us_funda2['ADATE'] <= end_date2) # notice that we use the calender year dates earlier set

    #subset using mask2
    us_funda_subset = us_funda2.loc[mask2].copy()

    # sort data on name and accounting standard
    us_funda_subset = us_funda_subset.sort_values(['A_NAME','AACC_STD']).copy()
    # through the import we also have duplicates with no data. However, we use Accounting standard as benchmark. The first observation is kept.
    us_funda_subset2 = us_funda_subset.drop_duplicates(subset=['GVKEY'],keep='first').copy()

    # next we merge annual and art financial statement data in order to replace the missing artificial acc figures under certain criteria
    merged_qa = pd.merge(us_fundacalc,us_funda_subset2, on='GVKEY', how='left')

    # looping through data and replacing trailing financial statements with numbers from annual database when certain criteria is met
    # FYEAR_END == AFYEAR_END 12 
    # additionally I impute missing data on the companies with year end 6 month prior to december (6,7,8,9,10,11)

    # I set up new dataframe combining the variables: GVKEY, NAME, CUSIP/ISIN, ACC_STD, 
    # CURR, SALES, OIADPQ, DLTTQ, DLCQ, CHEQ, FINCF, IVNCF and OANCF

    # I split the merged data set in order to populate data for companies with varying financial end dates

    # mask3 denotes the end month
    mask3 = [6,7,8,9,10,11]  # 6 month prior to december (6,7,8,9,10,11)

    # creating merged prior 6 month to december 
    merged_67891011 = merged_qa.loc[merged_qa['FYEAR_END'].isin(mask3)]

    # creating merged with all the other end month
    ## mask4 denotes the month not present in mask5
    mask4 = [5,4,3,2,1,12] 

    # creating merged prior 6 month to december 
    merged_12 = merged_qa.loc[merged_qa['FYEAR_END'].isin(mask4)]

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
    aprice = [] #closing price for quarter
    anshares = [] # common shares outstanding 
    aacc_standard = [] # acc standard
    acompany_name = [] # company name
    areported_currency = [] # reported currency
    acusip = [] #US specific, global use ISIN
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
            acusip.append(merged_12.loc[merged_12['GVKEY']==i].A_CUSIP.item())
        else:
            acusip.append(merged_12.loc[merged_12['GVKEY']==i].CUSIP.item())  
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
            afyear_end.append(merged_12.loc[merged_12['GVKEY']==i].AFYEAR_END.item())
        else:
            afyear_end.append(merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item())              
    del i
    
    print("Finished 12th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            aprice.append(merged_12.loc[merged_12['GVKEY']==i].APRICE_F.item())
        else:
            aprice.append(merged_12.loc[merged_12['GVKEY']==i].PRICE.item())              
    del i
    
    print("Finished 13th!")
    
    for i in companies_12:
        if merged_12.loc[merged_12['GVKEY']==i].FYEAR_END.item() == 12:
            anshares.append(merged_12.loc[merged_12['GVKEY']==i].ANSHARES.item())
        else:
            anshares.append(merged_12.loc[merged_12['GVKEY']==i].NSHARES.item())              
    del i
    
    print("Finished 14th!")

    # Next, I add the industry data from the imported industry identifier file

    aggroup = []
    agind = []
    agsector = []
    agsubind = []

    for i in companies_12:
        aggroup.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].GGROUP.item())
        agind.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].GIND.item())
        agsector.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].G_SECTOR.item())
        agsubind.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].G_SUBIND.item())
        
    del i

    # wrapping up loops in one final dataframe 
    ## will be named artificial financial statement
    us_fundacalc_12 = pd.DataFrame(
            {'GVKEY': companies_12,
             'NAME' : acompany_name,
             'CUSIP' : acusip,
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
             'PRICE' : aprice,
             'NSHARES' : anshares 
             })

    del [acompany_name,acusip,aacc_standard,areported_currency,aggroup,agind,agsector,agsubind,asales,aoiadp,
         aib,adltt,adlc,ache,aceq,afyear_end,merged_12,companies_12, aprice, anshares]

    print("Cleaning merged_67891011 subset...")

    ## lists for looped data population
    asales = [] # sales
    aoiadp = [] # operating income before dep
    adltt = [] # long term debt
    adlc = [] # debt in current liabilities
    ache = [] # Cash and short term investments
    aib = [] # Net income
    aceq = [] # book value of equity
    aprice = [] # price closing the fiscal period
    anshares = [] # number of shares outstanding
    aacc_standard = [] # acc standard
    acompany_name = [] # company name
    areported_currency = [] # reported currency
    acusip = [] #US specific, global use ISIN
    afyear_end = [] # financial year end information

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
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].CUSIP.item()):
            acusip.append(merged_67891011.loc[merged_67891011['GVKEY']==i].A_CUSIP.item())
        else:
            acusip.append(merged_67891011.loc[merged_67891011['GVKEY']==i].CUSIP.item())
                
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

    # FYEAR NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].FYEAR_END.item()):
            afyear_end.append(merged_67891011.loc[merged_67891011['GVKEY']==i].AFYEAR_END.item())
        else:
            afyear_end.append(merged_67891011.loc[merged_67891011['GVKEY']==i].FYEAR_END.item())
    
    print("Finished 12th!")
    
    del i
    
    # PRICE NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].PRICE.item()):
            aprice.append(merged_67891011.loc[merged_67891011['GVKEY']==i].APRICE_F.item())
        else:
            aprice.append(merged_67891011.loc[merged_67891011['GVKEY']==i].PRICE.item())
    
    print("Finished 13th!")
    
    del i
    
    # SHARES NaNs
    for i in companies_67891011:
        if pd.isnull(merged_67891011.loc[merged_67891011['GVKEY']==i].NSHARES.item()):
            anshares.append(merged_67891011.loc[merged_67891011['GVKEY']==i].ANSHARES.item())
        else:
            anshares.append(merged_67891011.loc[merged_67891011['GVKEY']==i].NSHARES.item())
    
    print("Finished 14th!")
    
    del i
    
    ## Finally, I loop over industry information for all companies in the list
    aggroup = []
    agind = []
    agsector = []
    agsubind = []
    
    for i in companies_67891011:
        aggroup.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].GGROUP.item())
        agind.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].GIND.item())
        agsector.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].G_SECTOR.item())
        agsubind.append(us_comp_ind.loc[us_comp_ind['GVKEY']==i].G_SUBIND.item())
        
    del i
        
    # wrapping up loops in one final dataframe 
    ## will be named artificial financial statement
    us_fundacalc_67891011 = pd.DataFrame(
        {'GVKEY': companies_67891011,
         'NAME' : acompany_name,
         'CUSIP' : acusip,
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
         'PRICE' : aprice,
         'NSHARES' : anshares,
         
      })
    
    del [acompany_name,acusip,aacc_standard,areported_currency,aggroup,agind,agsector,agsubind,asales,aoiadp,
    aib,adltt,adlc,ache,aceq,afyear_end,merged_67891011,companies_67891011,aprice,anshares]
                
    # finally, I can combine the two dataframes of cleaned data
    us_fundacalc2 = us_fundacalc_12.append(us_fundacalc_67891011, ignore_index=True).copy()
    print('Test whether the length of cleaned data articulates with origin: ')
    print(len(us_fundacalc2)==len(us_fundacalc)) ; print('If true, first test okay!')
    print(len(us_fundacalc2)==(len(us_fundacalc_12)+len(us_fundacalc_67891011))) ; print('If true, second test okay!')
    print('Total number of unique companies in trailing financial statements: ')
    print(us_fundacalc2.GVKEY.nunique())
    print("Total number of clean companies in sample before cleaning")  
    print(len(us_fundacalc.dropna()))
    print("Total number of clean companies in sample after cleaning")  
    print(len(us_fundacalc2.dropna()))
    print("Various financial year end in sample (cleaned)") 
    print(us_fundacalc2.FYEAR_END.value_counts())
    
    print('Firms retained because of Data cleaning technique:')
    print(len(us_fundacalc2.dropna()) - len(us_fundacalc.dropna()))
    
    data_clean = len(us_fundacalc2.dropna()) - len(us_fundacalc.dropna())

    print('Calculation of trailing financial statements and NaN handling finished!')

    ## Adding sub index information to the cleaned dataset
    ## merging us_fundacalc2 and the index identifiers
    us_fundacalc2 = pd.merge(us_fundacalc2,sub_index_id, on='GVKEY', how='left').copy()

    del [us_fundacalc_67891011,us_fundacalc_12]

    # 3. step: import and merge of compustat market data. Finalizing of raw trailing financial information.
    ############### Market prices ##################

    # subsetting on valuation date
    market_sub = us_marketprices2.loc[us_marketprices2['DATE']==end_date].copy()

    # sort on GVKEY and CUSIP
    market_sub = market_sub.sort_values(['GVKEY','CUSIP'])

    # drop duplicates before merge
    market_sub = market_sub.drop_duplicates(subset=['GVKEY'],keep='first').copy()

    # we only include closing price, shares outstanding, currency of stock price and date of valuation 
    market_sub = market_sub.drop(
        ['NAME', 'CUSIP','FYEAR_END','FYEARQ','DATA_QUARTER','FQYEAR'],axis=1).copy()

    # creating column to show year of valuation (stored for late use)
    market_sub['VALUE_YEAR'] = market_sub.DATE.dt.year

    # merge fundamentals and market prices
    us_fundaclean = pd.merge(us_fundacalc2,market_sub, on='GVKEY', how='left').copy()

    ## annual cleaned dataset ready calculation and SARD algo
    print('Companies excluded because of data cleaning and NaN handling: ')
    print(len(us_fundaclean)-len(us_fundaclean.dropna()))
    temp_count2 = len(us_fundaclean)-len(us_fundaclean.dropna())
    us_fundaclean = us_fundaclean.dropna().copy()
    print('Total companies in cleaned sample: ')
    print(len(us_fundaclean))
    
    us_fundaclean['CISO'] = 'USA'

    column_names_final = ['GVKEY', 'NAME', 'CISO' ,'CUSIP', 'INDEXID',
                     'ACC_STD', 'FYEAR_END' ,'YEAR','CURR', 'GGROUP', 'GIND',
           'G_SECTOR', 'G_SUBIND', 'SALES', 'OIADP', 'IB', 'DLTT', 'DLC', 'CHE',
           'CEQ',
           'PRICE', 'NSHARES', 'PRICE2', 'NSHARES2']
    
    nans = temp_count1 + temp_count2
        
    final = len(us_fundaclean)

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
               0,
               trail_reduction,
               pre_trail,
               post_trail,
               final
               ]
    
    data_elimination = pd.DataFrame(
        {'REASON': temp_index,
         'NUMBER' : removal,
 
      })
        
    print(data_elimination)
    
    # INITIAL - nans - restrict  - trail_reduct = final  
        
    # dynamic naming
    data_elimination.to_csv('us_data_elimination_'+sheet_year+'.csv',index=False)
        
    ## Storing of annual cleaned datasets
    us_fundaclean['GVKEY'] = us_fundaclean.GVKEY.astype(str)
    us_fundaclean['VALUE_YEAR'] = us_fundaclean.VALUE_YEAR.astype(int)
    us_fundaclean['GGROUP'] = us_fundaclean.GGROUP.astype(str)
    us_fundaclean['GIND'] = us_fundaclean.GIND.astype(str)
    us_fundaclean['G_SECTOR'] = us_fundaclean.G_SECTOR.astype(str)
    us_fundaclean['G_SUBIND'] = us_fundaclean.G_SUBIND.astype(str)

    # printing final shape of data
    print('Final shape of data: ')
    print(us_fundaclean.shape)

    # NB!! PRICE2 and NSHARES2 denote the market cap as of March 31st. 
    # The PRICE and NSHARES denote the price as of the recent quarter in the trailing financial statement
    # I keep both, but ocnduct analysis on PRICE2 and NSHARES2

    # dynamic naming
    us_fundaclean.to_csv('new_oecd_usfundaclean_'+sheet_year+'.csv',index=False)
    ## the process above should be repeated for all data entries 00-19

    #end time for entire data script
    end_action = time.time()
    print('Time elapsed throughout total script')
    print((end_action - start_action)/60)
    ## shutting down SQL api

    # test price
    # calculating market cap 
    us_fundaclean['MKT_CAP'] = us_fundaclean.NSHARES2 * us_fundaclean.PRICE2
    
    us_fundaclean['MKT_CAP_wrong'] = us_fundaclean.NSHARES * us_fundaclean.PRICE

    # calculating net interest bearing debt   
    us_fundaclean['NIBD'] = us_fundaclean.DLTT + us_fundaclean.DLC - us_fundaclean.CHE

    # calculating P/E ratio
    us_fundaclean['PE_RATIO'] = us_fundaclean.MKT_CAP / us_fundaclean.IB

    # calculating P/B ratio
    us_fundaclean['PB_RATIO'] = us_fundaclean.MKT_CAP / us_fundaclean.CEQ

    # EV multiples with sales and EBIT, where EBIT is approximated through OIADP
    ## EV is market cap plus NIBD
    us_fundaclean['EV'] = us_fundaclean.MKT_CAP + us_fundaclean.NIBD

    # calculating EV/SALES 
    us_fundaclean['EV_SALES'] = us_fundaclean.EV / us_fundaclean.SALES

    # calculating EV/SALES 
    us_fundaclean['EV_EBIT'] = us_fundaclean.EV / us_fundaclean.OIADP

    # calculating EBIT margin 
    us_fundaclean['EBIT_margin'] = us_fundaclean.OIADP / us_fundaclean.SALES

    # calculating Return on equity
    us_fundaclean['ROE'] = us_fundaclean.IB / us_fundaclean.CEQ

    # calculating Net debt (NIBD) / EBIT
    us_fundaclean['NET_DEBT_EBIT'] = us_fundaclean.NIBD / us_fundaclean.OIADP

    print('NET_DEBT_EBIT mean: ')
    print(us_fundaclean.NET_DEBT_EBIT.mean())
    print('NET_DEBT_EBIT median: ')
    print(us_fundaclean.NET_DEBT_EBIT.median())
    
    print('PE mean: ')
    print(us_fundaclean.PE_RATIO.mean())
    print('PE median: ')
    print(us_fundaclean.PE_RATIO.median())
    
    print('PB mean: ')
    print(us_fundaclean.PB_RATIO.mean())
    print('PB median: ')
    print(us_fundaclean.PB_RATIO.median())
    
    print('ROE mean: ')
    print(us_fundaclean.ROE.mean())
    print('ROE median: ')
    print(us_fundaclean.ROE.median())
    
    print('EV/EBIT mean: ')
    print(us_fundaclean.EV_EBIT.mean())
    print('EV/EBIT median: ')
    print(us_fundaclean.EV_EBIT.median())
    
    print('EV/SALES mean: ')
    print(us_fundaclean.EV_SALES.mean())
    print('EV/SALES median: ')
    print(us_fundaclean.EV_SALES.median())
    

# testing versus former
# US data
#
#ud_19 = pd.read_csv('usfundaclean_19.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_18 = pd.read_csv('usfundaclean_18.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_17 = pd.read_csv('usfundaclean_17.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_16 = pd.read_csv('usfundaclean_16.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_15 = pd.read_csv('usfundaclean_15.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_14 = pd.read_csv('usfundaclean_14.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_13 = pd.read_csv('usfundaclean_13.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_12 = pd.read_csv('usfundaclean_12.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_11 = pd.read_csv('usfundaclean_11.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_10 = pd.read_csv('usfundaclean_10.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_09 = pd.read_csv('usfundaclean_09.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_08 = pd.read_csv('usfundaclean_08.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_07 = pd.read_csv('usfundaclean_07.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_06 = pd.read_csv('usfundaclean_06.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_05 = pd.read_csv('usfundaclean_05.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_04 = pd.read_csv('usfundaclean_04.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_03 = pd.read_csv('usfundaclean_03.csv', dtype={'GVKEY': str,'VALUE_YEAR': str, 
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_02 = pd.read_csv('usfundaclean_02.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_01 = pd.read_csv('usfundaclean_01.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#ud_00 = pd.read_csv('usfundaclean_00.csv', dtype={'GVKEY': str, 'VALUE_YEAR' : int,
#                                                  'GGROUP': str, 'GIND': str, 'G_SECTOR': str,
#                                                  'G_SUBIND': str} )
#    
## Creating the US artifical financial statements total dataframe
##all company-year observation 
#usdfs = [ud_01,ud_02,ud_03,ud_04,ud_05,ud_06,ud_07,ud_08,
#            ud_09,ud_10,ud_11,ud_12,ud_13,ud_14,ud_15,
#            ud_16,ud_17,ud_18,ud_19]
#ustfin = ud_00.append(usdfs, ignore_index=True)
#
## deleting forms
#del [ud_01,ud_02,ud_03,ud_04,ud_05,ud_06,ud_07,ud_08,
#            ud_09,ud_10,ud_11,ud_12,ud_13,ud_14,ud_15,
#            ud_16,ud_17,ud_18,ud_19,usdfs,ud_00]
#
#X = ustfin.loc[ustfin['VALUE_YEAR']==us_fundaclean.DATE.dt.year.value_counts().idxmax()].copy()
#
## formatting accounting figures to actuals (denoted in mio)
#X[['SALES','OIADP','IB','DLTT','DLC',
#              'CHE','CEQ','OANCF','FINCF','IVNCF']] = X[['SALES',
#         'OIADP','IB','DLTT','DLC','CHE','CEQ','OANCF','FINCF','IVNCF']] * 1000000
#          
## calculating variables                        
## calculating market cap 
#X['MKT_CAP'] = X.NSHARES * (X.PRICE_CLOSE/X.QUNIT) # in some cases (i.e BRAZIL) stock price is denoted pr. 1000 units. Thus, we have this correction.
#
## net interest bearing debt
### long term debt (DLTT) + short term liabilities (DLC) - cash and short investments (CHE)
#X['NIBD'] = X.DLTT + X.DLC - X.CHE
#
## calculating P/E ratio
#X['PE_RATIO'] = X.MKT_CAP / X.IB
#
## calculating P/B ratio
#X['PB_RATIO'] = X.MKT_CAP / X.CEQ
#
## EV multiples with sales and EBIT, where EBIT is approximated through OIADP
### EV is market cap plus NIBD
#X['EV'] = X.MKT_CAP + X.NIBD
#
## calculating EV/SALES 
#X['EV_SALES'] = X.EV / X.SALES
#
## calculating EV/SALES 
#X['EV_EBIT'] = X.EV / X.OIADP
#
## calculating EBIT margin 
#X['EBIT_margin'] = X.OIADP / X.SALES
#
## calculating Return on equity
#X['ROE'] = X.IB / X.CEQ
#
## calculating Net debt (NIBD) / EBIT
#X['NET_DEBT_EBIT'] = X.NIBD / X.OIADP
#
#print(us_fundaclean.DATE.dt.year.head())
#
#print('NET_DEBT_EBIT mean: ')
#print(X.NET_DEBT_EBIT.mean())
#print('NET_DEBT_EBIT median: ')
#print(X.NET_DEBT_EBIT.median())
#
#print('PE mean: ')
#print(X.PE_RATIO.mean())
#print('PE median: ')
#print(X.PE_RATIO.median())
#
#print('PB mean: ')
#print(X.PB_RATIO.mean())
#print('PB median: ')
#print(X.PB_RATIO.median())
#
#print('ROE mean: ')
#print(X.ROE.mean())
#print('ROE median: ')
#print(X.ROE.median())
#
#print('EV/EBIT mean: ')
#print(X.EV_EBIT.mean())
#print('EV/EBIT median: ')
#print(X.EV_EBIT.median())
#
#print('EV/SALES mean: ')
#print(X.EV_SALES.mean())
#print('EV/SALES median: ')
#print(X.EV_SALES.median())
#
## investigating outliers
#
#outlier_filter = us_fundaclean['GVKEY'].isin(['007146','031673','006335','003505','003226','165675','004723',
#                '013041','006379','011749','003243','005543','016821','007585','177895']).copy()
#
#outlier_filter2 = X['GVKEY'].isin(['007146','031673','006335','003505','003226','165675','004723',
#                '013041','006379','011749','003243','005543','016821','007585','177895']).copy()
#
#ou_new = us_fundaclean[outlier_filter].copy()
#ou_old = X[outlier_filter2].copy()




