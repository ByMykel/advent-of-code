file = open("input.txt").read()

out = 0

for i in file.split("\n"):
    a, b = i.split(",")
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    contains = a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2

    out += 1 if contains else 0
        
print(out)