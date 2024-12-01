file = open("C:/Users/cools/OneDrive/Documents/aoc2024/day1/input.txt","r")
lines = [line.rstrip().split(" ") for line in file]
llist = []
rlist = dict()
for line in lines:
    llist.append(int(line[0]))
    if int(line[-1]) in rlist:
        rlist[int(line[-1])] +=1
    else:
        rlist[int(line[-1])] = 1
ans = 0
for element in llist:
    if element in rlist:
        ans += rlist[element]*element
print(ans)