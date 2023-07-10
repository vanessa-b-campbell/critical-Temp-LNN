from make_molwt import df_descriptors, cTemp_list
import numpy as np


########### For rapid single use correlation coefficient finder with tc:
name = "molWt and Tc"
c = df_descriptors['MolWt']
other_c_data = cTemp_list

c_matrix = np.corrcoef(c, other_c_data)       # correlation coefficient math, thank you ChatGPT
corr_coefficient = c_matrix[0, 1] 

print("{}: {}".format(name, corr_coefficient ))

########################################
