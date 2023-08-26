def EDA(column_name): 
            print(column_name.describe(),"\n")
            print("frequency:","\n",column_name.value_counts(),"\n")
            unique=list(pd.unique(column_name))
            unique.sort()
            print(len(unique))
            print(unique)