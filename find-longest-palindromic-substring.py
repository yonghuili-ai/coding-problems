
"""
Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.

leetcode 5
https://leetcode.com/problems/longest-palindromic-substring/description/
https://leetcode.com/problems/longest-palindromic-substring/solution/
The following is to expand around the center
"""

def question2(s):
    sz = len(s)
    i = 0
    res = 0
    start = 0
    while i<sz:
        l, r = i, i
        if (sz-i) <= res/2:
            break
        while r+1 < sz and s[r] == s[r+1]:
            r += 1
        i = r+1
        while l-1>=0 and r+1<sz and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        if res < r-l+1:
            start = l
            res = r-l+1
    return s[start:start+res]

print(question2("babad")) # bab
print(question2("cbbd"))  # bb
