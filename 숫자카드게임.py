#숫자 카드 게임
#행 , 열
N,M = map(int,(input("").split(" ")))

ArrEachList = []
semi = []

for i in range(N):
    ArrEachList.append(list(map(int,input("").split(" "))))

for i in range(N):
    temp = ArrEachList[i][0]
    for k in range(M):
        if ArrEachList[i][k] < temp:
            temp = ArrEachList[i][k]
    semi.append(temp)

temp = semi[0]
for i in range(N):
    if semi[i] > temp :
        temp = semi[i]
print(temp)
