def prep_iris():
    '''
    takes in iris df and returns a cleaned df
    '''
    #drops columns that aren't needed
    columns = ['species_id', 'measurement_id']
    iris_df.drop(columns, inplace=True, axis=1)
    #renames species column
    iris_df.rename(columns={'species_name':'species'} , inplace = True)
    # encode categorical variables
    dummy_df = pd.get_dummies(iris_df[['species']], dummy_na = False, drop_first=[True, True])
    iris_df = pd.concat([iris_df, dummy_df], axis = 1)
    return iris_df