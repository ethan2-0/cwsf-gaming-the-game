
words = []
with open("words.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]


wordsn = []
with open("wlist_match10.txt", "r") as f:
    wordsn = [x.replace("\n", "") for x in f.readlines()]
for i in range(len(wordsn)-1, -1, -1):
    if wordsn[i] in words:
        del wordsn[i]
with open("wlistNewMatch10.txt", "w") as f:
    for i in wordsn:
        f.write(i + "\n")
