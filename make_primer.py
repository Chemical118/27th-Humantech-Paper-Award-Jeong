from Bio import SeqIO
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np


whole_chla_seq = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.gbff"
only_chla_gene = "GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic_chro.gbff"

record = SeqIO.parse(only_chla_gene, "genbank")
ans_list = []
for i in record:
    record_len = len(i)
    ans = record_len
    for j in i.features:
        t = j.location.start.real
        if t != 0:
            ans = min(t, ans)
        t = j.location.end.real
        if record_len - t != 0:
            ans = min(record_len - t, ans)
    print(ans, i.id)
    ans_list.append(ans)

x = np.asarray(range(len(ans_list)))
label = list(range(1, len(ans_list)+1))
rc('font', family="NanumGothic")
plt.bar(x, ans_list)
plt.xticks(x, label)
plt.xlabel("염색체 순서")
plt.ylabel("DNA 길이 (bp)")
plt.show()
