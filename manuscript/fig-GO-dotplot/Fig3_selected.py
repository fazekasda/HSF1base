from plot import GOplotFix
import xlrd

wb = xlrd.open_workbook("Fig3_David_selected.xlsx")
sheet_names = wb.sheet_names()

ToPlot = []
limits = {
    "Xmin": 999999,
    "Xmax": -999999,
    "Smin": 999999,
    "Smax": -999999,
}

for s in range(3):
    fignum = ""
    sheet = wb.sheet_by_index(s)
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) == "":
            continue
        if fignum != sheet.cell_value(i, 0):
            if fignum != "":
                ToPlot.append([title, fname, data])
            fignum = sheet.cell_value(i, 0)
            data = []
            title = sheet.cell_value(i, 1)
            fname = f"images/Fig3_selected/Fig3_{sheet_names[s]}_{fignum}.svg"
        else:
            data.append([
                sheet.cell_value(i, 1),
                float(sheet.cell_value(i, 2)),
                float(sheet.cell_value(i, 3))
            ])
            if sheet.cell_value(i, 2) < limits["Smin"]:
                limits["Smin"] = sheet.cell_value(i, 2)
            if sheet.cell_value(i, 2) > limits["Smax"]:
                limits["Smax"] = sheet.cell_value(i, 2)
            if sheet.cell_value(i, 3) < limits["Xmin"]:
                limits["Xmin"] = sheet.cell_value(i, 3)
            if sheet.cell_value(i, 3) > limits["Xmax"]:
                limits["Xmax"] = sheet.cell_value(i, 3)
    ToPlot.append([title, fname, data])

for p in ToPlot:
    GOplotFix(p[0], p[1], p[2], limits["Xmin"],
              limits["Xmax"], limits["Smin"], limits["Smax"])
    break
