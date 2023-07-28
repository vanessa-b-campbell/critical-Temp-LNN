import pandas as pd
import torch
from torch.utils.data import Dataset

# 1. Defines the dataset as a class 
# 2. separate into test, train, validation data
# 3. seperates the data into input vectors and output targets
# 4. creates 2 attributes: 
#           -output the number of samples
#           -display the input vector of a given index and disply the output value at a given index

# takes in molecular fingerprints as input_vector
class MoleculeDataset(Dataset):
    input_mol = []
    def __init__(self, path):
        self.data = pd.read_csv(path)
        #print(self.data.shape)
        
        self.input_vector = self.data[self.data.columns[0:-1]].values   
        self.output_targets = self.data[self.data.columns[-1]].values

    
    def __len__(self):
        return len(self.output_targets)
    
    def __getitem__(self, index):
        x = self.input_vector[index]
        y = self.output_targets[index]

        return torch.tensor(x, dtype = torch.float32), torch.tensor(y, dtype = torch.float32)

# [1155 rows, 2049 columns]


#   laptop path:
# data = MoleculeDataset("C:/Users/color/Documents/Bilodeau_Research_Python/critical_temp_LNN/tc_only.csv")

#   workstation path
data = MoleculeDataset("/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/clean_fgrPrnt_datasets.csv")

#   testing prints
# print(len(data))
# print(data.input_vector[55])
# print(data.output_targets[55])

print("all good in the hood")