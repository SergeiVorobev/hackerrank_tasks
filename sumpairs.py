#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs = 0
    for i in ar:
        for j in ar:
            if i != j and i < j and sum([i,j])%k == 0:
                pairs+=1
    return pairs


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    
    ar = list(map(int, input().rstrip().split()))
    
    result = divisibleSumPairs(n, k, ar)
    
    print(result)
