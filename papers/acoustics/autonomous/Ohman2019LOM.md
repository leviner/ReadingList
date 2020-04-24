04/23/20
## Authors:
Ohman, Mark D. and  Davis, Russ E. and Sherman, Jeffrey T. and Grindley, Kyle R. and Whitmore, Benjamin M. and Nickels, Catherine F. and Ellen, Jeffrey S.
## Title:
Zooglider: An autonomous vehicle for optical and acoustic sensing of zooplankton
## Keywords:
autonomous, glider, acoustics, optics, zooplankton
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
A spray glider with integrated 200 and 1000 kHz sonar and zoocam shadow imaging camera.

## Notes:
Zooplankton are key parts of the food web. However many species are quite delicate and difficult to sample in situ. It's also difficult to sample well vertically in the water column. Space-time resolution can be improved using optics and acoustics systems.  Here, they outline the integration of instrumentation into a spray glider in order to sample mesozooplankton communities.

Zooglider
- IDG Spray glider using a hydraulic pump to transfer oil between internal and external bladders to control buoyancy.
- Center of mas is controlled to change diving behavior.
- GPS and data via iridium upon surfacing
- Seabird and Seapoint instrument integreations
- The platforms moves vertically at ~10 cm/s at a pitch angle of 16-18 degrees, which also correlates to ~15cm/s horizontal movement.
- In testing deployments, the zooglider is given a goal location to survey to, at which it increases imaging frequency.
- After each dive, CTD, chl a, roi counts, zonar averaged backscatter, and engineering data are sent via iridium. Altered waypoints and new sampling specifications can be sent.

Zoocam
- Shadowgraph imaging system (silhouette)
- sampling tunnel flow through optimized
- LED illumination (red) and reflected via a mirror into the sampling window.
- Optical field is 5x15 cm
- Total volume sampled is 250 mL
- Images are taken at 2Hz, averaging every 5cm of vertical displacement of the glider
- ROIs are calculated at sea and size statistics are transferred. Images are saved locally for recovery and processed as PNG, corrected for lighting, and ROIs identified. CNN is used to classify into taxonomic categories, then the detections are validated by human.
- To address biofouling, they use UV light when not imaging, and use a mechanical wiper to clean the sets of optical windows at the beginning of each dive.

Zonar
- 200 (10 degree) and 1000 (4 degree) kHz IDG transducers with a ping rate of 5 Hz @ 200 and 10Hz @ 10000. A 4 ping ensemble is sent every 4m of glider descent and ascent. These bursts are averaged across pings and then averaged into 1m depth bins.
- Because of the random orientation of scatterers, the orientation of the zonar does not impact the averaged scattering strength.
