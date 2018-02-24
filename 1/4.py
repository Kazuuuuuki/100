s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',', '')


a = s.split(" ") 

ans = []
for t in a:
   ans.append(len(t))

print(ans)

