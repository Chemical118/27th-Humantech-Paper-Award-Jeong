from Bio import SeqIO

whole_chla_seq = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.gbff"
only_chla_gene = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro.gbff"
record = SeqIO.parse(whole_chla_seq, "genbank")
Chlamydomonas_Chromosome = []

for i, v in enumerate(record):
    print(v.id, v.description)
    Chlamydomonas_Chromosome.append(v)
    if i + 1 == 17:
        break
SeqIO.write(Chlamydomonas_Chromosome, only_chla_gene, "genbank")
