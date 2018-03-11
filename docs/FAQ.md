# FAQ
### Doesn’t CASP already do what ProteinNet purports to do?
Yes and no. CASP is critical to making ProteinNet possible by supplying the structures needed to make an effective test set. CASP organizers go to extraordinary lengths to secure protein structures which have not yet been deposited in publicly available servers, and can thus serve as blind targets for genuine _pre_-diction as opposed to mere _post_-diction. CASP organizers furthermore manually examine and categorize these structures into known (TBM) and unknown (FM) topologies, providing an objective third-party assessment of prediction difficulty. Participation in the actual CASP experiment is the gold standard for demonstrating a method's effectiveness at protein structure prediction, much like participation in the actual ImageNet competition in years past.

Similar to ImageNet, CASP occurs infrequently (once every two years), and so it cannot be realistically expected that every new method is tested during the official CASP assessment. And unlike ImageNet, which provides both the training and test data, CASP only specifies what the test data is, in the form of the prediction targets. It is generally accepted that all available data up to the beginning of a CASP experiment are allowed to be used. This makes it challenging 

Happens only once every two years.
Once CASP starts, the experiment has already changed, as the available data set has changed.

### What about CAMEO?
CAMEO is effectively an ongoing version of CASP, and is a fantastic service for assessing prediction quality. However, the issues regarding standardized training / test splits are present in CAMEO as they are in CASP, i.e. every new day the CAMEO assessment changes, which makes it difficult to compare new methods to old ones in an apples-to-apples manner. Furthermore, CAMEO targets tend to be of known topology, making it difficult to assess a model's ability to predict novel protein topologies such as those in the CASP FM category.


### Why is it a big deal how protein data sets are split?
Explain why splits are critical. Uniqueness of protein problem vs. things like computer vision, etc.

### Why is CASP7 the earliest one provided?


### Why isn't the raw data and MSAs available yet?
The full data set is very large (tens of TBs compressed). We are currently looking for sponsors that are able to host it.
