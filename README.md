# Bioinformatic tools

> in-frame-STOP-finder.py

- This python script searches coding sequences for in-frame STOP codons (such as those found in pseudogenes and endogenous viral elements).
- The user defines whether they would like removal of the STOP (e.g., ready for selection tests), or soft-masking (conversion to lower-case)
- The script works with coding sequence found in a table column

>in-frame-STOP-finder-from-FASTA.py

- Python script that searches coding sequences for in-frame STOP codons (such as those found in pseudogenes and endogenous viral elements).
- The user defines whether they would like removal of the STOP (e.g., ready for selection tests), or soft-masking (conversion to lower-case)
- The script works with coding sequence found in multi-FASTA files

>coding-seq-translator.py

- Translates coding sequence found in a table column (i.e., has no built-in handling of STOPs)
- Outputs it to a new column
