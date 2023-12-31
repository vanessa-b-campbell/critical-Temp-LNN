# creating graphs of molWt/ Tc/ and others
# basic molwt/ tc stats as well using .describe()
# graphs are currently saved in D_graphs folder


# importing the molwt/ cTemp_list and all 209 descriptors from make_molwt.py 
from make_molwt import molWt, df_descriptors
import matplotlib.pyplot as plt

import pandas as pd

#print(df_descriptors.describe())

#print(molWt.describe())
# count    1156.000000
# mean      155.711547
# std       102.339623
# min         3.016029
# 25%        98.189000
# 50%       129.204500
# 75%       181.129500
# max       843.636000

# no_outliers = pd.read_csv('/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/No_outliers_smile_dataset.csv')
no_outliers = pd.read_csv('C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\Critical_Temp_Research\\critical-Temp-LNN\\csv_data\\No_outliers_smile_dataset.csv')

cTemp_list = no_outliers['critical_temp']

############## Create size distribution plot using matplotlib
plt.hist(molWt, bins = 25, edgecolor = 'black', color= '#A4B1FF')
plt.xlabel('Mol weight (amu)',fontsize=18)
plt.ylabel('frequency',fontsize=18)
plt.title('Primarly Small Molecules Around 155 amu',fontsize=18)
plt.show()


############## Create critical temp distribution plot using matplotlib
plt.hist(cTemp_list, bins = 25, edgecolor = 'black', color= '#A4B1FF')
plt.xlabel('critical temp (K)',fontsize=18)
plt.ylabel('frequency',fontsize=18)
plt.title('Critial Temperature Data: Average around 600 K',fontsize=18)
plt.show()

#print(cTemp_list.describe())
# count    1156.000000
# mean      602.708768
# std       240.781564
# min         3.300000
# 25%       509.250000
# 50%       602.100000
# 75%       692.332500
# max      7020.000000




############## Create Tc vs molwt graph
# plt.scatter(molWt, cTemp_list, color= '#A9369E')
# plt.xlabel('Mol weight (amu)')
# plt.ylabel('Critical temperature (K)')
# plt.title('Critical Temperature (K) vs Molecular size (amu): cc = 0.215')
# plt.show()





# ############# extract valence electrons, create a distribution curve,
# #                   then a tc vs ve- plot

# num_V_electrons = df_descriptors['NumValenceElectrons']

# # distribution
# plt.hist(num_V_electrons, bins = 50, edgecolor = 'black')
# plt.xlabel('number of valence electrons')
# plt.ylabel('frequency')
# plt.title('number of valence electrons')
# plt.show()

# # tc vs val electrons
# plt.scatter(num_V_electrons, cTemp_list)
# plt.xlabel('number of valence electrons')
# plt.ylabel('Critical temperature (K)')
# plt.title('Critical Temperature (K) vs number of valence electrons')
# plt.show()




# ################### mol weight vs num of val electrons
# plt.scatter(molWt, num_V_electrons)
# plt.ylabel('number of valence electrons')
# plt.xlabel('Mol weight (amu)')
# plt.title('number of valence electrons vs Mol weight (amu) ')
# plt.show()




# ############## NumRadicalElectrons vs tc
# NumRadicalElectrons = df_descriptors['NumRadicalElectrons']

# plt.scatter(NumRadicalElectrons, cTemp_list)
# plt.xlabel('Num Radical Electrons')
# plt.ylabel('Critical temperature (K)')
# plt.title('Critical temperature (K) vs Num Radical Electrons: cc= 0.758')
# plt.show()