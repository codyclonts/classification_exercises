def clean_iris(df):
    '''
    takes in iris df and returns a cleaned df
    '''
    #drops columns that aren't needed
    columns = ['species_id', 'measurement_id']
    df.drop(columns, inplace=True, axis=1)
    #renames species column
    df.rename(columns={'species_name':'species'} , inplace = True)
    # encode categorical variables
    dummy_df = pd.get_dummies(iris_df[['species']], dummy_na = False, drop_first=[True, True])
    df = pd.concat([iris_df, dummy_df], axis = 1)
    return df




    ## train, test, split iris df

    def split_iris_data(df):
    train_validate, test = train_test_split(df, test_size = .2, random_state=123, stratify = df.species)
    train, validate = train_test_split(train_validate,
                                       test_size = .3, 
                                       random_state = 123, 
                                       stratify = train_validate.species)
    return train, validate, test

  

## prep iris data

    def prep_iris(df):
    clean_iris(df)
    train, validate, test = split_iris_data(df)
    return train, validate, test


    ############## TELCO DATA PREPARE#########


    def split_telco_data(df):
    '''
    This function performs split on telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test




    def prep_telco_data(df):
    #drop columns that aren't necessary 
    
    columns = ['customer_id', 'payment_type_id', 'internet_service_type_id' , 'contract_type_id']
    df.drop(columns, inplace = True, axis = 1)
    
    #fix total charges
    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    df['total_charges'] = df.total_charges.astype(float)
    
    #get dummy variables
    dummy_df = pd.get_dummies(df[['gender', \
                                 'partner', \
                                 'dependents', \
                                 'phone_service', \
                                 'paperless_billing', \
                                 'churn', \
                                 'multiple_lines', \
                                 'online_security', \
                                 'device_protection', \
                                 'tech_support', \
                                 'streaming_tv', \
                                 'streaming_movies', \
                                 'contract_type', \
                                 'internet_service_type', \
                                 'payment_type']], dummy_na=False, \
                              drop_first=True)
    
    df = pd.concat([df, dummy_df], axis = 1)
    
    ## split the data
    train, validate, test = split_telco_data
    
    return train, validate, test
    






