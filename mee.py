def fcfs(seek,size,head):
    for s in seek:
        print (s,end=" -> ")

    total= 0 
    dist=  0

    for s in seek:
        dist = abs(s-head)
        total+=dist
        head = s
    print(f"total seek is {total}")

size = int(input("Enter no of Seeks : "))
seek = [0]*size
for i in range (size):
    seek[i]=int(input(f"Enter {i} Seek "))
head = int (input("Enter Head : "))
fcfs(seek,size,head)