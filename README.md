#### Consensus sequences

All consensus sequences and raw reads will be deposited under BioProject ID [PRJNA612578](https://www.ncbi.nlm.nih.gov/bioproject/612578).

|ID|gb\_accession|gisaid\_accession|collection\_date|location|percent\_coverage\_cds|avg\_depth|
|:---|:---|:---|:---|:---|:---|:---|
|PC00101P|MT192765|EPI\_ISL\_414648|2020-03-11|San Diego|99.7525|3516.14|
|MG0987||EPI\_ISL\_416457|2020-03-18|San Diego|99.5954|2465.6|
|SEARCH-0032-JOR||EPI\_ISL\_429992|2020-03-22|Jordan/Amman|99.77|60606.1|
|SEARCH-0033-JOR||EPI\_ISL\_429993|2020-03-16|Jordan/Amman|100|44936.5|
|SEARCH-0034-JOR||EPI\_ISL\_429994|2020-03-17|Jordan/Amman|100|35560.2|
|SEARCH-0035-JOR||EPI\_ISL\_429995|2020-03-30|Jordan/Amman|99.3|48715.3|
|SEARCH-0036-JOR||EPI\_ISL\_429996|2020-03-23|Jordan/Amman|100|32210.1|
|SEARCH-0037-JOR||EPI\_ISL\_429997|2020-03-16|Jordan/Amman|100|52690.4|
|SEARCH-0039-JOR||EPI\_ISL\_429998|2020-03-28|Jordan/Amman|100|64812.1|
|SEARCH-0041-JOR||EPI\_ISL\_429999|2020-03-17|Jordan/Amman|100|38163|
|SEARCH-0042-JOR||EPI\_ISL\_430000|2020-03-30|Jordan/Amman|100|54223.6|
|SEARCH-0043-JOR||EPI\_ISL\_430001|2020-03-17|Jordan/Amman|100|40737.6|
|SEARCH-0044-JOR||EPI\_ISL\_430002|2020-03-16|Jordan/Amman|100|53799.2|
|SEARCH-0045-JOR||EPI\_ISL\_430003|2020-03-16|Jordan/Amman|100|79270.1|
|SEARCH-0046-JOR||EPI\_ISL\_430004|2020-03-17|Jordan/Amman|100|58760.2|
|SEARCH-0047-JOR||EPI\_ISL\_430005|2020-03-26|Jordan/Amman|100|73368.1|
|SEARCH-0048-JOR||EPI\_ISL\_430006|2020-03-23|Jordan/Amman|100|42566|
|SEARCH-0049-JOR||EPI\_ISL\_430007|2020-03-19|Jordan/Amman|100|47203.2|
|SEARCH-0051-JOR||EPI\_ISL\_430008|2020-04-04|Jordan/Amman|97.98|55629.6|
|SEARCH-0052-JOR||EPI\_ISL\_430009|2020-03-30|Jordan/Irbid|100|29390.3|
|SEARCH-0053-JOR||EPI\_ISL\_430011|2020-03-19|Jordan/Amman|100|65439.2|
|SEARCH-0054-JOR||EPI\_ISL\_430012|2020-03-30|Jordan/Irbid|99.99|67262.4|
|SEARCH-0055-JOR||EPI\_ISL\_430013|2020-04-02|Jordan/Amman|96|67329.1|
|SEARCH-0056-JOR||EPI\_ISL\_430014|2020-03-17|Jordan/Amman|100|40156.9|
|SEARCH-0057-JOR||EPI\_ISL\_430015|2020-03-24|Jordan/Amman|100|33430.4|
|SEARCH-0007-SAN||EPI\_ISL\_429990|2020-03-21|San Diego|100|6215.17|
|SEARCH-0016-SAN||EPI\_ISL\_430016|2020-03-24|San Diego|100|6440.67|
|SEARCH-0017-SAN||EPI\_ISL\_429991|2020-03-24|San Diego|100|4947.09|
|SEARCH-0084-JOR|||2020-03-16|Jordan/Amman|100|34497.8|
|SEARCH-0058-NBG|||2020-03-23|New Orleans|99.93|48802|
|SEARCH-0059-NBG|||2020-03-23|New Orleans|99.62|42541.8|
|SEARCH-0060-NBG|||2020-03-25|New Orleans|99.88|48703.2|
|SEARCH-0063-NBG|||2020-03-31|New Orleans|97.49|31243.4|
|SEARCH-0064-NBG|||2020-03-31|New Orleans|98.68|40169.9|
|SEARCH-0065-NBG|||2020-03-31|New Orleans|98.57|51247.6|
|SEARCH-0066-NBG|||2020-03-23|New Orleans|98.85|39911.6|
|SEARCH-0067-NBG|||2020-03-25|New Orleans|97.68|42225.8|
|SEARCH-0068-NBG|||2020-03-25|New Orleans|100|51571.6|
|SEARCH-0070-NBG|||2020-03-26|New Orleans|99.92|49492.1|
|SEARCH-0071-NBG|||2020-03-26|New Orleans|100|56119|
|SEARCH-0072-NBG|||2020-03-26|New Orleans|98.18|16127.5|
|SEARCH-0075-NBG|||2020-03-31|New Orleans|98.09|12742|
|SEARCH-0076-NBG|||2020-03-31|New Orleans|99.99|14235.8|
|SEARCH-0077-NBG|||2020-03-31|New Orleans|98.62|16180.4|
|SEARCH-0078-NBG|||2020-03-31|New Orleans|96.58|11629.3|

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
