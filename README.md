# PubRec

Simple python module to get the number of citations of a paper (or list of papers) available on the [ADS archive](https://ui.adsabs.harvard.edu/).

## Example
Here a couple of examples:
* get the citations of papers listed in a file like in *example.txt*, where each line is a bibcode:  
`python pubrec.py --file example.txt`
* get the citations from individual bibcodes:  
`python pubrec.py --single 2019MNRAS.482.2234G 2018MNRAS.480.2011G`
