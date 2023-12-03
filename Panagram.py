str = input("str: ").upper()
chars = [0] * 26

for ch in str:
    ascii = ord(ch)
    if(ascii >= 65 and ascii<=90):
        chars[ascii-65] += 1

ans = True
for i in chars:
    if(i == 0):
        ans = False
        break

if(ans):
    print("Panagram")
else:
    print("Not Panagram")

