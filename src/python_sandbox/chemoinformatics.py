from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
import matplotlib.pyplot as plt

mol = Chem.MolFromSmiles("CCO")

if mol is None:
    print('SMILES文字列が無効です')
else:
    fig, ax = plt.subplots(figsize=(6, 4))
    
    from rdkit.Chem import Draw
    from io import BytesIO
    
    img = Draw.MolToImage(mol, size=(600, 400))
    
    ax.imshow(img)
    ax.axis('off')
    ax.set_title(mol)
    
    plt.tight_layout()
    plt.show()