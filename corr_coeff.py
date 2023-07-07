#%%
from make_molwt import df_descriptors, cTemp_list, molWt
import numpy as np


#%%

correlation_matrix = np.corrcoef(molWt, cTemp_list)
corr_coeff = correlation_matrix[0, 1]  # Extract the coefficient between X and Y

print(corr_coeff)







#%%
# Pearson's correlation coefficient calculator
# want to loop through each column and calculate the value
# make condition for loop to add name of column to list if >= 0.4

# convert to arrays? 


best_cor = []

bad_descript = []
# for each in bad_descript:
#     df = df_descriptors.drop(each, axis = 1)

for column in df_descriptors.columns:

    try:
        column_data = df_descriptors[column]
        correlation_matrix = np.corrcoef(column_data, cTemp_list)
        corr_coeff = correlation_matrix[0, 1]  # Extract the coefficient between X and Y
    
        if corr_coeff > 0.4:
            best_cor.append(column)
    
    except: 
        bad_descript.append(column)


print("best corr: {}".format(best_cor))
print("bad_descript: {}".format(bad_descript))