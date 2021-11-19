import openpyxl
from openpyxl.chart import BarChart,Reference

wb=openpyxl.Workbook()   #create new workbook
sheet=wb.active

for i in range(10):
    sheet.append([i])

#create chart
values=Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)
chart=BarChart()
chart.add_data(values)
chart.title="Bank of America Profits"
chart.x_axis.title='X Axis'
chart.y_axis.title='Y Axis'

sheet.add_chart(chart,"E2")
wb.save("/Users/aniron/Documents/BofA_Python_Training_15Nov21/day3/automate/barchart.xlsx")
print("Bar chart created........ great")