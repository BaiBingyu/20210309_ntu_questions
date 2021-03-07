# Question 7.1.2
# 2 dimentional
# convert index to coordinate
# all of the integers are input successively
total = input().split()

coor = list()
L = 50
for x in total:
    c = int(x)%L
    r = int(x)//L
    coor.append("("+str(c)+","+str(r)+")")
for i in range(len(total)):
    print(coor[i])