# Uses python3
import sys

def binary_search(a, x):
    #right=len(a)-1 since right is nth element in list and index starts from 0
    left, right = 0, len(a)-1
    while right>=left:
        mid=int(left + (right-left)/2)
        if a[mid]==x:
            return mid
        # below is similar to recursive call, we have updated the variable -
        #- and done one more loop with updated parameters        
        elif a[mid]>x:
            #eliminating upper half of list
            right=mid-1
        else:
            #eliminating the lower half of list
            left=mid+1
    
    return -1

'''   linear search function:-

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #n is length of search list as first element of input list
    n = data[0]
    #m is number of elements to be found(not really used)
    m = data[n + 1]
    #a is searchlist
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        #finding elements in the search list one by one
        print(binary_search(a, x), end = ' ')
