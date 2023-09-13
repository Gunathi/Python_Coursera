name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"


sender_counts = {}

with open(name) as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            sender = words[1]
            sender_counts[sender] = sender_counts.get(sender, 0) + 1

most_prolific_sender = None
max_count = 0

for sender, count in sender_counts.items():
    if count > max_count:
        most_prolific_sender = sender
        max_count = count

if most_prolific_sender is not None:
    print(most_prolific_sender, max_count)
    
 
