import os, re, pprint, openpyxl

os.chdir('H:\\work\\test')
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['1']
classes = []
for i in range(2,1215):
    Page = sheet.cell(row=int(i), column=1).value
    number = sheet.cell(row=int(i), column=3).value
    classesObject = str(Page)+' ('+str(number)+')'

    classes.append(classesObject)

a =0
for folderName, subfolders, filenames in os.walk('H:\\work\\test\\more test'):
    for filename in filenames:
        print(filename)
        old_name = (folderName+'\\'+filename)
        
        os.rename(old_name, folderName+'\\'+classes[a]+'.txt')
        a+=1
        
        
    break
