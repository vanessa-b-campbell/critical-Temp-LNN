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
c_temp_dataset = MoleculeDataset('/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/clean_fgrPrnt_datasets.csv')
#%%
# SPLITTING THE DATASET INTO TEST, TRAIN, VALIDATE 

d_train_val = int(len(c_temp_dataset)* 0.8) #train and validation combined- 80% of dataset #(924 molecules)

d_test = len(c_temp_dataset) - d_train_val  # testing- 20% of dataset 
#(232 molecules)

d_train = int(d_train_val*0.8) #training - 80% of t and v combined (64% of total dataset) 
#(739 molecules)

d_val = d_train_val - d_train #validation 16% of total data 
#(185 molecules)

# Define pytorch training and validation set objects:
# also random seeded split
train_set, val_set, test_set = torch.utils.data.random_split(
    c_temp_dataset, [d_train, d_val, d_test], generator=torch.Generator().manual_seed(0)
)



# Train with a random seed to initialize weights:
torch.manual_seed(0)

# Assign training to a device (often cpu when we are just starting out)
device = torch.device("cpu")
#################################################################################### hyperparameters

big_r_squared = 0
best_hid_lay_num_1 = 5
best_hid_lay_num_2 = 5 
best_hid_lay_num_3 = 5
best_hid_lay_num_4 = 5
best_hid_lay_num_5 = 5
best_batch = 3
best_epoch = 100
best_learn_rate = 0

for hidden_layer_size_1 in range(5,50,5):
    for hidden_layer_size_2 in range(5,50,5):
        for hidden_layer_size_3 in range(5,50,5):
            for hidden_layer_size_4 in range(5,50,5):
                for hidden_layer_size_5 in range(5,50,5):
                    for batch_size in range(3, 9, 3):
                        for epoch in range(100, 500, 100):
                            learn_range = (x * 0.0001 for x in range(1, 10, 9))
                            for learn_rate in learn_range:

                            
                                model = TempNet(hidden_layer_size_1, hidden_layer_size_2,hidden_layer_size_3,hidden_layer_size_4,hidden_layer_size_5)
                                model.to(device)
                                #epoch = 50
                                #learn_rate = 0.001
                                #batch_size = 4


                                # Build pytorch training and validation set dataloaders:
                                train_dataloader = DataLoader(train_set, batch_size, shuffle=True)
                                val_dataloader = DataLoader(val_set, batch_size, shuffle=True)


                                ## RUN TRAINING LOOP: ---

                                # Set up optimizer:
                                optimizer = optim.Adam(model.parameters(), lr = learn_rate) # learning rate ex: 1*10^-3
                                train_losses = []
                                val_losses = []
                                start_time = time.time()

                                for e in range(1,epoch+1):
                                    
                                    train_loss = train(model, device, train_dataloader, optimizer, e)
                                    train_losses.append(train_loss)
                                    
                                    val_loss = validation(model, device, val_dataloader, e)
                                    val_losses.append(val_loss)

                                end_time = time.time()
                                print("Time Elapsed = {}s".format(end_time - start_time))


                                # Model Statistics

                                input_all, target_all, pred_prob_all = predict(model, device, val_dataloader)

                                r2_function = r2_score(target_all, pred_prob_all)
                                if r2_function > big_r_squared:
                                    big_r_squared = r2_function
                                    best_hid_lay_num_1 = hidden_layer_size_1 
                                    best_hid_lay_num_2 = hidden_layer_size_2 
                                    best_hid_lay_num_3 = hidden_layer_size_3
                                    best_hid_lay_num_4 = hidden_layer_size_4
                                    best_hid_lay_num_5 = hidden_layer_size_5
                                    best_batch = batch_size
                                    best_epoch = epoch
                                    best_learn_rate = learn_rate

                                mae = mean_absolute_error(target_all, pred_prob_all)
                                rmse = mean_squared_error(target_all, pred_prob_all, squared=False)

# only a few digits are relevant
print("R2 Score: {:.4f}".format(big_r_squared))
print("MAE: {:.4f}".format(mae))
print("RMSE: {:.4f}".format(rmse))
#%%
print("Best Hidden Layer Numbers (1-5): {},{},{},{},{}".format(best_hid_lay_num_1,best_hid_lay_num_2,best_hid_lay_num_3,best_hid_lay_num_4,best_hid_lay_num_5))
print("Best Batch Size: {:.4f}".format(best_batch))
print("Best epoch size: {:.4f}".format(best_epoch))
print("Best learn rate: {:.4f}".format(best_learn_rate))


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

# Create a textbox using the text() function
textbox_x = 40
textbox_y = 80
plt.text(textbox_x, textbox_y, "epoch: {}\n lr: {}\n batch size: {}\n hl size: {},{},{},{},{} ".format(best_epoch,best_learn_rate,best_batch,\
                                                                                                       best_hid_lay_num_1,best_hid_lay_num_2,best_hid_lay_num_3,\
                                                                                                        best_hid_lay_num_4,best_hid_lay_num_5), \
         bbox=dict(facecolor='white', edgecolor='black'))

plt.show()


plt.figure(figsize=(4, 4), dpi=100)
plt.scatter(target_all, pred_prob_all, alpha=0.3)
plt.plot([min(target_all), max(target_all)], [min(target_all),
    max(target_all)], color="k", ls="--")
plt.xlim([min(target_all), max(target_all)])
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
plt.title("R2 Score: {:.4f} \n MAE: {:.4f} \n RMSE: {:.4f}".format(big_r_squared,mae,rmse))
plt.show()


