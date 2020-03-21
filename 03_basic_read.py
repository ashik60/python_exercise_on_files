file= open("03_basic_read.txt", "r")
#print(file.readlines())


for info in file:
    for item in info:
        print(item)
    #print(info, sep=("-"))

file.close()