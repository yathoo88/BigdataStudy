import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "테스트파일"
sheet["A2"] = "hello openpyxl"
sheet.merge_cells("A1:C1")
sheet["A1"].font = openpyxl.styles.Font(size=20)

workbook.save("newExcelFile.xlsx")