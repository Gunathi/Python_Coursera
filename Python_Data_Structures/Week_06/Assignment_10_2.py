name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_counts = {}
for line in handle:
    if line.startswith("From") and len(line.split()) > 2:
        words = line.split()
        if len(words) >= 6:
            time = words[5]
            hour = time.split(':')[0]
            hour_counts[hour] = hour_counts.get(hour, 0) + 1
                
key = sorted(hour_counts)
for i in key:
    print (i, hour_counts[i])
