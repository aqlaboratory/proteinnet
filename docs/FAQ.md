# FAQ
## Why not just use the PDB?
We certainly do use the PDB! But the PDB alone does not make a data set for the following reasons:
* Lack of a standardized approach for dealing with structural pathologies such as missing residues and fragments, multiple chains, etc.
* Lack of well-defined protein domains. We augment the PDB with information from ASTRAL to provided single domains and full-length protein entries.
* No MSAs or PSSMs, which can be extremely prohibitive to compute (millions of compute hours.)
* No standardized splits for training, validation, and test sets. This is a delicate process for protein sequences, as further explained here. The standard clustering provided by the PDB is not appropriate for machine learning purposes.

## Why is it a big deal how protein data sets are cross-validated?
Explain why splits are critical. Uniqueness of protein problem vs. things like computer vision, etc.

## Why is CASP7 the earliest one provided?


## Why isn't the raw data and MSAs available yet?
The full data set is very large (tens of TBs compressed). We are currently looking for sponsors that are able to host it.
