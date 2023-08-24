import pandas as pd
from sklearn.model_selection import train_test_split

def split_function(df, target_varible):
    ''' 
    Function takes in 2 positional arguments for a dataframe and target variable. Returns train, validate, test, dataframes stratified on the target variable. Roughly (60/20/20) split.
    
    '''
    train, test = train_test_split(df,
                                   random_state=666,
                                   test_size=.20,
                                   stratify= df[target_varible])
    
    train, validate = train_test_split(train,
                                   random_state=666,
                                   test_size=.25,
                                   stratify= train[target_varible])
    return train, validate, test

def prep_telco(df):
    '''
    This function takes in a dataframe. It will change dtype of total_charges to float, drop any duplicate observations, split into train, validate, test using split_function, impute 'internet_service_type' with "No Internet Service", drop ['contract_type_id', 'payment_type_id', 'internet_service_type_id'], create a new column with payment_type organized into either "Manual" or "Automatic", then drop payment_type, and create dummy vars from all categorical variables. Returns train, validate, test dataframes.
    '''
    
    # change dtype of total_charges to float
    df['total_charges'] = df.total_charges.str.replace(' ', '0').astype(float)
    
    #drop out any redundant, excessively empty, or bad columns
    df = df.drop_duplicates()
    df = df.drop(columns=['contract_type_id', 'payment_type_id', 'internet_service_type_id'])
    
    # Organize payment_type into Auto and Manual
    df['mapped_payment_type'] = df['payment_type'].apply(lambda x: 'Manual' if x in ['Electronic check', 'Mailed check'] else 'Automatic')
    # Drop payment_type
    df = df.drop(columns=['payment_type'])
    
    # split data into train, validate, test
    train, validate, test = split_function(df, target)
    
    # impute train['internet_service_type'] with 'No Internet Service'
    train['internet_service_type'] = train['internet_service_type'].fillna(value='No Internet Service')
    # impute train['internet_service_type'] with 'No Internet Service'
    validate['internet_service_type'] = validate['internet_service_type'].fillna(value='No Internet Service')
    # impute train['internet_service_type'] with 'No Internet Service'
    test['internet_service_type'] = test['internet_service_type'].fillna(value='No Internet Service')
    
    
    # Manually encode binary categorical variables for train
    train['gender_encoded'] = train.gender.map({'Female': 1, 'Male':0})
    train['partner_encoded'] = train.partner.map({'Yes':1, 'No':0})
    train['dependents_encoded'] = train.dependents.map({'Yes':1, 'No':0})
    train['phone_service_encoded'] = train.phone_service.map({'Yes':1, 'No':0})
    train['paperless_billing_encoded'] = train.paperless_billing.map({'Yes':1, 'No':0})
    train['churn_encoded'] = train.churn.map({'Yes':1, 'No':0})
    
    # Manually encode binary categorical variables for validate
    validate['gender_encoded'] = validate.gender.map({'Female': 1, 'Male':0})
    validate['partner_encoded'] = validate.partner.map({'Yes':1, 'No':0})
    validate['dependents_encoded'] = validate.dependents.map({'Yes':1, 'No':0})
    validate['phone_service_encoded'] = validate.phone_service.map({'Yes':1, 'No':0})
    validate['paperless_billing_encoded'] = validate.paperless_billing.map({'Yes':1, 'No':0})
    validate['churn_encoded'] = validate.churn.map({'Yes':1, 'No':0})
    
    # Manually encode binary categorical variables for test
    test['gender_encoded'] = test.gender.map({'Female': 1, 'Male':0})
    test['partner_encoded'] = test.partner.map({'Yes':1, 'No':0})
    test['dependents_encoded'] = test.dependents.map({'Yes':1, 'No':0})
    test['phone_service_encoded'] = test.phone_service.map({'Yes':1, 'No':0})
    test['paperless_billing_encoded'] = test.paperless_billing.map({'Yes':1, 'No':0})
    test['churn_encoded'] = test.churn.map({'Yes':1, 'No':0})
    
    
    # use pd.get_dummies to encode nonbinary categorical variables for train
    dummy_train = pd.get_dummies(train[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'mapped_payment_type']],
                                  drop_first=True,
                                  dtype=int)
    
    # use pd.get_dummies to encode nonbinary categorical variables for validate
    dummy_validate = pd.get_dummies(validate[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'mapped_payment_type']],
                                  drop_first=True,
                                  dtype=int)
    
    # use pd.get_dummies to encode nonbinary categorical variables for test
    dummy_test = pd.get_dummies(test[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'mapped_payment_type']],
                                  drop_first=True,
                                  dtype=int)

    train = pd.concat([train, dummy_train], axis=1)
    validate = pd.concat([validate, dummy_validate], axis=1)
    test = pd.concat([test, dummy_test], axis=1)
    
    return train, validate, test

target = 'churn'