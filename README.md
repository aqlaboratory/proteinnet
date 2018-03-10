# ProteinNet
ProteinNet is a standardized data set for machine learning of protein structure. It provides a series of comprehensive data sets containing sequences, structures (secondary and tertiary), multiple sequence alignments ([MSAs](https://en.wikipedia.org/wiki/Multiple_sequence_alignment)), position-specific scoring matrices ([PSSMs](https://en.wikipedia.org/wiki/Position_weight_matrix)), and standardized [training / validation / test](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets) splits. ProteinNet builds on the biennial [CASP](http://predictioncenter.org/) assessments, which carry out blind predictions of recently solved but publicly unavailable protein structures, to provide test sets that push the frontier of computational methodology. 

Construction of this data set consumed millions of compute hours and was possible thanks to the generous support of the [Research Computing](https://rc.hms.harvard.edu) group at [Harvard Medical School](https://hms.harvard.edu).

**Note that this is a preliminary and incomplete release.** The raw data used for construction of the data sets, including the MSAs, are not available yet.

## Motivation
Protein structure prediction is one of the central problems of biochemistry. While the problem is well-studied within the biological and chemical sciences, it is less well represented within the machine learning community. We believe that if the barrier to entry to protein structure prediction is lowered, it can become a major source of innovation in ML research, alongside the canonical tasks of computer vision, NLP, and speech recognition. Much like ImageNet helped spur the development of new computer vision techniques, ProteinNet aims to facilitate ML research on protein structure by providing a standardized data set and set of benchmarks that any group can use to develop and compare new methodologies to existing ones, with minimal effort required to get started.

# FAQ
## Why not just use the PDB?
We certainly do use the PDB! But the PDB alone does not make a data set for the following reasons:
* Lack of standardization across structures
* No individual domains (we integrate ASTRAL)
* No MSAs or PSSMs. Compute intensive, but also no standardization, and historical record
* No standardized splits. Clustering provided by the PDB is very problematic for ML purposes as it contains substantial information leakage.

## Why is it a big deal how protein data sets are cross-validated?
Explain why splits are critical. Uniqueness of protein problem vs. things like computer vision, etc.
