from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import csv


#### 1. read in csv file using pandas- path goes in parentheses

#   workstation directory 
# raw_data = pd.read_csv("C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\csv_data\\No_outliers_smile_dataset.csv")
raw_data = pd.read_csv('/home/jbd3qn/Downloads/critical-Temp-LNN/val_full.csv')
#   Laptop directory
#raw_data = pd.read_csv("C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\csv_data\\clean_smile_dataset.csv")

input_smiles = raw_data['smiles'].tolist()
output_cTemp = raw_data['critical_temp'].tolist()

# zip input_smiles and cTemp into a list of tuples
raw_data_list = list(zip(input_smiles, output_cTemp))



clean_fingerprints_strings = []
clean_fingerprints = []

# mol to fingerprint parameters
fingerprint_radius = 2
fingerprint_size = 2048

# loop will go through each SMILE string in the clean dataset and convert them to MORGAN fingerprints
# fingerprints are an object of rdkit so they need to be converted into a list object then added to
# a clean fingerprint list
for smile in input_smiles:
    mol = Chem.MolFromSmiles(smile) 
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
    clean_fingerprints_strings.append(fingerprint.ToList())

# adding each to clean_fingerprint list
for each in clean_fingerprints_strings:
    clean_fingerprints.append(each)

for index in range(0,len(output_cTemp)):
        clean_fingerprints[index].append(output_cTemp[index])
        


with open('/home/jbd3qn/Downloads/critical-Temp-LNN/fingerprint_val_full.csv', 'w', newline = '') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(clean_fingerprints)


# fingerprint_data = pd.DataFrame(clean_fingerprints)
# # fingerprint_data.columns = ['fingerprints', 'c_temp']

# fingerprint_data.to_csv('/home/jbd3qn/Downloads/critical-Temp-LNN/fingerprint_test_full.csv', index=False)