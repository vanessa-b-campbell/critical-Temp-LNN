import time

import torch
import torch.optim as optim
from torch.utils.data import DataLoader

from FCNN.data import PDBDataset
from FCNN.model import FCNN
from FCNN.process import train, validation


model_type = 'classification'

## SET UP DATALOADERS: ---

# Build starting dataset:
dataset = PDBDataset("categorical_data/lipo_tri.csv")

# Number of datapoints in the training set:
n_train = int(len(dataset) * 0.8)

# Number of datapoints in the validation set:
n_val = len(dataset) - n_train

# Define pytorch training and validation set objects:
train_set, val_set = torch.utils.data.random_split(
    dataset, [n_train, n_val], generator=torch.Generator().manual_seed(42)
)

# Build pytorch training and validation set dataloaders:
train_dataloader = DataLoader(train_set, batch_size=32, shuffle=True)
val_dataloader = DataLoader(val_set, batch_size=32, shuffle=True)
 

## RUN TRAINING LOOP: ---

# Train with a random seed to initialize weights:
torch.manual_seed(0)

# Assign training to a device (often cpu when we are just starting out)
device = torch.device("cpu")

# Set up model:
if (model_type== 'classification') | (model_type== 'ordinal'):
    n_classes=len(dataset.df[dataset.df.columns[-1]].drop_duplicates().values)
    model = FCNN(hidden_layer_size=256,output_layer_size=n_classes)
else:
    model = FCNN(hidden_layer_size=256)

model.to(device)

# Set up optimizer:
optimizer = optim.Adagrad(model.parameters(), lr=0.1)

train_losses = []
val_losses = []

start_time = time.time()
for epoch in range(1, 10):
    
    
    train_loss = train(model, device, train_dataloader, optimizer, model_type)
    train_losses.append(train_loss)
    

    val_loss = validation(model, device, val_dataloader, epoch, model_type)
    val_losses.append(val_loss)

end_time = time.time()
print("Time Elapsed = {}s".format(end_time - start_time))

