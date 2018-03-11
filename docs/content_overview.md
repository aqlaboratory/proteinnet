# Content Overview
ProteinNet is comprised of four main components, described in detail below:
* Protein Records
* Protein Metadata
* Raw Data
* Supporting Code

## Protein Records
The core component of ProteinNet is made up of the protein record entries which can be used to train machine learning models. Each protein entry is comprised of:
* Sequence
* PSSM + Information Content
* Secondary Structure
* Tertiary Structure

**Sequences** are the primary amino acid chains that constitue a protein. They are represented by a string of characters with an alphabet size of 20. Our standard parser converts this into a variable-length tensor comprised of 20-dimensional one-hot vectors.

**PSSMs**, a.k.a. position-specific scoring matrices, summarize the propensity of each residue position along the protein chain to mutate to other amino acids. They are represented by a sequence of real-valued 20-dimensional vectors, normalized to range in value between 0 and 1. An additional dimension, corresponding to the information content of a residue, is concatenated with each vector to bring the total dimensionality to 21. We will provide multiple types of PSSMs, but the preliminary release of ProteinNet contains PSSMs derived using [JackHMMer](http://hmmer.org) from UniParc and metagenomic sequences.

**Secondary structure** is a categorical classification (8 classes) of the local structure of proteins, with the most prominent examples being [alpha helices](https://en.wikipedia.org/wiki/Alpha_helix) and [beta sheets](https://en.wikipedia.org/wiki/Beta_sheet). We derive our classification from the tertiary structure of the protein using the [DSSP](http://swift.cmbi.ru.nl/gv/dssp/) software package. As a result, it is more suitable as a prediction target as opposed to an input modality, although it can be used in either way. Secondary structure is represented by a string of characters with an alphabet size of 8. Our standard parser converts this into a variable-length tensor comprised of 8-dimensional one-hot vectors.

**Tertiary structure **

Protein records are grouped into six separate (but partially overlapping) data sets, corresponding to each of the CASP competitions, starting with CASP7 and ending in the most recent CASP12. Each data set is comprised of training and validation sets that only include data available prior to the start of the CASP assessment, and a test set comprised of the structures used during the CASP competition. The training set is available in multiple "thinnings", corresponding to how densely sampled in sequence space the entries are. The thinnings are at 30%, 50%, 70%, 90%, 95%, and 100% levels of sequence identity. The validation set is subdivided into distinct non-overlapping groups of varying difficulty, defined by their maximum sequence identity to the training set (at 100% thinning.) The difficulty levels are at 10%, 20%, 30%, 40%, 50%, 70%, and 90% sequence identities. For more information on the data clustering / splitting process see the [relevant](splitting_methodology.md) documentation page.
