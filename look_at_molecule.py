# need to look at some of these molecules frfr
from rdkit import Chem
from rdkit.Chem import Draw
from get_functional_groups import benzaldehyde_list

print(benzaldehyde_list)

molecule_smile = 'O=Cc1ccccc1C(=O)O'
mol = Chem.MolFromSmiles(molecule_smile)

# Create the drawing options and set the desired colors
drawing_options = Draw.DrawingOptions()
drawing_options.atomFillColor   = (0.216, 0.118, 0.008)  # Set atom fill color to red




img = Draw.MolToImage(mol, options=drawing_options)

img.show()