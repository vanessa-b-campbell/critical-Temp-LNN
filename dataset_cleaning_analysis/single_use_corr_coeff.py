from make_molwt import df_descriptors, cTemp_list
import numpy as np


########### For rapid single use correlation coefficient finder with tc:
name = "molWt and Tc"
column_1 = df_descriptors['MolWt']
column_2 = cTemp_list

c_matrix = np.corrcoef(column_1, column_2)       # correlation coefficient math, thank you ChatGPT
corr_coefficient = c_matrix[0, 1] 

print("{}: {}".format(name, corr_coefficient ))

########################################

