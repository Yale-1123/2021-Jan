def is_overlap(rec1,rec2):
    if abs((rec1[0]+rec1[2])/2-(rec2[0]+rec2[2])/2)<(rec1[2]-rec1[0])/2+(rec2[2]-rec2[0])/2 and abs((rec1[1]+rec1[3])/2-(rec2[1]+rec2[3])/2)<(rec1[3]-rec1[1])/2+(rec2[3]-rec2[1])/2 :
        return True
    else:
        return False

rec1=[]
rec2=[]
for i in range(4):
    rec1.append(int(input()))
for i in range(4):
    rec2.append(int(input()))
print(is_overlap(rec1,rec2))




