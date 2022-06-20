#문제를 변형해서품
'''
문제를 조금  변형해서

가장 빠른길을 찾고

그 소요시간을 구하는것으로 변경해서 풀었다
'''


#테스트 케이스 갯수 T
#건물의갯수 N 건물간의 건설순서 규칙 개수 K
#각 건물당 건설에 걸리는 시간 d1 ~ dn
#셋째 줄부터 k+2줄까지 건설순서 x y

#마지막에는 건설해야할 건물의 번호 W

def getResult() :
    T = int(input(""))
    for k in range(T):
        TTime = 0    
        N,K = map(int,input("").split(" "))
        dn = list(map(int,input("").split(" ")))
        bo = [0] * K
        for i in range(K):
            bo[i] = list(map(int,input("").split(" ")))
        W = int(input(""))
        TTime += (dn[W-1])
        HTG = W
        while True:
            HTGL = []
            for i in range(K):
                if bo[i][1] == HTG:
                    HTGL.append(bo[i][0])
                    temp = HTGL[0]
                    for n in range(1,len(HTGL)):
                        if dn[temp-1] > dn[HTGL[n]-1]:
                            temp = HTGL[n]
                    HTG = temp
                    TTime += dn[temp-1]
            if ( HTG == 1 ):
                print(TTime)
                break

def main() :        
    getResult()

if ( __name__ == "__main__" ) :
    main()
