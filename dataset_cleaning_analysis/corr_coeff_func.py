import numpy as np

########### For rapid single use correlation coefficient finder with tc:
def corr_coeff_func(column_1, column_2, corr_name):

    c_matrix = np.corrcoef(column_1, column_2)       # correlation coefficient math, thank you ChatGPT
    corr_coefficient = c_matrix[0, 1] 

    print("{}: {}".format(corr_name, corr_coefficient ))

########################################

