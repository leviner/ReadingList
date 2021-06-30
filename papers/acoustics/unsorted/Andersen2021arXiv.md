06/25/21
## Authors:
Andersen, Lars Nonboe and Chu, Dezhang and Heimvoll, Harald and Korneliussen, Rolf and J. Macaulay, Gavin and Ona, Egil
## Title:
Quantitative processing of broadband data as implemented in a scientific splitbeam echosounder
## Keywords:
Broadband, splitbeam, signal processing, EK80
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Overview of broadband signal processing as implemented in EK80. Presents the equations for calculating frequency dependent TS and Sv.

## Notes:
Typical commercially available broadband systems have lacked one of the key features utilized by fisheries surveys:
- Large dynamic range (ensure the system doesn't saturate)
- Frequencies that are useful for detecting fish at 100s to 1000s m
- Split beam for calibration/target strength
- Ability to perform in situ calibration
- Compatible/simple transition with current survey systems
- Useful at ship speeds

The process of transmitting and receiving is as follows:
- A digital signal is generated and converted into an analog electrical signal
- The analog electrical signal is applied to the transducer which produces an acoustic (pressure) signal
- Any return is received by the transducer as  function of time and quadrant and converted to an electrical signal in the traducer
- The transceiver receives the retuning analog electrical signal from the transducer.

The analog electrical signal is amplified and filtered by an anti aliasing filter before being digitized at a specific frequency. The digital signal is passed through bandpass filters which reduce noise and decimate the signal.

Pulse compression

To increase signal to noise a match filter using the ideal transmit signal can be used, known as pulse compression. The received signal is convolved with a time-reversed match filter signal.

Angles

Position along the major and minor axes are calculated through a combination of the transducer halfs, such that the electrical angle along the minor axis is the product of the fore (quadrant 3, 4) and aft (quadrants 1, 2) halves.

Physical angles are determined using a constant that converts from phase angle to angle of arrival from the nominal frequency of the transducer (frequency at the center of the chirp pulse)

Sv

To estimate Sv a FT is used in a sliding window. Since spherical spreading can change significantly as a function of the window (beamwidth is a function of frequency) discrete FTs can be used and spreading loss compensated as a function of frequency and range.
