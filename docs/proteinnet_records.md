# ProteinNet Records
ProteinNet is comprised of ProteinNet Records which can be used to train machine learning models. Each ProteinNet Record is in turn comprised of:

* Sequence
* PSSM + Information Content
* Secondary Structure
* Tertiary Structure
* Mask

**Sequences** are the primary amino acid chains that constitue a protein. They are represented by a string of characters with an alphabet size of 20. Our standard [parser](../code/tf_parser.py) converts this into a variable-length tensor comprised of 20-dimensional one-hot vectors; one dimension per amino acid, ordered alphabetically.

**PSSMs**, a.k.a. [position-specific scoring matrices](https://en.wikipedia.org/wiki/Position_weight_matrix), summarize the propensity of each residue position along the protein chain to mutate to other amino acids. They are represented by a sequence of real-valued 20-dimensional vectors (one dimension for each amino acid, ordered alphabetically), normalized to range in value between 0 and 1. An additional dimension, corresponding to the information content of a residue, is concatenated with each vector to bring the total dimensionality to 21. We will provide multiple types of PSSMs, but this preliminary release of ProteinNet contains PSSMs derived using [JackHMMer](http://hmmer.org) from UniParc and metagenomic sequences.

**Secondary structure** is a categorical classification (8 classes) of the local structure of proteins, with the most prominent examples being [alpha helices](https://en.wikipedia.org/wiki/Alpha_helix) and [beta sheets](https://en.wikipedia.org/wiki/Beta_sheet). We derive our classification from the [tertiary structure](https://en.wikipedia.org/wiki/Protein_tertiary_structure) of the protein using the [DSSP](http://swift.cmbi.ru.nl/gv/dssp/) software package. As a result, it is more suitable as a prediction target as opposed to an input modality, although it can be used in either way. Secondary structure is represented by a string of characters with an alphabet size of 8. Our standard parser converts this into a variable-length tensor comprised of 8-dimensional one-hot vectors; one dimension per DSSP class, using the following ordering: LHBEGITS. Note that secondary structure is not available in the current preliminary release of ProteinNet.

**Tertiary structure** is the three-dimensional atomic representation of a protein. The preliminary release of ProteinNet only contains the [backbone](https://en.wikipedia.org/wiki/Backbone_chain) atoms, corresponding to the sequential chain of N, C_alpha, and C' atoms. Each amino acid residue is represented by a real-valued 3x3 matrix, corresponding to the Cartesian coordinates of the three backbone atoms in picometers (relative to PDB files everything is multiplied by 100). The full protein is thus represented by a sequence of 3n 3-dimensional vectors, where n is the number of amino acids in a protein.

**Masks** are one-bit indicators of whether the atomic coordinates for a protein residue are present. Many protein structures, due to intrinsic or experimental reasons, do not have precisely defined positions for all atoms. Masks provide an explicit indicator of this information that can be incorporated into the learning algorithm, for example to prevent the loss function from penalizing predictions made of unknown atomic coordinates. They are represented by a string of characters with an alphabet size of 2 (+/-). Our standard parser converts this into a 2D binary matrix where columns and rows of residues containing missing atoms are set to 0, and all other entries are set to 1.

## Organization

ProteinNet Records are grouped into six data sets, corresponding to each of the CASP competitions, starting with CASP7 and ending with the most recent CASP12 (later data sets are supersets of earlier ones.) Each data set is comprised of training and validation sets that only include data available prior to the start of the CASP assessment (this restriction is applied to both the structures and sequences used in constructing MSAs), and a test set comprised of the structures used during the CASP competition.

The training set is available in multiple "thinnings", corresponding to how densely sampled (in sequence space) the entries are. The thinnings are at 30%, 50%, 70%, 90%, 95%, and 100% levels of sequence identity.

The validation set is subdivided into distinct non-overlapping groups of varying difficulty, defined by their maximum sequence identity to the training set (at 100% thinning.) The difficulty levels are at 10%, 20%, 30%, 40%, 50%, 70%, and 90% sequence identities. For more information on the data clustering / splitting process see the [relevant](splitting_methodology.md) documentation page.

Finally the test set records are classified into template-based modeling targets (TBM) corresponding to structures with known protein topologies, and free modeling targets (FM) corresponding to targets with novel topologies. The classification is derived from the official CASP classification but somewhat simplified. Specifically, proteins containing both TBM and FM domains, as well as domains classified as "FM/TBM", are all classified as "TBM-hard".

We do not _a priori_ define the relationship between the various components of a ProteinNet Record. We envision the primary use case to employ sequence and PSSM information as input, and secondary and tertiary structure as prediction targets. However nothing in the data requires this. For example, it’s possible to take the structure as input, and predict the sequence! (e.g. protein design.)

## File Formats

ProteinNet Records are currently provided in two file formats, a human- and machine-readable text file where each ProteinNet Record is of the following form:

```
[ID]
<class>#<pdb_id>_<chain_number>_<chain_id>
[PRIMARY]
<sequence>
[EVOLUTIONARY]
<pssm>
<ic>
[SECONDARY]
<secondary_structure>
[TERTIARY]
<tertiary_structure>
[MASK]
<mask>
```

where the quantities inside `<>` are strings and space-delimited arrays of the form previously described. The `<class>` field of the ID entry is only present in the validation and test sets, and corresponds to the sequence identity class and CASP class, respectively. For test set entries, the remainder of the ID field only contains the CASP identifier.

ProteinNet Records are also provided as `TFRecord` entries for use with [TensorFlow](https://www.tensorflow.org), along with a simple [parser](../code/tf_parser.py) to process these records. The `TFRecord` entries are grouped into files containing 256 records each to facilitate shuffling.
