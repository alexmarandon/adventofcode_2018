fname = "input_01"
fhand = open(fname)

freq=0

for line in fhand:
    freq+=int(line)

print(freq)