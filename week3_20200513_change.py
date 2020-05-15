# Uses python3
import sys

def get_change(m):
    
    count=0
    
    while m!=0:
        while m>=10:
            m=m-10
            count=count+1
        while m>=5:
            m=m-5
            count=count+1
        while m>=1:
            m=m-1
            count=count+1
      
    return count

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
