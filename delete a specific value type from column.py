def replace_valuetype_column(column,value_type_name,dataframe):
    value_indexes= dataframe[column].loc[dataframe[column]==value_type_name].index
    dataframe.drop(value_indexes,axis=0,inplace=True)
    dataframe.reset_index(drop=True,inplace=True)