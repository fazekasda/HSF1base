from collections import defaultdict
import xlrd
import yaml

D_species = {
    "9606": "Homo sapiens",
    "10090": "Mus musculus",
    "10116": "Rattus norvegicus",
    "7227": "Drosophila melanogaster",
    "4932": "Saccharomyces cerevisiae",
    "10029": "Cricetulus griseus",
    "6239": "Caenorhabditis elegans",
    "10091": "Mus musculus castaneus",
}
D = {
    "MI:0432": "one hybrid",
    "MI:0254": "genetic interference",
    "MI:0402": "chromatin immunoprecipitation assay",
    "MI:1088": "phenotype-based detection assay",
    "MI:0402": "chromatin immunoprecipitation assay",
    "MI:0417": "footprinting",
    "MI:0412": "electrophoretic mobility supershift assay",
    "MI:0606": "DNase I footprinting",
    "MI:1183": "nuclease footprinting",
    "MI:0413": "electrophoretic mobility shift assay",
    "NCIT:C12588": "Hepatocyte",
    "NCIT:C25553": "Leukemic Cell",
    "EFO:0010041": "Nascent-Seq",
    "NCIT:C20226": "HeLa",
    "CLO:0037172": "HME1 cell",
    "CLO:0054401": "K562 derived cell line cell",
    "NCIT:C14156": "Apoptotic",
    "CLO:0007606": "MCF7 cell",
    "UBERON:0000992": "ovary",
    "comment:\"R1\"": "R1",
    "UBERON:0000473": "testis",
    "NCIT:C12598": "Oocyte",
    "comment:\"mitotic cell cycle arrest\"": "mitotic cell cycle arrest",
    "comment:\"R2\"": "R2",
    "comment:\"HMLER cells\"": "HMLER cells",
    "MMO:0000659": "RNA-seq assay",
    "UBERON:0018241": "prime adult stage",
    "UBERON:0004729": "nematode larval stage",
    "UBERON:0008367": "breast epithelium",
    "UBERON:0008367": "breast epithelium",
    "UBERON:0000068": "embryo stage",
    "comment:\"hsb-1(-)\"": "hsb-1(-)",
    "comment:\"HF73 cells\"": "HF73 cells",
    "comment:\"freely cycling cells\"": "freely cycling cells",
    "NCIT:C115935": "Healthy",
    "UBERON:0000361": "red bone marrow",
    "NCIT:C12605": "Spermatocyte",
    "comment:\"BPLER cells\"": "BPLER cells",
    "UBERON:0002956": "granular layer of cerebellar cortex ",
    "MMO:0000649": "high throughput transcription profiling by microarray",
    "NCIT:C16599": "Gametogenesis",
    "CLO:0002021": "BPE cell",
    "comment:\"hsf-1 overexpression\"": "hsf-1 overexpression",
    "UBERON:0002107": "liver",
    "MI:0078": "nucleotide sequence identification",
    "MI:0929": "northern blot",
    "MI:0113": "western blot",
    "ECO:0001071": "in vitro transcription assay evidence ",
    "MI:1196": "quantitative reverse transcription pcr",
    "MI:2247": "transcriptional regulation",
    "MI:0914": "association",
    "MI:2236": "up-regulates activity",
    "MI:2241": "down-regulates activity",
    "MI:0836": "temperature of interaction",
    "MI:2286": "functional association",
    "MI:0407": "direct interaction",
    "MI:1195": "quantitative pcr",
    "MI:2285": "miRNA interference luciferase reporter assay",
    "MI:0982": "electrophoretic mobility-based method",
    "ECO:0000049": "reporter gene assay evidence",
    "NCIT:C17638": "Immunoblot Analysis",
    "ECO:0001805": "luciferase reporter gene assay evidence",
    "CLO:0004009": "Hs 578T cell",
    "CLO:0009619": "WM793B cell",
    "CLO:0001056": "1205Lu cell",
    "BTO:0003424": "B16F10-Nex2 cell",
}


in_data = xlrd.open_workbook("HSF-1_all_targets_summary_1.2.xlsx")

out_table = {}
sheet = in_data.sheet_by_index(0)
for i in range(sheet.nrows):
    if i == 0:
        continue
    target = sheet.cell_value(i, 1).split(":")[1].strip()
    if target not in out_table:
        out_table[target] = {}
        out_table[target]["evidence"] = 0
        out_table[target]["evidences"] = []
    out_table[target]["evidence"] += 1
    out_table[target]["alias"] = sheet.cell_value(i, 5).replace(",", "&#44;")
    out_table[target]["taxid"] = sheet.cell_value(i, 9).split(":")[1]
    out_table[target]["species"] = D_species[out_table[target]["taxid"]]
    evidence = {}
    evidence["i_methods"] = sheet.cell_value(i, 6).split("|")
    evidence["pmids"] = sheet.cell_value(i, 8).split("|")
    evidence["i_types"] = sheet.cell_value(i, 11).split("|")
    evidence["expressions"] = sheet.cell_value(i, 27).split("|")
    evidence["params"] = sheet.cell_value(i, 29).split("|")
    evidence["p_methods_a"] = sheet.cell_value(i, 40).split("|")
    evidence["p_methods_b"] = sheet.cell_value(i, 41).split("|")
    evidence["c_mechanism"] = sheet.cell_value(i, 44).split("|")
    evidence["c_statement"] = sheet.cell_value(i, 45).split("|")
    out_table[target]["evidences"].append(evidence)


out_data = open("../HSF1base/static/data/browse.csv", "w")
i = 1
for row_k, row_v in out_table.items():
    out_data.write(
        f'{i},{row_v["alias"]},{row_v["evidence"]},{row_v["species"]},{row_v["taxid"]},{row_k}\n')
    i += 1
    # if i == 100:
    #     break

for row_k, row_v in out_table.items():
    # if row_k == "ENSG00000151929":
        csv = []
        for e in row_v["evidences"]:
            line = []
            line.append(row_v["alias"])
            line.append(f'<a href="https://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g={row_k}" target="_blank">{row_k}</a>')
            line.append(", ".join([ f'<a href="https://www.ncbi.nlm.nih.gov/pubmed/{p.split(":")[1]}" target="_blank"><i class="fas fa-file"></i></a>"' for p in e["pmids"]]))
            line.append(", ".join([D[p.strip()] for p in e["i_methods"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["i_types"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["expressions"] if p != ""]))
            #line.append(", ".join([D[p.strip()] for p in e["params"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["p_methods_a"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["p_methods_b"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["c_mechanism"] if p != ""]))
            line.append(", ".join([D[p.strip()] for p in e["c_statement"] if p != ""]))
            csv.append(",".join(line))
        yaml_data = {}
        yaml_data["title"] = f'{row_v["alias"]}'
        yaml_data["data_alias"] = row_v["alias"]
        yaml_data["data_id"] = row_k
        yaml_data["data_species"] = row_v["species"]
        yaml_data["data_taxid"] = row_v["taxid"]
        yaml_data["data_numevidence"] = row_v["evidence"]
        yaml_data["csv"] = "\n".join(csv)
        yaml_file = open(f'../HSF1base/content/target/{row_k.lower()}.md', "w")
        yaml_file.write("---\n")
        yaml_file.write(yaml.dump(yaml_data))
        yaml_file.write("---\n")
