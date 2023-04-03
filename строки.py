



#tmp = 'abcdef'
#print(tmp[0])

t = 'abzr'
for c in t:
    code = ord(c) + 3
    if code > 122:
        print(chr(97 + code - 122))
    else:
        print(chr(code))