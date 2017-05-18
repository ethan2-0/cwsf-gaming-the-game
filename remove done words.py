words = []
with open("words.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]

with open("words2.txt", "w") as f:
    for i in range(0, len(words)):
        if (i >= 5721 and i <= 10983) or (i >= 13017 and i <= 22640):
            f.write(words[i] + "\n")
