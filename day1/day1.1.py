file = open("day1/testin.txt","r")
lines = [line.rstrip().split(" ") for line in file]
llist = []
rlist = []
for line in lines:
    i = 0
    while i < len(llist) and int(line[0]) > llist[i]:
        i+=1
    llist.insert(i,int(line[0]))
    i = 0
    while i < len(rlist) and int(line[-1]) > rlist[i]:
        i+=1
    rlist.insert(i,int(line[-1]))
ans = 0
i = 0
while i < len(rlist):
    ans += abs(rlist[i]-llist[i])
    i+=1
print(ans)