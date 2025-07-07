from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles("CCO")
print(mol)