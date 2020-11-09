from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Definition
Makeall = bool(int(input("Are you want to make all? (Answer 0 or 1) : ")))
slic_chla_genbank_list = []
slic_chla_genbank = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro_slic" + (Makeall * "_all") + ".gbff"
slic_chla_txt = "Chlamydomonas_reinhardtii_slic_chromosome" + (Makeall * "_all") + ".txt"
whole_chla_seq = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.gbff"
only_chla_gene = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro.gbff"
telo_for = "CCCTAAAA"
telo_bac = "TTTTAGGG"
sample_count = 2000

# main part
f = open(slic_chla_txt, "w")
f.close()

record = SeqIO.parse(only_chla_gene, "genbank")
for index, iter_seq in enumerate(record):
    t = iter_seq.seq.upper()
    t_for = t[:sample_count]
    t_bac = t[-sample_count:]
    if t_for.count(telo_for) > 0 or Makeall:
        f = open(slic_chla_txt, "a")
        f.write(">" + str(index + 1) + " forward gene seq\n" + str(t_for) + "\n")
        slic_chla_genbank_list.append(SeqRecord(t_for))
    if t_bac.count(telo_bac) > 0 or Makeall:
        f = open(slic_chla_txt, "a")
        f.write(">" + str(index + 1) + " backword gene seq\n" + str(t_bac) + "\n")
        slic_chla_genbank_list.append(SeqRecord(t_bac))

SeqIO.write(slic_chla_genbank_list, slic_chla_genbank, "genbank")
