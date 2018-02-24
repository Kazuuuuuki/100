def word_ngram(s, n):
    s = s.split(" ")
    ans = []
    for i in range(len(s)-n+1):
        ans.append([])
        for j in range(n):
            ans[i].append(s[j+i])

    return ans

print(word_ngram("I am an NLPer",3))

def chr_ngram(s, n):
    s = s.replace(" ", "")
    ans = []
    for i in range(len(s)-n+1):
        ans.append([])
        for j in range(n):
            ans[i].append(s[i+j])

    return ans

print(chr_ngram("I am an NLPer",2))
