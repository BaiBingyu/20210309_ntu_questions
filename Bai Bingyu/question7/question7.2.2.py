# Question7 2 2
# 6 dimentional
# convert index to coordinate
# all of the integers are input successively
total = input().split()
index = list()
for i in total:
    index.append(int(i))
[L1,L2,L3,L4,L5]=[4, 8, 5, 9, 6]
coor = list()
for i in index:
    item = [0,0,0,0,0,0]
    item[5] = i//(L1*L2*L3*L4*L5)
    item[4] = (i%(L1*L2*L3*L4*L5))//(L1*L2*L3*L4)
    item[3] = ((i%(L1*L2*L3*L4*L5))%(L1*L2*L3*L4))//(L1*L2*L3)
    item[2] = (((i%(L1*L2*L3*L4*L5))%(L1*L2*L3*L4))%(L1*L2*L3))//(L1*L2)
    item[1] = ((((i%(L1*L2*L3*L4*L5))%(L1*L2*L3*L4))%(L1*L2*L3))%(L1*L2))//L1
    item[0] = ((((i%(L1*L2*L3*L4*L5))%(L1*L2*L3*L4))%(L1*L2*L3))%(L1*L2))%L1
    coor.append(item)
for i in range(len(total)):
    print(coor[i])