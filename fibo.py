#3 = 2
#7 = 13 
cnt1 = 0
doingList = []
donList = []
def fib1(n):
    global cnt1
    global donList
    global doingList
    
    doingList.append(n)
    if n == 1 or n == 2:
        donList = set(doingList)
        cnt1 = len(doingList) - len(donList)
        return 1
    return fib1(n-1) + fib1(n-2)


cnt2 = 0
fib2List = []
def fib2(n):
    global cnt2
    global fib2list
    fib2List.append(n)
    if n == 1 or n == 2:
        cnt2 += 1
        return 1
    cnt2 +=1
    return fib2(n-1) + fib2(n-2)


cnt3 = 0
fib3List = []
def fib3(n):
    global cnt3
    global fib3List
    cnt3+=1
    
    a,b=1,1
    for i in range(1,n):
        a,b = b,a+b
        cnt3+=1
        fib3List.append(i)
    return a

def fiboa( n ) :
    fn = [ 0, 1 ]
    for i in range( 2, n + 1 ) :
        fn.append( fn[i-1] + fn[i-2] )
    return fn[n]

def fibob( n ) :
    fn = [ 0 ] * ( n + 1 ) ; fn[1] = 1
    for i in range( 2, n + 1 ) :
        fn[n] = fn[i-1] + fn[i-2] 
    return fn[n]


def main() :
    fib1(10)

    print(fib2(10))
    print(fib3(10))
    print('갱신')
    print("수동 차이 :",cnt2 - cnt3)
    print("자동 차이 :",cnt1)

if ( __name__ == "__main__" ) :
    main()







