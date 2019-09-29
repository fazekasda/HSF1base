from collections import defaultdict
import xlrd
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import matplotlib

FIGs = [
    ["Fig1_Venn_David.xlsx", "Fig1.png"],
    ["Fig1B_Venn_David.xlsx", "Fig1B.png"],
    ["Fig2_Venn_David.xlsx", "Fig2.png"],
    ["Fig2B_Venn_David.xlsx", "Fig2B.png"],
]

for infile, outfile in FIGs:
    cats = defaultdict(list)
    wb = xlrd.open_workbook(infile)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        cats[sheet.cell_value(i, 1)].append(sheet.cell_value(i, 0))
    labels = []
    for k, v in cats.items():
        cats[k] = set(v)
        labels.append(k)
    fig = plt.figure(figsize=(4, 4))
    venn3(
        [
            cats[labels[0]],
            cats[labels[1]],
            cats[labels[2]],
        ],
        set_labels=(
            labels[0],
            labels[1],
            labels[2],
        )
    )
    fig.set_size_inches(10, 10)
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    plt.close()
