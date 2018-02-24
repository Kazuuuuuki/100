def word_ngram(s, n):
    s = s.split(" ")
    ans = []
    for i in range(len(s)-n+1):
        ans.append([])
        for j in range(n):
            ans[i].append(s[j+i])

    return ans


def chr_ngram(s, n):
    s = s.replace(" ", "")
    ans = []
    for i in range(len(s)-n+1):
        ans.append("")
        for j in range(n):
            ans[i] += s[i+j]

    return ans

x = "paraparaparadise"
y = "paragraph"



X = chr_ngram(x, 2)
Y = chr_ngram(y, 2)

sX = set(X)
sY = set(Y)

print(sX|sY)
print(sX-sY)
print(sX^sY)

print("se" in sX)
print("se" in sY)





