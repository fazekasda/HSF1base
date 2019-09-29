import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import venn
from matplotlib_venn import venn2


from collections import defaultdict

species_genes = pd. read_excel(
    "Venn_target_1_2_orto.xlsx", sheet_name=0).dropna(thresh=2)

is_vertebrate = {
    'Human': "Vertebrate",
    'Mouse': "Vertebrate",
    'Worm': "Non-vertebrate",
    'Fly': "Non-vertebrate",
    'Yeast': "Non-vertebrate",
}

targets = defaultdict(list)
targets_v = defaultdict(list)
for index, row in species_genes.iterrows():
    if row[0] == "Rat":
        continue
    targets[row[0]].append(row[1])
    targets_v[is_vertebrate[row[0]]].append(row[1])

list_sp = []
list_targets = []
for sp, t in targets.items():
    list_sp.append(sp)
    list_targets.append(set(t))

labels = venn.get_labels(list_targets, fill=['number'])
fig1, ax = venn.venn5(labels, names=list_sp)
fig1.savefig('species.svg', bbox_inches='tight')

plt.figure(figsize=(4, 4))
venn2(
    [
        set(targets_v["Vertebrate"]),
        set(targets_v["Non-vertebrate"])
    ],
    set_labels=(
        "Vertebrate",
        "Non-vertebrate"
    )
)
plt.savefig('species_vertebrate_venn.svg')
