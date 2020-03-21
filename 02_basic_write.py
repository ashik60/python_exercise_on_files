file= open("02_basic_write.txt", "w")
authors= [
    [1,'almasud','Abdullah Al Masud'],
    [2,'rimon','Rimon Ali'],
    [3,'niloy','Niloy Roy'],
    [4,'sourav','Sourav Dev Sharma'],
    [5,'sathi','Sathi Rani Roy']
]

for i in authors:
    file.write("{},{},{}\n".format(i[0],i[1],i[2]))
    
file.close()