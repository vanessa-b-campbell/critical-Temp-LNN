import functional_group_lists as fglist
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


# Class to hold all of the functions for modifying and understanding a single SMILES string

# as a DeltaMol object a SMILES string can be:
# turned into a 2D image
# substructure searched
# get functional group stat summary
# convert to fingerprint

class DeltaMol():
    def __init__(self, smile_string): 
        self.smile = smile_string


    def to_image(self): # 2D image

        mol = Chem.MolFromSmiles(self.smile)
        img = Draw.MolToImage(mol)
        img.show()



    def substruct_search(self, pattern): # substructure search

        mol = Chem.MolFromSmiles(self.smile)
        s_pattern = Chem.MolFromSmiles(pattern)
        self.has_pattern = mol.HasSubstructMatch(s_pattern)
        
        if self.has_pattern:
            print("{}, molecule has pattern".format(self.has_pattern))
        
        else: 
            mol = Chem.MolFromSmiles(self.smile)
            sm_pattern = Chem.MolFromSmarts(pattern)
            self.has_pattern = mol.HasSubstructMatch(sm_pattern)
            
            if self.has_pattern:
                print("{}, molecule has pattern".format(self.has_pattern))

            else: 
                print("{}, molecule does not have pattern".format(self.has_pattern))



    def get_functional_group(self): # functional group stat summary
        print('molecule has: ')
        for func_i in range(0, len(fglist.func_group_list)):

            self.mol = Chem.MolFromSmiles(self.smile)
            pattern = Chem.MolFromSmiles(fglist.func_group_list[func_i][0])
            match = self.mol.HasSubstructMatch(pattern) # will return a true or false
            
            if match: 
                print(fglist.func_group_list[func_i][2])


        for met_i in range(0, len(fglist.metalloid_group_list)):

            mol = Chem.MolFromSmiles(self.smile)
            pattern = Chem.MolFromSmarts(fglist.metalloid_group_list[met_i][0])
            match = mol.HasSubstructMatch(pattern) # will return a true or false
            
            if match: 
                print(fglist.metalloid_group_list[met_i][2])
    


    def to_fingerprint(self): # convert to fingerprint

        # mol to fingerprint parameters
        fingerprint_radius = 2
        fingerprint_size = 2048

        mol = Chem.MolFromSmiles(self.smile) 
        self.fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, fingerprint_radius, nBits=fingerprint_size)
        
        print(self.fingerprint.ToList())



# how to use
#my_mol = DeltaMol("C[SiH](Cl)Cl")
#my_mol.to_image()
#my_mol.substruct_search('[Si]')
#my_mol.get_functional_group()
#my_mol.to_fingerprint()