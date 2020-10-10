import os
import xlrd

file = os.getcwd() + "\\2020-2021-Approved-Stock-List-converted.xlsx"

wb = xlrd.open_workbook(file)
sheet1 = wb.sheet_by_index(1)
sheet2 = wb.sheet_by_index(2)
stocks = []

for i in range(18, 65):
    stocks.append([sheet1.cell_value(i, k) for k in range(6)])


for i in range(1, 3):
    stocks.append([sheet2.cell_value(i, k) for k in range(6)])


