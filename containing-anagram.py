"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.

similar to leetcode 438, which is harder than this one
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

def question1(s, t):
    if len(s) < len(t):
        return False
    for i in range(len(s)):
        if i + len(t) > len(s):
            break
        if isAnagram(s[i:i+len(t)], t):
            return True
    return False

def isAnagram(a, b):
    return sorted(a) == sorted(b)

print(question1("udacity", "ad"))
print(question1("ab", "abc"))
