import os

values  = {


}

with open("C:/Users/Tomas/source/repos/algdes-labs/gorilla/data/BLOSUM62.txt") as f:
    scores = []
    split = []

    for line in f:  
        if line.startswith('#'):
            continue     
        if line.startswith(' '):
            split = line.split(None)
            continue
        scores.append(line.split(None))
        
        i = 1
    for char in split:
        temp = {}
        for score in scores:
            temp[score[0]] = score[i]
        values[char] = temp
        i = i + 1


# print(values['M']['L'])

print(values)
