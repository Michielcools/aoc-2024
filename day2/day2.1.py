file = open("day2/input.txt","r")
lines = [line.rstrip().split(" ") for line in file]
lines = [list(map(int,line)) for line in lines]
ans = 0
for line in lines:
    i = 0
    good = True
    diff = 0
    pdiff = 0
    while i < len(line)-1 and good:
        diff = line[i+1] - line[i]
        if abs(diff) > 3 or abs(diff) < 1:
            good = False
        if diff*pdiff < 0:
            good = False
        pdiff = diff
        i+=1
    if good:
        ans+=1
print(ans)