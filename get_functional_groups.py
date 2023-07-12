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

# second list of metalloids and a few others 
metalloid_group_list = [["[Si]", silicon_list, 'silicon'],['[Se]', selenium_list, 'selenium'], 
                        ['[As]', arsenic_list, 'arsenic'],['[Ge]', germanium_list, 'germanium'],
                        ['[Sn]', tin_list, 'tin'], ['[Ti]',titanium_list, 'titanium'],['[H]',hydrogen_list, 'hydrogen']]


# create a second loop for the trouble mols using SMARTS instead of SMILES

nobel_gases = [neon_list, krypton_list, radon_list, helium_list, argon_list, xe_list ]



for func_i in range(0, len(func_group_list)):
    for smile in smiles_list:

        mol = Chem.MolFromSmiles(smile)
        match = mol.HasSubstructMatch(Chem.MolFromSmiles(func_group_list[func_i][0])) # will return a true or false
        if match: 
            (func_group_list[func_i][1]).append(smile)

    # Statistics
    percent = (len(func_group_list[func_i][1])/len(smiles_list))*100
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
    print("{:.2f}% of molecules have {} group".format(percent,metalloid_group_list[func_i][2]))


func_group_list.extend(metalloid_group_list)

gutter_list = []

for smile in smiles_list:
    used = False
    for functional_group in func_group_list:
        if smile in functional_group[1]:
            used = True
    
    if not used:
        gutter_list.append(smile)

for each in gutter_list:
    print(each)


print('\n')


# checking that all molecules are being defined and categorized
# if gutter_list leftover is equal to 0.00% then all molecules are being added 
# to at least one group type list
leftover = ( len(gutter_list) / len(smiles_list) ) * 100
print("{:.2f}% of molecules are in no group".format(leftover))



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
