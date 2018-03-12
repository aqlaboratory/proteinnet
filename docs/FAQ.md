# FAQ
### Why not just use the PDB?
We certainly do use the [PDB](https://www.rcsb.org/)! But the PDB alone does not make a data set for the following reasons:
* The PDB only provides structural data. It does not include MSAs or PSSMs, which can be very expensive to compute (millions of compute hours.)
* Raw PDB files lack a standardized approach for dealing with structural pathologies such as missing residues and multiple chains.
* Lack of protein domain boundaries, which we have found to be useful in modeling. We augment the PDB with information from [ASTRAL](http://scop.berkeley.edu/) to provide single domains as well as full-length protein entries.
* No standardized splits for training, validation, and test sets. This is a delicate process for protein sequences, as further explained here. The standard clustering provided by the PDB is not appropriate for machine learning purposes.

### Doesn’t CASP already do what ProteinNet purports to do?
Yes and no. [CASP](http://predictioncenter.org) is critical to making ProteinNet possible by supplying the structures needed to make an effective test set. CASP organizers go to extraordinary lengths to secure protein structures which have not yet been deposited in publicly available servers, and can thus serve as blind targets for genuine _pre_-diction as opposed to mere _post_-diction. CASP organizers furthermore manually examine and categorize these structures into known (TBM) and unknown (FM) topologies, providing an objective third-party assessment of prediction difficulty. Participation in the actual CASP competition is the gold standard for demonstrating a method's effectiveness at protein structure prediction, much like participation in the actual [ImageNet](http://www.image-net.org) competition in years past.

Similar to ImageNet however, CASP occurs infrequently (once every two years), and so it cannot be realistically expected that every new method is tested during the official CASP assessment. And unlike ImageNet, which provides both the training and test data, CASP only specifies what the test data is, in the form of prediction targets. It is generally accepted that all available data up to the beginning of a CASP competition are allowed to be used. This makes it challenging to fairly assess model accuracy after the completion of a CASP assessment, as the test structures are then usually widely available and can be inadvertently included in the training data. ProteinNet aims to address this shortcoming by providing time-reset training data that faithfully mimic the conditions of both the sequence and structural universes prior to the commencement of each CASP competition, making it possible to carry out retrospective assessments that mimic, but do not replace, the actual CASP competitions.

Note that like all such data sets, ProteinNet relies on the honor system. Unlike CASP, which has a built-in mechanism to insure that predictors only get one shot at making a prediction, the ProteinNet test set is publicly available, making overfitting possible through repeated evaluations. We consider such repeated evaluations, if they are not properly documented in the description of the testing methodology, to be a violation of the spirit of scientific inquiry. A general rule of thumb is that a test set is evaluated only once per paper, or that all test set evaluations are reported.

### What about CAMEO?
[CAMEO](https://www.cameo3d.org) is effectively an ongoing version of CASP, and is a fantastic service for assessing prediction quality. However, the issues regarding standardized training / test splits are present in CAMEO as they are in CASP, i.e. every new day the CAMEO assessment changes, which makes it impossible to compare new methods to old ones in an apples-to-apples manner. Furthermore, CAMEO targets tend to be of known topology, making it difficult to assess a model's ability to predict novel protein topologies such as those in the CASP FM category.

### Why care about time-reset protein sequences? Aren't structures all that matter?
With the advent of [co-evolution based methods](https://www.nature.com/articles/nrg3414) for protein structure prediction, which rely on building very large multiple sequence alignments (MSAs) to predict contacts in a 3D structure, the availability of protein sequences can now have a profound impact on a method's ability to predict protein structure. Thus the set of sequences included in a training set is as important as the set of structures.

### Why is CASP7 the earliest one provided?
CASP assessments prior to CASP7 do not have standardized parseable data, and the categorization of proteins into TBM / FM categories is not as well established. If the need arises to train models with very minimal data, for example for one-shot learning, we will consider building ProteinNet counterparts of earlier CASPs.

### Why isn't the raw data and MSAs available yet?
The full data set is very large (tens of TBs compressed). We are currently looking for sponsors that are able to host it. If you think you can help, [get in touch](mailto:alquraishi@hms.harvard.edu?subject=ProteinNet%20Hosting)!
