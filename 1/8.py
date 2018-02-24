def cipher(s):
    ans = ""
    for i in range(len(s)):
        if s[i].islower():
            ans += chr(217 - ord(s[i]))
        else:
            ans += s[i]

    return ans

print(cipher("I Am An Engineer."))

print(cipher(cipher("I Am An Engineer.")))
