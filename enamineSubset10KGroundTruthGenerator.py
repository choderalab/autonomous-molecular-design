import pandas as pd
import deepchem as dc

bace_model = dc.models.GraphConvModel(n_tasks=1, mode='regression', batch_size=50, random_seed=0, model_dir="./models/bace")
esol_model = dc.models.GraphConvModel(n_tasks=1, mode='regression', batch_size=50, random_seed=0, model_dir="./models/esol")
logD_model = dc.models.GraphConvModel(n_tasks=1, mode='regression', batch_size=50, random_seed=0, model_dir="./models/logD")

bace_model.restore()
esol_model.restore()
logD_model.restore()

###load data from CSV in same folder as file
from deepchem.utils.save import load_from_disk
dataset_file= "./enamineSubset10K.csv"
dataset = load_from_disk(dataset_file)
print(type(dataset))
print("Columns of dataset: %s" % str(dataset.columns.values))
print("Number of examples in dataset: %s" % str(dataset.shape[0]))

###featurize the data using ConvMols
featurizer = dc.feat.ConvMolFeaturizer()

bace_loader = dc.data.CSVLoader(tasks=["bace"], smiles_field="SMILES",featurizer=featurizer)
bace_dataset = bace_loader.featurize(dataset_file)
bace_predicted = bace_model.predict(bace_dataset)

print(type(bace_predicted))

esol_loader = dc.data.CSVLoader(tasks=["esol"], smiles_field="SMILES",featurizer=featurizer)
esol_dataset = esol_loader.featurize(dataset_file)
esol_predicted =esol_model.predict(esol_dataset)

logD_loader = dc.data.CSVLoader(tasks=["logD"], smiles_field="SMILES",featurizer=featurizer)
logD_dataset = logD_loader.featurize(dataset_file)
logD_predicted = logD_model.predict(logD_dataset)

dataset["esol"] = esol_predicted
dataset["bace"] = bace_predicted
dataset["logD"] = logD_predicted

dataset.to_csv("./enamineSubset10KGroundTruth_2.csv")