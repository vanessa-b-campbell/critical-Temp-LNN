import functional_group_lists as fglist
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import pandas as pd

# is_clean? || do_clean? test if clean or maybe actually clean- this will be hard to
# soft code
# substructure searched throughout whole dataset + statisitc created
# get functional group stat summary
# convert to fingerprint

class DeltaMolData:
    def __init__(self, path):

        #### 1. read in csv file using pandas
        self.raw_data = pd.read_csv(path)

        # first convert the first and second column into list
        self.input_column = self.raw_data.iloc[:,0].tolist()
        self.output_column = self.raw_data.iloc[:,1].tolist()

        # zip input_smiles and cTemp into a list of tuples
        self.raw_data_list = list(zip(self.input_column, self.output_column))

    def make_clean(self):
        pass 



    def get_functioanl_group(self):
        
        for func_i in range(0, len(fglist.func_group_list)):
            for smile in self.input_column:

                mol = Chem.MolFromSmiles(smile)
                pattern = Chem.MolFromSmiles(fglist.func_group_list[func_i][0])
                match = mol.HasSubstructMatch(pattern) # will return a true or false
                if match: 
                    (fglist.func_group_list[func_i][1]).append(smile)

            # Statistics
            # still inside the loop- percentage of molecules that are a specific group is calculated and printed 
            # for each fnctional group type
            percent = (len(fglist.func_group_list[func_i][1])/len(self.input_column))*100
            message = ("{:.2f}% of molecules have {} group".format(percent,fglist.func_group_list[func_i][2]))
            fglist.full_func_stats.append(message)
            
        

        # second for loop is identical to first except this pulls from SMARTS functional group list
        # and converts from SMARTs to mols for functional groups
        for func_i in range(0, len(fglist.metalloid_group_list)):
            for smile in self.input_column:
                mol = Chem.MolFromSmiles(smile)
                pattern = Chem.MolFromSmarts(fglist.metalloid_group_list[func_i][0])
                match = mol.HasSubstructMatch(pattern)
                if match:
                    (fglist.metalloid_group_list[func_i][1]).append(smile)
            # Statistic
            percent = (len(fglist.metalloid_group_list[func_i][1])/ len(self.input_column)) * 100
            message = ("{:.2f}% of molecules have {} group".format(percent,fglist.metalloid_group_list[func_i][2]))
            fglist.full_func_stats.append(message)

        fglist.func_group_list.extend(fglist.metalloid_group_list)

        gutter_list = []

        for smile in self.input_column:
            used = False
            for functional_group in fglist.func_group_list:
                if smile in functional_group[1]:
                    used = True
    
            if not used:
                gutter_list.append(smile)

        # calculate what percentage of molecules are leftover
        leftover = ( len(gutter_list) / len(self.input_column) ) * 100

        # if no molecules are leftover then print a confirmation
        if leftover == 0:
            print('\n')
            print('All molecules are accounted for')

        # if there are reming molecules print the percentage 
        # remaining and each in gutter_list
        else:
            print('\n')
            print("{:.2f}% of molecules are in no group".format(leftover))
            for each in gutter_list:
                print('\n')
                print(each)

       
        self.inorganic_percent = "inorganic percent: {:.2f}%".format((1- (len(fglist.carbon_list) / len(self.input_column) ) ) * 100)
        self.full_func_stats = ("\n".join(fglist.full_func_stats))



    def to_fingerprints():
        pass



data = DeltaMolData("/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/clean_smile_dataset.csv")
data.get_functioanl_group()
#print(data.inorganic_percent)
print(data.full_func_stats)
