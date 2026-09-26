text = "python programming"
words=text.split()
frequency = {}
for x in words:
    if x in frequency:
       frequency[x] += 1
    else:
        frequency[x] = 1
print(frequency)
