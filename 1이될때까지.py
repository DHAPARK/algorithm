N,K = map(int,input("").split(" "))

# N - 1
# N - K
cnt = 0
result = N
while result != 1:
    if N % K == 0:
        result = result / K
        cnt+=1
        continue
    else:
        result = result - 1
        cnt+=1
print(cnt)
