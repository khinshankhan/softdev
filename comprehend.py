def read(filename):
    listi = []
    with open(filename) as file:
        for line in file:
            lineb = line.strip()
            temp = lineb.split(' ')
            for i in temp:
                listi.append(i)
    return listi

#print read("uncletomcabin.txt")

def word(word1, word2):
    return 1 if word1 == word2 else 0

def freq(word):
    return reduce(word, )
