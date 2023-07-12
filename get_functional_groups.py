from rdkit import Chem
import pandas as pd 
import re

# use PubChem to convert target functional groups into smile strings
# then turn those into patterns Rdkit recognizes inside the clean_smile_dataset
# using substructure searching

# bring in the clean smiles- make the SMILES as a list

SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/clean_smile_dataset.csv")
# SMILEs_data = pd.read_csv("C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\clean_smile_dataset.csv")


smiles_list = SMILEs_data['SMILEs'].tolist()



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
iodine_list = []
toluene_list = []
aniline_list = []
acetophenone_list = []
benzaldehyde_list=[]
benzoic_acid_list = []
benzonitrile_list = []
ortho_xylene_list = []
# make into list of lists
func_group_list = [['C1=CC=C(C=C1)O', phenol_list, 'phenol'], ['C1=CC=CC=C1', benzene_list, 'benzene'], 
                    ['C(=O)O', carboxylic_list, 'carboxylic acid'], ['F', fluorine_list, 'fluorine'],  
                ['N', nitrogen_list, 'nitrogen'], 
                ['[Xe]', xe_list, 'Xe'], ['Cl', chlorine_list, 'chlorine'], 
                ['[Ti]', thallium_list, 'thallium'], ['[Ar]', argon_list, 'Argon'],
                ['Br', bromine_list, 'bromine'], ['S', sulfur_list, 'sulfur'], 
                ['I', iodine_list, 'iodine'], ['Cc1ccccc1', toluene_list, 'toluene'], 
                ['Nc1ccccc1 c1ccc(cc1)N', aniline_list, 'aniline'], 
                ['O=C(c1ccccc1)C CC(=O)c1ccccc1', acetophenone_list, 'acetophenone'],
                ['O=Cc1ccccc1 c1ccc(cc1)C=O', benzaldehyde_list, 'benzaldehyde'],
                ['C1=CC=C(C=C1)C(=O)O', benzoic_acid_list, 'benzoic acid'],
                ['C1=CC=C(C=C1)C#N', benzonitrile_list, 'benzonitrile'],
                ['CC1=CC=CC=C1C', ortho_xylene_list, 'ortho-xylene']]

# to add : 1. aromatics, 2.catch all present elements
# wtf is wrong with Si and Sc? 
############# diobedient molecules/elements
# ["[Si]", silicon_list, 'silicon'], 
# ['[Sc]', scandium_list, 'scandium'],


# Will need a list of pattern SMILE string
# loop through each dataset smile for a given pattern
# if true the name of the smile string, and maybe even the critical temp corresponding to it, 
# needs to be added or put somewhere identifying it....
# make a matrix? indexing will get ugly... debugging a nightmare
new_smiles_with_brackets = []

# for smile in smiles_list: # for each smile
#     #print(smile)
#     new_smile = smile

#     if "Si" in new_smile or "Sc" in new_smile or "Cl" in new_smile: # super fast first-check that keeps going until no more groups are found

#         if new_smile.find('Si') != -1:      # smile.find returns -1 if the parameter 'Si' is not found, meaning "Si" exists if any number >= 0 is returned
#             index = new_smile.find('Si') # find index of this section of string
#             new_smile = new_smile[:index] + '[' + new_smile[index:index+2] + ']' + new_smile[index+2:] # create new smile to insert
#         if new_smile.find('Sc') != -1:
#             index = new_smile.find('Sc')
#             new_smile = new_smile[:index] + '[' + new_smile[index:index+2] + ']' + new_smile[index+2:]
#         if new_smile.find('Cl') != -1:
#             index = new_smile.find('Cl')
#             new_smile = new_smile[:index] + '[' + new_smile[index:index+2] + ']' + new_smile[index+2:]

#     print(new_smile)
#     new_smiles_with_brackets.append(new_smile)

    




        
        # for char_index in range(0, len(smile)):
        #     if (smile[char_index] == "S" and (smile[char_index+1]) == "i") or (smile[char_index] == "S" and \
        #             (smile[char_index+1]) == "c") or (smile[char_index] == "C" and (smile[char_index+1]) == "l"):
                
        #         smile = smile[0:char_index] + '[' + smile[char_index:char_index+2] + ']' + smile[char_index+2:]
        #         break
        # print(smile)



for func_i in range(0, len(func_group_list)):
    for smile in smiles_list:

        mol = Chem.MolFromSmiles(smile)
        #try: 
        match = mol.HasSubstructMatch(Chem.MolFromSmiles(func_group_list[func_i][0])) # will return a true or false
        if match: 
            #print('match')
            (func_group_list[func_i][1]).append(smile)

    # Statistics
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
    print('\n')
    print("{:.2f}% of molecules have {} group".format(percent,func_group_list[func_i][2]))


gutter_list = []

for smile in smiles_list:
    used = False
    for functional_group in func_group_list:
        if smile in functional_group[1]:
            used = True
    
    if not used:
        gutter_list.append(smile)

#print(gutter_list)
leftover = ( len(gutter_list) / len(smiles_list) ) * 100
print("{:.2f}% of molecules are in no group".format(leftover))

# for each in gutter_list:
#     print(each)

# check = False
# while check:
#     for smile in smiles_list:
#     #take smile and check if its in any of the list
#         for index in range(0,len(func_group_list)):
    
#             if smile in func_group_list[func_i][1]:
#                 check = True #stop the loop here
#                 gutter_list.append(smile)
            
# the problem here is that a molecule might only be in one list, that lsit could be index 5. So if it loops
# through the first list and doesn't find it, it will append it to gutter_list -DO NOT WANT
# gutter_list is only for molecules that aren't in any of the list- so 
# need to go through ALL the lists, if its in any of them --loop stops and nothing happens
# if it gets through all the list and it's not there needs to be added to gutter_list


        # if match == False: 
        # if smile not in gutter_list and smile not in func_group_list[func_i][1]:
            # elif smile not in gutter_list:  
            #     gutter_list.append(smile)
        
        #except KeyError: 
        # if re.findall(func_group_list[func_i][0], smile):        
        #     (func_group_list[func_i][1]).append(smile)
        #     gutter_list.drop(smile)
        
            # elif smile not in gutter_list:
            #     gutter_list.append(smile)
                

    









    
# print(sulfur_list)

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
