# clean this wack ass dataset

from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd

#### 1. read in csv file using pandas
raw_data = pd.read_csv("C:/Users/color/Documents/Bilodeau_Research_Python/critical_temp_LNN/tc_only.csv")


#### 2. convert csv file into dictionary with SMILEs the keys and Tc the cooresponding values

# first convert the first and second column into list
input_smiles = raw_data['SMILES'].tolist()
output_cTemp = raw_data['Tc'].tolist()

# deleting  Unusual charge on atom 6 number of radical electrons set to zero Datapoints
for index in range(1111, 1118,1):
    print("Removed SMILEs with '.': {}".format(input_smiles[index]))
    del input_smiles[index]
    del output_cTemp[index]
for index in range(1125, 1128,1):
    print("Removed SMILEs with '.': {}".format(input_smiles[index]))
    del input_smiles[index]
    del output_cTemp[index]

# then into a dictionary using the zip() function
raw_data_dict = dict(zip(input_smiles, output_cTemp))



#### 3. Remove 'FAILED' SMILE string/ WARNING SMILE string/ ERROR SMILE string
if 'FAILED' in raw_data_dict: 
    print("removed failed smiles: {}".format(raw_data_dict['FAILED']))
    del raw_data_dict['FAILED']


if '[HH]' in raw_data_dict: 
    print("removed [HH] smiles: {}".format(raw_data_dict['[HH]']))
    del raw_data_dict['[HH]']

if 'FCl(F)F' in raw_data_dict: 
    print("removed FCl(F)F smiles: {}".format(raw_data_dict['FCl(F)F']))
    del raw_data_dict['FCl(F)F']

if 'FCl(F)(F)(F)F' in raw_data_dict: 
    print("removed FCl(F)(F)(F)F smiles: {}".format(raw_data_dict['FCl(F)(F)(F)F']))
    del raw_data_dict['FCl(F)(F)(F)F']


#### 4. convert dictionary keys into finger prints- 
####    then create new dictionary with fingerprints as the keys and Tc is the value

# mol to fingerprint parameters
fingerprint_radius = 2
fingerprint_size = 2048


critical_temp = []
input_fingerprints = []


# loop through each molecule's SMILES string
for k,v in raw_data_dict.items():
    try:
        mol = Chem.MolFromSmiles(k)
        fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
        
        input_fingerprints.append(fingerprint.ToList())
        critical_temp.append(v)
        
    except Exception as e:
        print(f"Error at key {k}: {v}-{e}")
    

# check
# for key, value in raw_fingerprint_dict.items():
#     print("{} {}".format(key, value))
for each in input_fingerprints:
    print(input_fingerprints)

fingerprint_temp_csv = []
for each in input_fingerprints:
    fingerprint_temp_csv= [input_fingerprints, critical_temp]

print(fingerprint_temp_csv)