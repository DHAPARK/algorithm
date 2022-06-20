yun = [31,29,31,30,31,30,31,31,30,31,30,31]
pug = [31,28,31,30,31,30,31,31,30,31,30,31]

FLAG = []

#윤년 : 100의배수가 아니며 4의 배수 , or 400의 배수

def getResult(yr,mt):
    
    if ((yr % 100 != 0 and yr % 4 == 0) or yr % 400 == 0) :
        FLAG = yun
    else :
        FLAG = pug
    
    if ( mt == 1 ):
        yr -= 1
        mt = 13
    mt -= 1
    
    print("{0} {1} {2}".format(yr,mt,FLAG[mt-1]))
    
    
def main() :
    T = int(input(""))
    
    for i in range(T):
        yi,mi = map(int,input("").split(" "))
        getResult(yi,mi)
        
    pass

if (__name__ == "__main__") :
    main()
