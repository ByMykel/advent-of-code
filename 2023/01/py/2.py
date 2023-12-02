import os
import re

file_path = os.path.abspath(os.path.join("2023/01/input.txt"))

with open(file_path, "r") as file:
    content = file.read()

out = 0
valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in content.split("\n"):
    r = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', i)
    for j in range(len(r)):
        if not r[j].isdigit():
            r[j] = str(valid_digits.index(r[j]) + 1)
    out += 0 if len(r) == 0 else int(r[0] + r[-1])
    print(i, r, 0 if len(r) == 0 else int(r[0] + r[-1]), out)

print(out)
