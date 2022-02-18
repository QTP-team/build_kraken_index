## 1 Introduction
The process is to build a custom Kraken database and Bracken database.

## 2 Usage
### 2.1 Use conda to install related dependencies
```
conda env create -n kraken2_index -f env.yaml
conda activate kraken2_index
```

### 2.2 Get complete classification information
When using GTDBtk annotation, if it is not annotated to the phylum, class, order, family, or genus level, the genome is used as the name; if it is not annotated to the species level, the genus + genome is used as the name.
```
python rules/complete_taxo.py -i data/taxo.txt -t data/tmp.txt -o data/complete_taxo.txt
```

### 2.3 Democonvert taxonomy system from GTDB to NCBI and add genomes to database's genomic library
Use https://github.com/rrwick/Metagenomics-Index-Correction/blob/master/tax_from_gtdb.py to convert a GTDB taxonomy into the style of an NCBI taxonomy
```
mkdir taxonomy/
python rules/tax_from_gtdb.py --gtdb data/complete_taxo.txt --assemblies library/ --nodes taxonomy/nodes.dmp --names taxonomy/names.dmp --kraken_dir kraken_library

for file in kraken_library/*.fa
do
    kraken2-build --add-to-library $file --db kraken_database
done
```

### 2.4 Build Kraken database
```
mv taxonomy kraken_database
kraken2-build --build --db kraken_database --threads 8
```

### 2.5 Build Bracken database
Build a bracken library with a k-mer length of 35 and a reads length of 150
```
bracken-build -d kraken_database -t 8 -k 35 -l 150
```

### 2.6 Output
```kraken_database/hash.k2d```  Contains the minimizer to taxon mappings.<br>
```kraken_database/opts.k2d```  Contains information about the options used to build the database.<br>
```kraken_database/taxo.k2d```  Contains taxonomy information used to build the database.<br>
```kraken_database/database150mers.kraken```   The classifications for each perfect read of 150 base pairs from one of the input sequences.<br>
```kraken_database/database150mers.kmer_distrib```  The kmer distribution file.
