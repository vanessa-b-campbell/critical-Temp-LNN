# function to look at some of these molecules
from rdkit import Chem
from rdkit.Chem import Draw


def mol_image_func(molecule_smile):

    mol = Chem.MolFromSmiles(molecule_smile)

    # Create the drawing options and set the desired colors
    drawing_options = Draw.DrawingOptions()
    

    img = Draw.MolToImage(mol, options=drawing_options)

    img.show()