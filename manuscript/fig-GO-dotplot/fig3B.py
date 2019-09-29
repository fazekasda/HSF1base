from plot import GOplot
import xlrd

wb = xlrd.open_workbook("Fig3B_David.xlsx")

fignum = ""
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    if sheet.cell_value(i, 0) == "":
        continue
    if fignum != sheet.cell_value(i, 0):
        if fignum != "":
            GOplot(title, fname, data)
        fignum = sheet.cell_value(i, 0)
        data = []
        title = sheet.cell_value(i, 1)
        fname = f"Fig3B_0_{fignum}.png"
    else:
        data.append([
            sheet.cell_value(i, 1),
            float(sheet.cell_value(i, 2)),
            float(sheet.cell_value(i, 4))
        ])

fignum = ""
sheet = wb.sheet_by_index(1)
for i in range(sheet.nrows):
    if sheet.cell_value(i, 0) == "":
        continue
    if fignum != sheet.cell_value(i, 0):
        if fignum != "":
            GOplot(title, fname, data)
        fignum = sheet.cell_value(i, 0)
        data = []
        title = sheet.cell_value(i, 1)
        fname = f"Fig3B_1_{fignum}.png"
    else:
        data.append([
            sheet.cell_value(i, 1),
            float(sheet.cell_value(i, 2)),
            float(sheet.cell_value(i, 3))
        ])

fignum = ""
sheet = wb.sheet_by_index(2)
for i in range(sheet.nrows):
    if sheet.cell_value(i, 0) == "":
        continue
    if fignum != sheet.cell_value(i, 0):
        if fignum != "":
            GOplot(title, fname, data)
        fignum = sheet.cell_value(i, 0)
        data = []
        title = sheet.cell_value(i, 1)
        fname = f"Fig3B_2_{fignum}.png"
    else:
        data.append([
            sheet.cell_value(i, 1),
            float(sheet.cell_value(i, 2)),
            float(sheet.cell_value(i, 3))
        ])

# data = [
#     ["chaperone-mediated protein folding", 43.47, 3.07E-10],
#     ["protein folding", 16.72, 1.54E-10],
#     ["cellular response to heat", 31.48, 5.38E-06],
#     ["response to heat", 30.43, 4.95E-06],
#     ["cellular response to unfolded protein", 29.64, 5.06E-04],
#     ["response to topologically incorrect protein", 19.76, 2.52E-03],
#     ["response to unfolded protein", 29.64, 6.07E-04],
# ]
# GOplot("PANTHER GO-Slim Biological Process", "test.png", data)
