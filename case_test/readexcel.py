import xlrd,os

data=xlrd.open_workbook("F:\git\case\\aa.xlsx")
#table=data.sheet_by_index(0)
#table=data.sheets()[0]
table = data.sheet_by_name(u'1')
nrows=table.nrows
ncols=table.ncols
print(nrows,ncols)
aa=table.row_values(0)
bb=table.col_values(0)
print(aa,bb)

#遍历每一行
for i in range(nrows):
    print(table.row_values(i))


#简单写入
table.put_cell(0, 0, 1, '单元格的值', 0)