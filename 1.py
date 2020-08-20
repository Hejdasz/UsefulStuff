f = rarfile.RarFile(p / 'test.rar')
rf.testrar()                                #extract rar
rf.extractall(d)
rf.close()

exampleZip.extractall(p)                     #extract zip
exampleZip.close()


print(exampleZip.namelist())                 #show files in zip


for f in rf.infolist():
    Fname = f.filename
    FnameSplit = Fname.split()               #show files in rar
    print(FnameSplit[-1])



mylist = [f for f in glob.glob("*.rar")]     #list of all files in dir

list_of_files = glob.glob('*') #            * latest file in folder
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)



def set_key(dictionary, key, value):                #append dic
     if key not in dictionary:
         dictionary[key] = value
     elif type(dictionary[key]) == list:
         dictionary[key].append(value)
     else:
         dictionary[key] = [dictionary[key], value]
