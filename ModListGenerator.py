words = []
with open("words2.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]
fl = open('./output_2mod4.txt', 'a');

i = 2
mod = 4
le = len(words)

while(i < le):
    for j in range (100):
        fl.write(words[i] + str(j) + '\n')
    i += mod
