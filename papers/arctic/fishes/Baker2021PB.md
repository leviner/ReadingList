04/27/21
## Authors:
Baker, Matthew R.
## Title:
Contrast of warm and cold phases in the Bering Sea to understand spatial distributions of Arctic and sub-Arctic gadids
## Keywords:
Arctic cod, walleye pollock, pacific cod, saffron cod, sea ice, thermal tolerance, habitat
## Geographic Coverage
Bering Sea
## Field Dates:
N/A
## Significance:
Analyses of 20+ years of ground fish surveys in the Bering Sea to identify habitat and temperature associations as well as recent changes in distribution of the four key North Pacific gadids.

## Notes:
The response of species to climate change may differ as a function of habitat constraints, thermal tolerances, behavior, and life cycle. Here, they examine the four species of gadids prevalent in the Pacific Arctic: sub-Arctic species Pacific cod and pollock and Arctic species Arctic cod and saffron cod.

(Note, this introduction is an excellent lit review of physical changes in the region and the role of temperature in species distributions)

This work aims to define the thermal tolerance ranges of the four key gadid species based on survey observations of biomass and water conditions, focusing on the differences between cold and warm stanzas experience in the Bering Sea.

Methods
- Survey Datasets
  - Eastern Bering Sea bottom trawl survey data dating back to 1982
  - Northern Bering Sea survey in 2010, 2017, and 2018
  - All survey data was collected with the same trawl gear (83-112), and normalized to CPUE (kg/ha)
- Environmental conditions included top layer (contiguous 1C of surface) and bottom (contiguous 1 degree of deepest) and the transition layer depth was identified as the region between the two.
- Sediment data from the historic NOAA dataset was included.
- Years were classified as 'cold' or warm' based on their temperature relative to the aggregate mean bottom temperatures for the EBS and NBS. 2017 and 2018 were separated out for their extreme conditions relative to the north Pacific marine heat wave that drove the warming in 2014-2016.
- Spatial distributions (weighted mean lat and lon) for each species were calculated
- Random Forests were used to predict the probability of species presence as a function of environmental conditions including sediment type and water conditions (note: a lot of detail included on he setup and plotting method).
- Habitat matrix was calculated as the joint PDF of temperature and depth.

Results
- There was no consistent warming trend in the Bering, however the recent years appear to start a new phase, with significant reductions in ice extent, leading to a complete absence of the cold pool in 2018.
- For Arctic gadids, areas with the highest variance in biomass were identical to the regions of total biomass, thus the major changes in biomass occur within the core habitat (increase in density but not range). For the sub-Arctic species, the highest variance was outside of their core habitat, suggesting that as biomass increases these species expand into other habitat. *"...indicating an ability to expand ranges at increased densities, or alternatively, an ability to increase biomass when the volume of suitable habitat expands"*
- Random forest associations:
  - Polar cod were sensitive to bottom temperature and were only found in water < 2C
  - Saffron cod, with less temperature dependence, were only found north of 58 N
  - Pollock were strongly influenced by temperature and a narrow intermediate (0-4) range of bottom temperatures, though spatially they had a bimodal distribution across longitude, likely reflecting ontogenetic behaviors in habitat partitioning.
- Biomass-weighted locations and temperatures
  - Polar cod: There was ~1C difference in temperatures occupied by Arctic cod in warm vs. cold periods, and moved slightly south during cold periods. In 2017 and 2018, Polar cod were nearly absent from the southeastern region of their historic summer distribution.
  - Saffron cod: Saffron cod were in water 2 C colder in cold years and ~2 C warmer in warm years, with no changes in latitude or longitude, occupying the same temperature regimes across all regimes.
  - Walleye pollock: ~0.5C colder in cold years an 1C warmer in warm years. In warm regimes, pollock biomass spread and shifted slightly north.
  - Pacific cod: Similar to pollock, there were no significant differences in depth, longitude, or latitude.
- In the NBS, there was a substantial (> 6000%) increase in pollock biomass while there was a 99% decrease.
- Most of the Polar cod in 2019 and 2018 in the NBS were 0 - 15 cm, while the lengths in 2017 were larger. In 2017-218, there was an increase in the adult size classes in walleye pollock and pacific cod in the NBS in particular.
