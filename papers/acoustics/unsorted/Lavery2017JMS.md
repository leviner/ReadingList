12/11/19
## Authors:
Lavery, A. and Bassett, C. and  Lawson, G.L. and Jech, M.
## Title:
Exploiting signal processing approaches for broadband echosounders
## Keywords:
broadband, acoustic, wideband, signal processing
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Demonstration of a) calibration based on frequency-dependent bandwidth and b) use of tapered match filter on untapered signal to resolve targets near boundaries.

## Notes:
Broadband here is defined as a system that uses FM transmit signals overa large range of frequencies. A typical transducer can transmit an octave bandwidth, and bandwidth typically increases with frequency.

Broadband matched-filter processing can improve the temporal (range) resolution since range is independent of pulse length and determined by 1/bandwidth. The signal to noise ratio increases as a function of bandwidth*pulse length.

These signals make processing and calibration more difficult. Use of multiple spheres spanning the range of ka =0.5 to 35, where k = 2pi*lamba (wavenumber) and a is the sphere radius in meters. Using multiple spheres in this range will fill across nulls. However this becomes difficult since TS decreases with smaller spheres and can make calibration more difficult.

In broadband, you can use frequency-dependence of the of the beam pattern and the known frequency response to estimate the angle within the beam.

They conducted two experiments:
1. Calibrating using frequency-dependent spectrum of the calibration sphere to locate the sphere
2. Signal processing checks for detecting targets near boundaries

The beamwidth decreases with increasing frequency, so a target off axis will be closer to the edge at a lower frequency than a higher. Thus the TS will decrease as frequency increases, and you can use the measurement of this change in FR to infer the angular position of the target. It appears that the corrected TS spactra are in agreement with the target at the center of the beam, though once outside the main lobe there can be very large errors. However, the shape of the spectrum can still be used to identify how far axis and thus used to calibrate. At the expense of target tracking and position, operating a split-beam transducer in single beam expands the potential bandwidth. In CW this has to be done based on amplitude in time series, while in FM you can infer position.

When a weaker target is located near a larger target, the side lobes of the larger target can mask the weaker target. Suppression of the side lobes can be done by transmitting an untapered signal, then using a replica of a tapered signal to do the match filtering. It was possible to improve the resolution and identify 38WC spheres at ~10cm form a boundary when using a slow tapered signal, but this was also accomplished by applying a tapered MF to non-tapered received signal. This way you get full spectra coverage and the reduction of the side lobes.
