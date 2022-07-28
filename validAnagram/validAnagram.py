"""
Verify if a word is a valid anagram from another

Using a hashmap
"""

def check(a, b):
    if len(a) != len(b):
        return False
    hm1 = {}
    hm2 = {}

    for char in a:
        if char in hm1:
            hm1[char] += 1
        else:
            hm1[char] = 1
    
    for char in b:
        if char in hm2:
            hm2[char] += 1
        else:
            hm2[char] = 1
    
    for item in hm1:
        if item not in hm2:
            return False
    return True
            


a = "miles"
b = "smile"
c = "elvis"
d = "lives"


print(check(a, b))
print(check(c, d))
print(check(c, a))

