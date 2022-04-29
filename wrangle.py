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
    # provide message on status for user
    print('Reading from .csv file.')
    # pass .csv data into a dataframe
    df = pd.read_csv('client_data.csv')
    # provide message on status for user
    print('Data acquisition complete.')
    
    return df




def wrangle_client(df):
    '''
    This function takes in a dataframe, drops the Unnamed index column, drops all rows with null values within the dataframe. 
    It then renames columns for understanding and ease of use, then creates binned categorical columns for ages and dependent numbers. 
    Lastly, it manually scales the monthly_income column.
    '''

    # drop Unnamed column as it is not needed
    df = df.drop(['Unnamed: 0'], axis=1)
    
    # drop rows with nulls
    df = df.dropna(axis = 0)
    
    # rename columns to make them lower case and more clearly defined
    df = df.rename(columns = {
        'SeriousDlqin2yrs': 'serious_delinquency' , 'RevolvingUtilizationOfUnsecuredLines': 'revolv_unsec_utilization' , 'NumberOfTime30-59DaysPastDueNotWorse': 'quantity_30_59_pd',
        'DebtRatio': 'debt_to_income_ratio', 'MonthlyIncome': 'monthly_income', 'NumberOfOpenCreditLinesAndLoans': 'quantity_loans_and_lines', 'NumberOfTimes90DaysLate':
        'quantity_90_days_pd', 'NumberRealEstateLoansOrLines': 'quantity_real_estate_loans', 'NumberOfTime60-89DaysPastDueNotWorse': 'quantity_60_89_days_pd',
        'NumberOfDependents':'quantity_dependents'})                
    
    # Make categorical column for age bins.
    df['age_bins'] = pd.cut(df.age, bins=[0, 19, 24, 34, 44, 54, 64, 74, 84, 105], 
                              labels = ['age_0-19', 'age_20_24','age_25-34', 'age_35-44', 'age_45-54', 'age_54-64', 'age_65-74', 'age_75-84', 'age_85-105'])
    
    # Make categorical column for dependent bins.
    df['quantity_dependents_bins'] = pd.cut(df.quantity_dependents, bins=[-1, 0, 2, 4, 6, 21], 
                              labels = ['0_dep','1_2_dep', '3_4_dep', '5_6_dep', '7_or_more_dep'])
    
    # manually remove outliers from the monthly_income column. 
    df = df[df.monthly_income < 15_000]
    
    
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
   
    # Split data into 2 groups train/validate and test
    train_val, test = train_test_split(df, train_size=0.8,random_state=123)
    # Split train/validate into 2 separate groups
    train, validate = train_test_split(train_val, train_size=0.7, random_state=123)
    
    # provide user with the shape of each split
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
    
   
    return train, validate, test