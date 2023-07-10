from rdkit import Chem
import pandas as pd 

# use PubChem to convert target functional groups into smile strings
# then turn those into patterns Rdkit recognizes inside the clean_smile_dataset
# using substructure searching

# bring in the clean smiles- make the SMILES as a list
SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/clean_smile_dataset.csv")



smiles_list = SMILEs_data['SMILEs'].tolist()

# benzene, phenol group, carboxylic acid, amine
func_group_list = ['C1=CC=C(C=C1)O', 'C1=CC=CC=C1']


big_list = []

# Will need a list of pattern SMILE string
# loop through each dataset smile for a given pattern
# if true the name of the smile string, and maybe even the critical temp corresponding to it, 
# needs to be added or put somewhere identifying it....
# make a matrix? indexing will get ugly... debugging a nightmare


for smile in smiles_list:
    for pattern in func_group_list:

        mol = Chem.MolFromSmiles(smile)

        if mol.HasSubstructMatch(Chem.MolFromSmiles(pattern)):        # will return a true or false
            big_list.append(smile)
            big_list.append(pattern)
            
print(big_list)

