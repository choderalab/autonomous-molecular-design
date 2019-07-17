import random
import pandas as pd

filepath = "./2019q1-2_Enamine_REAL_diversity_set_MFP2_512_0.6_8.5M_SMILES.smiles"
number_smiles_desired = 100000
subset_smiles = []
esols = []
logDs = []
bace_affs =[]

mols_df = pd.DataFrame(subset_smiles, columns = ["SMILES"])
print(mols_df)

#read in lines
with open(filepath) as file:
    lines = file.readlines()[1:] #strip newlines and first line (headers)
print("File read.")

#randomly specify the indices of the molecule subset to take
indices = random.sample(range(len(lines)), number_smiles_desired)
print("Indices calculated.")

for idx in indices:
    subset_smiles.append( lines[idx].strip().split()[0].strip() )
print("Smiles appended to list.")

mols_df = pd.DataFrame(subset_smiles, columns = ["SMILES"])
mols_df.to_csv("./enamineSubset100K.csv")
