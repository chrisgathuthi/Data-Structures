class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
    def isAnagramSimple(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)

test = Solution()
result = test.isAnagram(s="car", t="rac")
print(result)

simple = Solution()
result = simple.isAnagramSimple(s="car", t="rac")
print(result)
"""
At the for loop we are iterating according to the length of string
Then in each loop we are using the array index to find elements of the string and 
add it to the dictionary as keys and initialize it to 1.
Then at the same time we are looking if the element exists and add the value to the 1
in simple terms, create key with value 1 then check if there's another key and the value
add it to one meaning we are incrementing the value by one
we are using the get() because it will provide a default and avoid a keyErro
"""
