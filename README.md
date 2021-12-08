#### Consensus sequences

All consensus sequences will be deposited on GISAID and on NCBI under BioProject ID [PRJNA612578](https://www.ncbi.nlm.nih.gov/bioproject/612578).
[metadata.csv](https://raw.githubusercontent.com/andersen-lab/HCoV-19-Genomics/master/metadata.csv) contains collection dates, location, originating labs and sequencing metrics: coverage and average depth.

| Location                         |   Number of Sequences |
|:---------------------------------|----------------------:|
| Jordan/Amman                     |                   483 |
| Jordan/Aqaba                     |                    41 |
| Jordan/Irbid                     |                    58 |
| Jordan/Mafraq                    |                     2 |
| Jordan/Zarqa                     |                     5 |
| MEX/Baja California              |                    26 |
| MEX/Baja California/Ensenada     |                    39 |
| MEX/Baja California/Mexicali     |                   296 |
| MEX/Baja California/Rosarito     |                     1 |
| MEX/Baja California/Tecate       |                     7 |
| MEX/Baja California/Tijuana      |                   943 |
| MEX/Chiapas/Baja California	   |			 1 |
| MEX/Chihuahua                    |                     9 |
| MEX/Chihuahua/Chihuahua          |                    22 |
| MEX/Chihuahua/Ciudad Juarez      |                    25 |
| MEX/Coahuila/Saltillo	           |                    57 |
| MEX/Coahuila/Torreon             |                    36 |
| MEX/Jalisco/Puerto Vallarta      |                    60 |
| MEX/Nuevo Leon/Guadalupe	   |			32 |
| MEX/Nuevo Leon/Monterrey         |                    60 |
| MEX/Nuevo Leon/San Nicolas De Los Garza |             26 |
| MEX/Nuevo Leon/Santa Catarina    |                    12 | 
| MEX/Sinaloa/Culiacan             |                   249 |
| MEX/Sinaloa/Los Mochis           |                   110 |
| MEX/Sinaloa/Mazatlan             |                    81 |
| MEX/Sonora                       |                    32 |
| MEX/Sonora/Hermosillo            |                    43 |
| MEX/Sonora/Obregon               |                    66 |
| MEX/Sonora/San Luis Río Colorado |                    35 |
| PAK/Islamabad Capital Territory/Islamabad |		51 |
| PAK/Punjab/Lahore		   |                     7 |
| USA/Alaska/Anchorage             |                     1 |
| USA/Arizona/Maricopa             |                     2 |
| USA/Arizona/Pima                 |                     2 |
| USA/Arizona/Yuma                 |                     1 |
| USA/California/Alameda           |                     2 |
| USA/California/Contra Costa      |                     3 |
| USA/California/Cruise_Ship_1     |                     8 |
| USA/California/Cruise_Ship_2     |                    32 |
| USA/California/Davis             |                     1 |
| USA/California/El Dorado         |                     4 |
| USA/California/Fresno            |                     1 |
| USA/California/Imperial          |                   160 |
| USA/California/Kern              |                     2 |
| USA/California/Los Angeles       |                   155 |
| USA/California/Marin             |                     1 |
| USA/California/Modesto           |                     1 |
| USA/California/Monterey          |                     1 |
| USA/California/Orange            |                    45 |
| USA/California/Placer            |                     1 |
| USA/California/Riverside         |                   170 |
| USA/California/Sacramento        |                     2 |
| USA/California/San Bernardino    |                    14 |
| USA/California/San Diego         |                 37840 |
| USA/California/San Francisco     |                     1 |
| USA/California/San Mateo         |                     1 |
| USA/California/Santa Barbara     |                     3 |
| USA/California/Santa Barbara     |                     1 |
| USA/California/Santa Clara       |                     3 |
| USA/California/Sonoma            |                     1 |
| USA/California/Sutter            |                     1 |
| USA/California/Tulare            |                     1 |
| USA/California/Ventura           |                     3 |
| USA/Florida/Saint Johns          |                     1 |
| USA/Hawaii/Honolulu              |                     1 |
| USA/Idaho/Ada                    |                     1 |
| USA/Illinois/Cook                |                     2 |
| USA/Illinois/DuPage              |                     2 |
| USA/Illinois/Rock Island         |                     1 |
| USA/Kentucky/Jefferson           |                     1 |
| USA/Louisiana/New Orleans        |                   143 |
| USA/Maryland/Anne Arundel        |                     1 |
| USA/Maryland/Montgomery          |                     1 |
| USA/Michigan/Wayne               |                     1 |
| USA/Minnesota/Anoka              |                     1 |
| USA/Minnesota/Ramsey             |                     1 |
| USA/Nevada/Clark                 |                     1 |
| USA/Nevada/Douglas               |                     1 |
| USA/New Jersey/Monmouth          |                     1 |
| USA/New York/Orange              |                     1 |
| USA/New York/Warren              |                     1 |
| USA/New York/Westchester         |                     1 |
| USA/North Carolina/Durham        |                     1 |
| USA/Ohio/Clark                   |                     1 |
| USA/Ohio/Hamilton                |                     1 |
| USA/Oklahoma/Tulsa               |                     1 |
| USA/Pennsylvania/Allegheny       |                     1 |
| USA/Tennessee/Grainger           |                     1 |
| USA/Tennessee/Sumner             |                     1 |
| USA/Texas/Bell                   |                     1 |
| USA/Texas/Montgomery             |                     2 |
| USA/Utah/Salt Lake               |                     1 |
| USA/Virginia/Fairfax             |                     1 |
| USA/Washington/King              |                     3 |
| USA/Washington/Kitsap            |                     1 |
| USA/West Virginia/Kanawha        |                     1 |
| USA/Wisconsin/Bayfield           |                     1 |
| USA/Wyoming/Albany               |                     1 |

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
