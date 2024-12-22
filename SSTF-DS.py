def sstf(seek,head):
    print("Requests:", seek)
    total = 0
    print("Order of access : ")
    print(head,end=" -> ")
    
    while seek:
        closest = min(seek, key=lambda x: abs(x - head))
        print(closest, end=" -> ") 
        total += abs(head - closest)  
        head = closest 
        seek.remove(closest) 
        
    print("\nTotal Seek Time:", total)

size = int(input("Enter number of requests: "))
seek = list(map(int, input("Enter the requests separated by space: ").split()))
head = int(input("Enter the initial head position: "))

sstf(seek,head)