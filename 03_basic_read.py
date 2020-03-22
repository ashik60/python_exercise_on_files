file= open("03_basic_read.txt", "r")
#print(file.readlines())


for info in file:    
    name=info.split(",")
    print(f'{name[0]}-{name[2]}')
    #print(info, sep=("-"))

file.close()