from make_molwt import df_descriptors, cTemp_list, molWt
import numpy as np

# Pearson's correlation coefficient calculator
# want to loop through each column and calculate the value
# make condition for loop to add name of column to list if >= 0.4

# bad_descript is a bad molecular description that cannot make a correlation coefficient with Tc
# dont_care is any correlation coefficient less than 0.4
# best_cor is any molecular description that has a correlation coefficient greater than 0.4
best_cor = []
dont_care = []
bad_descript = []

# lopping through the string columns
for column in df_descriptors.columns:


    column_data = df_descriptors[column]                            # getting the data in the column from each column's name
    correlation_matrix = np.corrcoef(column_data, cTemp_list)       # correlation coefficient math, thank you ChatGPT
    corr_coeff = correlation_matrix[0, 1]                           # Extract the coefficient between X and Y

    # if the data in the column cannot make a correlation coefficient with temp (give nan) add to bad_descript list
    if np.isnan(corr_coeff):
        bad_descript.append(column)

    # else if add correlation coefficients to dont_care if less than 0.4
    elif corr_coeff < 0.4:
        dont_care.append(column)
        
    # add anything left to best _cor
    else:
        best_cor.append(column)
        best_cor.append(corr_coeff)

    

# print each list for checking
print("best corr count: {}".format(len(best_cor)-1))
print("don't care count: {}".format(len(dont_care)))
print("bad_descript count: {}".format(len(bad_descript)))


# confirming that all descriptors are accounted for and are getting caught by a conditional 
if (len(best_cor)/2+ len(bad_descript)+ len(dont_care) ) == len(df_descriptors.columns):
    print("All descriptors are accounted for.")
else:
    print("you fucked up. Missing decriptors.")


# printing the best of the best
print("Best correltations: {}".format(best_cor))


