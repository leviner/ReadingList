11/07/21
## Authors:
lee, Wu-Jung and Mayorga, Emilio and Setiawan, Landung and Majeed, Imran and Nguyen, Kavin, and Stanvea, Valentina
## Title:
Echopype: A Python library for interoperable and scalable processing of water column sonar data for biological information
## Keywords:
sonar, data, computing, open source, acoustics
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Overview of Echopype python library for processing of water column sonar data

## Notes:
A major issue right now in acoustics is scalable data workflows and interoperability that ensures reproducability and consistency with data conventions.

Echopype converts raw data from multiple sonar instruments (Simrad, Nortek, ASL) into netCDF data, consistent with the ICES SONAR-nertCDF4 convention. Coordinate convention follows:
- Beam (frequency channel)
- range bin (distance)
- frequency
- ping time (sequential observations of the three previous coordinates)

Data are padded such that beam groups are consistent in size.

Echopype dataset can be saved as a netCDF or Zarr format; Zarr storage is chunked and compressed. Further manipulation of data can be handled directly through xarray methods. Both formats allow for simple accessibility using Dask for distributed computing methods.

Package subpackages and methods are described:
- convert: handles raw data from attached or remote (e.g., AWS) file systems.
- calibrate: provides functionality for conversion to Sv using instrument-specific methodologies.
- qc: quality control methods to identify non-uniformity .
- preprocess: computation of bin-averaged acoustic quantities.
- metrics: derive summary statistics (e.g., mwd, frequency differencing).
- viaualize: echogram visualization.
