#%%
from make_molwt import df_descriptors, cTemp_list, molWt
import numpy as np

numradelec = df_descriptors['NumRadicalElectrons']

maxpartcharg = df_descriptors['MaxPartialCharge']
df_descriptors.drop('MaxPartialCharge', axis = 1)
#%%

correlation_matrix = np.corrcoef(numradelec, cTemp_list)
corr_coeff = correlation_matrix[0, 1]  # Extract the coefficient between X and Y

print(corr_coeff)







#%%
# Pearson's correlation coefficient calculator
# want to loop through each column and calculate the value
# make condition for loop to add name of column to list if >= 0.4

# convert to arrays? 

best_cor = []
dont_care = []
bad_descript = []
# for each in bad_descript:
#     df = df_descriptors.drop(each, axis = 1)

for column in df_descriptors.columns:


    column_data = df_descriptors[column]
    correlation_matrix = np.corrcoef(column_data, cTemp_list)
    corr_coeff = correlation_matrix[0, 1]  # Extract the coefficient between X and Y

    if np.isnan(corr_coeff):
        bad_descript.append(column)
        # df_descriptors.drop(column, axis = 1, inplace= True)


    elif corr_coeff <= 0.4:
        dont_care.append(column)
        

    else:
        best_cor.append(column)
        # best_cor.append(corr_coeff)
    

    # except RuntimeWarning: 
    #     print('Bad description')
    #     bad_descript.append(column)
    #     df_descriptors = df_descriptors.drop(column, axis = 1)

# print(df_descriptors['fr_phos_acid'])
for thing in best_cor:
    print("best corr: {}".format(thing))

for each in bad_descript:
    print("bad_descript: {}".format(each))
# %%
if (len(best_cor)+ len(bad_descript)+ len(dont_care) ) == len(df_descriptors.columns):
    print("yes")
else:
    print("you fucked up")

print(len(best_cor))
print(len(bad_descript))
print(len(dont_care))
print(len(df_descriptors.columns))

print(best_cor)