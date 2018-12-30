

fname = "input_01"
fhand = open(fname)

freq=0
prev_freq = []

loop=0
while True:
    fhand.seek(0)
    for i, line in enumerate(fhand):
        freq+=int(line)
        check = freq in prev_freq
        #print(i, freq, check)
        prev_freq.append(freq)
        if check: 
            #print(freq, "break")
            break
    if check:
        break
    print(loop, freq, "end of file")
    loop+=1
    #if loop==200: break
print("input freq:", freq)