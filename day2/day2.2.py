def checkline(line):
    i = 0
    good = True
    diff = 0
    pdiff = 0
    dampened = False
    while i < len(line)-1 and good:
        diff = line[i+1] - line[i]
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if diff*pdiff < 0:
            return False
        pdiff = diff
        i+=1
    return True

file = open("day2/input.txt","r")
lines = [line.rstrip().split(" ") for line in file]
lines = [list(map(int,line)) for line in lines]
ans = 0
for line in lines:
    good = checkline(line)
    if good:
        ans+=1
    else:
        i = 0
        while i < len(line):
            if checkline(line[0:i]+line[i+1:]):
                ans += 1
                break
            i+=1
            
print(ans)