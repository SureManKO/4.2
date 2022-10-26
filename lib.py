N = int(input("Введите количество списков\n"))
strings = []
symbols = []
repeats = []
for i in range(N):
    strings.append(input("Введите строку  " + str(i + 1) + "\n"))
for i in range(len(strings)):
    onestring = strings[i]
    for j in range(len(onestring)):
        gotcha = False
        for k in range(len(symbols)):
            if(onestring[j] == symbols[k]):
                repeats[k] = True
                gotcha = True
        if(not(gotcha)):
            symbols.append(onestring[j])
            repeats.append(False)
K = 0
for i in range(len(repeats)):
    if(repeats[i]): K+=1
print("Количество повторяющихся символов: " + str(K))