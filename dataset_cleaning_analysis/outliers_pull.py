#%%
import pandas as pd
import csv
data = pd.read_csv('C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\csv_data\\clean_smile_dataset.csv')

input_column = data.iloc[:,0].tolist()
temp_column = data.iloc[:,1].tolist()

data_list = list(zip(input_column, temp_column))

# print(data_list)

outlier_list = []
no_outliers_list = []

for index in range(0, len(data)):
    if temp_column[index] >= 1200:
        outlier_list.append(input_column[index])
        outlier_list.append(temp_column[index])

print(outlier_list)

#%%
for pair in data_list:
    if pair[1] not in outlier_list:
        no_outliers_list.append(pair)
print(no_outliers_list)


filename_1 = 'No_outliers_smile_dataset.csv'

# with open(filename_1, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(no_outliers_list)
# print(f"Data saved to {filename_1} successfully.")