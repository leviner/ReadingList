06/28/20
## Authors:
Liu, Yingjian and Qiu, Meng and Liu, Chao and Guo, Zhongwen
## Title:
Big data challenges in ocean observation: a survey
## Keywords:
big data, data storage, data analysis, ocean observations
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Overview and examples of methods for 'big data' in marine science, including industry standards and examples of applications

## Notes:
Oceanography is evolving towards the use of observatories to collect long-term and real-time data.  OOI for example uses of 800 intruments across 7 arrays, with AUVs, profilers, gliders, and fixed instruments to produce over 200 unique data products to collect observations from the air-sea interface to the sea floor. These data must be stored, read, calibrated, QC'd, processed, analyzed, and derived, creating new challenges as the systems are scaled up. Here, they outline systems of data acquisition, storage, computing, and analysis.

Data acquisition
- Ships and traditional ship-based methods, which have been improved as new instruments (i.e., multibeam) and capabilities (i.e., DP) have been introduced
- Satellites
- Seafloor electro-optical cabling: high bandwidth cable to provide both power and data transfer
- Drifters and floats: passive lagrangian platforms
- Moorings
- Gliders: buoyancy driven AUVs with low power consumption and high spatial coverage
- AUVs: Because of they're ability to move against currents, they can systematically survey a particular line/area/volume

Current major observing projects
- Argo : global array of free-drifting profiling floats that cover the upper 2000m of the water column
- Global Ocean Observing System: Combination of Argo, drifters, systems installed on yachts, research vessels, and commercial ships, and fixed mooring platforms
- Ocean Networks Canada: Two cabled observatories in the NE Pacific
- Integrated Ocean Observing System: National system integrating sensors across a variety of platforms across all scales
- Ocean Observing Initiative: Infrastructure project deploying sensors, mostly moorings, auvs, drifters with combined cabled and telemetered data delivery

Data storage - Long term observations and multiple data sources involve many different sensors, rapid expansion and complexity of data. There is a large amount of variety (few variables with huge volumes, large variety with few samples), and thus requires a variety of storage types across databases and raw storage.
- Storage itself: the three main structure as direct-attached storage network-attached storage, and storage area network, the last of which is best designed for scalable and bandwidth intensive systems.
- NoSQL databases
  - Key-value databases: data are stored to corresponding keys (dictionary style) which doesn't require pre-definition of structure or datatypes and thus is easily expandable
  - Column-oriented: process data according to column rather than row, where data doesn't have to be scanned and filtered and is directly selected
  - Document-oriented: "Documents", objects with no required structure, and thus no empty fields are necessary as in relational databases
- In-memory databases: Intermediate steps such as in-memory architecture can increase the speed of data delivery

Computing and analysis - because of the size of the data, parallel computing structure is necessary to efficiently mine and analyze data.
- Computational model: data can be stored across hundreds or thousands of servers, so parallel programming models are necessary to work with these distributed data. They give examples of specific industry examples.
-  Data analysis: There are many traditional methods (clustering, factor, correlation, regression analysis) that are applicable, and there are analyses that can be used to speed up the extraction of key information from the datasets. Data mining is essential to extract useful information (k-means, svm, c4.5, naive bayes, etc.). These need to be adapted for multi-source datasets and dynamic analysis of real-time stream data. Parallel processing improves efficiency by processing in a distributed and parallel manner. Once setup to be analyzed in parallel, more traditional methods can be implemented on larger datasets.
