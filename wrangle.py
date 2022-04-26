# Import for data manipulation
import pandas as pd
import numpy as np

#Import to split data
from sklearn.model_selection import train_test_split

# Import to acquire df
import env
import os



def get_client_data():
    '''
    This function acquires data from a local .csv file and informs the user of completion.
    '''
    print('Reading from .csv file.')
    df = pd.read_csv('client_data.csv')
    print('Data acquisition complete.')
    return df





def wrangle_client(df):
    '''
    This function takes in a dataframe, drops the Unnamed index column, drops all rows with null values within the dataframe. 
    It then renames columns for understanding and ease of use, then creates binned categorical columns 
    for ages and dependent numbers. 
    '''
    

    # drop Unnamed column as it is not needed
    df = df.drop(['Unnamed: 0'], axis=1)
    
    # drop rows with nulls
    df = df.dropna(axis = 0)
    
    # rename columns
    df = df.rename(columns = {
        'SeriousDlqin2yrs': 'serious_delinquency' , 'RevolvingUtilizationOfUnsecuredLines': 'revolv_unsec_utilization' , 'NumberOfTime30-59DaysPastDueNotWorse': 'quantity_30_59_pd',
        'DebtRatio': 'debt_to_income_ratio', 'MonthlyIncome': 'monthly_income', 'NumberOfOpenCreditLinesAndLoans': 'quantity_loans_and_lines', 'NumberOfTimes90DaysLate':
        'quantity_90_days_pd', 'NumberRealEstateLoansOrLines': 'quantity_real_estate_loans', 'NumberOfTime60-89DaysPastDueNotWorse': 'quantity_60_89_days_pd',
        'NumberOfDependents':'quantity_dependents'})
                  
    
    # Make categorical column for age.
    df['age_bins'] = pd.cut(df.age, bins=[0, 19, 29, 39, 49, 59, 69, 79, 89, 105], 
                              labels = ['age_0-19','age_20-29', 'age_30-39', 'age_40-49', 'age_50-59', 'age_60-69', 'age_70-79', 'age_80-89', 'age_90-105'])
    
    # Make categorical column for dependents.
    df['quantity_dependents_bins'] = pd.cut(df.quantity_dependents, bins=[-1, 0, 2, 4, 6, 21], 
                              labels = ['0_dep','1_2_dep', '3_4_dep', '5_6_dep', '7_or_more_dep'])
    
    
    # convert datatypes
    #df = df.astype(convert_dict)
    

   
    # Make dummy columns for state_county_code using the binned column for processin gin modeling later. 
    #dummy_df = pd.get_dummies(df[['county_code_bin']], dummy_na=False, drop_first=[True])
    
    # Add dummy columns to dataframe
    #df = pd.concat([df, dummy_df], axis=1)


    
    return df




def split_data(df):
    '''
    This function splits a dataframe into train, validate, and test in order to explore 
    the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
   
    train_val, test = train_test_split(df, train_size=0.8,random_state=123)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=123)
    
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
    
   
    return train, validate, test