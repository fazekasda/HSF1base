from collections import defaultdict
import xlrd

species = {
    "9606": "Homo sapiens",
    "10090": "Mus musculus",
    "10116": "Rattus norvegicus",
    "7227": "Drosophila melanogaster",
    "4932": "Saccharomyces cerevisiae",
    "10029": "Cricetulus griseus",
    "6239": "Caenorhabditis elegans",
    "10091": "Mus musculus castaneus",
}
in_data = xlrd.open_workbook("HSF-1_all_targets_summary_1.2.xlsx")

out_table = {}
sheet = in_data.sheet_by_index(0)
for i in range(sheet.nrows):
    if i == 0:
        continue
    target = sheet.cell_value(i, 1).split(":")[1]
    if target not in out_table:
        out_table[target] = {}
        out_table[target]["evidence"] = 0
    out_table[target]["evidence"] += 1
    out_table[target]["alias"] = sheet.cell_value(i, 5).replace(",", "&#44;")
    out_table[target]["taxid"] = sheet.cell_value(i, 9).split(":")[1]
    out_table[target]["species"] = species[out_table[target]["taxid"]]

out_data = open("../HSF1base/static/data/browse.csv", "w")
i = 1
for row_k, row_v in out_table.items():
    out_data.write(
        f'{i},{row_v["alias"]},{row_v["evidence"]},{row_v["species"]},{row_v["taxid"]},{row_k}\n')
    i += 1
    # if i == 1000:
    #     break
