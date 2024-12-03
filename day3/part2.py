file = open("day3/input.txt","r")
lines = [line.rstrip() for line in file]
ans = 0
do = True
for line in lines:
    i = 0
    while i < len(line):
        if line[i:i+4] == "do()":
            do = True
        elif line[i:i+7] == "don't()":
            do = False
        elif line[i:i+4] == "mul(" and do:
            j = i+4
            while j < len(line) and line[j] != ")":
                j+=1
            if j < len(line):
                instruction = line[i+4:j].split(",")
                if len(instruction) == 2 and instruction[0].isdigit() and instruction[1].isdigit():
                    ans += int(instruction[0])*int(instruction[1])
        i +=1
print(ans)