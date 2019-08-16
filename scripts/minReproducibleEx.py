import deepchem as dc
import numpy as np

dataset_file= "../data/enamineSubset10K.csv"
featurizer = dc.feat.ConvMolFeaturizer()
bace_loader = dc.data.CSVLoader(tasks=["bace"], smiles_field="SMILES",featurizer=featurizer)
bace_dataset = bace_loader.featurize(dataset_file)

predictions = []
###restore model and make prediction
for _ in range(5):
    bace_model = dc.models.GraphConvModel(n_tasks=1, mode='regression', batch_size=50, random_seed=0, model_dir="../models/bace")
    bace_model.restore()
    bace_predicted = bace_model.predict(bace_dataset)
    predictions.append(bace_predicted)
    print("Prediction complete.")
for i in range( len(predictions)-1 ):
    print(i)
    assert np.testing.assert_array_almost_equal(predictions[i], predictions[i+1])
    #assert np.array_equal(predictions[i], predictions[i+1])

print("Done.")