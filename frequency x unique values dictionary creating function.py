def valuexfrequency_dict(unique_values,column):
    my_dict=dict()
    for i in unique_values:
        my_dict.update({column.loc[column==i].count():i})
    return my_dict