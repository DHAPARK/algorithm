n = 1260
leakList = [500,100,50,10]
leakList2 = []
def pro1():
    global n
    global leakList
    global leakList2
    result = n
    sum = 0
    for i in range(4):
        if result >= leakList[i]:
            cnt = int(result / leakList[i])
            result = result - (leakList[i] * cnt)
            leakList2.append(cnt)
        else:
            break
    for i in range(len(leakList2)):
        #print(leakList[i],"짜리",leakList2[i],"개")
        sum += leakList2[i]
    print(sum)
pro1()
