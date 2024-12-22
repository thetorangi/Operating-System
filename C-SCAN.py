def scan(seek,head,direct):
    seek.append(199)
    seek.append(0)
    seek.sort()
    direct=direct.lower()
    total = 0
    print(head,end=" -> ")

    if direct[0] == 'l':
        arr1 = [x for x in seek if x <= head]  
        arr2 = [x for x in seek if x > head]

        for i in range(len(arr1)-1,-1,-1):
            total += abs (head - arr1[i])
            print(arr1[i],end=" -> ")
            head=arr1[i]
        for i in range (len(arr2)-1,-1,-1):
            total += abs(head-arr2[i])
            print(arr2[i],end=" -> ")
            head=arr2[i]

        print("\nTotal seek is : ", total)

    elif direct[0]=='r':
        arr1 = [x for x in seek if x >= head]  
        arr2 = [x for x in seek if x < head]  
        for i in range(len(arr1)):
            total += abs (head - arr1[i])
            print(arr1[i],end=" -> ")
            head=arr1[i]
        for i in range (len(arr2)):
            total += abs(head-arr2[i])
            print(arr2[i],end=" -> ")
            head=arr2[i]
        print("\nTotal seek is : ", total)


    else:
        print("Wrong Direction ")

size = int(input("Enter number of requests: "))
seek = list(map(int, input("Enter the requests separated by space: ").split()))
head = int(input("Enter the initial head position: "))
direct = input("Direction : ")

scan(seek,head,direct)