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
