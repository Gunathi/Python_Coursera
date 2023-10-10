import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().strip()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# {'B': 1, 'u': 6, 't': 12, ' ': 29, 's': 11, 'o': 8, 'f': 3, 'w': 4, 'h': 9, 'a': 10, 'l': 6, 'i': 13, 'g': 3, 'r': 7, 'y': 2, 'n': 9, 'd': 6, 'e': 12, 'b': 1, 'k': 3, 'I': 1, 'J': 1, 'A': 1, 'v': 1, 'm': 1, 'W': 1, 'c': 1, 'p': 1}

