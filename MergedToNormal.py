import os, re, pprint, openpyxl
os.chdir('H:\\work\\test')
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['1']

classes = {}

for i in range(2,1214):                   
                       
            if sheet.cell(row=int(i), column=1).value == None:
                sheet.cell(row=int(i), column=1).value = sheet.cell(row=int(i-1), column=1).value
                
                
wb.save('example.xlsx')
print("\n"+"end")
