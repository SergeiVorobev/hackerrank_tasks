#!/bin/python3


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    
    # Exclude not equals strings
    if len(s)%2 == 1:
        return(-1)
    else:
        # define median and changes
        m = len(s)//2
        changes = 0
        
        # define strings
        s1, s2 = (s[:m], s[m:])
        
        # define dictionary with key char and countity of chars as value
        s1_d, s2_d = ({}, {})
        for i in s1:
            if i not in s1_d:
                s1_d[i] = s1.count(i)
        for j in s2:
            if j not in s2_d:
                s2_d[j] = s2.count(j)
        
        # evaluate quantity of each characters in both dictionary
        temp = 0 # temp is a quantity of a character which is not exist in the second string
        for key in s1_d:
            if key not in s2_d:
                changes += s1_d[key]
                temp += changes
            else:
                if s1_d[key] != s2_d[key]:
                    changes += abs(s1_d[key] - s2_d[key]) - temp # we decrease changes by temp, because we use these chars to cover not another chars
        return(changes)
        

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
    