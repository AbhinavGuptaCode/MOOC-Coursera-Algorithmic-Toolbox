# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1=0
    max2=0
    index1=0
    
    
    for i in range(n):
        if numbers[i]>max1:
            max1=numbers[i]
            index1=i
    
    for j in range(n):
        if numbers[j]>max2 and j!=index1:
            max2=numbers[j]
    
    max_product=max1*max2

    return max_product

input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
