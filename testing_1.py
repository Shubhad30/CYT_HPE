#text=input("Enter the filename:")
l=[]
with open("test1.txt") as f:
    for line in f:
        for i in line.split():
            l.append(i)
for i in l:
    flag=0
    with open("english1000.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if i in part:
                        flag=1
    if(flag==1):
        print(i," exists.")
    else:
        print(i," doesnt exists..")
