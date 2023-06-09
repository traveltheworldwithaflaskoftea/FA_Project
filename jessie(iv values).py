#IV < 0.02 : Not useful for prediction 
iv_zero = ['FLAG_DOCUMENT_20', 'AMT_REQ_CREDIT_BUREAU_HOUR','FLAG_DOCUMENT_14','FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_18', 'FLAG_DOCUMENT_19', 'REG_REGION_NOT_WORK_REGION', 'FLAG_DOCUMENT_6', 'REG_REGION_NOT_LIVE_REGION', 'AMT_REQ_CREDIT_BUREAU_QRT', 'FLAG_DOCUMENT_13', 'FLAG_CONT_MOBILE', 'LIVE_REGION_NOT_WORK_REGION','FLAG_DOCUMENT_9', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_21', 'FLAG_DOCUMENT_11', 'FLAG_DOCUMENT_15', 'FLAG_EMP_PHONE', 'AMT_REQ_CREDIT_BUREAU_WEEK', 'FLAG_DOCUMENT_4',  'AMT_REQ_CREDIT_BUREAU_DAY', '']
not_useful = ['CNT_FAM_MEMBERS', 'FLAG_WORK_PHONE', 'DEF_30_CNT_SOCIAL_CIRCLE', 'FLAG_OWN_REALTY', 'FLAG_OWN_CAR', 'AMT_INCOME_TOTAL', 'HOUR_APPR_PROCESS_START', 'FLAG_PHONE', 'FLAG_EMAIL', 'NAME_EDUCATION_TYPE', 'DEF_60_CNT_SOCIAL_CIRCLE', 'WEEKDAY_APPR_PROCESS_START', 'REG_CITY_NOT_LIVE_CITY', 'OBS_30_CNT_SOCIAL_CIRCLE', 'NAME_CONTRACT_TYPE', 'FLAG_DOCUMENT_3', 'AMT_REQ_CREDIT_BUREAU_MON', 'FLAG_DOCUMENT_8', 'NAME_FAMILY_STATUS',  'CNT_CHILDREN',  'AMT_REQ_CREDIT_BUREAU_YEAR', 'OBS_60_CNT_SOCIAL_CIRCLE', 'NAME_HOUSING_TYPE', 'NAME_TYPE_SUITE', 'NAME_INCOME_TYPE', 'LIVE_CITY_NOT_WORK_CITY', 'REG_CITY_NOT_WORK_CITY', '' ]
# 0.02 <= IV < 0.1 : Weak Predictive Power
weak = ['REGION_POPULATION_RELATIVE', 'REGION_RATING_CLIENT_W_CITY','DAYS_REGISTRATION', 'NAME_EDUCATION_TYPE', 'AMT_CREDIT', 'DAYS_BIRTH', 'REGION_RATING_CLIENT', 'DAYS_EMPLOYED', 'DAYS_LAST_PHONE_CHANGE' ] 
# 0.1 <= IV < 0.5 : Medium Predictive Power 
medium = ['EXT_SOURCE_2'] 
# 0.3 <= IV < 0.5 : Strong predictive Power 
strong = ['EXT_SOURCE_3'] 


#General Scorecard 
# 0.02 <= IV < 0.1 : Weak Predictive Power
weak = ['DAYS_LAST_PHONE_CHANGE', 'REGION_POPULATION_RELATIVE', 'DAYS_EMPLOYED', 'TOTAL_FLAG_DOCUMENTS', 'DAYS_ID_PUBLISH', 'OCCUPATION_TYPE', 'NAME_CONTRACT_TYPE', 'AMT_CREDIT', 'NAME_INCOME_TYPE','DAYS_BIRTH', 'REGION_RATING_CLIENT', 'ORGANIZATION_TYPE',  'APARTMENTS_AVG', 'NAME_EDUCATION_TYPE' ] 
# 0.02 <= IV < 0.1 : Weak Predictive Power
#All IV > 0.5
scorecard_weaks = ['DAYS_EMPLOYED', 'OCCUPATION_TYPE', 'AMT_CREDIT', 'DAYS_BIRTH', 'ORGANIZATION_TYPE','NAME_EDUCATION_TYPE' ]
# 0.1 <= IV < 0.5 : Medium Predictive Power 
medium = ['EXT_SOURCE_2'] 
# 0.3 <= IV < 0.5 : Strong predictive Power 
strong = ['EXT_SOURCE_3'] 

Weak values 
0.033889
0.023462
0.086452
0.030121
0.024044
0.080745
0.023458
0.052247
0.026677
0.056463
0.038565
0.062716
0.02466
0.055954