# clean this wack ass dataset


from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd

#### 1. read in csv file using pandas
raw_data = pd.read_csv("/home/jbd3qn/Downloads/tc_only.csv")



# mol to fingerprint parameters
fingerprint_radius = 2
fingerprint_size = 2048


#### 2. convert csv file into a list of tuples

# first convert the first and second column into list
input_smiles = raw_data['SMILES'].tolist()
output_cTemp = raw_data['Tc'].tolist()


raw_data_list = list(zip(input_smiles, output_cTemp))
bad_smiles = ['FAILED', '[HH]', 'FCl(F)F', 'FCl(F)(F)(F)F']


clean_data_list =[]
clean_fingerprints = []



for item in raw_data_list:
    if item[0] not in bad_smiles:
        if '.' not in item[0]:
            clean_data_list.append(item)


for smile, temp in clean_data_list:
    print(smile, temp)


for smile in clean_data_list:
    mol = Chem.MolFromSmiles(smile[0])
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
    clean_fingerprints.append(fingerprint.ToList())

for fPrint in clean_fingerprints:
    print(fPrint)


# input_fingerprints = []

# # mol to fingerprint parameters
# fingerprint_radius = 2
# fingerprint_size = 2048

# for smile, temp in clean_data_list:

#     mol = Chem.MolFromSmiles(smile)
#     fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
#     input_fingerprints.append(fingerprint.ToList())
