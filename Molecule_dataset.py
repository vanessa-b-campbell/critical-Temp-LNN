# using rdkit convert SMILEs strings into something a .py file can actually use. 
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
IPythonConsole.ipython_useSVG=True  #< set this to False if you want PNGs instead of SVGs

import pandas as pd
import torch
from torch.utils.data import Dataset


class MoleculeDataset(Dataset):
    input_mol = []
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.input_smiles = self.data['SMILES'].tolist()
        self.output_cTemp = self.data['Tc'].tolist()
        
        for each in self.input_smiles:
            self.input_mol = Chem.MolFromSmiles(each)
        
    def __len__(self):
        return len(self.output_cTemp)



data = MoleculeDataset("C:/Users/color/Documents/Bilodeau_Research_Python/critical_temp_LNN/tc_only.csv")
print(len(data))
# dataset is 1214 x 2