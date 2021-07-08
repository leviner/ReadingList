07/06/21
## Authors:
Klevjar, Thor A. and Kaardvedt, Stein
## Title:
Split-beam target tracking can be used to study the swimming behaviour of deep-living plankton in situ
## Keywords:
acoustic, tracking, target strength, behavior, speed, swimming
## Geographic Coverage
Oslofjord, Norway
## Field Dates:
03/15/20013 - 03/17/2003
## Significance:


## Notes:
Shipboard EK500 splitbeam data was collected while three-point anchored. A large pelagic trawl was used to ground truth the species composition. A threshold for targets of -83 was used. Tracks were recorded where there was a minimum of 10 observations and no more than 1 skip and a change in vertical resolution of 10 cm. Swimming speeds were calculated based on the length of track and number of observations. Due to the errors associated with range, it was expected that swimming speeds would increase with depth.

Two additional filtration steps of managing errors:
- if echo n-1 match n+1...n+3, echo n was reassigned to the position of n-1.
- position of n was interpolated to be between n-1 and n+1 if it was not
- Data was then smoothed with a 3 point running mean

Large difference (bimodal) in TS was apparent and used to separate fish from zoops. Swimming speed (vertical and horizontal components) were reduced by use of filter/smoothing. Smoothing reduced bin-bin jumping as a result of split-beam resolution. This made the swim speed less dependent on range. This greatly improved the likely accuracy of distant tracks but creates a bias against fast swimming fish and may remove true behavioral artifacts.
