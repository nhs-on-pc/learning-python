from openpyexcel import load_workbook
wb = load_workbook('DanhSach.xlsx', read_only=True)
print(wb.sheetnames)
print(wb.active)
#sheet = wb['Sheet1']
sheet = wb.active
# Print dimension
print(sheet.calculate_dimension())

print(sheet['A1'].value)

print(sheet.rows)

for row in sheet.rows:
    for cell in row:
        print(cell.value)

print("--------")
print(sheet['E2:E5'])