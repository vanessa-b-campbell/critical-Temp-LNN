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
gutter_list = SMILEs_data['SMILEs']
# benzene, phenol group, carboxylic acid, amine
phenol_list = []
benzene_list = []
carboxylic_list = []
fluorine_list = []
nitrogen_list = []
silicon_list = []
xe_list = []
chlorine_list = []
thallium_list = []
argon_list = []
bromine_list = []
sulfur_list = []
scandium_list = []
func_group_list = [('C1=CC=C(C=C1)O', phenol_list, 'phenol'), ('C1=CC=CC=C1', benzene_list, 'benzene'), 
                    ('C(=O)O', carboxylic_list, 'carboxylic acid'), ('[F]', fluorine_list, 'fluorine')]#, 
                  # ('N', nitrogen_list, 'nirogen'), ("[Si]", silicon_list, 'silicon'), 
                  # ('[Xe]', xe_list, 'Xe'), ('Cl', chlorine_list, 'chlorine'), 
                  # ('[Ti]', thallium_list, 'thallium'), ('[Ar]', argon_list, 'Argon'),
                  # ('Br', bromine_list, 'bromine'), ('S', sulfur_list, 'sulfur'), ('Sc', scandium_list, 'scandium')]



# Will need a list of pattern SMILE string
# loop through each dataset smile for a given pattern
# if true the name of the smile string, and maybe even the critical temp corresponding to it, 
# needs to be added or put somewhere identifying it....
# make a matrix? indexing will get ugly... debugging a nightmare


for func_i in range(0, len(func_group_list)):
    for smile in smiles_list:

        mol = Chem.MolFromSmiles(smile)
        try: 
            match = mol.HasSubstructMatch(Chem.MolFromSmiles(func_group_list[func_i][0])) # will return a true or false
            if match: 
                (func_group_list[func_i][1]).append(smile)
                gutter_list.drop(smile)
        
        

        # if match == False: 
        # if smile not in gutter_list and smile not in func_group_list[func_i][1]:
            # elif smile not in gutter_list:  
            #     gutter_list.append(smile)
        
        except KeyError: 
            if re.findall(func_group_list[func_i][0], smile):        
                (func_group_list[func_i][1]).append(smile)
                gutter_list.drop(smile)
            
            # elif smile not in gutter_list:
            #     gutter_list.append(smile)
                
    # Statistics
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
    print('\n')
    print("{:.2f}% of molecules have a {} group".format(percent,func_group_list[func_i][2]))
    
leftover = (len(gutter_list)/len(smiles_list))*100
print("{:.2f}% of molecules are in no group".format(leftover))

    
print(sulfur_list)

# print("phenol: {}".format(phenol_list))
# print('\n')
# print("benzene: {}".format(benzene_list))
# print('\n')
#print("carboxylic acid group: {}".format(carboxylic_list))
# print("silicon: {}".format(silicon_list))


########## problems to ask Landon || figure out:
#   1. rdkit can't seem to search for Si, Sn, and a few other one- why? - impliment a try/except for 
#       regex to search? || youtube rdkit and see if there is a work around only using this library?

#   2. One molecule can end up being added to more than one functional group list- however
#       gutter_list should only have molecules that have not been put into any list whatsoever
#       and yet no matter what conditional I put 100% of the molecules end up in the gutter_list- wtf!
