import pandas as pd

# names of files to read fro
r_filenameTSV_Peptide= 'C:/Users/sitas/CKG/data/imports/databases/Protein.tsv'

# names of files to write to

w_filenameCSV_Peptide = 'C:/Users/sitas/Protein.csv'

# read the data
tsv_read = pd.read_csv(r_filenameTSV_Peptide, sep='\t',nrows=1000)

# print the first 10 records

print(tsv_read.head(10))

# write to files
with open(w_filenameCSV_Peptide,'w') as write_csv:
    write_csv.write(tsv_read.to_csv(sep=',', index=False))
