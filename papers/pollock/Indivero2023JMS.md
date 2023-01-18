05/01/19
## Authors:
Indivero, Julia and Essington, Timothy E. and Ianelli, James N. and Thorson, James T.
## Title:
Incorporating distribution shifts and spatio-temporal variation when estimating weight-at-age for stock assessments: a case study involving the Bering Sea pollock (Gadus chalcogrammus)
## Keywords:
pollock, age-weight, stock assessment 
## Geographic Coverage
Eastern Bering Sea
## Field Dates:
N/A
## Significance:
Exploration of size-at-age spatial variability and how to address it in assessment models.

## Notes:
Spatio-temporal models can account for persistant spatial differences and how those spatial differences shift over time. These models are now being used to account for missing data in both space and time, including correcting for sampling differences like effort by area-weighting. But spatio-temporal models aren't used to standardize weight at age. These are typically produced with measurements from survey/fishery data. Standardizing weight at age is difficult sur to the role of environmental differences (temperature, food availability) on growth combined with the rolse of size and condition on spatial distribution (fish concentrate in suitable habitat or physiologically are unable to move between domains).

Here, they use EBS pollock as a case study to incoporate spatial and temporal changes in weight into abundance models to estimate weight at age for the population. The goals were to address
- How does weight-at-age vary spatially and temporally?
- How do local variations impact the size at age matrix?
- How does local variation in size vs abundance change the matrix?
- How does this complex method compare to a simpler empirical estimate?

Model was fitted using groundfish survey data from 1982-2019 using ahe, weight, and length measurements from specimen subsamples. Density at age was from the density-dependence corrected CPUE. Mean local size (w) for each year and age at each location was estimated using a glmm with a predictor for spatial, temporal, and spatio-temporal variation. The final model extrapolated density and weight at age across 500 equally spaced location in the Bering Sea and interpolated across the 51000+ grid cells of the model. Both density and weight were stimated across all years at each of these locations. An average weight at age for each age-class was claculated from the abundance-weighted size at age in every grid cell.

There were spatial differences by age-class, with smaller fish tending to be heavier on the outer shelf and larger fish being heavier on the innner shelf. The within-age variance was highest for young fish and decreased with age.

The size-at-age matrix was similarly impacted by both the spatial (10-25% impact) and spatio-temporal (2-20%) variance. 

Annual changes in size-at-age were due to local changes in size rather than local changes in abundance. I.e., when removing local variation in abundance, the variation in size did not change significantly, while when removing the variation in size, local variation dropped.

Compared with the empirical  mean, the use of spatio-temporal size-at-age marginally changed the annual biomass and abudnance estimates, and improved the ability to avoid underestimation. 

One of the key results was the large decrease in size-at-age for pollock, particularly larger fish, that is apparent over the course of the study period (1982-2019), consistent with reports from the fishery. Possible explanations are changes in the environment or size-selective fishing. 

By estimating abundance and sie together, they can compendate for uneven distributions in abundance an dpossible shifts in the distribution of fish when extrapolation from local size estimates to population size estimates. 

