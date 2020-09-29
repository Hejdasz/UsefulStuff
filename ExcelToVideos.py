import os, re, pprint, openpyxl
import shutil 

os.chdir('F:\\test')
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['4']

row_count = sheet.max_row
classes = []
pages = []
for i in range(2,row_count+1):
    Page = sheet.cell(row=int(i), column=2).value
    number = sheet.cell(row=int(i), column=3).value
    pages.append(number)
    classes.append(Page)
b = 0
'''	
for a in classes:
	print(a)
	b+=1

print(b)
'''

print(len(classes))
print(len(pages))

xd = input()
a =0

for folderName, subfolders, filenames in os.walk('F:\\test\\to sort'):
	
	for filename in filenames:

		print(filename)
		print(classes[a])
		print()					
		old_name = (folderName+'\\'+filename)

		new_name = folderName+'\\'+classes[a]+'.mp4'
		os.rename(old_name,new_name)		
		dest = pages[a]
		print(dest)		
		dir = os.path.join('F:\\test\\sorted',dest)		
		if os.path.exists(dir) == True:
			shutil.move(new_name,dir)
		else:
			os.mkdir(dir)
			shutil.move(new_name,dir)		
		a+=1
