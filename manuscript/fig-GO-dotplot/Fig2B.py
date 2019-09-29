from plot import GOplot
import xlrd

wb = xlrd.open_workbook("Fig2B_David.xlsx")
sheet_names = wb.sheet_names()
for s in range(4):
    fignum = ""
    sheet = wb.sheet_by_index(s)
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) == "":
            continue
        if fignum != sheet.cell_value(i, 0):
            if fignum != "" and len(data) > 1:
                GOplot(title, fname, data)
            fignum = sheet.cell_value(i, 0)
            data = []
            title = sheet.cell_value(i, 1)
            fname = f"Fig2B_{sheet_names[s]}_{fignum}.png"
        else:
            data.append([
                sheet.cell_value(i, 1),
                float(sheet.cell_value(i, 2)),
                float(sheet.cell_value(i, 3))
            ])
    GOplot(title, fname, data)
