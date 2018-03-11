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

There are six separate data sets, corresponding to each of the CASP competitions starting with CASP7 and ending in the most recent CASP12. Each data set is comprised of training and validation sets that only include data available prior to the start of the CASP assessment, and a test set comprised of the structures used during the CASP competition. The training and validation sets are themselves in subdivided. For the training set, we provide multiple levels of "thinning", i.e. 
