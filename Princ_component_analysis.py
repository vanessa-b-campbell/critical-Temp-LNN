# attempting to use princial component analysis to see if I can extrat more info from the 209 columns of descriptors


from make_molwt import df_descriptors, cTemp_list, molWt
import numpy as np
from sklearn.decomposition import PCA

c = df_descriptors['MolWt']
other_c_data = cTemp_list

data_1 = np.array(c)