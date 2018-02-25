import func3 as f
#|以下のやつも消すべき??消すならもう少し正規表現が複雑になる。
category_lines = f.category_lines()

categories = []
for i in range(len(category_lines)):
    categories.append(category_lines[i][11:len(category_lines[i])-2])

print(categories)
