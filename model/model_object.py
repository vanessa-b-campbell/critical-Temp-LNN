# the nn model

import torch.nn as nn
import torch.nn.functional as F

# dataset is [1155 rows, 2049 columns]
# training set input vector is 2048 columns
# training set outout targets is a 1 column

class TempNet(nn.Module):
    def __init__(self, hidden_layer_size_1 = 256, hidden_layer_size_2 = 256, hidden_layer_size_3 = 256):
        super(TempNet, self).__init__()
        # super is saying that class TempNet is inheriting traits from nn.Module class
        
        input_size = 2048 
        output_size = 1

        # two linear layers - nn.Linear(size of dataset, size of output)
        # self.fc1 = nn.Linear(input_size, hidden_layer_size_1)
        # self.fc2 = nn.Linear(hidden_layer_size_1, output_size)

        
        self.fc1 = nn.Linear(input_size, hidden_layer_size_1) #(raw training dataset)
        # nn.Linear(size of dataset, size of output)
        self.fc2_a = nn.Linear(hidden_layer_size_1, hidden_layer_size_2)
        self.fc2_b = nn.Linear(hidden_layer_size_2, hidden_layer_size_3)
    
        self.fc2 = nn.Linear(hidden_layer_size_3, output_size) 
    


    def forward(self, x):
        # x = self.fc1(x)
        # x = F.relu(x)
        # x = self.fc2(x)

        x = self.fc1(x)
        x = F.relu(x)

        x = self.fc2_a(x)
        x = F.relu(x)

        x = self.fc2_b(x)
        x = F.relu(x)

        x = self.fc2(x)
        # output will have the same dimensions as the target output (1)
        return x #output 
    

# testing 
model = TempNet()
#print(model)

print("model object is good")