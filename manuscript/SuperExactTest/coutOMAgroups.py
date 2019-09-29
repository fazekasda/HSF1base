species = {
    "HUMAN": 0,
    "YEAST": 0,
    "RATNO": 0,
    "MOUSE": 0,
    "CAEEL": 0,
    "DROME": 0,
}
sps = species.keys()

with open("oma-groups.txt") as omag:
    for line in omag:
        if line[0] == "#":
            continue
        ids = line.strip().split("\t")[2:]
        for omaid in ids:
            for sp in sps:
                if omaid.startswith(sp):
                    species[sp] += 1
print(species)
