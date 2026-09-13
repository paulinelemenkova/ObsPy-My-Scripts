# ObsPy Seismological Data Processing Scripts

A reference collection of Python scripts using ObsPy for seismological data processing. The material works through the core ObsPy workflow: date and time handling (`UTCDateTime`), reading and plotting seismograms, waveform customisation and record sections, filtering (low/high/band-pass and band-stop) and downsampling, event triggering (STA/LTA), array analysis, instrument-response correction, and retrieving data from FDSN/IRIS and other data centres. It includes historical example traces such as the 1954 Uccle (UCC) records.

## Scripts

- `Script-OBSPY.py` — end-to-end ObsPy reference: UTCDateTime, reading and plotting seismograms, waveform filtering and downsampling, event triggering, array analysis, instrument-response handling and FDSN/IRIS data retrieval

## Data

The script reads ObsPy's online example seismograms and local MiniSEED traces (for example historical 1954 Uccle / UCC records). Adjust the `os.chdir` path to your own data directory.

## Requirements

Python 3 with `obspy`, `numpy` and `matplotlib`.

## Author

Polina Lemenkova — ORCID: https://orcid.org/0000-0002-5759-1089

## License

MIT — see the LICENSE file (Copyright Polina Lemenkova).
