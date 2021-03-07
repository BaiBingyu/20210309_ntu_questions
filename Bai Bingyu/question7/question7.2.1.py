# Question7.2.1
# 6 dimentional
# convert coordinate to index
# all of the integers are input successively
total = input().split()
coor = list()
for i in range(len(total)-1):
    if i % 6 == 0:
        coor.append([int(total[i]),int(total[i+1]),\
                     int(total[i+2]),int(total[i+3]),\
                    int(total[i+4]),int(total[i+5])])
    else:
        pass
[L1,L2,L3,L4,L5]=[4, 8, 5, 9, 6]
index = list()
for x in coor:
    i = x[5]*(L1*L2*L3*L4*L5)+\
        x[4]*(L1*L2*L3*L4)+\
        x[3]*(L1*L2*L3)+\
        x[2]*(L1*L2)+\
        x[1]*L1+x[0]
    index.append(i)
for i in range(len(coor)):
    print(str(index[i]))
    
    
