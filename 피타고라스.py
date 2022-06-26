#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:05:50 2022

@author: dohyeonpark
"""
def pytha01() :
    
    #몇번도는지 측정을위한 cnt
    cnt = 0
    
    pythaList = []
    def checkOne(a,b,c) :
        if (a*a) + (b*b) == (c*c):
            return True
    def checkTwo(a,b,c) :
        if 0 < a and a < b and b < c and c < 50:
            return True
    
    for a in range(51):
        for b in range(51):
            for c in range(51):
                cnt+=1
                if checkOne(a,b,c) and checkTwo(a,b,c) :
                    pythaList.append((a,b,c))
    
    print("pytha01의 도는 횟수 : ",cnt)
    return pythaList


#목적 : 01보다는 조금더 루프를 줄여볼수있는 
def pytha02(n) :
    #pytha02의 도는횟수를 측정하기위한 cnt변수
    cnt = 0
    
    pythaList = []
    def checkOne(a,b,c) :
        if (a*a) + (b*b) == (c*c):
            return True
    def checkTwo(a,b,c) :
        if 0 < a and a < b and b < c and c < 50:
            return True
    
    for a in range(n+1):
        for b in range(n+1):
            #아래 for문을 돌기전에 위에서부터 n제곱의 최대치가 넘어버리면 돌지않게 조건문
            if ((a*a) + (b*b)) > ((n) * (n)):
                continue
            for c in range(n+1):
                cnt+=1
                if checkOne(a,b,c) and checkTwo(a,b,c) :
                    pythaList.append((a,b,c))
    print("pytha02의 도는 횟수 : ",cnt)
    return pythaList





#목적 : 02보다는 조금더 루프를 줄여볼수있는 
def pytha03(n) :
    #pytha02의 도는횟수를 측정하기위한 cnt변수
    cnt = 0
    
    pythaList = []
    def checkOne(a,b,c) :
        if (a*a) + (b*b) == (c*c):
            return True
    def checkTwo(a,b,c) :
        if 0 < a and a < b and b < c and c < 50:
            return True
    
    for a in range(n+1):
        for b in range(n+1):
            #아래 for문을 돌기전에 위에서부터 n제곱의 최대치가 넘어버리면 돌지않게 조건문
            if (((a*a) + (b*b)) > ((n) * (n))) or (a >= b):
                continue
            for c in range(n+1):
                cnt+=1
                if checkOne(a,b,c) and checkTwo(a,b,c) :
                    pythaList.append((a,b,c))
    print("pytha03의 도는 횟수 : ",cnt)
    return pythaList


#목적 : 03보다는 조금더 루프를 줄여볼수있는 
def pytha04(n) :
    #pytha02의 도는횟수를 측정하기위한 cnt변수
    cnt = 0
    
    pythaList = []
    def checkOne(a,b,c) :
        if (a*a) + (b*b) == (c*c):
            return True
    def checkTwo(a,b,c) :
        if 0 < a and a < b and b < c and c < 50:
            return True
    
    for a in range(3,n):
        for b in range(4,n):
            #아래 for문을 돌기전에 위에서부터 n제곱의 최대치가 넘어버리면 돌지않게 조건문
            if (((a*a) + (b*b)) > ((n) * (n))) or (a >= b):
                continue
            for c in range(5,n+1):
                cnt+=1
                if checkOne(a,b,c) and checkTwo(a,b,c) :
                    pythaList.append((a,b,c))
    print("pytha04의 도는 횟수 : ",cnt)
    return pythaList



#목적 : 05보다는 조금더 루프를 줄여볼수있는 
def pytha05( n , cnt = 0 , pythaList = [] , TempAr = [0] * 3 ) :
    #pytha05의 도는횟수를 측정하기위한 cnt변수
    def checkTwo( a,b ) :
        if 0 < a and a < b:
            return True
    def judge( num ) :
        value = num ** 0.5
        if ( value ) % 1 == 0 :
            return True,int( value )
        else:
            return False,0
        
    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            #아래 for문을 돌기전에 위에서부터 n제곱의 최대치가 넘어버리면 돌지않게 조건문
            if (( a*a + b*b ) >= ( n*n )) or ( a>=b ) :
                continue
            TempAr[0] = ( a*a )+( b*b )
            TempAr[1],TempAr[2] = judge( TempAr[0] )
            if checkTwo( a , b ) and TempAr[1] :
                pythaList.append(( a , b , TempAr[2] ))
    print("pytha05의 도는 횟수 : ",cnt)
    return pythaList




#목적 : 05보다는 조금더 루프를 줄여볼수있는 
def pytha06( n , cnt = 0 , pythaList = [] , TempAr = [0] * 2 ) :
    #pytha05의 도는횟수를 측정하기위한 cnt변수
    def checkTwo( a,b ) :
        if 0 < a and a < b:
            return True
        
    def judge( num ) :
        value = num ** 0.5
        if ( value ) % 1 == 0 :
            return True,int( value )
        else:
            return False,0
        
    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            #아래 for문을 돌기전에 위에서부터 n제곱의 최대치가 넘어버리면 돌지않게 조건문
            if (( a*a + b*b ) < ( n*n )) :
                TempAr[0],TempAr[1] = judge(( a*a )+( b*b ))
                if checkTwo( a , b ) and TempAr[0] :
                    pythaList.append(( a , b , TempAr[1] ))
    print("pytha06의 도는 횟수 : ",cnt)
    return pythaList





#목적 : 06보다는 조금더 루프를 줄여볼수있는 
def pytha07( n , cnt = 0 , pythaList = [] , TempAr = [0] * 2 ) :
    #pytha05의 도는횟수를 측정하기위한 cnt변수
    def checkTwo( a,b ) :
        if 0 < a and a < b and (a*a + b*b) < (n*n):
            value = (a*a + b*b) ** 0.5
            if ( value ) % 1 == 0 :
                pythaList.append(( a , b ,int( value )))
                return True
            else:
                return False,0
        else:
            return False,0
        
    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            checkTwo( a , b )
            
    print("pytha07의 도는 횟수 : ",cnt)
    return pythaList



#목적 : 07보다는 쓸모없는 코드 지우기 
def pytha08( n , cnt = 0 , pythaList = []) :
    def checkTwo( a,b ) :
        if 0 < a and a < b and (a*a + b*b) < (n*n) and ((a*a + b*b) ** 0.5) % 1 == 0:
            pythaList.append(( a , b ,int( (a*a + b*b) ** 0.5 )))

    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            checkTwo( a , b )
    print("pytha08의 도는 횟수 : ",cnt)
    return pythaList



#목적 : 08보다는 쓸모없는 코드 지우기 
def pytha09( n , cnt = 0 , pythaList = []) :
    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            if 0 < a and a < b and ( a*a + b*b ) < ( n*n ) and ((a*a + b*b) ** 0.5) % 1 == 0:
                pythaList.append(( a , b ,int( (a*a + b*b) ** 0.5 ) ))

    print("pytha09의 도는 횟수 : ",cnt)
    return pythaList





#목적 : 09보다는 쓸모없는 코드 지우기 
def pytha10( n , cnt = 0 , pythaList = []) :
        
    for a in range( 3,n ) :
        for b in range( 4,n ) :
            cnt+=1
            if 0 < a and a < b and ( a*a + b*b ) < ( n*n ) and ((a*a + b*b) ** 0.5) % 1 == 0:
                pythaList.append(( a , b ,int( (a*a + b*b) ** 0.5 ) ))

    print("pytha10의 도는 횟수 : ",cnt)
    return pythaList




#목적 : 10보다는 쓸모없는 코드 지우기 
def pytha11( n , cnt = 0 , pythaList = []) :    
    pythaListN = [i**2 for i in range(5,n)]
    for a in range(3,n):
        for b in range(4,n):
            cnt+=1
            if a < b and (a**2 + b**2) in pythaListN:
                pythaList.append((a,b,int((a**2 + b**2) ** 0.5)))
    
    print("pytha11의 도는 횟수 : ",cnt)
    return pythaList



#출력 예시
#ABCDEFG AABBCC GFEDCBA
#A                    A
#AB                  BA

#ABCDEFG        GFEDCBA

    
def main() :
    #print(pytha01())
    #print(pytha02(50))
    #print(pytha03(50))
    #print(pytha04(50))
    #print(pytha05(50))
    #print(pytha06(50))
    #print(pytha07(50))
    #print(pytha08(50))
    print(pytha09(50))
    #print(pytha10(50))
    #print(pytha11(50))
    

    
if ( __name__ == "__main__" ) :

    main()
