# Telco Churn:
<hr style="border:2px solid black">

## <u>Project Description</u>

## Goals: 
* Discover drivers of churn at the TelcoCo telecommunications firm
* Use drivers to develop a machine learning model to predict customer churn

<hr style="border:2px solid black">

# Initial Thoughts
 
* Is there a price threshold where customer churn rate significantly increases?
* Can we identify actionable features that significantly increase churn rate?
 
<hr style="border:2px solid black"> 


# Data Dictionary
| Feature               | Definition |
|:----------------------|:-----------|
| payment_type_id       | (int64) ID of the payment type. |
| internet_service_type_id | (int64) ID of the internet service type. |
| contract_type_id      | (int64) ID of the contract type. |
| customer_id           | (object) Unique identifier for each customer. |
| gender                | (object) Gender of the customer. |
| senior_citizen        | (int64) Whether the customer is a senior citizen (1) or not (0). |
| partner               | (object) Whether the customer has a partner or not. |
| dependents            | (object) Whether the customer has dependents or not. |
| tenure                | (int64) Number of months the customer has been with the service. |
| phone_service         | (object) Whether the customer has phone service or not. |
| multiple_lines        | (object) Whether the customer has multiple lines or not. |
| online_security       | (object) Whether the customer has online security service or not. |
| online_backup         | (object) Whether the customer has online backup service or not. |
| device_protection     | (object) Whether the customer has device protection service or not. |
| tech_support          | (object) Whether the customer has tech support service or not. |
| streaming_tv          | (object) Whether the customer has streaming TV service or not. |
| streaming_movies      | (object) Whether the customer has streaming movies service or not. |
| paperless_billing     | (object) Whether the customer has paperless billing or not. |
| monthly_charges       | (float64) Monthly charges for the service. |
| total_charges         | (object) Total charges for the service. |
| churn                 | (object) Whether the customer churned (left) the service or not. |
| contract_type         | (object) Type of contract the customer has. |
| internet_service_type | (object) Type of internet service the customer has. |
| payment_type          | (object) Type of payment the customer uses. |

## Summary

- The dataset contains information about customers and their telecom service usage.
- The features include both categorical and numerical data.
- The target variable is `churn`, indicating whether a customer churned or not.
<hr style="border:2px solid black"> 


# The Plan
 
Plan --> Acquire --> Prepare --> Explore --> Model --> Deliver
 

#### Acquire
    * Use custom acquire module to create mySQL connection and read Telco_churn into pd.DataFrame
#### Prepare
    * Removed columns with duplicate information
    * Checked for nulls in the data (internet_service_type) and imputed for "No Internet Service"
    * Changed dtype for 'total_charges' to float
    * Reorganized 'payment_type' into values='Auto' and 'Manual'
    * Encoded categorical variables
    * Split data into train, validate and test (approx. 60/20/20), stratifying on 'churn'
#### Explore
    * Vizualize data distributions to identify potential drivers of churn
    * Perform stats testing on potential drivers of churn
    * Choose features for the model
#### Model
    * Decistion Tree Classifier - Iterate multiple models to tune hyperparameters
    * KNN - Iterate multiple models to tune hyperparameters
    * Logistic Regression

<hr style="border:2px solid black"> 

# Steps to Reproduce
>1) Clone this repo.
2) Create env.py file with credentials to access Codeup mySQL server
3) Run notebook.
<hr style="border:2px solid black"> 
 
### <u>Recommendations:</u>

>* Include tech support for all Fiber optic customers.
>* Incentivise customers to enroll in automatic payments. (i.e. rebate for enrollment)
>* Incentivise Month-to-Month customers to sign one or two year contracts.

### <u>Next Steps:</u>
>* Prescriptive Model: Identify the features that would be easiest for the business to take action. Then create a model using those features to find where executives can focus to lower churn rate.
>* Predictive Model: further EDA to find significant relationships for all potential features. Then create a model using all of the significant features.