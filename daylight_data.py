# using rdkit convert SMILEs strings into something a .py file can actually use. 
from rdkit import Chem
from rdkit.Chem import AllChem

import warnings
import pandas as pd

data = pd.read_csv("C:/Users/color/Documents/Bilodeau_Research_Python/critical_temp_LNN/tc_only.csv")

input_smiles = data['SMILES'].tolist()
output_cTemp = data['Tc'].tolist()

# removing the strings in the dataset that failed
string_to_remove = 'FAILED'
input_smiles = [item for item in input_smiles if item != string_to_remove]
# now length 1189

radius = 2
bit_length = 2048


input_fingerprints = []

for each in input_smiles:
    mol = Chem.MolFromSmiles(each)
    #might need number of atoms?
    fp = Chem.rdMolDescriptors.GetHashedTopologicalTorsionFingerprint(mol, nBits=bit_length, targetSize=4, includeChirality=False)
    input_fingerprints.append(fp)
