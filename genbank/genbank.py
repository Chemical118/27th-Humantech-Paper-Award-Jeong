from Bio import SeqIO

# Definition
slic_chla_genbank_part = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro_slic"
whole_chla_seq = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.gbff"
only_chla_gene = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro.gbff"
telo_for = "CCCTAAAA"
telo_bac = "TTTTAGGG"
sample_count = 2000

# main part
record = SeqIO.parse(only_chla_gene, "genbank")
for index, iter_seq in enumerate(record):
    t = iter_seq.seq.upper()
    t_for = t[:sample_count]
    t_bac = t[-sample_count:]
    if t_for.count(telo_for) > 0:
        SeqIO.write(iter_seq[:sample_count], slic_chla_genbank_part + str(index + 1) + "_for.gbff", "genbank")
    if t_bac.count(telo_bac) > 0:
        SeqIO.write(iter_seq[-sample_count:], slic_chla_genbank_part + str(index + 1) + "_bac.gbff", "genbank")
