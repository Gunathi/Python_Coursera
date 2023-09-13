counts = dict()
line = input("Enter line of text: ")
words = line.split()

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

print(counts)
