import os

file_path = os.path.abspath(os.path.join("2023/01/input.txt"))

with open(file_path, "r") as file:
    content = file.read()

out = 0

for i in content.split("\n"):
    n = [s for s in i if s.isdigit()]
    out += 0 if len(n) == 0 else int(n[0] + n[-1]) 

print(out)