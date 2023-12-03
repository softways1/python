class Anagram:
    str1 = ""
    str2 = ""
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def isAnagram(self):
        chars = [0] * 26
        for ch in self.str1:
            ascii = ord(ch)
            chars[ascii-65] += 1
        for ch in self.str2:
            ascii = ord(ch)
            chars[ascii-65] -= 1
        ans = True
        for i in chars:
            if(i != 0):
                ans = False
                break
        return ans

str1 = input("str1: ").upper()
str2 = input("str2: ").upper()

ob = Anagram(str1, str2)
ans = ob.isAnagram()

if(ans):
    print("Yes Anagram.")
else:
    print("Not Anagram.")
        
