def threshold_filter(column,data_frame,min_threshold,max_threshold):
    outlier_indexes=np.array([])
    for i in data_frame[column].values:
        if i  < min_threshold:
            data_frame=data_frame[data_frame[column]!=i]
        
        elif i > max_threshold:
            data_frame=data_frame[data_frame[column]!=i]
        
        else:
            pass
    return data_frame