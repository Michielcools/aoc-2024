file = open("day4/input.txt","r")
lines = [line.rstrip() for line in file]
i = 0
ans =0
while i < len(lines):
    j = 0
    while j < len(lines[0]):
        if lines[i][j] == "X":
            if j > 2 and lines[i][j] + lines[i][j-1] + lines[i][j-2] + lines[i][j-3] == 'XMAS':
                ans += 1
            if j < len(lines[0])-3 and lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3] == 'XMAS':
                ans += 1
            if i > 2 and lines[i][j] + lines[i-1][j] + lines[i-2][j] + lines[i-3][j] == 'XMAS':
                ans += 1
            if i < len(lines)-3 and lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == 'XMAS':
                ans += 1
            if j > 2 and i > 2 and lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3] == 'XMAS':
                ans += 1
            if j > 2 and i < len(lines)-3 and lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == 'XMAS':
                ans += 1  
            if j < len(lines[0])-3 and i > 2 and lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3] == 'XMAS':
                ans += 1
            if j < len(lines[0])-3 and i < len(lines)-3 and lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == 'XMAS':
                ans += 1                                      
        j+=1
    i+=1
print(ans)