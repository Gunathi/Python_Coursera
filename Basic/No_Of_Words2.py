#use abc.txt file that I have provided or any text file.But that text file should contain in the same folder as python file
name = input('Enter file: ')
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, " : ", bigcount)
