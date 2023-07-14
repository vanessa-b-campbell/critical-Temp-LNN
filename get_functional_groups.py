from rdkit import Chem
import pandas as pd 

# use PubChem to convert target functional groups into smile strings
# then turn those into patterns Rdkit recognizes inside the clean_smile_dataset
# using substructure searching

# bring in the clean smiles

# workstation directory
SMILEs_data = pd.read_csv("/home/jbd3qn/Downloads/critical-Temp-LNN/csv_data/clean_smile_dataset.csv")

# laptop directory
#SMILEs_data = pd.read_csv("C:\\Users\\color\\Documents\\Bilodeau_Research_Python\\critical-Temp-LNN\\clean_smile_dataset.csv")


# make the SMILES as a list
smiles_list = SMILEs_data['SMILEs'].tolist()


# all pattern lists
phenol_list = []
benzene_list = []
carboxylic_list = []
fluorine_list = []
nitrogen_list = []
silicon_list = []
xe_list = []
chlorine_list = []
titanium_list = []
argon_list = []
bromine_list = []
sulfur_list = []
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
thallium_list = []
hydrogen_list =[]

# SMILES pattern list
# ordered loosely on periodic table columns and aromaic groups

# [  'SMILES string of functioanl group'  , empty_group_list,    'name of the functional group'   ]

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

                ['[Cs]', caesium_list, 'caesium'],['C', carbon_list, 'carbon'] ]


# second list for SMARTS patterns
# mostly for metalloids/ metals/ hydrogen
# [  '[SMARTS string]',   empty_group_list,    'name of functional group' ]
metalloid_group_list = [["[Si]", silicon_list, 'silicon'],['[Se]', selenium_list, 'selenium'], 
                        ['[As]', arsenic_list, 'arsenic'],['[Ge]', germanium_list, 'germanium'],
                        ['[Sn]', tin_list, 'tin'], ['[Ti]',titanium_list, 'titanium'],['[H]',hydrogen_list, 'hydrogen']]


########## IDEA could be useful later: not being used in code currently
# nobel_gases = [neon_list, krypton_list, radon_list, helium_list, argon_list, xe_list ]
##########


# loop will go through each in the functional group list by index 
# then will go through each SMILEs string in dataset
# dataset SMILES becomes mol
# pattern becomes mol
# match will return true if match is found in smiles
# if match is found then the smile will be added to that functional group's 
# empty list
for func_i in range(0, len(func_group_list)):
    for smile in smiles_list:

        mol = Chem.MolFromSmiles(smile)
        pattern = Chem.MolFromSmiles(func_group_list[func_i][0])
        match = mol.HasSubstructMatch(pattern) # will return a true or false
        if match: 
            (func_group_list[func_i][1]).append(smile)

    # Statistics
    # still inside the loop- percentage of molecules that are a specific group is calculated and printed 
    # for each fnctional group type
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
    print("{:.2f}% of molecules have {} group".format(percent,func_group_list[func_i][2]))
    if percent == 0.00:
        print('missed one: {}'.format(func_group_list[func_i][2]))


# second for loop is identical to first except this pulls from SMARTS functional group list
# and converts from SMARTs to mols for functional groups
for func_i in range(0, len(metalloid_group_list)):
    for smile in smiles_list:
        mol = Chem.MolFromSmiles(smile)
        pattern = Chem.MolFromSmarts(metalloid_group_list[func_i][0])
        match = mol.HasSubstructMatch(pattern)
        if match:
            (metalloid_group_list[func_i][1]).append(smile)
    # Statistic
    percent = (len(metalloid_group_list[func_i][1])/ len(smiles_list)) * 100
    print("{:.2f}% of molecules have {} group".format(percent,metalloid_group_list[func_i][2]))


# combines SMARTS group list to SMILES group list
# the purpose of this is to ensure that all molecules in the dataset are being
# accounted for- therfore they are ending up in at least one list
func_group_list.extend(metalloid_group_list)

# gutter_list holds remaining molecules in the dataset that are in no group type list
gutter_list = []

# for loop tests each smiles in dataset to see if they're in at
# least one list
# if they are not then add that molecule to the gutter_list
# to identify why it's not in any list
for smile in smiles_list:
    used = False
    for functional_group in func_group_list:
        if smile in functional_group[1]:
            used = True
    
    if not used:
        gutter_list.append(smile)



# calculate what percentage of molecules are leftover
leftover = ( len(gutter_list) / len(smiles_list) ) * 100

# if no molecules are leftover then print a confirmation
if leftover == 0:
    print('\n')
    print('All molecules are accounted for')

# if there are reming molecules print the percentage 
# remaining and each in gutter_list
else:
    print("{:.2f}% of molecules are in no group".format(leftover))
    for each in gutter_list:
        print('\n')
        print(each)



print('\n')

# calculate the percentage of molecules that are aromatics
# in theory there shouldn't be any duplicates in the aromatic type lists
# this is based on the unlikely probability that one molecule will have more than
# one aromatic type-- but this is a possible source of error in the calculated statistic
aromatic_percent = (( len(phenol_list) + len(toluene_list) + len(aniline_list) + len(acetophenone_list) \
                    + len(benzaldehyde_list) + len(benzoic_acid_list) + len(benzonitrile_list) + len(ortho_xylene_list)\
                         + len(styrene_list) )/ len(smiles_list)  ) *100
print("{:.2f}% of molecules have an aromatic group".format(aromatic_percent))




# calculating the percentage of inorganic molecules
# it's possible I missed one of the inorganic molecules in the back and forth
# but unlikely
# also assuming metalloids and noble gases are inorganic 
inorganic_percent = ((len(caesium_list) + len(tin_list) + len(silicon_list) + len(germanium_list)\
                    + len(arsenic_list) + len(tellurium_list) + len(antimony_list) + len(helium_list)\
                        + len(neon_list)+ len(argon_list) + len(krypton_list) + len(xe_list)\
                            + len(radon_list)  + len(titanium_list))/ len(smiles_list)) * 100 
print("{:.2f}% of molecules are inorganic".format(inorganic_percent))

print('\n')
print("all good in the hood")