# clean NIST dataset and save clean data as 
# 1. SMILES and temp in csv
# 2. fingerprints and temp csv
import csv
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd



#### 1. read in csv file using pandas
raw_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/tc_only.csv")

#raw_data.shape = (1214,2)





###### 2. convert csv file into a list of tuples

# first convert the first and second column into list
input_smiles = raw_data['SMILES'].tolist()
output_cTemp = raw_data['Tc'].tolist()

# zip input_smiles and cTemp into a list of tuples
raw_data_list = list(zip(input_smiles, output_cTemp))





###### 3. remove the 5 error types of smiles in data and creating a new list of tuples with clean SMILEs

# error causing SMILE string in dataset
bad_smiles = ['FAILED', '[HH]', 'FCl(F)F', 'FCl(F)(F)(F)F']

# creating clean data list
clean_data_list =[]

# loop will go through each item in the raw dataset and test if any of the SMILE strings match the error causing ones
# or if the string has a '.' inside it
# If the SMILE string does not have either, it will be added to the new clean dataset list
for item in raw_data_list:
    if item[0] not in bad_smiles:
        if '.' not in item[0]:
            clean_data_list.append(item)

# len(raw_data_list) = 1214
# len(clean_data_list) = 1156




###### 4. convert the clean SMILE strings into fingerprints
clean_fingerprints_strings = []
clean_fingerprints = []

# mol to fingerprint parameters
fingerprint_radius = 2
fingerprint_size = 2048

# loop will go through each SMILE string in the clean dataset and convert them to MORGAN fingerprints
# fingerprints are an object of rdkit so they need to be converted into a list object then added to
# a clean fingerprint list
for smile in clean_data_list:
    mol = Chem.MolFromSmiles(smile[0]) # index 0 because only want first coloumn 
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
    clean_fingerprints_strings.append(fingerprint.ToList())

# adding to clean_fingerprint list- I don't like chatGPT code here
clean_fingerprints = [[ int(num) for num in sublist] for sublist in clean_fingerprints_strings]





##### 5. combinging clean data with corresponding Tc 
clean_tc = []

# Clean SMILES and critical temp
for index in range(0,len(clean_data_list)):
    clean_tc.append(clean_data_list[index][1])
    
# Clean fingerprints and critical temp
for index in range(0,len(clean_tc)):
    clean_fingerprints[index].append(clean_tc[index])






##### 6. Create two new csv files. First will be on the clean SMILES/temp
# second will be the clean fingerprints/temp. 
# the first csv file should be organized identically to the original tc.cvs file 
# the second should model after the lipofilicity dataset 

filename_1 = 'clean_smile_dataset.csv'
filename_2 = 'clean_fgrPrnt_dataset.csv'


# with open(filename_1, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(clean_data_list)
# print(f"Data saved to {filename_1} successfully.")

# with open(filename_2, 'w', newline = '') as csvfile: 
#     writer = csv.writer(csvfile)
#     writer.writerows(clean_fingerprints)
# print(f"Data saved to {filename_2} successfully")

print("All good here")