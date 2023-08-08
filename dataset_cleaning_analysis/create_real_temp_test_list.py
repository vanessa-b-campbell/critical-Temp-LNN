import pandas as pd

# Read in the test list
test_list = pd.read_csv('C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\chemprop\\test_preds_temp.csv')

predict_temp = test_list.iloc[:,1].tolist()

clean_smiles = pd.read_csv('C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\csv_data\\No_outliers_smile_dataset.csv')

real_temp = []
real = []

for i in range(0, len(test_list)):
    for index in range(0, len(clean_smiles)):
        if clean_smiles['smiles'][index] == test_list['smiles'][i]:
            real.append(clean_smiles['smiles'][index])
            real.append(clean_smiles['critical_temp'][index])
            real_temp.append(clean_smiles['critical_temp'][index])


print(len(predict_temp))
# real_vs_predict = []

# real_vs_predict = list(zip(real_temp, predict_temp))

# print(real_vs_predict)