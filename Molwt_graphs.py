
from make_molwt import molWt, cTemp_list, df_descriptors
import matplotlib.pyplot as plt






############## 2. Create size distribution plot using matplotlib
plt.hist(molWt, bins = 50, edgecolor = 'black')
plt.xlabel('Mol weight (amu)')
plt.ylabel('frequency')
plt.title('Size distribution (amu)')
plt.show()






############## 3. Create Tc vs molwt graph
#molWt_tc_data
plt.scatter(molWt, cTemp_list)
plt.xlabel('Mol weight (amu)')
plt.ylabel('Critical temperature (C)')
plt.title('Critical Temperature (C) vs Molecular size (amu)')
plt.show()
# how to get list of statistics, ie mean, median





############# 4. extract valence electrons, create a distribution curve,
#                   then a tc vs ve- plot

num_V_electrons = df_descriptors['NumValenceElectrons']

# distribution
plt.hist(num_V_electrons, bins = 50, edgecolor = 'black')
plt.xlabel('number of valence electrons')
plt.ylabel('frequency')
plt.title('number of valence electrons')
plt.show()

# tc vs val electrons
plt.scatter(num_V_electrons, cTemp_list)
plt.xlabel('number of valence electrons')
plt.ylabel('Critical temperature (C)')
plt.title('Critical Temperature (C) vs number of valence electrons')
plt.show()




################### mol weight vs num of val electrons
plt.scatter(molWt, num_V_electrons)
plt.ylabel('number of valence electrons')
plt.xlabel('Mol weight (amu)')
plt.title('number of valence electrons vs Mol weight (amu) ')
plt.show()




############## NumRadicalElectrons vs tc
NumRadicalElectrons = df_descriptors['NumRadicalElectrons']

plt.scatter(NumRadicalElectrons, cTemp_list)
plt.xlabel('Num Radical Electrons')
plt.ylabel('Critical temperature (C)')
plt.title('Critical temperature (C) vs Num Radical Electrons ')
plt.show()