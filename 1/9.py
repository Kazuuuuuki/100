import random

def change(s):
    s_words = s.split(" ")
    for i in range(len(s_words)):
        if (len(s_words[i]) > 4):
            tmp = list(s_words[i][1:len(s_words[i])-1])
            random.shuffle(tmp)
            s_words[i] = s_words[i][0] + "".join(tmp) + s_words[i][len(s_words[i])-1]


    ans = " ".join(s_words)

    return ans

print(change("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
                   
