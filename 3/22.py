import func3 as f
category_lines = f.category_lines()

categories = []
for i in range(len(category_lines)):
    categories.append(category_lines[i][11:len(category_lines[i])-2])

print(categories)