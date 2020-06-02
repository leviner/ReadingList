06/02/20
## Authors:
Campbell, R W and Roberts, P L and Jaffe, J
## Title:
The Prince William Sound Plankton Camera: a profiling in situ observatory of plankton and particulates
## Keywords:
machine learning, zooplankton, computer vision, neural network
## Geographic Coverage
Prince William Sound
## Field Dates:
N/A
## Significance:
Application of convolutional neural network for identification of zooplankton species/taxa from profiling camera system over a 2-year deployment in PWS.

## Notes:
Assessing zooplankton in the context of ecosystem studies can be difficult due to the difficulty with enumerating. There is typically a high diversity of planktonic organisms which are typically measured using net sampling methods which and requires post-collection efforts to identify species which is time consuming and difficult for fragile taxa. In situ imagery addresses these concerns by providing the ability to identify taxa and size imaged plankton. Systems such as the VPR, ZOOVIS, and SPC as well as shadowgraph instruments have been developed. The difficulty is that most of these systems collect more images than can be manually identified.

Recent computing advances and methods development of convolutional neural networks are now being used to conduct zooplankton classification, and transfer network from previously conducted studies of zooplankton imagery can greatly speed up the training process. Here, they integrated a camera system into a near-shore profiler system and describe the CNN-based classification system used to identify zooplanlton images.

Profiler
- Prince William Sound Autonomous Moored Profiler is a buoyed platform in 200m depth and uses a cellular link for data transfer once it pierces the surface then pulls itself back to depth.
- The camera is a 12 MP color camera and uses a white led to focus images through a condenser lens, imaging ~450 ml with a pixel size of 22.6 um.
  - 4 Hz imaging of 12-bit.
  - An onboard computer segments all images and only retains ROIs that contain individual plankton and then down-sampled in order to store all data.
    - ROIs detected using Canny algorithm, then further processed to connect broken edges together
    - OpenCV findContours was used to detect the contours passing a size threshold and create a padded box to be subsampled and saved.
  - Images were downloaded via ethernet every 4-6 weeks on maintenance visits
- Live statistics were returned by the AMP to oversee data collection and the onboard system managed ROI timestamping and storage.

Image Processing
- Full resolution and color ROIs were reconstructed, contrast enhanced, and converted to 8 bits (each pixel as an integer)
- These images were then reprocessed
  - converted to greyscale and Sobel edge detector, then thresholded pixels to be 255 (where sobel values >2.5x the median) or 0.
  - Edges were then closes and the contour mask was smoothed with a Gaussian filter and applied to the color image.
- Images were rescaled to equal sizing of 299 x 299
  - To incorporate size as a classification feature, some features from the original ROIs (length, area, texture features) were included as a parallel network to be included before the final model layers

CNN
- Training
  - Images were split by size range, and 1/3 of the images from each year in each size group were used
  - Images were identified using Matlab GUIDE GUI system, including 18,868 images in 43 classes across taxa and visual characteristics
  - Accuracy was the primary metric of success
  - A subset of images were randomly flipped, rotated, and sheared between each training epoch

Results - 2,424,329 ROIs were collected over two years of instrument deployment
  - CNN model
    - Trained for 500 epochs
    - Training accuracy increasing to >90% by the 100th epoch
    - Validation accuracy and loss were variable but also improved at a similar rate
    - Wide range of F1 scores across the taxa (measure of accuracy as a function of precision and recall)
    - Assigning taxa based on the probability threshold is a function of the probability cutoff
      - More restrictive probability thresholds result in improved accuracy, however this potentially discards a significant number of images which may be taxa dependent such as among species with similar features

Discussion
- The image set was diverse, and there are discrepancies in the resolution, noise, and ability to identify for the human and likely computer reviewer
- Human accuracy is expected to be ~84-95% which may be possible for some taxa in the CNN based on confidence thresholds
- Filtering by probability can improve precision but is problematic for related classes
- Training set size can be a limitation for these very deep CNNs , and the inclusion of other datasets or transfer learning could improve the model
- The usefulness of this automatic classification is science-dependent
