def filter_frequency(frequency_array,threshold):
    filtered_frequency=[]
    for i in frequency_array:
        if i>threshold:
            filtered_frequency.append(i)
    return filtered_frequency