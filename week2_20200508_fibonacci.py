# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    
    #initializing total_last(n-2)th and (n-1)th fibonacci number
    total_last=0
    total_current=1
    #also introducing variable that will tabulate fib_n (nth fib number)
    fib_n=0
    for i in range(2,n+1):
        fib_n=total_last+total_current
        total_last=total_current
        total_current=fib_n
                    
    return fib_n
    

n=int(input())
print(calc_fib(n))
