# sard_thesis_journey
This repository includes all material in relation to my master thesis on the SARD approach in a broad global setting

Scripts require a Python 3.6 installation. Type in 'python' and the name of script in the terminal.

An overview of scripts and data included in the repo is given below:

Data import, construction and trailing financial statements

  total_data_extract_global_and_us
    data import from WRDS, both us and global data. This requires a WRDS username and password.
    (OBS approx run time 12-14 hrs)
    
  new_trailing_fin_statement_global5
    trailing financial statements for Global firms
    (OBS approx run time 8-9 hrs)
    
  new_trailing_fin_statement_us2
    trailing financial statements for US firms
    (OBS approx run time 8-9 hrs)
    
  new_data_construct_allfirms_v3
    final data construction including data cleaning and subsamples
    (OBS approx run time 10-15 mins)


Selection models, SARD and benchmark

  KKsard_subs_selector_v1
    Original SARD model based on Kold and Knudsen, runned over all years (2000-2019) and for the three different samples; 
    eu firms, global firms, all firms
    
  random_lvl_indbenchmark_sub_selector_v1
    random level up benchmark used in H1 to test accuracy of SARD vs industry
  indSARD_subs_selector_v1
    industry level up SARD selector
    
Error evaluation and heatmaps

  new_heatmaps_evebit_subs_v1
    heatmaps of statistical tests, evebit only
    
    
Data and error vectors

  datasets
    us_firms: 'induwtd.csv'
    global_companies:'indgwtd.csv'
    all_firms:'indwctd.csv'
    eu_firms: 'indeuwtd.csv'
    
error vectors (used for heatmaps) OBS! all errors can be made through the scripts enclosed!
  
  All firms errors 
    KK_errors_alldata_1_7.csv
    KK_errors_alldata_2_7.csv
    KK_errors_alldata_3_7.csv
    KK_errors_alldata_4_7.csv
    KK_errors_alldata_5_7.csv
 
  Global firm errors 
    KK_errors_globaldata_1_7.csv
    KK_errors_globaldata_2_7.csv
    KK_errors_globaldata_3_7.csv
    KK_errors_globaldata_4_7.csv
    KK_errors_globaldata_5_7.csv
    
  EU firms
    KK_errors_eudata_1_7.csv
    KK_errors_eudata_2_7.csv
    KK_errors_eudata_3_7.csv
    KK_errors_eudata_4_7.csv
    KK_errors_eudata_5_7.csv
 
   
  
  
    
  
   
    
    
    
