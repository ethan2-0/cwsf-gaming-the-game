import main as main

f1=open('./output.txt', 'a')
i = 364216
while (i < 2461200):
    print(i)
    f1.write(main.get_word(i) + "\r\n")
    i += 1
