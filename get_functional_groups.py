from rdkit import Chem
import pandas as pd 

# use PubChem to convert target functional groups into smile strings
# then turn those into patterns Rdkit recognizes inside the clean_smile_dataset
# using substructure searching

# bring in the clean smiles- make the SMILES as a list
SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/clean_smile_dataset.csv")
# SMILEs_data = pd.read_csv("C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\clean_smile_dataset.csv")


smiles_list = SMILEs_data['SMILEs'].tolist()


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
styrene_list = []
oxygen_list = []
neon_list = []
krypton_list =[]
radon_list = []
helium_list = []
phosphorus_list=[]
arsenic_list = []
antimony_list = []
carbon_list = []
selenium_list = []
caesium_list = []
germanium_list = []
tellurium_list = []
tin_list = []

func_group_list = [ ['C1=CC=CC=C1', benzene_list, 'benzene'], 
                    ['C(=O)O', carboxylic_list, 'carboxylic acid'], ['[Ti]', thallium_list, 'thallium'], 
                    

                ['N', nitrogen_list, 'nitrogen'], ['P', phosphorus_list, 'phosphorus'],
                

                

                ['S', sulfur_list, 'sulfur'], ['O', oxygen_list, 'oxygen' ],
                 

                ['Cl', chlorine_list, 'chlorine'], ['F', fluorine_list, 'fluorine'],  
                ['I', iodine_list, 'iodine'], ['Br', bromine_list, 'bromine'],

                ['C1=CC=C(C=C1)O', phenol_list, 'phenol'],['Cc1ccccc1', toluene_list, 'toluene'], 
                ['Nc1ccccc1 c1ccc(cc1)N', aniline_list, 'aniline'], 
                ['O=C(c1ccccc1)C CC(=O)c1ccccc1', acetophenone_list, 'acetophenone'],
                ['O=Cc1ccccc1 c1ccc(cc1)C=O', benzaldehyde_list, 'benzaldehyde'],
                ['C1=CC=C(C=C1)C(=O)O', benzoic_acid_list, 'benzoic acid'],
                ['C1=CC=C(C=C1)C#N', benzonitrile_list, 'benzonitrile'],
                ['CC1=CC=CC=C1C', ortho_xylene_list, 'ortho-xylene'],
                ['C=CC1=CC=CC=C1', styrene_list, 'styrene'], 

                ['[Ne]', neon_list, 'neon'], ['[Kr]', krypton_list, 'krypton'], 
                ['[Rn]', radon_list, 'radon'], ['[He]', helium_list, 'helium'],
                ['[Ar]', argon_list, 'Argon'], ['[Xe]', xe_list, 'Xe'],

                ['[Cs]', caesium_list, 'caesium']]


metalloid_group_list = [["[Si]", silicon_list, 'silicon'],['[Se]', selenium_list, 'selenium'], 
                        ['[As]', arsenic_list, 'arsenic'],['[Ge]', germanium_list, 'germanium'],
                        ['[Sn]', tin_list, 'tin']]

# wtf is wrong with the metalloids? 
############# diobedient molecules/elements
# ["[Si]", silicon_list, 'silicon'], 
# ['[Se]', selenium_list, 'selenium'],

# ['[As]', arsenic_list, 'arsenic'],
# ['[Ge]', germanium_list, 'germanium'],
# ['[Sn]', tin_list, 'tin'],


# create a second loop for the trouble mols using SMARTS instead of SMILES

nobel_gases = [neon_list, krypton_list, radon_list, helium_list, argon_list, xe_list ]

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
        match = mol.HasSubstructMatch(Chem.MolFromSmiles(func_group_list[func_i][0])) # will return a true or false
        if match: 
            (func_group_list[func_i][1]).append(smile)

    # Statistics
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
    print('from functional group list #1:')
    print('\n')
    print("{:.2f}% of molecules have {} group".format(percent,func_group_list[func_i][2]))
    if percent == 0.00:
        print('missed one: {}'.format(func_group_list[func_i][2]))


for func_i in range(0, len(metalloid_group_list)):
    for smile in smiles_list:
        mol = Chem.MolFromSmiles(smile)
        match = mol.HasSubstructMatch(Chem.MolFromSmarts(metalloid_group_list[func_i][0]))
        if match:
            (metalloid_group_list[func_i][1]).append(smile)
    # Statistic
    percent = (len(metalloid_group_list[func_i][1])/ len(smiles_list)) * 100
    print('from metalloid list:')
    print('\n')
    print("{:.2f}% of molecules have {} group".format(percent,metalloid_group_list[func_i][2]))



gutter_list = []

for smile in smiles_list:
    used = False
    for functional_group in func_group_list:
        if smile in functional_group[1]:
            used = True
    
    if not used:
        gutter_list.append(smile)

for smile in smiles_list:
    used = False
    for metalloid in metalloid_group_list:
        if smile in metalloid_group_list[1]:
            used = True
    
    if not used and smile not in gutter_list:
        gutter_list.append(smile)

#print(gutter_list)
leftover = ( len(gutter_list) / len(smiles_list) ) * 100
print("{:.2f}% of molecules are in no group".format(leftover))


aromatic_percent = (( len(phenol_list) + len(toluene_list) + len(aniline_list) + len(acetophenone_list) \
                    + len(benzaldehyde_list) + len(benzoic_acid_list) + len(benzonitrile_list) + len(ortho_xylene_list)\
                         + len(styrene_list) )/ len(smiles_list)  ) *100
print("{:.2f}% of molecules have an aromatic group".format(aromatic_percent))

inorganic_percent = ((len(caesium_list) + len(tin_list) + len(silicon_list) + len(germanium_list)\
                      + len(arsenic_list) + len(tellurium_list) + len(antimony_list) + len(helium_list)\
                        + len(neon_list)+ len(argon_list) + len(krypton_list) + len(xe_list)\
                            + len(radon_list) + len(scandium_list))/ len(smiles_list)) * 100 
print("{:.2f}% of molecules are inorganic".format(inorganic_percent))


for each in gutter_list:
    print(each)