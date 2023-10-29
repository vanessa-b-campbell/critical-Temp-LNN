# training function: for epoch in range- train the model- calculate the loss 
import time
import matplotlib.pyplot as plt

import torch
import torch.optim as optim
from torch.utils.data import DataLoader


from model_data_object import MoleculeDataset
from model_object import TempNet
from model_process import train, validation, predict

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error



## SET UP DATALOADERS: ---

#%%
# c_temp_dataset = MoleculeDataset('/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/no_outliers_fgprnt_data.csv')
# #%%
# # SPLITTING THE DATASET INTO TEST, TRAIN, VALIDATE 

# d_train_val = int(len(c_temp_dataset)* 0.8) #train and validation combined- 80% of dataset #(924 molecules)

# d_test = len(c_temp_dataset) - d_train_val  # testing- 20% of dataset 
# #(232 molecules)

# d_train = int(d_train_val*0.8) #training - 80% of t and v combined (64% of total dataset) 
# #(739 molecules)

# d_val = d_train_val - d_train #validation 16% of total data 
# #(185 molecules)

# # Define pytorch training and validation set objects:
# # also random seeded split
# train_set, val_set, test_set = torch.utils.data.random_split(
#     c_temp_dataset, [d_train, d_val, d_test], generator=torch.Generator().manual_seed(0)
# )
d_test = MoleculeDataset('/home/jbd3qn/Downloads/critical-Temp-LNN/fingerprint_test_full.csv')
test_set = torch.utils.data.dataset.Subset(d_test, range(0, len(d_test)))


d_train = MoleculeDataset('/home/jbd3qn/Downloads/critical-Temp-LNN/fingerprint_train_full.csv')
train_set = torch.utils.data.dataset.Subset(d_train, range(0, len(d_train)))

d_val = MoleculeDataset('/home/jbd3qn/Downloads/critical-Temp-LNN/fingerprint_val_full.csv')
val_set = torch.utils.data.dataset.Subset(d_val, range(0, len(d_val)))

# Train with a random seed to initialize weights:
torch.manual_seed(0)

# Assign training to a device (often cpu when we are just starting out)
device = torch.device("cpu")


#################################################################################### hyperparameters
hidden_layer_size_1 = 5
hidden_layer_size_2 = 5
hidden_layer_size_3 = 5
hidden_layer_size_4 = 5
hidden_layer_size_5 = 5
model = TempNet(hidden_layer_size_1, hidden_layer_size_2,hidden_layer_size_3,hidden_layer_size_4,hidden_layer_size_5)
model.to(device)
epoch = 300
learn_rate = 0.0001
batch_size = 3




# Build pytorch training and validation set dataloaders:
train_dataloader = DataLoader(train_set, batch_size, shuffle=True)
val_dataloader = DataLoader(val_set, batch_size, shuffle=True)
test_dataloader = DataLoader(test_set, batch_size, shuffle=False)


## RUN TRAINING LOOP: ---

# Set up optimizer:
optimizer = optim.Adam(model.parameters(), lr = learn_rate) # learning rate ex: 1*10^-3

train_losses = []
val_losses = []
test_losses = []

start_time = time.time()



for e in range(1,epoch+1):
    
    train_loss = train(model, device, train_dataloader, optimizer, e)
    train_losses.append(train_loss)
    
    val_loss = validation(model, device, val_dataloader, e)
    val_losses.append(val_loss)

end_time = time.time()
print("Time Elapsed = {}s".format(end_time - start_time))





# Model Statistics
input_all, target_all, pred_prob_all = predict(model, device, test_dataloader)

print("input_all: {i}".format(i = input_all))
print("target_all: {t}".format(t = target_all))
print("pred_prob_all: {p}".format(p = pred_prob_all))

r2_function = r2_score(target_all, pred_prob_all)
mae = mean_absolute_error(target_all, pred_prob_all)
rmse = mean_squared_error(target_all, pred_prob_all, squared=False)

# only a few digits are relevant
print("R2 Score: {:.4f}".format(r2_function))
print("MAE: {:.4f}".format(mae))
print("RMSE: {:.4f}".format(rmse))

# plotting loss vs epochs for validation and training
#fig1 = plt.figure()
plt.plot(train_losses, label ='train losses')
plt.legend()
plt.xlabel('time')
plt.ylabel('train losses')

#fig2 = plt.figure()
plt.plot(val_losses, label ='validation losses')
plt.legend()
plt.xlabel('time')
plt.ylabel('losses')
plt.title('FCNN')
# Create a textbox using the text() function
textbox_x = 40
textbox_y = 80
plt.text(textbox_x, textbox_y, "epoch: {}\n lr: {}\n batch size: {}\n hl size: {},{},{},{}, {}"\
    .format(epoch,learn_rate,batch_size,hidden_layer_size_1, hidden_layer_size_2,hidden_layer_size_3,hidden_layer_size_4,hidden_layer_size_5), \
        bbox=dict(facecolor='white', edgecolor='black'))

plt.show()

# validation scatter 
# plt.figure(figsize=(4, 4), dpi=100)
# plt.scatter(target_all, pred_prob_all, alpha=0.3)
# plt.plot([min(target_all), max(target_all)], [min(target_all),
#     max(target_all)], color="k", ls="--")
# plt.xlim([min(target_all), max(target_all)])
# plt.xlabel("True Values")
# plt.ylabel("Predicted Values")
# plt.title("Validation scatter\nFCNN \n R2 Score: {:.4f} \n MAE: {:.4f} \n RMSE: {:.4f}".format(r2_function,mae,rmse))
# plt.show()

# testing scatter
hex_color = '#B65DCA'
legend_text = "FCNN \n R2 Score: {:.4f} \n MAE: {:.4f} \n RMSE: {:.4f}".format(r2_function,mae,rmse)
# Convert the hex code to an RGB tuple
rgb_color = tuple(int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5))
plt.figure(figsize=(4, 4), dpi=100)
plt.scatter(target_all, pred_prob_all, c=[rgb_color], alpha=0.75)
plt.plot([min(target_all), max(target_all)], [min(target_all),
    max(target_all)], color="k", ls="--")
plt.xlim([min(target_all), max(target_all)])
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
# plt.legend([legend_text], loc="lower right")
plt.title('FCNN testing performance (predicted vs true)')
plt.show()

# %%
