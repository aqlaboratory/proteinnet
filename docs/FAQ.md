# FAQ
## Why not just use the PDB?
We certainly do use the PDB! But the PDB alone does not make a data set for the following reasons:
* Lack of standardization across structures
* No individual domains (we integrate ASTRAL)
* No MSAs or PSSMs. Compute intensive, but also no standardization, and historical record
* No standardized splits. Clustering provided by the PDB is very problematic for ML purposes as it contains substantial information leakage.

## Why is it a big deal how protein data sets are cross-validated?
Explain why splits are critical. Uniqueness of protein problem vs. things like computer vision, etc.

## Why is CASP7 the earliest one provided?


## Why isn't the raw data and MSAs available yet?
The full data set is very large (tens of TBs compressed). We are currently looking for sponsors that are able to host it.
