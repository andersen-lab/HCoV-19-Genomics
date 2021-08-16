#### Consensus sequences

All consensus sequences will be deposited on GISAID and on NCBI under BioProject ID [PRJNA612578](https://www.ncbi.nlm.nih.gov/bioproject/612578).
[metadata.csv](https://raw.githubusercontent.com/andersen-lab/HCoV-19-Genomics/master/metadata.csv) contains collection dates, location, originating labs and sequencing metrics: coverage and average depth.

| Location                         | Number of sequences |
|:---------------------------------|:--------------------|
| Jordan/Amman                     | 483                 |
| Jordan/Aqaba                     | 41                  |
| Jordan/Irbid                     | 58                  |
| Jordan/Mafraq                    | 2                   |
| Jordan/Zarqa                     | 5                   |
| MEX/Baja California		   | 26                  |
| MEX/Baja California/Ensenada     | 16                  |
| MEX/Baja California/Mexicali     | 254                 |
| MEX/Baja California/Rosarito     | 1                   |
| MEX/Baja California/Tecate       | 7			 |
| MEX/Baja California/Tijuana      | 857                 |
| MEX/Chihuahua                    | 9                   |
| MEX/Sonora                       | 32                  |
| MEX/Sonora/San Luis Río Colorado | 35                  |
| USA/Alaska/Anchorage		   | 1			 |
| USA/Arizona/Maricopa	           | 1                   |
| USA/Arizona/Pima                 | 1                   |
| USA/Arizona/Yuma                 | 1                   |
| USA/California/Alameda           | 1                   |
| USA/California/Contra Costa      | 3                   |
| USA/California/Cruise_Ship_1     | 8                   |
| USA/California/Cruise_Ship_2     | 32                  |
| USA/California/Davis             | 1                   |
| USA/California/El Dorado         | 4			 |
| USA/California/Fresno		   | 1			 |
| USA/California/Imperial          | 151                 |
| USA/California/Kern              | 2                   |
| USA/California/Los Angeles       | 132                 |
| USA/California/Modesto           | 1                   |
| USA/California/Monterey          | 1                   |
| USA/California/Orange            | 23                  |
| USA/California/Riverside         | 103                 |
| USA/California/Sacramento        | 1                   |
| USA/California/San Bernadino     | 8                   |
| USA/California/San Diego         | 15263               |
| USA/California/San Francisco     | 1                   |
| USA/California/San Mateo	   | 1			 |
| USA/California/Santa Barbara     | 4                   |
| USA/California/Santa Clara       | 3                   |
| USA/California/Sonoma            | 1                   |
| USA/California/Sutter            | 1                   |
| USA/California/Ventura           | 3                   |
| USA/Florida/Saint Johns	   | 1			 |
| USA/Hawaii/Honolulu		   | 1                   |
| USA/Idaho/Ada                    | 1                   | 
| USA/Illinois/Cook                | 1                   | 
| USA/Illinois/DuPage              | 1                   | 
| USA/Illinois/Rock Island         | 1                   | 
| USA/Louisiana/New Orleans        | 143                 | 
| USA/Maryland/Anne Arundel        | 1                   | 
| USA/Michigan/Wayne               | 1                   | 
| USA/Minnesota/Anoka              | 1                   | 
| USA/Minnesota/Ramsey             | 1                   | 
| USA/Nevada/Clark                 | 1                   | 
| USA/New York/Orange              | 1                   | 
| USA/New York/Warren              | 1                   | 
| USA/New York/Westchester         | 1                   | 
| USA/Ohio/Clark                   | 1                   | 
| USA/Ohio/Hamilton                | 1                   | 
| USA/Oklahoma/Tulsa               | 1                   | 
| USA/Pennsylvania/Allegheny       | 1                   | 
| USA/Tennessee/Grainger           | 1                   | 
| USA/Tennessee/Sumner             | 1                   | 
| USA/Texas/Bell                   | 1                   | 
| USA/Texas/Montgomery             | 2                   | 
| USA/Utah/Salt Lake               | 1                   | 
| USA/Washington/King              | 3                   | 
| USA/Washington/Kitsap            | 1                   | 
| USA/West Virginia/Kanawha        | 1                   | 
| USA/Wyoming/Albany               | 1                   | 

#### Raw read files

Raw read files for both Illumina and Oxford Nanopore data are available on,

* [Google cloud](https://console.cloud.google.com/storage/browser/andersen-lab_hcov-19-genomics).
* SRA under BioProject ID: [PRJNA612578](https://www.ncbi.nlm.nih.gov/bioproject/612578).

The sequencing is being performed using an amplicon-based sequencing scheme using [PrimalSeq](https://www.nature.com/articles/nprot.2017.066) with [artic nCoV-2019 scheme](https://github.com/artic-network/artic-ncov2019/tree/master/primer_schemes/nCoV-2019).

Nanopore data was processed using the [artic-nCoV019 pipeline](https://github.com/artic-network/artic-ncov2019) with [minimap2](https://github.com/lh3/minimap2) and [medaka](https://github.com/nanoporetech/medaka).
Illumina data was processed using [iVar](https://github.com/andersen-lab/ivar) ([Grubaguh et al. Genome Biology 2019](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1618-7)) with [bwa](https://github.com/lh3/bwa).

**Disclaimer**. Please note that this data is still based on work in progress and should be considered preliminary. If you intend to include any of these data in publications, please let us know – otherwise please feel free to download and use without restrictions. We have shared this data with the hope that people will download and use it, as well as scrutinize it so we can improve our methods and analyses. Please contact us if you have any questions or comments – we’ll buy beers for #ResearchParasites that spot flaws and faults in the data and come up with improvements!

---
**Andersen Lab**
The Scripps Research Institute
La Jolla, CA, USA
[data@andersen-lab.com](mailto:data@andersen-lab.com)
