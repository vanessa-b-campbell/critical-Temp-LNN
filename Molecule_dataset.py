# using rdkit convert SMILEs strings into something a .py file can actually use. 

import pandas as pd
import torch
from torch.utils.data import Dataset


class MoleculeDataset(Dataset):
    input_mol = []
    def __init__(self, path):
        self.data = pd.read_csv(path)
        print(self.data.shape)
        
        self.input_vector = self.data[self.data.columns[0:-1]].values

        # very last column is the output target (the y)
        self.output_targets = self.data[self.data.columns[-1]].values

    
    def __len__(self):
        return len(self.output_targets)
    
    def __getitem__(self, index):
        x = self.input_vector[index]
        y = self.output_targets[index]

        return torch.tensor(x, dtype = torch.float32), torch.tensor(y, dtype = torch.float32)

#   laptop path:
# data = MoleculeDataset("C:/Users/color/Documents/Bilodeau_Research_Python/critical_temp_LNN/tc_only.csv")

data = MoleculeDataset("/home/jbd3qn/Downloads/clean_fgrPrnt_dataset.csv")
print(len(data))

