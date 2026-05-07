



availible = ["CSS", "Apple", "Apples", "Django", "Git", "HTML", "Python"]
availible = availible
query = "A"
suggestions = []
for i in availible:
    if query.lower() in i.lower():
        suggestions.append(i)
print(suggestions)
        



