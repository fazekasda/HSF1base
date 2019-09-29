import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

from collections import defaultdict

species_file = {
    "human": "HSF-1_all_targets_human.mitab",
    "worm": "celegans_to_human.mitab",
    "fly": "drosi_to_human.mitab",
    "mouse": "mouse_to_human.mitab",
    "rat": "rat_to_human.mitab",
    "yeast": "yeast_to_human.mitab",
}
all_species = list(set(species_file.keys()))
species_targets = {}

for sp, mitab in species_file.items():
    species_targets[sp] = []
    with open(mitab) as mitab_file:
        for line in mitab_file:
            cells = line.strip().split("\t")
            target = cells[1].split(":")[1].upper()
            species_targets[sp].append(target)

for sp, ls in species_targets.items():
    species_targets[sp] = set(ls)

sp_comb_num = {}
with open("species_list.tsv", "w") as out_file:
    # 1 sp
    for sp, _ in species_targets.items():
        targets = set(species_targets[sp])
        for s in all_species:
            if s != sp:
                targets = targets - set(species_targets[s])
        sp_comb_num[f"{sp}"] = len(targets)
        out_file.write(f"{sp}: {len(targets)}\n")
        out_file.write("\n".join(list(targets)))
        out_file.write("\n\n\n")
    # 2 sp
    for sp1, _ in species_targets.items():
        for sp2, _ in species_targets.items():
            if sp1 == sp2:
                continue
            targets = set(species_targets[sp1]) & set(species_targets[sp2])
            for s in all_species:
                if s != sp1 and s != sp2:
                    targets = targets - set(species_targets[s])
            sp_comb_num[f"{sp1},{sp2}"] = len(targets)
            out_file.write(f"{sp1}, {sp2}: {len(targets)}\n")
            out_file.write("\n".join(list(targets)))
            out_file.write("\n\n\n")
    # 3 sp
    for sp1, _ in species_targets.items():
        for sp2, _ in species_targets.items():
            for sp3, _ in species_targets.items():
                if sp1 == sp2 or sp1 == sp3 or sp2 == sp3:
                    continue
                targets = set(species_targets[sp1]) & set(
                    species_targets[sp2]) & set(species_targets[sp3])
                for s in all_species:
                    if s != sp1 and s != sp2 and s != sp3:
                        targets = targets - set(species_targets[s])
                sp_comb_num[f"{sp1},{sp2},{sp3}"] = len(targets)
                out_file.write(f"{sp1}, {sp2}, {sp3}: {len(targets)}\n")
                out_file.write("\n".join(list(targets)))
                out_file.write("\n\n\n")
    # 4 sp
    for sp1, _ in species_targets.items():
        for sp2, _ in species_targets.items():
            for sp3, _ in species_targets.items():
                for sp4, _ in species_targets.items():
                    if sp1 == sp2 or sp1 == sp3 or sp1 == sp4 or sp2 == sp3 or sp2 == sp4 or sp3 == sp4:
                        continue
                    targets = set(species_targets[sp1]) & set(
                        species_targets[sp2]) & set(species_targets[sp3]) & set(species_targets[sp4])
                    for s in all_species:
                        if s != sp1 and s != sp2 and s != sp3 and s != sp4:
                            targets = targets - set(species_targets[s])
                    sp_comb_num[f"{sp1},{sp2},{sp3},{sp4}"] = len(targets)
                    out_file.write(
                        f"{sp1}, {sp2}, {sp3}, {sp4}: {len(targets)}\n")
                    out_file.write("\n".join(list(targets)))
                    out_file.write("\n\n\n")
    # 5 sp
    for sp1, _ in species_targets.items():
        for sp2, _ in species_targets.items():
            for sp3, _ in species_targets.items():
                for sp4, _ in species_targets.items():
                    for sp5, _ in species_targets.items():
                        if sp1 == sp2 or sp1 == sp3 or sp1 == sp4 or sp1 == sp5 or sp2 == sp3 or sp2 == sp4 or sp2 == sp5 or sp3 == sp4 or sp3 == sp5 or sp4 == sp5:
                            continue
                        targets = set(species_targets[sp1]) & set(
                            species_targets[sp2]) & set(species_targets[sp3]) & set(species_targets[sp4]) & set(species_targets[sp5])
                        for s in all_species:
                            if s != sp1 and s != sp2 and s != sp3 and s != sp4 and s != sp5:
                                targets = targets - set(species_targets[s])
                        sp_comb_num[f"{sp1}, {sp2}, {sp3}, {sp4}, {sp5}"] = len(
                            targets)
                        out_file.write(
                            f"{sp1},{sp2},{sp3},{sp4},{sp5}: {len(targets)}\n")
                        out_file.write("\n".join(list(targets)))
                        out_file.write("\n\n\n")
    # 6 sp
    targets = set(species_targets[all_species[0]]) & \
        set(species_targets[all_species[1]]) & \
        set(species_targets[all_species[2]]) & \
        set(species_targets[all_species[3]]) & \
        set(species_targets[all_species[4]]) & \
        set(species_targets[all_species[5]])
    sp_comb_num[f"{all_species[0]},{all_species[1]},{all_species[2]},{all_species[3]},{all_species[4]},{all_species[5]}"] = len(
        targets)
    out_file.write(
        f"{all_species[0]}, {all_species[1]}, {all_species[2]}, {all_species[3]}, {all_species[4]}, {all_species[5]}: {len(targets)}\n")
    out_file.write("\n".join(list(targets)))
    out_file.write("\n\n\n")

with open("species_list_num.tsv", "w") as out_file:
    out_file.write("species combination\ttargets\n")
    for sp, n in sp_comb_num.items():
        out_file.write(f"{sp}\t{n}\n")

isvertebrate = {
    #    "human": True,
    "worm": False,
    "fly": False,
    "mouse": True,
    "rat": True,
    "yeast": False,
}
vertebrate = []
nonvertebrate = []
for sp, v in isvertebrate.items():
    if v:
        vertebrate.extend(species_targets[sp])
    else:
        nonvertebrate.extend(species_targets[sp])
vertebrate = set(vertebrate)
nonvertebrate = set(nonvertebrate)
only_vertebrate = vertebrate - nonvertebrate
only_nonvertebrate = nonvertebrate - vertebrate
common_v = vertebrate & nonvertebrate
with open("species_vertebrate_list.tsv", "w") as out_file:
    out_file.write(f"vertebrate: {len(only_vertebrate)}\n")
    out_file.write("\n".join(list(only_vertebrate)))
    out_file.write("\n\n\n")
    out_file.write(f"nonvertebrate: {len(only_nonvertebrate)}\n")
    out_file.write("\n".join(list(only_nonvertebrate)))
    out_file.write("\n\n\n")
    out_file.write(f"common: {len(common_v)}\n")
    out_file.write("\n".join(list(common_v)))
    out_file.write("\n\n\n")

plt.figure(figsize=(4, 4))
venn2(
    [
        vertebrate,
        nonvertebrate
    ],
    set_labels=(
        "Vertebrate",
        "Non-vertebrate"
    )
)
plt.savefig('species_vertebrate_venn.svg')
