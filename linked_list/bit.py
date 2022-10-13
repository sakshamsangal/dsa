# User function Template for python3

class Solution:
    # function to return sum of count of set bits in the integers from 1 to n.
    def count_set_bits(self, n):
        s = 0
        for i in range(n):
            c = 0
            while i:
                if i & 1:
                    c += 1
                i = i >> 1
            s += c
        return s
