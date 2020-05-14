05/14/20
## Authors:
Brautaset, Olav and Waldeland, Anders Ueland and Johnsen, Espen and Malde, Ketil and Eikvil, Line and Salberg, Arnt-Børre and Handegard, Nils Olav
## Title:
Acoustic classification in multifrequency echosounder data using deep convolutional neural networks
## Keywords:
acoustic classification, big data, deep learning, machine learning, sandeel
## Geographic Coverage
North Sea
## Field Dates:
N/A
## Significance:
Use of a CNN to identify sandeel in multiple years of multifrequency data, demonstrating potential and advantages. Model performance was good but highly dependent on annotation and training setup, and performance varied by year.

## Notes:
In acoustic-trawl surveys, the assigning of backscatter to a category representing a single or group of species is typically done manually and can incur a lot of bias. Using survey features in addition to sampling, such as location and environmental conditions, plus acoustic features (response, position, angle) can help reduce this bias. Frequency response is the most commonly used tool, and is implemented in various ways, supervised and unsupervised. This method requires some additional assumptions, such as smoothing or bin size.

CNNs are leading models for image classification as they build a library of features from raw data. Typically early layers find the simple edges, lines, and corners while later layers look for more complicated features. Here the use deep learning to classify echosounder data from an acoustic survey without previous identification.

Methods

The data used comes from a sandeel survey in the North Sea with data collected at 18, 38, 120, and 200 kHz. Data were all interpolated into a common time/range grid and missing pings were filled in with -75 sV. There are 4 classes of acoustic assignment in the survey: sandeel, other, age-0, and possible sandeel. Every pixel was assigned a class based on response using LSSS. Identified regions of sandeel were annotated and "boxed". background values, inevitably caputured by the box which were below some Sv threshold were assigned to a "no-data/ignore" label.

Training data
- The echograms were divided into 4 (freqquencies) x 256 x 256 pixel segments and thresholded at -75 and 0 Sv.
- The dataset was built to contain an equal number of "background" and fish classes, plus seabed.
- Training and validation datasets were separated by witholding certain years.

Deep learning
- U-net pixel-wise segmentation netwrok witth convolutional encoder-decoder.
- Input:  4 frequency channels across a 256 x 256 pixel range-time subset.
- This gets "encoded" to a 16x16 "image" with only 1024 abstract features
- The decoder then ouputs for each class (background, other, sandeel) a 256x256 output.
- The three classes are then mapped to each pixel of the output, resulting in a 3x256x256 where each of the 3 layers is the probability of each class, summing to 1. This was then translated to a binary output where the predicted class was marked as 1.

The model was run for 5000 iterations using 16 random "images", and evaluated every 20th iteration. Precision is the prediced proportion of sandeel pixels that are correct, and recall is the fraction of the sandeel labels that are correctly predicted; If every pixel was labeled sandeel, recall would be 100%, but precision would be low. By predicting only 1 correct pixel, precision would be 1, but recall would low.

The model performed well on annotated date, however had difficulty on entire echograms as input, driven by two primary issues: missing annotations, thus innaccurate recall estimates, and false-positive predicitions on background classes with strong scatter (i.e., surface bubbles, which were not part of the "background" training set).

The primary advantage of such a model is that it doesn't require prioir feature extraction (i.e., calculating frequency response first), and avoids any need for pixel averaging and thus handles any resolution data.

Some issues
- the model is difficult to interpret.
- Manual annotations might be incorect and it is not possible to keep track of that uncertainty.
- Requires a large amount of training data.
- the survey annotations were not quite meant for machine learning (including low background noise is not an issue for abundance estimation)
- There is a major class imbalance in true acoustic data (a lot of background, little signal), so it is necessary to balance the exposure of the training model.

This process is more time efficient for looking at the entire survey dataset then doing so manually. There was a lot of variabiity in performance across years which could be due to missing annotations or other features, such as poor identification in low abundance where SNR is lower.
