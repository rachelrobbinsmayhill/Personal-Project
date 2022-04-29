CAN I GET A LITTLE CREDIT?

An Exploration of Credit Worthiness

Using Classification to Predict Serious Repayment Delinquency

===

Personal Project        
By: Rachel Robbins-Mayhill     |     Codeup     |     Innis Cohort     |     April 2022
 
===
 
Table of Contents
---
 
* I. [Project Overview](#i-project-overview)<br>
[1. Goals](#1-goal)<br>
[2. Description](#2-description)<br>
[3. Initial Thoughts & Hypothesis](#3initial-thoughts--hypothesis)<br>
[4. Initial Questions](#4initial-questions)<br>
[5. Deliverables](#5-deliverables)<br>
* II. [Project Data Context](#ii-project-data-context)<br>
[1. Data Dictionary](#1-data-dictionary)<br>
* III. [Project Plan - Data Science Pipeline](#iii-project-plan---using-the-data-science-pipeline)<br>
[1. Project Planning](#1-plan)<br>
[2. Data Acquisition](#2-acquire)<br>
[3. Data Preparation](#3-prepare)<br>
[4. Data Exploration](#4explore)<br>
[5. Modeling & Evaluation](#5-model--evaluate)<br>
[6. Product Delivery](#6-delivery)<br>
* IV. [Project Modules](#iv-project-modules)<br>
* V. [Project Reproduction](#v-project-reproduction)<br>
 
 
 
## I. PROJECT OVERVIEW - EXECUTIVE SUMMARY
 
#### 1. GOAL:
The goal of this project is to build a model a classification model that can predict who will be seriously delinquent in loan repayment beased upon historical data.
 
#### 2. DESCRIPTION:
Banks play a crucial role in market economies. They decide who can get financing and on what terms and can make or break investment decisions. For markets and society to function, individuals and companies need access to credit. 

Credit scoring algorithms, which make a guess at the probability of default, are the methods banks use to determine whether or not a loan should be granted. This project aims to improve upon the state of the art in credit scoring, by predicting the probability that somebody will experience serious delinquency in the next two years. For the purpose of this project 'Serious Delinquency' is defined as being 90 days or more past due on payment. 

I am interested in this project because identifying at-risk borrower populations helps to protect the consumer, the business, the market, and society as a whole. Identifying borrowers who are at risk of default helps to prevent the consumer from entering into a situation that could be harmful to their long-term financial stability. It helps the banking institution prevent significant and costly losses which could impact business sustainability and limit the potential to help others. Lastly, as we saw with the housing crisis of 2008, accurately identifying at-risk loan applicants can prevent the destabilizing of the market which can have far-reaching consequences for society as a whole.

#### 3.INITIAL THOUGHTS & HYPOTHESIS: 
The initial hypothesis of the project was that those with serious delinquency were younger, had lower monthly income, higher debt to income ratio, and a greater ratio of revolving unsecured line utilization. The thought behind this was younger people are at the beginning of their income trajectory within their professional lives, making less than those with more life/professional experience as they get older. Younger borrowers may still be learning to manage their finances and may take on more debt than reasonable given their financial situation. These thoughts and the subsequent hypothesis drove the initial exploratory questions for this project. 


#### 4.INITIAL QUESTIONS:
- Are borrowers in certain age groups more likely to be seriously delinquent?
- Are borrowers with lower monthly income more likely to be seriously delinquent?
- Are borrowers with higher debt to income ratio more likely to be seriously delinquent?
- Are borrowers with higher revolving unsecured line utilization more likely to be seriously delinquent?
 
#### 5. KEY FINDINGS:
 
 
 
.......how they apply to the business, recommendations and next steps. If your primary deliverable is a model, it's great to also include how the model expects to perform on future data....


 
#### 5. DELIVERABLES:
- [x] README file - provides an overview of the project and steps for project reproduction
- [x] Draft Jupyter Notebook - provides all steps taken to produce the project
- [x] wrangle.py - provides reproducible code to automate acquiring, preparing, and splitting the data
- [x] Report Jupyter Notebook - provides final presentation-ready wrangle and exploration

 
 
## II. PROJECT DATA CONTEXT
 
#### 1. DATA DICTIONARY:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
 
|  Variables             |    Definition                              |    DataType             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
column_name    |  Description                        |  datatype   |
serious_ delinquency (*target)  | Person experienced 90 days past due delinquency or worse | booolean(Y/N) | 
revolv_unsec_utilization | Total balance on credit cards and personal lines of credit except real estate and no installment debt like car loans divided by the sum of credit limits | float (percentage) | 
quantity_real_estate_loans | Number of mortgage and real estate loans including home equity lines of credit | integer | 
quantity_loans_and_lines | Number of Open loans (installment like car loan or mortgage) and Lines of credit (e.g. credit cards) | integer | 
quantity_dependents | Number of dependents in family excluding themselves (spouse, children etc.) | float | 
quantity_90_days_pd | Number of times borrower has been 90 days or more past due. | integer | 
quantity_60_89_days_pd | Number of times borrower has been 60-89 days past due but no worse in the last 2 years. | integer | 
quantity_30-59_pd | Number of times borrower has been 30-59 days past due but no worse in the last 2 years. | integer | 
monthly_income | Monthly income | float | 
debt_to_income_ratio | Monthly debt payments, alimony,living costs divided by monthy gross income | float (percentage) | 
age | Age of borrower in years | integer | 


 
## III. PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver
 
#### 1. PLAN
- [x]  Review project expectations
- [x]  Draft project goal to include measures of success
- [x]  Create questions related to the project
- [x]  Create questions related to the data
- [x]  Create a plan for completing the project using the data science pipeline
- [x]  Create a data dictionary to define variables and data context
- [x]  Draft starting hypothesis
- [x]  Create local folder and repository for project
 
#### 2. ACQUIRE
- [x]  Create .gitignore
- [x]  Obtain client_data.csv and save in local folder/project repository
- [x]  Create wrangle.py module
- [x]  Store functions needed to acquire the dataset
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
- [x]  Using Jupyter Notebook
     - [x]  Run all required imports
     - [x]  Import functions from wrangle.py module
     - [x]  Summarize dataset using methods and document observations
 
#### 3. PREPARE
Using Jupyter Notebook
- [x]  Import functions from wrangle.py module
- [x]  Summarize dataset using methods and document observations
- [x]  Clean data
    - [x]  Address missing values, data errors, unnecessary data, renaming for functionality
    - [x]  Categorical features or discrete features need to be numbers that represent those categories
    - [x]  Continuous features may need to be standardized to compare like datatypes
    - [x]  Consider feature engineering to combine features or bin continuous data into categorical    
- [x]  Split data into train, validate, and test samples
Using Python Scripting Program (Jupyter Notebook)
- [x]  Create prepare function within wrangle.py
- [x]  Store functions needed to prepare the data
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
 
#### 4.EXPLORE
Using Jupyter Notebook:
- [x]  Answer key questions about hypotheses
     - [x]  Run at least two statistical tests
     - [x]  Document findings
- [x]  Create visualizations with the intent to discover variable relationships
     - [x]  Identify variables related to serious delinquency
     - [x]  Identify any potential data integrity issues
- [x]  Summarize conclusions, provide clear answers, and summarize takeaways
     - [x] Explain plan of action as deduced from work to this point
 
#### 5. MODEL & EVALUATE
Using Jupyter Notebook:
- [x] Establish baseline accuracy
- [x] Train and fit multiple (3+) models with varying algorithms and/or hyperparameters
- [x] Compare evaluation metrics across models
- [x] Remove unnecessary features
- [x] Evaluate best performing models using validate set
- [x] Choose best performing validation model for use on test set
- [x] Test final model on out-of-sample testing dataset
- [x] Summarize performance
- [x] Interpret and document findings
 
#### 6. DELIVERY
- [x]  Prepare final notebook in Jupyter Notebook
     - [x]  Include introduction of project and goals     
     - [x]  Provide executive summary of findings, key takeaways, and recommendations
     - [x]  Create clear walk-though of the Data Science Pipeline using headings and dividers
     - [x]  Explicitly define questions asked during the initial analysis
     - [x]  Visualize relationships
     - [x]  Provide final takeaways, recommend course of action, and next steps
     - [x]  Comment code thoroughly

 
## IV. PROJECT MODULES:
- [x] wrangle.py - provides reproducible python code to automate acquiring, preparing, and splitting the data
 
  
## V. PROJECT REPRODUCTION:
### Steps to Reproduce
- [x] Make .gitignore and add any file types you would like ignored, such as .pycache or .ipynb_checkpoints
- [x] You will need the client_data.csv found inside this repo, so do NOT add .csv files to the .gitignore
- [x] Clone this repo (including the wrangle.py)
- [x] Import python libraries:  pandas, matplotlib, seaborn, numpy, and sklearn
- [x] Follow steps as outlined in the README.md. and work.ipynb
- [x] Run final_report.ipynb to view the final product