import matplotlib.pyplot as plt

seq_dict = {"A": 1, "G": 2, "T": 3, "C": 4, " ": 0}


def seqencing(a, b, name):
    print("******", name, "******")
    li_ratio = []
    li_diff = []
    for j in range(len(a)):
        print(a, str(j + 1))
        mis = 0
        mat = 0
        for i in range(min(len(a), len(b))):
            if seq_dict[a[i]] == 0 or seq_dict[b[i]] == 0:
                print(" ", end="")
            elif seq_dict[a[i]] != seq_dict[b[i]] and seq_dict[a[i]] % 2 == seq_dict[b[i]] % 2:
                print("|", end="")
                mat += 1
            else:
                print("*", end="")
                mis += 1
        if mis == 0:
            t = (mat - mis) * 1.5
        else:
            t = mat / mis
        li_ratio.append(t)
        li_diff.append(mat - mis)
        print("\n" + b, round(t, 2))
        b = " " + b
    fig = plt.figure(figsize=(9.60, 7.20))
    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()
    line1 = ax1.plot(li_diff, color='orange', label='diff.')
    line2 = ax2.plot(li_ratio, label='ratio')
    lines = line2 + line1
    labels = [l.get_label() for l in lines]
    ax1.set_ylabel('diff. of match and mismatch')
    ax2.set_ylabel('ratio of match and mismatch')
    ax1.set_xlabel('moved bp')
    plt.legend(lines, labels)
    plt.title(name)
    plt.show()


data = [("ACAAAACCCCTTAAAACCCCCATTTAGGGGTTTTAGGGTTTTAGGGTTTTAGGGTTTTAG", "TS1 primer Sample"),
        ("AATCCGTCGAGCAGAGTTTAGGGGTTTTAGGGTTTTAGGGTTTTAGGGTTTTAG", "TS2 primer Sample"),
        ("ACAAAACCCCTTAAAACCCCCATTTAG", "TS1 primer"),
        ("AATCCGTCGAGCAGAGTT", "TS2 primer"), ]  # ("Sequence", "label")

data_check = "CCAAAATCCCAAATTCCCAAATTCCCAAATTCGGCGCG"  # ACX primer

for data_temp, label in data:
    seqencing(data_temp, data_check, label)
