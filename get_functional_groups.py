from rdkit import Chem
import pandas as pd 
import re

# use PubChem to convert target functional groups into smile strings
# then turn those into patterns Rdkit recognizes inside the clean_smile_dataset
# using substructure searching

# bring in the clean smiles- make the SMILES as a list
SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/clean_smile_dataset.csv")


# ('[Sn]', silicon_list),
smiles_list = SMILEs_data['SMILEs'].tolist()

# benzene, phenol group, carboxylic acid, amine
phenol_list = []
benzene_list = []
carboxylic_list = []
fluorine_list = []
nitrogen_list = []
silicon_list = []
xe_list = []
func_group_list = [('C1=CC=C(C=C1)O', phenol_list, 'phenol'), ('C1=CC=CC=C1', benzene_list, 'benzene'), 
                   ('C(=O)O', carboxylic_list, 'carboxylic acid'), ('F', fluorine_list, 'fluorine'), 
                   ('N', nitrogen_list, 'nirogen'), ('[Si]', silicon_list, 'silicon'), 
                   ('[Xe]', xe_list, 'Xe')]

gutter_list = []

# Will need a list of pattern SMILE string
# loop through each dataset smile for a given pattern
# if true the name of the smile string, and maybe even the critical temp corresponding to it, 
# needs to be added or put somewhere identifying it....
# make a matrix? indexing will get ugly... debugging a nightmare


for func_i in range(0, len(func_group_list)):
    for smile in smiles_list:

        mol = Chem.MolFromSmiles(smile)
        match = mol.HasSubstructMatch(Chem.MolFromSmiles(func_group_list[func_i][0]))
        print(match)
        if match: # will return a true or false
            (func_group_list[func_i][1]).append(smile)
        
        
        # if re.findall(func_group_list[func_i][0], smile):        
        #      (func_group_list[func_i][1]).append(smile)

        if match == False: 
            if smile not in gutter_list:
                gutter_list.append(smile)
    
    # Statistics
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
    print('\n')
    print("{:.2f}%'of molecules have a {} group".format(percent,func_group_list[func_i][2]))
    

leftover = (len(gutter_list)/len(smiles_list))*100
print("{:.2f}%'are left".format(leftover))



# print("phenol: {}".format(phenol_list))
# print('\n')
# print("benzene: {}".format(benzene_list))
# print('\n')
#print("carboxylic acid group: {}".format(carboxylic_list))
# print("silicon: {}".format(silicon_list))


