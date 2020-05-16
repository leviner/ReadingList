# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, journal, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.  Upon reading each paper, a new note file is made, an addition is entered into the `.bib` file, and `readingStats.py` is executed to repopulate the below list and update the figures above.


## acoustics 
 

### autonomous 
 
* [Benoit-Bird2018LOM - Equipping an underwater glider with a new echosounder to explore ocean ecosystems](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Benoit-Bird2018LOM.md) 
     * An EK80 (WBT-Mini) was installed on a slocum glider and deployed in Monterey Bay.  This paper documents the instrumentation, installation, and preliminary data from the first deployments. 
* [DeRobertis2018InPrep - Comparison of acoustic backscatter measurements from unmanned sailing vehicles and a noise-reduced research vessel](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/DeRobertis2018InPrep.md) 
     * Currently in preparation manuscript on the 2016 Saildrone deployment in the Bering Sea, investigating vessel avoidance during opportunistic and follow-the-leader ship-saildrone comparisons. 
* [Kaartvedt2009MEPS - Use of bottom-mounted echo sounders in exploring behavior of mesopelagic fishes](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Kaartvedt2009MEPS.md) 
     * Reporting of observations from 3 months of a 15-month deployment of a moored upward facing EK60 in a fjord, with brief discussions of the behavior of lanternfish. Behaviors were derived from tracked fish, using population movement as the "current" to be removed from individual tracks. 
* [Kuhn2020MEPS - Test of unmanned surface vehicles to conduct remote focal follow studies of a marine predator](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Kuhn2020MEPS.md) 
     * Showed the feasibility of using saildrones to conduct focal follow surveys of northern fur seals and characterize their habitat use. 
* [Mordy2017O - Advances in Ecosystem Research: Saildrone Surveys of Oceanography, Fish, and Marine Mammals in the Bering Sea](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Mordy2017O.md) 
     * Overview of the 2016 Saildrone mission in the Bering Sea investigating relationships between fur seal bheavior and pollock distribution 
* [ODriscoll2018AS - Acoustic deployments reveal Antarctic silverfish under ice in the Ross Sea](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/ODriscoll2018AS.md) 
     * This is a proof of concept study using a moored echosounder (ASL AZFP) and discrete observations from ships (acoustic and optical) to determine the abundance and spawning grounds of Antarctic silverfish. 
* [Ohman2019LOM - Zooglider: An autonomous vehicle for optical and acoustic sensing of zooplankton](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Ohman2019LOM.md) 
     * A spray glider with integrated 200 and 1000 kHz sonar and zoocam shadow imaging camera. 
* [Ross2013MO - On the use of high-frequency broadband sonar to classify biological scattering layers from a cabled observatory in Saanich Inlet, British Columbia](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Ross2013MO.md) 
     * Used clustering to reduce the volume and discriminate between species/layers in long-term mooring data via spectral response, normalized spectra, and acoustic color. 
* [Urmy2012JMS - Measuring the vertical distributional variability of pelagic fauna in Monterey Bay](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Urmy2012JMS.md) 
     * Use of a moored 38kHz echosounder to look at the vertical distribution of backscatter and temporal variability over an 18-month deployment in Monterey Bay, CA, USA. 
* [UrmyHorne2016DSRI - Multi-scale responses of scattering layers to environmental variability in Monterey Bay, California](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/UrmyHorne2016DSRI.md) 
     * Use of a moored 38kHz echosounder to correlate backscatter with oceanographic variability over an 18-month deployment in Monterey Bay, CA, USA.  Same system used in [Urmy et al, 2012, *J. Mar. Sci.*](https://academic.oup.com/icesjms/article/69/2/184/701699). 
* [Verfuss2019MPB - A review of unmanned vehicles for the detection and monitoring of marine fauna](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Verfuss2019MPB.md) 
     * A review of passive and active acoustic integration into unmanned vehicles, aimed at marine animal monitoring. 

### targets 
 
* [Arrhenius2000FR - Can stationary bottom split-beam hydroacoustics be used to measure fish swimming speed in situ?](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Arrhenius2000FR.md) 
     * Arrhenius et al. deployed an upward facing echosounder in two lakes to determine the ability of a split-beam echosounder to track fish, using a stereo-video system to validate the recorded swim speeds. 
* [Balk2017FR - Surface-induced errors in target strength and position estimates during horizontal acoustic surveys.](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Balk2017FR.md) 
     * Simulations and field observations of TS and angle biases due to surface reflection in horizontal acoustics and target tracking.   
* [Bassett2018JMS - Broadband echosounder measurements of the frequency response of fishes and euphausiids in the Gulf of Alaska](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Bassett2018JMS.md) 
     * Demonstrate the variability in Sv spectra among different monospecific aggregations in the Gulf of Alaska and the limited ability to discriminate among species. 
* [Boswell2020FR - Examining the relationship between morphological variation and modeled broadband scattering responses of reef-associated fishes from the Southeast United States](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Boswell2020FR.md) 
     * Used CT scan swimbladder models to look at variability in common reef fish species in the Gulf of Mexico. Variability was high, and they report new TS-L relationships for their taxa. 
* [BrautasetJMS2020 - Acoustic classification in multifrequency echosounder data using deep convolutional neural networks](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/BrautasetJMS2020.md) 
     * Use of a CNN to identify sandeel in multiple years of multifrequency data, demonstrating potential and advantages. Model performance was good but highly dependent on annotation and training setup, and performance varied by year. 
* [Brede1990IMR - Target tracking with a split-beam echo sounder](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Brede1990IMR.md) 
     * Demonstration of the ability to track targets and the ability to determine target strength and directivity in the beam. 
* [EhrenbergTorkelson1996JMS - Application of dual-beam and split-beam target tracking in fisheries acoustics](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/EhrenbergTorkelson1996JMS.md) 
     * Discussion of dual-beam and split-beam fish tracking techniques and their application for fisheries research.  Appendix contains calculations for error/noise in split-beam angular estimates. 
* [Foote1987JASA - Fish target strengths for use in echo integrator surveys](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Foote1987JASA.md) 
     * An investigation into the backscattering cross section, or target strength, of fish, and the methods for in situ determination of TS and relating it to fish length.  Foote proposes a set of regression analyses from in situ measurements for generalized fish families based on available data. 
* [Stanton2003JMR - Inferring fish orientation from broadband-acoustic echoes](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Stanton2003JMR.md) 
     * Demonstration of the use of pulse-compressed broadband signal to constrain fish orientation by identifying multiple scattering sources within a single fish. 
* [TorgersenKaartvedt2001JMR - In situ swimming behaviour of individual mesopelagic fish studied by split-beam echo target tracking](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/TorgersenKaartvedt2001JMR.md) 
     * One of the earlier papers presenting the use of target tracking of individual fish to evaluate individual behavior.  Used a 38 kHz EK500 for data collection. 

### unsorted 
 
* [DeRobertis2019JMS - Amplifier linearity accounts for discrepancies in echo-integration measurements from two widely used echosounders](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/DeRobertis2019JMS.md) 
     * Found that echo-integration measurements of Ek80 are lower than those of EK60, and the range-dependency of the differences suggested a non-linear amplification in one of the systems which was identified within the EK60. 
* [Lavery2017JMS - Exploiting signal processing approaches for broadband echosounders](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/Lavery2017JMS.md) 
     * Demonstration of a) calibration based on frequency-dependent bandwidth and b) use of tapered match filter on untapered signal to resolve targets near boundaries. 
* [LevineDeRobertis2019FR - Don’t work too hard: Subsampling leads to efficient analysis of large acoustic datasets](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/LevineDeRobertis2019FR.md) 
     * Demonstration of systematic subsampling to produce similar survey means with reduced user effort. 
* [Ona1996JMS - Acoustic sampling and signal processing near the seabed: The deadzone revisited](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/Ona1996JMS.md) 
     * Description and equations for acoustic dead zone and sA correction. 
* [Rose1995JMS - Cod (Gadus morhua L.) migration speeds and transport relative to currents on the north-east Newfoundland Shelf](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/Rose1995JMS.md) 
     * Observations of cod migration from spawning to feeding grounds over 3 years using acoustic detection of shoal centroid.  Observations indicate fish use active behavior to remain within the migration route. 

## ecology 
 

### fishes 
 
* [Basolo1990S - Female preferences predates the evolution of the sword in swordtail fish](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Basolo1990S.md) 
     * Observations testing the selection by females of a non-ancestral trait in males. 
* [Berdahl2013S - Emergent Sensing of Complex Environments by Mobile Animal Groups](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Berdahl2013S.md) 
     * Investigating the mechanisms of group behavior response to environmental gradients in fish. 
* [Biro2003E - From individuals to populations: Prey fish risk-taking mediates mortality in whole-system experiments](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Biro2003E.md) 
     * Whole lake studies of rainbow trout where they conclude that mortality due to predation depends largely on food-dependent risk taking rather than predator density. 
* [Brown2014BES - Background level of risk determines the intensity of predator neophobia in juvenile convict cichlids](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Brown2014BES.md) 
     * Background level of predation risk (pre-exposure) is a stronger driver of neophobic response than concentration of cue. 
* [Catano2017O - Predator identity and time of day interact to shape the risk–reward trade-off for herbivorous coral reef fishes](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Catano2017O.md) 
     * Herbivorous fish show a threat-sensitive response by decreasing foraging near models of predators, but the effect is dependent on time of day. 
* [Chapman2011EL - To boldly go: Individual differences in boldness influence migratory tendency](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Chapman2011EL.md) 
     * Investigating the role of boldness in determining which individuals migrate in a partially migrating species.  Individual predation vulnerability, higher in bold fish, possibly the main factor driving the decision to migrate. 
* [Chapman2012JFB - Partial migration in fishes: Causes and consequences](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Chapman2012JFB.md) 
     * Review of partial migration strategies, and the evolutionary causes and management consequences. 
* [Clayton1987B - Why Mudskippers Build Walls](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Clayton1987B.md) 
     * Shows the impact of compressibility (increasing density) on territoriality through the use of mudwalls to define spaces and limit aggression between neighbors. 
* [Couzin2011S - Uninformed Individuals Promote Democratic Consensus in Animal Groups](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Couzin2011S.md) 
     * In the presence of a strongly opinionated majority, the introduction of naive (unbiased) individuals helps to return group decision making to the majority 
* [Dixson2008PRSB - Coral reef fish smell leaves to find island homes](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Dixson2008PRSB.md) 
     * Clownfish appear to have an innate olfactory attraction to rainforest vegetation which could be used to search out suitable habitat on island-associated reefs. 
* [Ebersole1977E - The Adaptive Significance of Interspecific Territoriality in the Reef Fish Eupomacentrus Leucostictus](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Ebersole1977E.md) 
     * Both food resource and nest defense are prominent functions of interspecific territoriality 
* [Fausch1984CJZ - Profitable stream positions for salmonids: relating specific growth rate to net energy gain](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Fausch1984CJZ.md) 
     * Salmon select focal points based on water-velocity and food supply to maximize net gain, and in specific regions, further organization is dictated by hierarchies in which dominant fish hold more optimal positions and thus increase their growth rates. 
* [Fausch2014EBF - A historical perspective on drift foraging models for stream salmonids](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Fausch2014EBF.md) 
     * An overview, given by Fausch, of the development of his drift foraging model and expansion and extended applications that have occurred since. 
* [Genner1999JAE - Resource control by territorial male cichlid fish in Lake Malawi](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Genner1999JAE.md) 
     * Interspecific territoriality may reduce competition between species with different diets, thus promoting coexistence and high levels of diversity. 
* [Mehner2012FB - Diel vertical migration of freshwater fishes - proximate triggers, ultimate causes and research perspectives](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Mehner2012FB.md) 
     * Review of patterns and mechanism of DVM in freshwater fish. 
* [Methot1986CR - Frame trawl for sampling pelagic juvenile fish](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Methot1986CR.md) 
     * Overview of Methot net for sampling of pelagic juvenile fish and zooplankton 
* [Parrish2002BB - Self-organized fish schools: An examination of emergent properties](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Parrish2002BB.md) 
     * Tries to detangle the role of social and asocial forcings, and the mechanisms of why fish school through exploration of previous model development and their own. 
* [Pedersen2009FR - Advection and retention as life trait modulators of capelin larvae-A case study from the Norwegian coast and the Barents Sea](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Pedersen2009FR.md) 
     * Use of particle simulation modeling and larval surveys to investigate the role of mesoscale eddies on the transport/retention of capelin larvae along he Norwegian coast. 
* [Philipp2009TAFS - Selection for Vulnerability to Angling in Largemouth Bass](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Philipp2009TAFS.md) 
     * Long-term breeding study showing that vulnerability to recreational angling in largemouth bass is an inheritable trait. 
* [Power1984E - Depth Distributions of Armored Catfish: Predator-Induced Resource Avoidance?](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Power1984E.md) 
     * Showed that for this population of loricariids, predation avoidance was more important than resource exploitation, and is dependent on age. 
* [Robinson2019MEPS - Predation strategies of larval clownfish capturing evasive copepod prey](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Robinson2019MEPS.md) 
     * Observe and quantify the feeding success and failure of larval fish as a function of both fish age (day post-hatch) and copepod stage. 
* [Rose1995JMR - Cod (Gadus morhua L.) migration speeds and transport relative to currents on the north-east Newfoundland Shelf](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Rose1995JMR.md) 
     * Observations of cod migration behavior by tracking agreggations using acoustics. They identify changes in school behavior with seaward/shoreward flow that suggest active transport. 
* [ScheuerellSchindler2003E - Diel Vertical Migration by Juvenile Sockeye Salmon: Empirical Evidence for the Antipredation Window](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/ScheuerellSchindler2003E.md) 
     * Juvenile sockeye migrate to maintain a specific light environment to minimize predation risk in lakes. 
* [Sisneros2009IZ - Adaptive hearing in the vocal plainfin midshipman fish: getting in tune for the breeding season and implications for acoustic communication.](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Sisneros2009IZ.md) 
     * A review of the plasticity of frequency sensitivity in midhsipman 
* [Ward2011PNAS - Fast and accurate decisions through collective vigilance in fish shoals](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Ward2011PNAS.md) 
     * Lab tests showing that speed and accuracy of predator avoidance increase as a function of group size. 
* [WardHart2003FF - The effects of kin and familiarity on interactions between fish](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/WardHart2003FF.md) 
     * Review of literature on role of recognition of relatedness in interactions. 
* [Warner1988N - Traditionality of mating-site preferences in a coral reef fish](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/Warner1988N.md) 
     * Observations of traditionalism in wrasse who appear establish mating territories based on traditional sites rather than resource assessment. 
* [WarnerHoffman1980E - Population Density and the Economics of Territorial Defense in a Coral Reef Fish](https://github.com/leviner/ReadingList/tree/master/papers/ecology/fishes/WarnerHoffman1980E.md) 
     * Implications of density on mating success of territorial male reef fishes, showing that decreased density of fish leads to less time defending and thus more time for mating. 

### general 
 
* [Burrows2019NCC - Ocean community warming responses explained by thermal affinities and temperature gradients](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Burrows2019NCC.md) 
     * Demonstrate the effect of temperature on community shifts independent of other pressures based on the thermal niches of species within marine communities. 
* [Gross1994TREE - The evolution of behavioural ecology](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Gross1994TREE.md) 
     * Brief letter on the history of behavioral ecology as a field 
* [Heithaus2007JAE - State-dependent risk-taking by green sea turtles mediates top-down effects of tiger shark intimidation in a marine ecosystem](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Heithaus2007JAE.md) 
     * Found that sea turtles in better condition were more likely to move out of regions of higher food quality when risk of predation increased.  Shark presence has non-lethal implications on the turtle and thus the seagrass population. 
* [Helfman1999EBF - Behavior and fish conservation: introduction, motivation, and overview Gene](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Helfman1999EBF.md) 
     * The introduction to a special issue on behavior and fish conservation 
* [Lampert1989FE - The Adaptive Significance of Diel Vertical Migration of Zooplankton](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Lampert1989FE.md) 
     * Describes how DVM varies individually within a migrating population based on a compromise between predation pressure, food availability and temperature gradients. 
* [Lima1998B - Nonlethal Effects in the Ecology of Predator-Prey Interactions](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Lima1998B.md) 
     * Prey put in a significant amount of effort to avoid predation, and this behavior has major implications at the individual, population, and ecosystem level.  A review of the current research. 
* [LimaDill1990CJZ - Behavioral decisions made under the risk of predation: a review and prospectus](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/LimaDill1990CJZ.md) 
     * Risk of predation is integral to decision making.  Here they outline many of the factors influenced by predation risk. 
* [Pister1999EBF - Professional obligations in the conservation of fishes](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Pister1999EBF.md) 
     * Editorial on the values and professional responsibilities of a fisheries researcher 
* [Shuterlad1998AB - The importance of behavioural studies in conservation biology.](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Shuterlad1998AB.md) 
     * Review discussing key fields and research where behavioral studies can assist conservation 
* [Woillez2009ALR - Notes on survey-based spatial indicators for monitoring fish populations](https://github.com/leviner/ReadingList/tree/master/papers/ecology/general/Woillez2009ALR.md) 
     * A manual of spatial indicators for use in fisheries ecology to describe population distribution. 

## other 
 

### visualizations 
 
* [Rougier2014PLOSCB - Ten Simple Rules for Better Figures](https://github.com/leviner/ReadingList/tree/master/papers/other/visualizations/Rougier2014PLOSCB.md) 
     * Study of body and lipid condition under different temperature-food conditions, showing temperature directly impacts larval A cod and pollock, and condition varies with both temperature and food availability. 

## pacificArctic 
 

### circulation 
 
* [AhlnasGarrison1984A - Satellite and oceanographic observations of the warm coastal current in the Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/AhlnasGarrison1984A.md) 
     * Satellite observations of the Alaskan Coastal Current and the role of the current in the melt back of Chukchi Sea ice. 
* [CorlettPickart2017PO - The Chukchi slope current](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/CorlettPickart2017PO.md) 
     * The authors describe the observation of a westward flow that advects a significant portion of Pacific-origin water, predominantly winter water, westward along the slope, as well as a weaker shelfbreak jet moving shallower water to the east. 
* [Danielson2017DSRII - A comparison between late summer 2012 and 2013 water masses, macronutrients, and phytoplankton standing crops in the northern Bering and Chukchi Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Danielson2017DSRII.md) 
     * This paper presents an overview of the physical, chemical, and phytoplankton observations as they relate to winds, flow, and ice conditions as observed during the 2012 and 2013 Arctic EIS program.  First set of "physics to fish" observations covering the whole region. 
* [Gong2015DSRII - Summertime circulation in the eastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Gong2015DSRII.md) 
     * Description of the water masses and transport across the Chukchi as observed in late-summer, focussed on the flow from Bering Strait to Barrow canyon and the implications on the Arctic basin. 
* [Gong2016DSRII - Early summer water mass transformation in the eastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Gong2016DSRII.md) 
     * Detection of a dense Chukchi Sea Water and the description of possible sources due to formation relating tot he modification of water masses as they are transported across the NE Chukchi Shelf via observation during early summer. 
* [Martini2016JGRO - Dependence of subsurface chlorophyll on seasonal water masses in the Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Martini2016JGRO.md) 
     * Mapping of the subsurface chlorophyll maximum in the NE Chukchi Sea in late-summer, and the variability in nutrients and chlorophyll with hydrography and meltwater/summer water fronts.  They show that SCM depth in late summer is sensitive to seasonal changes in hydrography. 
* [Pickart2016DSRII - Circulation of winter water on the Chukchi shelf in early Summer](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Pickart2016DSRII.md) 
     * Study of the movement of winter water in the NE Chukchi Sea, describing the circulation and transport around Hanna Shoal towards Barrow Canyon. 
* [Pisareva2017DSRII - On the nature of wind-forced upwelling in Barrow Canyon](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Pisareva2017DSRII.md) 
     * Study of Barrow Canyon upwelling, describing differences in warm and cold seasons and wind speed dependence. 
* [Stabeno2018JGRO - Flow Patterns in the Eastern Chukchi Sea: 2010–2015](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Stabeno2018JGRO.md) 
     * A synthesis of mooring, drifter, model, and satellite observations of the flow and physical oceanography in the NE Chukchi Sea. 
* [WangJC2015 - Historical changes in the Beaufort-Chukchi-Bering Seas surface winds and waves, 1971-2013](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/WangJC2015.md) 
     * Analysis of historical trends in wind speed and surface waves in the PAR to determine long term trends in waves, showing increases in wave height and period. 
* [Weingartner1997AFS - A review of the Physical Oceanography of the Northeastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Weingartner1997AFS.md) 
     * A review of the physical oceanography published in 'Fish Ecology in Arctic North America', AFS symposium proceedings.  Outlines the physical oceanography during the ice-free season in the NE Chukchi. 
* [Woodgate2005DSRII - A year in the physical oceanography of the Chukchi Sea: Moored measurements from autumn 1990-1991](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2005DSRII.md) 
     * Mooring data from a 1-year deployment of CTDs and ADCPs across US and Russian waters of the Chukchi Shelf, to present the seasonality and flow across the entire Chukchi Sea over 1 year. 
* [Woodgate2012GRL - Observed increases in Bering Strait oceanic fluxes from the Pacific to the Arctic from 2001 to 2011 and their impacts on the Arctic Ocean water column](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2012GRL.md) 
     * Trends of transport at Bering Strait from 2001 to 2011 
* [Woodgate2015OCN - A Synthesis of Year-Round Interdisciplinary Mooring Measurements in the Bering Strait (1990-2014) and the RUSALCA Years (2004-2011)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2015OCN.md) 
     * Overview of the ADCP and other moored sensors deployed from 1990-2014 in the Bering Strait.  Stresses the importance of the Bering Strait as the sole conduit of water into the Arctic from the Pacific.  Near-complete 24 year time series of flow through Bering Strait. 
* [Woodgate2018PO - Increases in the Pacific inflow to the Arctic from 1990 to 2015, and insights into seasonal trends and driving mechanisms from year-round Bering Strait mooring data](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2018PO.md) 
     * Trends of transport at Bering Strait from continuous measurements from 19990 - 2016.  Transport increase of .01-.02 Sv/year, driven by changes in the pressure head. 

### fishes 
 
* [Aronovich1975AC - Egg incubation and larval rearing of navaga (Eleginus navaga Pall.), polar cod (Boreogadus saida lepechin) and arctic flounder (Liopsetta glacialis Pall.) in the laboratory](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Aronovich1975AC.md) 
     * Early description of Arctic cod egg and larval stages through incubation experiments, with developmental timing and growth rates 
* [Benoit2008JGRO - Hydroacoustic detection of large winter aggregations of Arctic cod (Boreogadus saida) at depth in ice-covered Franklin Bay (Beaufort Sea)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Benoit2008JGRO.md) 
     * This study describes the presence and dispersal of a large, dense aggregation of Arctic cod observed overwinter in Franklin Bay, and aims to explore the physical and behavioral mechanisms responsible for their retention in deep water. 
* [Benoit2014PB - Pre-winter distribution and habitat characteristics of polar cod (Boreogadus saida) in southeastern Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Benoit2014PB.md) 
     * Investigate the distribution of age-0 and age-1+ aggregations of Arctic cod in the Canadian Beaufort in early Winter. 
* [Berge2020CB - Artificial light during the polar night disrupts Arctic fish and zooplankton behaviour down to 200 m depth](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Berge2020CB.md) 
     * Measurements of ship light influence on water column backscatter, which indicate that orientation change is likely responsible for rapid variability, and ship impacts are spatially limited. 
* [Bouchard2016PB - Contrasting the early life histories of sympatric Arctic gadids Boreogadus saida and Arctogadus glacialis in the Canadian Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Bouchard2016PB.md) 
     * Comparison of A. glacialis and B. saida early life stages, including hatching, feeding, length at age, and mortality over April to August in two years of freeze-in sampling. 
* [Bouchard2017PO - Climate warming enhances polar cod recruitment, at least transiently](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Bouchard2017PO.md) 
     * Analysis of the impact of ice retreat timing and SST on the success of B. saida in the Canadian Beaufort over a 10 year period of sampling.  Describe the positive correlations between hatcher success and SST/early ice retreat. 
* [BouchardFortier2008MEPS - Effects of polynyas on the hatching season, early growth and survival of polar cod Boreogadus saida in the Laptev Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/BouchardFortier2008MEPS.md) 
     * Observations of larval Arctic cod populations in a high polynya occurrence (2005) and low occurrence (2003) year.  Conclude that maximizing pre-winter size is more important than matching food availability when hatching, and freshwater input (warm) promotes earlier hatching a growth to maximize both size at age and pre-winter success. 
* [BouchardFortier2011PO - Circum-arctic comparison of the hatching season of polar cod Boreogadus saida: A test of the freshwater winter refuge hypothesis](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/BouchardFortier2011PO.md) 
     * This paper looks at the hatch date frequency distribution in six regions of differing freshwater input, and find evidence to support the winter refuge hypothesis that Arctic cod in lower saline environments have a greater pre-winter size due to faster development and earlier hatching. 
* [Bradstreet1986DFO - Aspects of the Biology of Arctic Cod ( Boreogadus saida ) and its Importance in Arctic Marine Food Chains](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Bradstreet1986DFO.md) 
     * Technical report on the importance of Arctic cod to the Canadian Arctic ecosystem, covers aspects of distribution, physiology, and ecological significance across North American waters.  Includes review of much of the work done prior to the 1980s, and a focus on ringed seal predation of A. cod. 
* [Buckley2016EBF - Variation in the diet of Arctic Cod (Boreogadus saida) in the Pacific Arctic and Bering Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Buckley2016EBF.md) 
     * They look at the summer diet of arctic cod across multiple age classes from opportunistic samples throughout the Chukchi and Bering Sea.  Along a north-south gradient in the ECS, copepods dominate diets at higher latitudes, euphausiids at lower latitudes.  Larger fish have a more diverse diet of larger prey (decapods, fishes).  Arctic cod are highly opportunistic. 
* [Copeman2017MEPS - Temperature impacts on lipid allocation among juvenile gadid species at the Pacific Arctic-Boreal interface: An experimental laboratory approach](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Copeman2017MEPS.md) 
     * Measured temperature dependence of lipid accumulation in juvenile Arctic cod, Saffron cod, Pacific cod, and pollock. 
* [Craig1982CJFAS - Ecological Studies of Arctic Cod (Boreogadus saida) in Beaufort Sea Coastal Waters, Alaska](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Craig1982CJFAS.md) 
     * One of the earlier papers investigating the life history of Arctic cod from samples collected off the north slope of Alaska both nearshore and on the shelf break.  Arctic cod were found to be present in the coastal Beaufort year round. 
* [Crawford2016PB - Occurrence of a gelatinous predator (Cyanea capillata) may affect the distribution of Boreogadus saida, a key Arctic prey fish species](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Crawford2016PB.md) 
     * This paper presents evidence of jellyfish avoidance by Arctic cod in a shallow bay of the Canadian Arctic Archipelago.  The authors describe observations of partitioning which they attribute primarily to avoidance. 
* [Dahlke2018SA - Northern cod species face spawning habitat losses if global warming exceeds 1.5°C](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Dahlke2018SA.md) 
     * Investigating the mpact of temperature and pCO2 on egg and larval development from broodstock. Additionally, they model loss of appropriate spawning areas based on future climate scenarios. 
* [DeRobertis2015DSRIIa - Species and size selectivity of two midwater trawls used in an acoustic survey of the Alaska Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/DeRobertis2015DSRIIa.md) 
     * De Robertis et al. conducted a trawl selectivity experiment using recapture nets on a modified-Marinovich trawl to asses the species- and size-specific selectivity.  There is significant escapement, even for the most abundant species, and this analysis is required to properly calculate biomass/abundance estimates for juvenile Arctic cod. 
* [DeRobertis2017DSRIIb - Abundance and distribution of Arctic cod (Boreogadus saida) and other pelagic fishes over the U.S. Continental Shelf of the Northern Bering and Chukchi Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/DeRobertis2017DSRIIb.md) 
     * Two broad-scale baseline acoustic-trawl surveys were conducted in 2012 and 2013. 
* [Drost2016JEB - Acclimation potential of Arctic cod (Boreogadus saida) from the rapidly warming Arctic Ocean](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Drost2016JEB.md) 
     * Laboratory observations of thermal tolerance via measurements of respiration and heart rate to acute changes across various acclimation temperatures.  Shows ability to acclimate to temperatures through changes in aerobic ability and scope after 1-month of exposure. 
* [Eisner2013PB - Pelagic fish and zooplankton species assemblages in relation to water mass characteristics in the northern Bering and southeast Chukchi seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Eisner2013PB.md) 
     * Characterization of the zooplankton and pelagic fish community in relation to the physical and biological properties of the water masses in the northern Bering and southern Chukchi Seas. 
* [Fossheim2015N - Recent warming leads to a rapid borealization of fish communities in the Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Fossheim2015N.md) 
     * Evidence of rapid borealization in the Barents sea through community-wide geographic shifts from 2004-2012, credited to the northward expansion of thermal habitat for boreal species. Consequences for shifting energy pathways. 
* [Geoffroy2011PB - The aggregation of polar cod (Boreogadus saida) in the deep Atlantic layer of ice-covered Amundsen Gulf (Beaufort Sea) in winter](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Geoffroy2011PB.md) 
     * Overwinter observations of vertical distribution of Arctic cod aggregations in the Canadian Beaufort, showing changes in depth distribution with water, light, and prey conditions. 
* [Geoffroy2016PB - Vertical segregation of age-0 and age-1+ polar cod (Boreogadus saida) over the annual cycle in the Canadian Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Geoffroy2016PB.md) 
     * The authors observed two distinct layers of arctic cod, an epipelagic layer of age-0 fish which forms in spring, begins DVM in summer, and settles to depth in late fall, and a mesopelagic layer of age-1+ fish.  They used TS to estimate length at depth to show a stratification and seasonal vaibility in the two layers, as well as estimate biomass. 
* [Geoffroy2019FMS - Mesopelagic sound scattering layers of the high Arctic: Seasonal variations in biomass, species assemblage, and trophic relationships](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Geoffroy2019FMS.md) 
     * Observations of mesopelagic scattering layers in the high arctic, describing the seasonality of the SSL, including the condition of the organisms and trophic interactions. 
* [GrahamHop1995A - Aspects of Reproduction and Larval Biology of Arctic Cod (Boreogadus saida)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/GrahamHop1995A.md) 
     * Study of larval fish ecology of Arctic cod, describing timing and sizes of larval phases. 
* [Gray2016PB - Variability in the summer diets of juvenile polar cod (Boreogadus saida) in the northeastern Chukchi and western Beaufort Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Gray2016PB.md) 
     * Description of diet variability in age-0 to age-2 arctic cod in the Chukchi and Beaufort Seas.  Publication of enumerated prey species. 
* [HopGjosaeter2013MBR - Polar cod ( Boreogadus saida ) and capelin ( Mallotus villosus ) as key species in marine food webs of the Arctic and the Barents Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/HopGjosaeter2013MBR.md) 
     * Comparison of the distribution of B. saida and capelin based on observations of both stocks since the 1970s.  Gives overview of both species life cycle and impacts of heating and reduced sea ice on populations individually and potential interactions. 
* [Huserbraten2019CB - Polar cod in jeopardy under the retreating Arctic sea ice](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Huserbraten2019CB.md) 
     * Backtracking modelling of age-0 polar cod dispersal, indicating that recruitment is largely correlated with ice presence and summer surface temperatures. 
* [Kent2016JFB - Laboratory rearing of wild Arctic cod Boreogadus saida from egg to adulthood](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Kent2016JFB.md) 
     * Specifics of process used for multiyear rearing of B. saida in aquarium conditions, including specific measurements of spawning, growth, and key development milestones for fish reared at 3.5C. 
* [Kessel2016PB - Distinct patterns of Arctic cod (Boreogadus saida) presence and absence in a shallow high Arctic embayment, revealed across open-water and ice-covered periods through acoustic telemetry](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Kessel2016PB.md) 
     * The authors use acoustic telemetry (tagging) to investigate the spatial distribution of arctic cod in Resolute Bay in ice free and covered periods, and their presence in relation to environmental changes and predator presence. 
* [Koenker2018JMS - Impacts of temperature and food availability on the condition of larval Arctic cod (Boreogadus saida) and walleye pollock (Gadus chalcogrammus)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Koenker2018JMS.md) 
     * Study of body and lipid condition under different temperature-food conditions, showing temperature directly impacts larval A cod and pollock, and condition varies with both temperature and food availability. 
* [Kono2016PB - Distribution pattern of Polar cod (Boreogadus saida) larvae and larval fish assemblages in relation to oceanographic parameters in the northern Bering Sea and Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Kono2016PB.md) 
     * Examination of larval A. cod in relation to the environment in 2008 and 2013.  They hypothesize two different spawning areas, one in the Gulf of Anadyr and one possibly in the Chukchi leading to distributions in similar water conditions in two separate regions. 
* [Laurel2016PB - Temperature-dependent growth and behavior of juvenile Arctic cod (Boreogadus saida) and co-occurring North Pacific gadids](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Laurel2016PB.md) 
     * Laboratory temperature experiments were conducted on gadidae to investigate the importance of temperature on fish growath and survival.  Arctic fishes can grow faster at cooler temperatures, but have a limited range.  Their ability to grow under future climate scenarios is presented. 
* [Laurel2017JMS - Temperature-dependent growth as a function of size and age in juvenile Arctic cod (Boreogadus saida)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Laurel2017JMS.md) 
     * Laboratory experiments of the effect of temperature on growth rates in age-0 and age-1 Arctic cod.  Optimal temperature decreases with size, and growth is strongly dependent on both environmental temperature and size.  Source of L-W regressions and growth rates for juvenile fishes. 
* [Leblanc2019E - The co-distribution of Arctic cod and its seabird predators across the marginal ice zone in Baffin Bay](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Leblanc2019E.md) 
     * Concurrent obervations of arctic cod (acoustics) and diving/surface feeding seabirds (observers) across Baffin bay in marginal ice conditions.  They find little correlation between the distribution of fish and seabirds, and relate the distributions of each with ice concentrations. 
* [Leblanc2019PB - Pelagic production and the recruitment of juvenile polar cod Boreogadus saida in Canadian Arctic seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Leblanc2019PB.md) 
     * Acoustic surveys in the canadian arctic show correlation with polar cod biomass and earlier ice breakup date. 
* [Loggerwell2015PO - Fish communities across a spectrum of habitats in the western Beaufort Sea and Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Loggerwell2015PO.md) 
     * Synthesized five years of surveys to look at differences in abundance (density) of animals from the lagoon to shelf slope in the Chukchi and Beaufort.  They also looked at icthyoplankton.  Based on Icthyoplankton, they state that the Beaufort Sea shelf is likely a spawning location for Arctic cod. 
* [LowryFrost1981CFN - Distribution, growth, and foods of Arctic cod (Boreogadus saida) in the Bering, Chukchi and Beaufort Seas.](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/LowryFrost1981CFN.md) 
     * Observations of the biology of Arctic cod caught in bottom trawls in late-summer, 1977. 
* [Marsh2017DSRII - Ontogenetic, spatial and temporal variation in trophic level and diet of Chukchi Sea fishes](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Marsh2017DSRII.md) 
     * Examined the isoscapes and relation to water masses in the Chukchi Sea, looking for diet niches of pelagic fishes, particularly Arctic cod. 
* [Marsh2019PB - Environmental and biological influences on the distribution and population dynamics of Arctic cod (Boreogadus saida) in the US Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Marsh2019PB.md) 
     * Model of Arctic cod presence/absence and abundance in comparison with abiotic and biotic factors. Based on 2012 and 2013 Arctic Eis data and work done in other regions, they estimate the potential of the age-1+ stock to produce the number of age-0 Arctic cod observed in the summer surveys, and find the estimates to be much lower than what is observed, providing a set of potential explanations. 
* [Matley2012MEPS - Seabird predation on Arctic cod during summer in the Canadian Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Matley2012MEPS.md) 
     * Observations of the foraging behavior of birds relative to environment (wind, sea state) and cod availability (schooling vs. non-schooling) in the Canadian High Arctic. Kleptoparasitism appears to be highly efficient foraging method, while dive plunging to depth allows for feeding in non-schooling and lower visibility conditions. 
* [Mishin2018JI - Ichthyoplankton of Russian Arctic Seas: 1. Polar cod Boreogadus saida](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Mishin2018JI.md) 
     * Distribution and size composition of polar cod on the Russian Arctic seas from surveys conducted in 2015-2017.  Size increases as a function of season and latitude. 
* [Mueter2016PB - The ecology of gadid fishes in the circumpolar Arctic with a special emphasis on the polar cod (Boreogadus saida)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Mueter2016PB.md) 
     * This is the introduction paper for the 2016 Polar Biology special issue that came out of the 2014 ESSAS annual meeting, focused on Arctic cod and their role in Arctic food webs. 
* [Parker-Stetter2011PB - Distribution of polar cod and age-0 fish in the U.S. Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Parker-Stetter2011PB.md) 
     * Investigation of the offshore distribution of Arctic cod in the U.S. Beaufort Sea to examine the density and water property associations. 
* [Petrik2015PO - Progress in Oceanography Biophysical transport model suggests climate variability determines distribution of Walleye Pollock early life stages in the eastern Bering Sea through effects on spawning](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Petrik2015PO.md) 
     * Biophysical modeling of early life history for walleye pollock in the EBS, suggesting temperature (ice conditions) and the resultin difference in temperature-dependent growth is the primary driver of inerannual variability in distribution. 
* [Petrik2016JMS - Modelled connectivity between Walleye Pollock (Gadus chalcogrammus) spawning and age-0 nursery areas in warm and cold years with implications for juvenile survival](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Petrik2016JMS.md) 
     * Modeled connectivity of age-0 pollock population to spawning locations in the Eastern Bering. Patterns mostly follow along-isobath flow, though differ between warm and cold years. 
* [Ponomarenko2000JI - Eggs, larvae, and juveniles of polar cod Boreogadus saida in the Barents, Kara, and White Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Ponomarenko2000JI.md) 
     * Observations of eggs, larvae, and juveniles from 14 years of sampling Polar cod.  The early life cycle is described, and differences in specimen and development are attributed environmental conditions. 
* [Quast1974FB - Density distribution of juvenile Arctic cod, Boregogadus saida in the Eastern Chukchi Sea in the fall of 1970](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Quast1974FB.md) 
     * This was the first fisheries survey of Arctic cod in the NE Chukchi (as far as I know), and showed that there were primarily young of the year A. cod, with a depth-dependent density.  Quast also speculates about the origin of the juvenile cod. 
* [Vestfals2019PB - Distribution of early life stages of Arctic cod and saffron cod in the Pacific Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Vestfals2019PB.md) 
     * Vestfals et al aim to narrow down the potential spawning grounds for arctic and saffron cod based on the physical oceanography and summer distribution.  It contains a good review in the intro of the current literature on early life history. 
* [VikeboMEPS2019 - Drift, growth, and survival of larval Northeast Arctic cod with simple rules of behaviour](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/VikeboMEPS2019.md) 
     * Modeling efforts to investigate the role of vertical behavior on dispersion and success. 
* [Whitehouse2014PB - A trophic mass balance model of the eastern Chukchi Sea with comparisons to other high-latitude systems](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Whitehouse2014PB.md) 
     * This study aimed to describe the trophic structure and function of the Chukchi Sea foodweb using an ecopath model, representing just one of many possible mass-balance solutions.  Fish estimates were taken from beam trawl samples of the Eastern Chukchi shelf. 
* [Wyllie-Echeverria1997AFS - Water masses and transport of age-0 Arctic cod and age-0 Bering flounder into the northeastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Wyllie-Echeverria1997AFS.md) 
     * Describe the abundance and distribution of larval bering flounder in late summer from 1989-1991 in relation to the sampled water masses.  Included collection of age-0 Arctic cod throughout the NE Chukchi to investigate water mass associations. 

### ice 
 
* [AlexanderNiebauer1981LO - Oceanography of the eastern Bering Sea ice-edge zone in spring1](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/ice/AlexanderNiebauer1981LO.md) 
     * They investigate enhanced productivity and upwelling at the ice edge in the Eastern Bering Sea 
* [Duarte2012NCC - Abrupt climate change in the Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/ice/Duarte2012NCC.md) 
     * Discussion of the causes and impacts of climate change in the Arctic. 
* [Steele2008GRL - Arctic Ocean surface warming trends over the past 100 years](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/ice/Steele2008GRL.md) 
     * Observations of surface warming trends across the arctic and the association with the Arctic Oscilation. 
* [Stroeve2014GRL - Changes in Arctic melt season and implications for sea ice loss](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/ice/Stroeve2014GRL.md) 
     * Analysis of changes in melt and freeze timing of the artcic and implications for heat storage and SST due to albedo effects.  Contains a table of melt and freeze onset by region. 

### plankton 
 
* [Ashjian2017DSRII - Mesozooplankton abundance and distribution in association with hydrography on Hanna Shoal, NE Chukchi Sea, during August 2012 and 2013](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Ashjian2017DSRII.md) 
     * Description of the late-summer zooplankton community composition at Hannah Shoal during August of 2012 and 2013, focusing on copepods and euphausiids of interest for bowhead whales. 
* [Darnis2019PO - Could offspring predation offset the successful reproduction of the arctic copepod Calanus hyperboreus under reduced sea-ice cover conditions?](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Darnis2019PO.md) 
     * Year-round observations of C. hyperboreus growth and reproduction in the Canadian Beaufort Sea.  Hypothesize top-down control of the C. hyperboreus population by other omnivore species (M. longa, C. glacialis), increased by extended ice-free periods. 
* [Day2013CSR - The offshore northeastern Chukchi Sea, Alaska: A complex high-latitude ecosystem](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Day2013CSR.md) 
     * Synthesis of the findings from the Chukchi Sea Environmental Studies Program from 2008-2010 at three regions of oil exploration interest near Hanna Shoal. 
* [Ershova2015PB - Inter-annual variability of summer mesozooplankton communities of the western Chukchi Sea: 2004–2012](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Ershova2015PB.md) 
     * Description of the zooplankton community in relation to water masses during 4 years of the RUSALCA survey program.  Community structure strongly correlated with bottom temperature. 
* [Im2019PO - Evidence for resource partitioning by ontogeny and species in calanoid copepods](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Im2019PO.md) 
     * Observations of fine-scale feeding habitat partitioning by clanoid species in the East Sea through stable isotope analysis. 
* [Kitamura2017CSR - Seasonal dynamics of zooplankton in the southern Chukchi Sea revealed from acoustic backscattering strength](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Kitamura2017CSR.md) 
     * Use of AZFPs to describe the seasonality of zooplankton biomass, and identify the dominant scatterers in the southern Chukchi Sea, finding a seasonal peak in biomass in autumn and a minimum in early spring, not corresponnding with phytoplankton production.  Zooplpankton communities in the southern Chukchi are largely driven by advection from the Bering. 
* [Neely2018GRL - Unraveling Phytoplankton Community Dynamics in the Northern Chukchi Sea Under Sea-Ice-Covered and Sea-Ice-Free Conditions](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Neely2018GRL.md) 
     * Multivariate classification of phytoplankton groups in association with ice and ice-free conditions in the N. Chukchi sea, showing clear variability as a function of depth and ice presence during the ICESCAPE program. 
* [Okkonen2020po - Krill diel vertical migration: A diagnostic for variability of wind forcing over the Beaufort and Chukchi Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/Okkonen2020po.md) 
     * Use of ADCPs to measure intensity of DVM in krill and correlate with wind and upwelling conditions in the western Beaufort. 
* [PinchukEisner2017DSRII - Spatial heterogeneity in zooplankton summer distribution in the eastern Chukchi Sea in 2012–2013 as a result of large-scale interactions of water masses](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/plankton/PinchukEisner2017DSRII.md) 
     * Describe the differences in zooplankton distribution (focussed on Calanus species of copepods) between 2012 and 2013 as part of the Arctic EIS study.  Zooplankton distribution is wind-driven and a balance between melt water and northward advection of warm Pacific water. 
