import torch 

'''
defines the 3 modes of the model
    1. train
    2. validate
    3. predict 

each function takes in parameters: 
        1. the model (created in model_object.py)
        2. the device to run everything on (cpu)
        3. dataloader (our dataset as defined in model_data_object.py)
        4. optim
        5. epoch, although it is only necessary if you want to print out the loss after 
        the it's calculated in the function (i.e validation function)
'''

def train(model, device, train_dataloader, optim, epoch):
# training function: for epoch in range- train the model- calculate the loss 
    '''
defines the training mode:
        loss as a L1 loss function (best for linear nns)
        loopes through the input vectors and output targets and feeds the input into the model
        calculate the loss and add to total loss
        updates weights


the train function purpose is to update the weights (back propigation line)
Also if dropout layers were used (not for this model) they would be used here
'''
    
    # Set the model to training mode:
    model.train()

    # Define loss function:
    loss_fn = torch.nn.L1Loss()
    # Create a loss variable to keep track of total losses in the test set
    loss_collect = 0

    for b_i, (input_vectors, targets) in enumerate(train_dataloader):
    # X is assigned to the input vector portion of the dataset
    # y is assigned to the output target of the dataset? 
        
        # Assign X and y to the appropriate device:
        input_vectors, targets = input_vectors.to(device), targets.to(device)
        
        # Zero out the optimizer:
        optim.zero_grad()
        # Make a prediction:
        # feeding the input vector data into the model
        pred = model(input_vectors)

        # Calculate the loss: 
        loss = loss_fn(pred, targets.view(-1,1))
        
        # Backpropagation: (this updates the weights)
        loss.backward()
        optim.step()
        # Calculate the loss and add it to our total loss
        loss_collect += loss.item()  # loss summed across the batch

        # Return our normalized losses so we can analyze them later:

        if b_i % 10 == 0:
            print('epoch: {} [{}/{} ({:.0f}%)]\t training loss: {:.1f}'.format(
                epoch, b_i * len(input_vectors), len(train_dataloader.dataset),
                100 * b_i * len(input_vectors) / len(train_dataloader.dataset),
                loss.item()))
        # print(
        # "\nEpoch:{}   training dataset: Loss per Datapoint: {:.4f}".format(
        #     epoch, loss_collect
        # )
        # )
    loss_collect /= len(train_dataloader.dataset)
    return loss_collect





def validation(model, device, val_dataloader, epoch):
    '''
defines the validation mode:
        prints the loss without updating the weights (removing the gradient)
        loopes through the input vectors and output targets and feeds the input into the model
        calculate the loss and add to total loss


the validation function purpose is to check up on the model's progress using 20% 
of the TRAINING dataset. So all said and done the raw data will be split into three (test, train, validation)
the validation output is how you make decisions on whether to change the hyperparameters 
ex(# of layers, width of layers, # of epochs)
'''

    
    # Set our model to evaluation mode:
    model.eval()
    
    # Create a loss variable to keep track of total losses in the test set
    # this is the loss variable with the evaluation mode
    loss_collect = 0
    
    loss_fn = torch.nn.L1Loss()
    
    
    # Remove gradients (stops weights from updating):
    with torch.no_grad():
        
        # Looping over the dataloader allows us to pull out or input/output data:
        for input_vectors, targets in val_dataloader:
            
            # Assign input_vectors and targets to the appropriate device:
            input_vectors, targets = input_vectors.to(device), targets.to(device)

            # Make a prediction:
            pred = model(input_vectors)
            
            # Calculate the loss and add it to our total loss
            loss = loss_fn(pred, targets.view(-1,1)) # object
            
            loss_collect += loss.item()  # converts loss to a number
            # loss summed across the batch
            
    loss_collect /= len(val_dataloader.dataset) # normalizing 
    

    print('\nTest dataset: Overall Loss: {:.1f},  ({:.2f}%)\n'.format(
        len(val_dataloader.dataset)*loss_collect,loss_collect))
    # Print out our test loss so we know how things are going
    # print(
    #     "\nEpoch:{}   Validation dataset: Loss per Datapoint: {:.4f}".format(
    #         epoch, loss_collect
    #     )
    # )
    # Return our normalized losses so we can analyze them later:
    return loss_collect






def predict(model, device, dataloader):
    '''
defines the prediction mode:
        prints the loss without updating the weights (removing the gradient)
        loopes through the input vectors and output targets and feeds the input into the model
        calculate the loss and add to total loss
        concatinates the outputs so they are in [#datapoints x 1] rather than [batchsize x 1]


the predict function creates the output we compare to everything. It can take in either the validation dataset
or the training dataset
'''
    
    # Set our model to evaluation mode:
    model.eval()

    # setting x and y and prediction to empty lists
    input_vectors_all = []
    targets_all = []
    pred_prob_all = []
    
    # Remove gradients:
    with torch.no_grad():

        # Looping over the dataloader allows us to pull out or input/output data:
        for input_vector, target in dataloader:

            # Assign X and y to the appropriate device:
            input_vector, target = input_vector.to(device), target.to(device)

            # Make a prediction:
            pred_prob = model(input_vector)

            input_vectors_all.append(input_vector)
            targets_all.append(target)
            pred_prob_all.append(pred_prob)

    #concatinates the outputs so they are in [#datapoints x 1] rather than [batchsize x 1]        
    input_vectors_all = torch.concat(input_vectors_all)
    targets_all = torch.concat(targets_all)
    pred_prob_all = torch.concat(pred_prob_all).view(-1)
    
    
    return input_vectors_all, targets_all, pred_prob_all
    