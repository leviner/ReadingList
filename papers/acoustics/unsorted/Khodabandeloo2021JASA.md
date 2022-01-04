01/03/22
## Authors:
Khodabandeloo, Babak and  Ona, Egil and Macaulay, Gavin J. and Korneliussen, Rolf
## Title:
Nonlinear crosstalk in broadband multi-channel echosounders
## Keywords:
acoustics, broadband, crosstalk, interference
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Investigation of crosstalk issues in EK80

# Notes:
Crosstalk, particularly due to cross-channel interference as a result of energy loss to harmonics can be in issue in wideband data collection. A fraction of the energy recieved by the 90 - 170 kHz channel (120 kHz transducer) is likely due to the second harmonic from the 45 - 90 kHz (70 kHz transducer) signal. This cross-channel interference has been recognized but the effect is not fully determined. You can ping sequentially to avoid this, but that leads to significant reductions in ping rate.

Crosstalk can lead to incorrect spectra and thus incorrect target identification. You can also get target artifacts. Initial suggestions to address crosstalk include:
- Pinging each channel sequentially
- Group the channels in a way that minimizes cross-talk (sequential ping groups)
- Liimit the bandwidth of each channel such that the harmonics don't overlap
- Changes in the processing stage
- Change the transmit pulse to reduce harmonics.