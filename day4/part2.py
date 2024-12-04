file = open("day4/input.txt","r")
lines = [line.rstrip() for line in file]
i = 1
ans =0
while i < len(lines)-1:
    j = 1
    while j < len(lines[0])-1:
        if lines[i][j] == "A":
            xcount = 0
            if lines[i-1][j-1]+lines[i+1][j+1] == "SM" or lines[i-1][j-1]+lines[i+1][j+1] == "MS":
                xcount += 1
            if lines[i-1][j+1]+lines[i+1][j-1] == "SM" or lines[i-1][j+1]+lines[i+1][j-1] == "MS":
                xcount += 1
            if xcount == 2:
                ans += 1
        j+=1
    i+=1
print(ans)