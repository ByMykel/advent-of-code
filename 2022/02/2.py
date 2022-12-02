file = open("input.txt").read()

out = 0
score = {
    "B X": 1, # lose
    "C X": 2, # lose
    "A X": 3, # lose
    "A Y": 4, # draw
    "B Y": 5, # draw
    "C Y": 6, # draw
    "C Z": 7, # win
    "A Z": 8, # win
    "B Z": 9, # win
}

for i in file.split("\n"):
    out += score[i]

print(out)