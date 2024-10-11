with open("input.txt", "r") as f:
    x = f.read()
    y = list(x)

floor = 0

for id, char in enumerate(y):
    if char == '(':
        floor += 1

    if char == ')': 
        floor -= 1

    if floor < 0:
        print(id + 1)
        break
print(floor)

