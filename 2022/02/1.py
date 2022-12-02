file = open("input.txt").read()

out = 0
score = {
    "A X": 4, # draw
    "B Y": 5, # draw
    "C Z": 6, # draw
    "C X": 7, # win
    "A Y": 8, # win
    "B Z": 9, # win
    "B X": 1, # lose
    "C Y": 2, # lose
    "A Z": 3, # lose
}

for i in file.split("\n"):
    out += score[i]

print(out)