import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

from collections import defaultdict

table_human_1 = pd. read_excel(
    "HSF_targets_tissue_specific_human.xlsx", sheet_name=0).dropna(thresh=2)
table_human_2 = pd. read_excel(
    "HSF_targets_tissue_specific_human.xlsx", sheet_name=1)
table_human_3 = pd. read_excel(
    "HSF_targets_tissue_specific_human.xlsx", sheet_name=2)

table_mouse_1 = pd. read_excel(
    "HSF_targets_tissue_specific_mouse.xlsx", sheet_name=0).dropna(thresh=2)
table_mouse_2 = pd. read_excel(
    "HSF_targets_tissue_specific_mouse.xlsx", sheet_name=1)

# human
genes = defaultdict(list)
celltypes = defaultdict(lambda: defaultdict(lambda: 0))
list_tissues = []
for index, row in table_human_1.iterrows():
    celltype = row[2]
    gene = row[1]
    celltypes[celltype][gene] += 1
    genes[gene].append(celltype)
    list_tissues.append(celltype)
unique_tissues = set(list_tissues)

combination = defaultdict(list)
for k, v in genes.items():
    c = list(set(v))
    c.sort()
    combination[tuple(c)].append(k)
with open("human_celltypes.tsv", "w") as out_table:
    for k, v in combination.items():
        comb = "; ".join(list(k))
        out_table.write(f"{comb}\t \n")
        for g in v:
            out_table.write(f" \t{g}\n")
        out_table.write("\n\n")

# human tissue
tissues = {}
tissuenames = []
tissues[table_human_3.columns[0]] = list(set(list(
    table_human_3[table_human_3.columns[0]].dropna().str.strip())))
tissuenames.append(table_human_3.columns[0])
tissues[table_human_3.columns[3]] = list(set(list(
    table_human_3[table_human_3.columns[3]].dropna().str.strip())))
tissuenames.append(table_human_3.columns[3])
tissues[table_human_3.columns[6]] = list(set(list(
    table_human_3[table_human_3.columns[6]].dropna().str.strip())))
tissuenames.append(table_human_3.columns[6])

plt.figure(figsize=(4, 4))
venn3(
    [
        set(tissues[tissuenames[0]]),
        set(tissues[tissuenames[1]]),
        set(tissues[tissuenames[2]])
    ],
    set_labels=(
        tissuenames[0],
        tissuenames[1],
        tissuenames[2]
    )
)
plt.savefig('human_tissue_venn.png')

with open("human_tissue.tsv", "w") as out_table:
    # list(a - (b | c)) # a only
    out_table.write(f"{tissuenames[0]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[0]]) -
                                   (set(tissues[tissuenames[1]]) | set(tissues[tissuenames[2]])))))
    out_table.write("\n\n\n")

    # list(b - (a | c)) # b only
    out_table.write(f"{tissuenames[1]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[1]]) -
                                   (set(tissues[tissuenames[0]]) | set(tissues[tissuenames[2]])))))
    out_table.write("\n\n\n")

    # list(c - (a | b)) # c only
    out_table.write(f"{tissuenames[2]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[2]]) -
                                   (set(tissues[tissuenames[0]]) | set(tissues[tissuenames[1]])))))
    out_table.write("\n\n\n")

    # list((a & b) - c) # a,b only
    out_table.write(f"{tissuenames[0]}; {tissuenames[1]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[1]])) - set(tissues[tissuenames[2]]))))
    out_table.write("\n\n\n")

    # list((a & c) - b) # a,c only
    out_table.write(f"{tissuenames[0]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[2]])) - set(tissues[tissuenames[1]]))))
    out_table.write("\n\n\n")

    # list((b & c) - a) # b,c only
    out_table.write(f"{tissuenames[1]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[1]]) & set(
        tissues[tissuenames[2]])) - set(tissues[tissuenames[0]]))))
    out_table.write("\n\n\n")

    # list(a & b & c) # common
    out_table.write(
        f"{tissuenames[0]}; {tissuenames[1]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list(set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[1]]) & set(tissues[tissuenames[2]]))))
    out_table.write("\n\n\n")


# mouse
genes = defaultdict(list)
celltypes = defaultdict(lambda: defaultdict(lambda: 0))
list_tissues = []
for index, row in table_mouse_1.iterrows():
    celltype = row[2]
    gene = row[1]
    celltypes[celltype][gene] += 1
    genes[gene].append(celltype)
    list_tissues.append(celltype)
unique_tissues = set(list_tissues)

combination = defaultdict(list)
for k, v in genes.items():
    c = list(set(v))
    c.sort()
    combination[tuple(c)].append(k)
with open("mouse_celltypes.tsv", "w") as out_table:
    for k, v in combination.items():
        comb = "; ".join(list(k))
        out_table.write(f"{comb}\t \n")
        for g in v:
            out_table.write(f" \t{g}\n")
        out_table.write("\n\n")

# mouse tissue
tissues = {}
tissuenames = []
tissues[table_mouse_2.columns[0]] = list(
    table_mouse_2[table_mouse_2.columns[0]].dropna().str.strip())
tissuenames.append(table_mouse_2.columns[0])
tissues[table_mouse_2.columns[3]] = list(
    table_mouse_2[table_mouse_2.columns[3]].dropna().str.strip())
tissuenames.append(table_mouse_2.columns[3])
tissues[table_mouse_2.columns[6]] = list(
    table_mouse_2[table_mouse_2.columns[6]].dropna().str.strip())
tissuenames.append(table_mouse_2.columns[6])

plt.figure(figsize=(4, 4))
venn3(
    [
        set(tissues[tissuenames[0]]),
        set(tissues[tissuenames[1]]),
        set(tissues[tissuenames[2]])
    ],
    set_labels=(
        tissuenames[0],
        tissuenames[1],
        tissuenames[2]
    )
)
plt.savefig('mouse_tissue_venn.png')

with open("mouse_tissue.tsv", "w") as out_table:
    # list(a - (b | c)) # a only
    out_table.write(f"{tissuenames[0]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[0]]) -
                                   (set(tissues[tissuenames[1]]) | set(tissues[tissuenames[2]])))))
    out_table.write("\n\n\n")

    # list(b - (a | c)) # b only
    out_table.write(f"{tissuenames[1]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[1]]) -
                                   (set(tissues[tissuenames[0]]) | set(tissues[tissuenames[2]])))))
    out_table.write("\n\n\n")

    # list(c - (a | b)) # c only
    out_table.write(f"{tissuenames[2]}\n")
    out_table.write("\n".join(list(set(tissues[tissuenames[2]]) -
                                   (set(tissues[tissuenames[0]]) | set(tissues[tissuenames[1]])))))
    out_table.write("\n\n\n")

    # list((a & b) - c) # a,b only
    out_table.write(f"{tissuenames[0]}; {tissuenames[1]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[1]])) - set(tissues[tissuenames[2]]))))
    out_table.write("\n\n\n")

    # list((a & c) - b) # a,c only
    out_table.write(f"{tissuenames[0]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[2]])) - set(tissues[tissuenames[1]]))))
    out_table.write("\n\n\n")

    # list((b & c) - a) # b,c only
    out_table.write(f"{tissuenames[1]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list((set(tissues[tissuenames[1]]) & set(
        tissues[tissuenames[2]])) - set(tissues[tissuenames[0]]))))
    out_table.write("\n\n\n")

    # list(a & b & c) # common
    out_table.write(
        f"{tissuenames[0]}; {tissuenames[1]}; {tissuenames[2]}\t \n")
    out_table.write("\n".join(list(set(tissues[tissuenames[0]]) & set(
        tissues[tissuenames[1]]) & set(tissues[tissuenames[2]]))))
    out_table.write("\n\n\n")
