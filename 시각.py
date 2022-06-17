#정수 n 입력
time = int(input(""))

cnt = 0

for i in range(time+1):
    for k in range(60):
        for j in range(60):
            if '3' in str(i)+str(k)+str(j):
                cnt+=1
print(cnt)
