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
| MEX/Baja California/Ensenada     | 1                   |
| MEX/Baja California/Mexicali     | 1                   |
| MEX/Baja California/Rosarito     | 1                   |
| MEX/Baja California/Tijuana      | 435                 |
| MEX/Sonora/San Luis Río Colorado | 2                   |
| USA/Arizona/Yuma                 | 1                   |
| USA/California/Cruise_Ship_1     | 8                   |
| USA/California/Cruise_Ship_2     | 32                  |
| USA/California/Davis             | 1                   |
| USA/California/Imperial          | 131                 |
| USA/California/Kern              | 1                   |
| USA/California/Los Angeles       | 11                  |
| USA/California/Modesto           | 1                   |
| USA/California/Orange            | 3                   |
| USA/California/Riverside         | 32                  |
| USA/California/San Bernadino     | 2                   |
| USA/California/San Diego         | 4518                |
| USA/California/Santa Barbara     | 1                   |
| USA/California/Ventura           | 1                   |
| USA/Louisiana/New Orleans        | 143                 |
| USA/West Virginia/Kanawha        | 1                   |

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
