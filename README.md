# spark

This script was developed to detect a specific protein domain (ARK/SPARK). An efficient screening of numerous datasets is possible.


```
python SPARK_finder.py
--in  STR  Folder containing input FASTA files.
--out STR  Output folder.
```

`--in` specifies a folder containing all input FASTA files that will be processed by the SPARK finder. Files with the following extensions will be recognized: ".fasta", ".fa", and ".faa".

`--out` specifies an output folder. This folder is created if it does not exist already.


### References
Héctor Montero, Tak Lee, Boas Pucker, Gabriel Ferreras-Garrucho, Giles Oldroyd, Samuel F. Brockington, Akio Miyao, Uta Paszkowski. A mycorrhiza-associated receptor-like kinase with an ancient origin in the green lineage. Proceedings of the National Academy of Sciences Jun 2021, 118 (25) e2105281118; DOI: [10.1073/pnas.2105281118](https://doi.org/10.1073/pnas.2105281118)
