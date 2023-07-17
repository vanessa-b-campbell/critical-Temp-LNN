# need to look at some of these molecules frfr
from rdkit import Chem
from rdkit.Chem import Draw

molecule_smile = 'CCCCCOC(=O)CO'
mol = Chem.MolFromSmiles(molecule_smile)
img = Draw.MolToImage(mol)
img.show()