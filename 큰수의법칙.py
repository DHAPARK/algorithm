tiaojian = input("")
N,M,K = tiaojian.split(" ")
#배열 사이즈 N
#숫자가 더해지는 횟수 M
#같은숫자가 더해질수있는 횟수 K
ArrMem = input("")
ArrStr = ArrMem.split(" ")
Arr = []
Arr = list(map(int,ArrStr))
Arr.sort()
Arr.reverse()
sum = 0
cnt = 0
for i in range(int(M)):
    if cnt == int(K):
        cnt = 0
        sum += Arr[1]
    else:
        sum += Arr[0]
    cnt += 1
    
print(sum)
