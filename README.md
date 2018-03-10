# ProteinNet
ProteinNet is a standardized data set for machine learning of protein structure. It provides a series of comprehensive data sets containing sequences, structures ([secondary](https://en.wikipedia.org/wiki/Protein_secondary_structure) and [tertiary](https://en.wikipedia.org/wiki/Protein_tertiary_structure)), multiple sequence alignments ([MSAs](https://en.wikipedia.org/wiki/Multiple_sequence_alignment)), position-specific scoring matrices ([PSSMs](https://en.wikipedia.org/wiki/Position_weight_matrix)), and standardized [training / validation / test](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets) splits. ProteinNet builds on the biennial [CASP](http://predictioncenter.org/) assessments, which carry out blind predictions of recently solved but publicly unavailable protein structures, to provide test sets that push the frontiers of computational methodology. 

Construction of this data set consumed millions of compute hours and was possible thanks to the generous support of the [Research Computing](https://rc.hms.harvard.edu) group at [Harvard Medical School](https://hms.harvard.edu).

**Note that this is a preliminary and incomplete release.** The raw data used for construction of the data sets, including the MSAs, are not yet available.

## Motivation
Protein structure prediction is one of the central problems of biochemistry. While the problem is well-studied within the biological and chemical sciences, it is less well represented within the machine learning community. We believe that if the barrier to entry to protein structure prediction is lowered, it can become a major source of innovation in ML research, alongside the canonical tasks of computer vision, NLP, and speech recognition. Much like ImageNet helped spur the development of new computer vision techniques, ProteinNet aims to facilitate ML research on protein structure by providing a standardized data set and set of benchmarks that any group can use to develop and compare new methodologies to existing ones, with minimal effort required to get started.

## Why not just use the [PDB](https://www.rcsb.org/)?
We certainly do use the PDB! But the PDB alone does not make a data set for the following reasons:
* Lack of a standardized approach for dealing with structural pathologies such as missing residues and fragments, multiple chains, etc.
* Lack of well-defined protein domains. We augment the PDB with information from [ASTRAL](http://scop.berkeley.edu/) to provide single domains as well as full-length protein entries.
* No MSAs or PSSMs, which can be extremely prohibitive to compute (millions of compute hours.)
* No standardized splits for training, validation, and test sets. This is a delicate process for protein sequences, as further explained here. The standard clustering provided by the PDB is not appropriate for machine learning purposes.

## Download

| All | CASP7 | CASP8 | CASP9 | CASP10 | CASP11 | CASP12 |
| --- | --- | --- | --- | --- | --- | --- |
| Text-Based | Text-Based | Text-Based | Text-Based | Text-Based | Text-Based | Text-Based |
| TF Records | TF Records | TF Records | TF Records | TF Records | TF Records | TF Records |

## Further Information

Please click the links below for additional information on ProteinNet.

* Contents overview
* Data split methodology
* FAQ
