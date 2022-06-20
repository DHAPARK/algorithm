#1부터 N까지 배열이 있다면 인접한 인덱스의 차가 2 이상이게 만들기


class NodeArr:
    def __init__( self, NodeList=[] ) :
        self.NL = NodeList

class Node:
    def __init__( self , data ) :
        self.data = data
        
def main( num ) :
    NA = NodeArr(  )

    startFrom = int(( num / 2 )) - 1
    startTo = int(( num / 2 ))
    
    
    for i in range( 1 , int(num / 2) +1) :
        if ( i % 2 == 1 ) :
            startFrom = startFrom - ( 2 * i )
        elif ( i % 2 == 0 ) :
            startFrom = startFrom + ( 2 * i )
        
        NA.NL.insert( startFrom , Node( (num+1) - i ) )            
        
            
    for i in range( 1 , int(num / 2)+1 ) :
        if ( i % 2 == 1 ) :
            startTo = startTo + ( 2 * i )
        elif ( i % 2 == 0 ) :
            startTo = startTo - ( 2 * i )
        
        NA.NL.insert( startTo , Node( i ) )

    print(NA.NL)
    for val in NA.NL:
        print(val.data,end=" ")
        
if ( __name__ == "__main__" ) :

    num = int(input("숫자 몇 까지?"))
    
    main(num)
