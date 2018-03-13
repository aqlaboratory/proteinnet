# ProteinNet
ProteinNet is a standardized data set for machine learning of protein structure. It provides protein sequences, structures ([secondary](https://en.wikipedia.org/wiki/Protein_secondary_structure) and [tertiary](https://en.wikipedia.org/wiki/Protein_tertiary_structure)), multiple sequence alignments ([MSAs](https://en.wikipedia.org/wiki/Multiple_sequence_alignment)), position-specific scoring matrices ([PSSMs](https://en.wikipedia.org/wiki/Position_weight_matrix)), and standardized [training / validation / test](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets) splits. ProteinNet builds on the biennial [CASP](http://predictioncenter.org/) assessments, which carry out blind predictions of recently solved but publicly unavailable protein structures, to provide test sets that push the frontiers of computational methodology. It is organized as a series of data sets, spanning CASP 7 through 12 (covering a ten-year period), to provide a range of data set sizes that enable assessment of new methods in relatively data poor and data rich regimes.

**Note that this is a preliminary and incomplete release.** The raw data used for construction of the data sets, as well as the MSAs, are not yet available.

### Motivation
Protein structure prediction is one of the central problems of biochemistry. While the problem is well-studied within the biological and chemical sciences, it is less well represented within the machine learning community. We suspect this is due to two reasons: 1) a high barrier to entry for non-domain experts, and 2) lack of standardization in terms of training / validation / test splits that make fair and consistent comparisons across methods possible. If these two issues are addressed, we believe protein structure prediction can become a major source of innovation in ML research, alongside the canonical tasks of computer vision, NLP, and speech recognition. Much like [ImageNet](http://www.image-net.org) helped [spur the development](https://qz.com/1034972/the-data-that-changed-the-direction-of-ai-research-and-possibly-the-world/) of new computer vision techniques, ProteinNet aims to facilitate ML research on protein structure by providing a standardized data set, and standardized training / validation / test splits, that any group can use with minimal effort to get started.

### Approach
Once every two years the [CASP](http://predictioncenter.org/) assessment is held. During this competition structure predictors from across the globe are presented with protein sequences whose structures have been recently solved but which have not yet been made publicly available. The predictors make blind predictions of these structures, which are then assessed for their accuracy. The CASP structures thus provide a standardized benchmark for how well prediction methods perform at a _given moment in time_. The basic idea behind ProteinNet is to piggyback on CASP, by using CASP structures as test sets. ProteinNet augments these test sets with training / validation sets that _reset the historical record_ to the conditions preceding each CASP experiment. In particular, ProteinNet restricts the set of sequences (used for building PSSMs and MSAs) and structures to those available prior to the commencement of each CASP. This is critical as standard databases such as [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) do not maintain historical versions. We use time-reset versions of the [UniParc](http://www.uniprot.org/uniparc/) dataset as well as metagenomic sequences from the [JGI](https://img.jgi.doe.gov/) to build sequence databases for deriving MSAs. ProteinNet further provides carefully split validation sets that range in difficulty from easy (>90% seq. id.), useful for assessing a model's ability to predict minor changes in protein structure such as mutations, to extremely difficult (<10 seq. id.), useful for assessing a model's abiliy to predict entirely new protein folds, as in the CASP Free Modeling (FM) category. In a sense, our validation sets provide a series of transferability challenges to test how well a model can withstand distributional shifts in the data set. We have found that our most difficult validation subsets exceed the difficulty of CASP FM targets.

### Download
| All | CASP7 | CASP8 | CASP9 | CASP10 | CASP11 | CASP12* |
| --- | --- | --- | --- | --- | --- | --- |
| Text-Based | Text-Based | Text-Based | Text-Based | Text-Based | Text-Based | Text-Based |
| TF Records | TF Records | TF Records | TF Records | TF Records | TF Records | TF Records |

\* CASP12 test set is currently incomplete, owing to an embargo placed on some structures. When the embargo is lifted we will release all structures.

### Documentation
* [ProteinNet Records](docs/proteinnet_records.md)
* [Splitting Methodology](docs/splitting_methodology.md)
* [Raw Data](docs/raw_data.md)
* [FAQ](docs/FAQ.md)

### Citation
Please cite the forthcoming preprint on ProteinNet when it becomes available.

### Acknowledgements
Construction of this data set consumed millions of compute hours and was possible thanks to the generous support of the [Research Computing](https://rc.hms.harvard.edu) group at [Harvard Medical School](https://hms.harvard.edu). We also thank [Martin Steinegger](https://github.com/martin-steinegger) and Milot 
