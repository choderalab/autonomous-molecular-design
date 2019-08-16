Autonomous Molecular Design
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/Autonomous Molecular Design.png)](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/Autonomous Molecular Design)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/Autonomous Molecular Design/branch/master)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/Autonomous Molecular Design/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/Autonomous Molecular Design/branch/master)


Drug discovery is an incredibly expensive and time-consuming process that aims to choose a few useful compounds out of the many billions of possible molecules that make up chemical space. Given the size of the search space, advanced algorithms are necessary to traverse this space in a fully-autonomous manner. This code base is a sandbox for development of active-learning algorithms and their applications to autonomous molecular design.

Data
----

This project used the 8.5-million-compound Enamine REAL diverse drug-like dataset, available at https://enamine.net/library-synthesis/real-compounds/real-compound-libraries. Random subsets of size 10,000 and 100,000 were selected using scripts/enamineRandomSubsetGenerator.py. These datasets included only SMILES-encoded structures.

To featurize our datasets, we trained a DeepChem graph convolutional neural network on each of the three properties we considered (beta-secretase 1 affinity or "bace", solobulity or "esol", and the log of the distribution coefficient logD). We then used these networks to make predictions for each property on each molecule in each dataset. This was performed using the scripts/enamineSubsetXXKGroundTruthGenerator.py files. All datasets are available in the directory labeled "data".

Note: the predictions made by the DeepChem models seem to vary widely given a fixed dataset and a given model. This issue is discussed at https://github.com/deepchem/deepchem/issues/1629.


Models
------

The models directory contains Jupyter notebooks used for creating the ground truth property models and those models' checkpoints, and a notebook that was used early on to implement a DeepChem tutorial model.

The notebooks directory contains Jupyter notebooks containing the sandbox model in the SimpleADDScenario and the more up-to-date SimpleADDScenarioColab notebooks, a notebook for visualing the distributions of molecular properties, and a notebook used for establishing a random-search baseline.

The scripts directory also contains a file simpleaddscenariocolab.py which is a script version of the Colab notebook edited to run on an HPC cluster (preliminary version of the file).

The images directory contains plots/images generated measuring the model progress with a variety of metrics.

Notes
-----

The temp directory contains a file "training_dataset.csv" that is used for training the model ensemble on the subsets of the data seen as the model progesses. This file is written to and read during the running of the sandbox model.

The list of packages and versions I had installed when DeepChem first worked for me is available at "DG Conda List Output 2019_6_10 (Functioning DeepChem)".


### Copyright

Copyright (c) 2019, Chodera Lab


#### Acknowledgements

DeepChem is available at https://github.com/deepchem/deepchem and https://deepchem.io.
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.
