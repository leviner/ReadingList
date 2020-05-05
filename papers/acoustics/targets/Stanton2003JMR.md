05/04/20
## Authors:
Stanton, Timothy K. and Reeder, D. Benjamin and Jech, J. Michael
## Title:
Inferring fish orientation from broadband-acoustic echoes
## Keywords:
scattering, broadband, acoustics, target
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Demonstration of the use of pulse-compressed broadband signal to constrain fish orientation by identifying multiple scattering sources within a single fish.

## Notes:
Orientation correlates with behavior, and is helpful for quantifying the acoustic data since backscattering can be orientation dependent. Direct  measurement is typically done with cameras, though the sample volume is small. Using acoustics, there are two used methods:
- Echo tracing, or target tracking, where you assume the orientation based on the movement of sequential pings
- Assumed based on scattering models and known species compositions

Here, they propose using broadband, where individual features of a fish can be resolved and used to estimate orientation.  They use pulse compression processing.
- Matched Filter: the noisy signal is cross-correlated with the known sent signal, resulting in a return signal of much higher amplitude but shorter duration than the original signal. This increases the signal and not noise, increasing the SNR. The width of the main lobe (highest amplitude signal) is proportional to the bandwidth, larger bandwidth = improved range resoltuion.
- In pulse compression, the signal is designed such that the resulting "matched" signal is shorter. Because the return signal from the target is not actually known, we use the transmission signal.

The challenge is interpreting the returned signal. A typical return from a clear target will actually have multiple spikes representing scattering features. For long pings, features of an organisms body contribute to these echoes, and once the are compressed, you can see them separated in time. As the angle of incidence increases, the arrival tie of those echoes will begin to deviate according to the orientation of the fish (i.e., a skull and swimbladder will be separated in space from the transducer as the fish starts to look up/down). Thus the arrivals of multiple body parts can be resolved.

Experiments:
- Live individuals (see Reeder et al), ~22cm, with separate xmit and receive xducers. 40-94 kHz chirp and the fish, tethered were rotated.
- After tests, fish were studied via xray and CT scan.
- They were able to resolve separate features, with a resolution of 2cm after pulse compression.
- At normal incidence (lateral) there was a signle peak, but as the angle increased two resolved peaks could be seen.

This work assumes there are scattering features spread laterally throughout the fish, though this distribution is not consistent and so the relationship between time of signal separation and orientation will vary.

Bandwidth is limiting as it sets the resolution. The bandwidth should be chosen based on the size of the fish since the angle of detection threshold will be set by this resolution.
