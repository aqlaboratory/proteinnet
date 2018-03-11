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

**Sequence** 

Protein records are grouped into six separate (but partially overlapping) data sets, corresponding to each of the CASP competitions, starting with CASP7 and ending in the most recent CASP12. Each data set is comprised of training and validation sets that only include data available prior to the start of the CASP assessment, and a test set comprised of the structures used during the CASP competition. The training set is available in multiple "thinnings", corresponding to how densely sampled in sequence space the entries are. The thinnings are at 30%, 50%, 70%, 90%, 95%, and 100% levels of sequence identity. The validation set is subdivided into distinct non-overlapping groups of varying difficulty, defined by their maximum sequence identity to the training set (at 100% thinning.) The difficulty levels are at 10%, 20%, 30%, 40%, 50%, 70%, and 90% sequence identities. For more information on the data clustering / splitting process see the [relevant](splitting_methodology.md) documentation page.
