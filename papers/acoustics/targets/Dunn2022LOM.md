01/30/23
## Authors:
Dunn, Muriel and Zedel, Len
## Title:
Evaluation of discrete target detection with an acoustic Doppler current profiler
## Keywords:
single targets, ADCP, echo counting, signal processing
## Geographic Coverage
Bay of Fundy
## Field Dates:
N/A
## Significance:
Proof-of-concept demonstration comparing single target detection by ADCP to split-beam echosounder. Associated with BAMFF software package.

## Notes:
A bottom mounted frame was used to hold a RDI 600 kHz broadband ADCP along with a 120 kHz Biosonics DTX split-beam echosounder. The system was used near the mouth of the Bay of Fundy. The DTX recorded at 4 Hz. The ADCP was at 1Hz, 1 m depth bins with no data averaging. Due to a programming error, they did not record any velocity data but retained the backscatter and correlation data. The two systems were staggered to record samples 3 times an hour on alternating 10 minute intervals. Overall they recorded 9d with both systems and a total of 220 matched segments.

BAMFF
The raw data is read in and split into beam-dependent variables (velocity, correlation, and intensity)
1. Backscatter is calibrated to absolute signal levels
2. Data from each range been are identified as targets in each beam individually based on correlation and Sv thresholds. Each beam is processed individually. Histograms of Sv were generated to inform the threshold.
3. The targets are grouped and matched with their appropriate velocity

Sonar5-Pro was used for the fish tracking of the DTX data.

The DTX generally detected more targets, particularly in the densest parts of agreggations. In low density periods, the ADCP tends to detect higher densities of targets (31% less when agregations we >1500 targets m-2 20 min-1 vs 46% more when <30 targets m-2 20 min -1>).

Sensitivity analysis of the number of discrete targets identified indicates a lot of flexibility in the choice to Sv and correlation thresholds. A key thing is that the correlation is not calibration-dependent and can be fairly robust to different instruments/configurations.

Due to the small beam width (1.5) there is a strong depth dependency of the ability to observe single targets by the ADCP, particularly at fast displacement speeds. At slow speeds, the ADCP may over estimate targets due to repeat detections of the same target, while the split-beam target tracking accounts for this.
