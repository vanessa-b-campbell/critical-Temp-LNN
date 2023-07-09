# create the distribution for size in data set


import numpy as np
import pandas as pd
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

# call in the clean smiles csv file
SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/clean_smile_dataset.csv")


########### 1. Get mol weight + get critical temp

# extract the critical temp column and keep the pandas object type
cTemp_list = SMILEs_data['critical_temp']



# get molecular descriptors from SMILEs
def RDkit_descriptors(smile):
    mols = [Chem.MolFromSmiles(i) for i in smile] 
    calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
    desc_names = calc.GetDescriptorNames()
    
    Mol_descriptors =[]
    for mol in mols:
        # Calculate all 200 descriptors for each molecule
        descriptors = calc.CalcDescriptors(mol)
        Mol_descriptors.append(descriptors)
    return Mol_descriptors,desc_names 


Mol_descriptors,desc_names = RDkit_descriptors(SMILEs_data['SMILEs'])

df_descriptors = pd.DataFrame(Mol_descriptors,columns=desc_names)

# pull out molwt: 
molWt = df_descriptors['MolWt']

# combine molWt and cTemp
molWt_tc_data = pd.concat([molWt, cTemp_list], axis = 1)

# create csv file for later referencing, (indexing is turned off (False))
molWt_tc_data.to_csv('molWt_tc_data.csv', index = False)





