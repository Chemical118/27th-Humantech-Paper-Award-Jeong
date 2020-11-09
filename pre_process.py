from Bio import SeqIO

Chlamydomonas_Alldna = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.fna"

Chlamydomonas_Chromosome = []
record = SeqIO.parse(Chlamydomonas_Alldna, "fasta")
for i,v in enumerate(record):
    Chlamydomonas_Chromosome.append(v)
    if i + 1 == 17:
        break
print(Chlamydomonas_Chromosome)
SeqIO.write(Chlamydomonas_Chromosome,"Chlamydomonas_reinhardtii_only_chromosome.fna", "fasta")