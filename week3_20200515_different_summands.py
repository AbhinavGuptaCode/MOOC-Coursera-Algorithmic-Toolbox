# Uses python3
import sys

def optimal_summands(n):
    summands = []
        
    for i in range(1,n+1):
        n=n-i
        if n==0:
            summands.append(i)
            break
        elif n>(i):
            summands.append(i)
        #below statement mean we are not appending any element in summands, going to next loop
        #therefore add i back to n
        else:
            n=n+i        
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
