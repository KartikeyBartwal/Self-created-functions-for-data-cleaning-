 '''
Note: Please import the following libraries before using the functions: statistics, maths
'''



#Creating a function to find outlier values in a column
#Creating a function to find outlier values in a column
def column_outlier_values(column,df):
    outlier_values=[]
    threshold=3
    mean=statistics.mean(column.values)
    variance=statistics.variance(column.values)
    std=math.sqrt(variance)
    for i in column.values:
        z_score= (i-mean)/std
        if abs(z_score) > threshold:
            outlier_values.append(i)
    return outlier_values




#Function to find the indexes of the outlier values in a column
#Function to find the indexes of the outlier values in a column
def column_outlier_indexes(column,df):
    universal_outlier_indexes=[]
    #target values whose index we need to find
    outlier_value_list=[]
    outlier_value_list=outlier_value_list + column_outlier_values(column,df)
    #index column for original dataframe
    df["index_for_outlier_removal"]=df.index
    #finding the indexex of target values
    for i in outlier_value_list:
        target_row_i=df.loc[column==i]
        required_index_i=target_row_i["index_for_outlier_removal"]
        required_index_i=int(required_index_i)
        universal_outlier_indexes.append(required_index_i)
    df.drop(df[["index_for_outlier_removal"]],axis=1,inplace=True)
    return universal_outlier_indexes





# This function will directly give you the index of the outliers in a column of a dataframe. 
# This function will directly give you the index of the outliers in a column of a dataframe. 
def column_outlier_value_indexes(column,df):
    outlier_values=[]
    threshold=3
    mean=statistics.mean(column.values)
    variance=statistics.variance(column.values)
    std=math.sqrt(variance)
    for i in column.values:
        z_score= (i-mean)/std
        if abs(z_score) > threshold:
            outlier_values.append(i)
    outlier_indexes=[]
    outlier_value_list=outlier_values
    df["index_for_outlier_removal"]=df.index
    for i in outlier_value_list:
        target_row_i=df.loc[column==i]
        required_index_i=target_row_i["index_for_outlier_removal"]
        required_index_i=int(required_index_i)
        outlier_indexes.append(required_index_i)
    df.drop(outlier_indexes,axis=0,inplace=True)
    return df