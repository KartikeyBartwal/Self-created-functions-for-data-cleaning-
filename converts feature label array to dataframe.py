def form_dataframe(features,label,feature_col_name,label_col_name):
    features=pd.DataFrame(features,columns=feature_col_name)
    features.reset_index(drop=True,inplace=True)
    label=pd.DataFrame(label,columns=label_col_name)
    label.reset_index(drop=True,inplace=True)
    return pd.concat([features,label],axis=1)