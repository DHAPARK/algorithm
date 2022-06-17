N = int(input(""))
move = input("").split(" ")

x,y = 0,0
mypos = [y,x]

#N-1이 각 마지막
cliff = N-1

for i in range(len(move)):
    #이동할수없는 상태 먼저 파악
    if (x == 0 and move[i] == "L") or (y == 0 and move[i] == "U") or (x == cliff and move[i] == "R") or (y == cliff and move[i] == "D"):
        continue
    if move[i] == "R":
        x += 1
    if move[i] == "L":
        x -= 1
    if move[i] == "D":
        y += 1
    if move[i] == "U":
        y -= 1

print(y+1,x+1)

#결과물 좌표에 둘다 1씩 더해줘야함
