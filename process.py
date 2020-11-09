from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Definition
Chla_process_fasta = "Chlamydomonas_reinhardtii_only_chromosome.fna"
Front_back_Chla_seq_list = []
Front_back_Chla_seq_fasta = "Chlamydomonas_reinhardtii_only_telo_chromosome.fna"
Chla_telo_txt = "Chlamydomonas_reinhardtii_only_telo_chromosome.txt"
telo_for = "CCCTAAAA"
telo_bac = "TTTTAGGG"
sample_count = 1000

# main part
f = open(Chla_telo_txt, "w")
f.close()

record = SeqIO.parse(Chla_process_fasta, "fasta")
for index, iter_seq in enumerate(record):
    t = iter_seq.seq.upper()
    t_for = t[:sample_count]
    t_bac = t[-sample_count:]
    if t_for.count(telo_for) > 0:
        f = open(Chla_telo_txt, "a")
        f.write(str(index + 1) + "번째 염색체 앞쪽 서열\n\n" + str(t_for) + "\n\n")
        Front_back_Chla_seq_list.append(SeqRecord(t_for))
    if t_bac.count(telo_bac) > 0:
        f = open(Chla_telo_txt, "a")
        f.write(str(index + 1) + "번째 염색체 뒤쪽 서열\n\n" + str(t_bac) + "\n\n")
        Front_back_Chla_seq_list.append(SeqRecord(t_bac))

SeqIO.write(Front_back_Chla_seq_list, Front_back_Chla_seq_fasta, "fasta")
