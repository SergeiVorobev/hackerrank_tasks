class Solution:
    def romanToInt(self, s: str) -> int:
        int_str = []
        length = len(s)
        for i in range(length - 1):
            j = 0
            if i < (length - 1) and s[i] == "I":
                if i < (length - 1) and s[i] == s[i + 1]:
                    if s[i] == s[i + 2] and i < (length - 2):
                        int_str.append(3)
                        j += 2
                    else:
                        int_str.append(2)
                        j += 1
                if i < (length - 1) and s[i + 1] == 'V':
                    int_str.append(4) 
                    j += 1
                if i < (length - 1) and s[i + 1] == 'X':
                    int_str.append(9)
                    j += 1
            if i < (length - 1) and s[i] == 'V':
                if s[i + 1] == 'I':
                    if s[i + 2] == 'I' and i < (length - 2):
                        if s[i + 3] == 'I' and i < (length - 3):
                            int_str.append(8)
                            j += 3
                        else:
                            int_str.append(7)
                            j += 2
                    else:
                        int_str.append(6)
                        j += 1
                else:
                    int_str.append(1)
            if i < (length - 1) and s[i] == 'X':
                if s[i + 1] == 'I':
                    if i < (length - 2) and s[i + 2] == 'I':
                        int_str.append(12)
                        j += 2
                    if i < (length - 3) and s[i + 3] == 'I':
                        int_str.append(13)
                        j += 3
                    else:
                        int_str(11)
                        j += 1
                    i = j
                    j = 0
                if i < (length - 1) and s[i + 1] == 'X':
                    if i < (length - 2) and s[i + 2] == 'X':
                        if i < (length - 3) and s[i + 3] == 'X':
                            if i < (length - 4) and s[i + 4] == 'X':
                                if i < (length - 5) and s[i + 5] == 'X':
                                    if i < (length - 6) and s[i + 6] == 'X':
                                        if i < (length - 7) and s[i + 7] == 'X':
                                            if  i < (length - 8) and s[i + 8] == 'X':
                                                int_str.append(90)
                                                j += 9
                                            else:
                                                int_str.append(80)
                                                j += 8
                                        else:
                                            int_str.append(70)
                                            j += 7
                                    else:
                                        int_str.append(60)
                                        j += 6
                                else:
                                    int_str.append(50)
                                    j += 5
                            else:
                                int_str.append(40)
                                j += 4
                        else:
                            int_str.append(30)
                            j += 3
                    else:
                        int_str.append(20)
                        j += 2
                if i < (length - 1) and s[i + 1] == 'L':
                    int_str.append(40)
                    j += 1
                if i < (length - 1) and s[i + 1] == 'C':
                    int_str.append(90)
                    j += 1
                else:
                    int_str.append(10)            
            if i < (length - 1) and s[i] == "L":
                int_str.append(50)
                j += 1
            if i < (length - 1) and s[i] == "C":
                if s[i + 1] == 'D':
                    int_str.append(400)
                    j += 2
                if s[i + 1] == 'M':
                    int_str.append(900)
                    j += 2
                else:
                    int_str.append(100)
                    j += 1
            if i < (length - 1) and s[i] == "D":
                int_str.append(500)
                j += 1
            if i < (length - 1) and s[i] == "M":
                int_str.append(1000)
                j += 1
            i += j
            if i == length - 1: break


        result = 0
        for i in int_str:
            result += i
        return result
    
example = Solution()
# print(example.romanToInt('III'))
print(example.romanToInt('MCMXCIV'))