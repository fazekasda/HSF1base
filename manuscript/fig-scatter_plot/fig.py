from plot import GOplotFix
import xlrd

figs = [
    ["Fig1_David_selected3_rovid_corHB_v2.xlsx", "Fig1"],
    ["Fig3_David_selected3_rov_corHB_v2.xlsx", "Fig2"],
    ["Fig2_David_selected3_rov_corHB_v2.xlsx", "Fig3"],
    ["Fig4_David_selected4_rov_corHB_v2.xlsx", "Fig4"],
]

for f in figs:
    wb = xlrd.open_workbook(f[0])
    sheet = wb.sheet_by_index(0)
    ToPlot = []
    limits = {
        "Xmin": 999999,
        "Xmax": -999999,
        "Smin": 999999,
        "Smax": -999999,
    }
    fignum = ""
    linenum = 0
    for i in range(sheet.nrows):
        if fignum != sheet.cell_value(i, 0):
            if fignum != "":
                ToPlot.append([title, fname, data])
            fignum = sheet.cell_value(i, 0)
            data = []
            title = sheet.cell_value(i, 1)
            fname = f"images/{f[1]}_{fignum}.png"
            linenum = 0
        else:
            if sheet.cell_value(i, 1) == "":
                data.append([
                    "---",
                    0.0,
                    0.0,
                    linenum
                ])
                linenum += 1
            else:
                data.append([
                    sheet.cell_value(i, 1),
                    float(sheet.cell_value(i, 2)),
                    float(sheet.cell_value(i, 3)),
                    linenum
                ])
                linenum += 1
                if float(sheet.cell_value(i, 2)) < limits["Smin"]:
                    limits["Smin"] = float(sheet.cell_value(i, 2))
                if float(sheet.cell_value(i, 2)) > limits["Smax"]:
                    limits["Smax"] = float(sheet.cell_value(i, 2))
                if float(sheet.cell_value(i, 3)) < limits["Xmin"]:
                    limits["Xmin"] = float(sheet.cell_value(i, 3))
                if float(sheet.cell_value(i, 3)) > limits["Xmax"]:
                    limits["Xmax"] = float(sheet.cell_value(i, 3))
    ToPlot.append([title, fname, data])

    for p in ToPlot:
        GOplotFix(p[0], p[1], p[2], limits["Xmin"],
                  limits["Xmax"], limits["Smin"], limits["Smax"], Plegend=True)
        print(p[1])
