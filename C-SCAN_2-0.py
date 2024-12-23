def scan(seek, head, direction):
    seek += [0, 199]
    seek.sort()
    total = 0
    
    left = [x for x in seek if x <= head]
    right = [x for x in seek if x > head]

    if direction.lower()[0] == 'l':
        sequence = left[::-1] + right[::-1]  
    elif direction.lower()[0] == 'r':
        sequence = right + left
    else:
        print("Invalid Direction")
        return

    print(head, end=" -> ")
    for req in sequence:
        total += abs(head - req)
        head = req
        print(req, end=" -> ")

    print("\nTotal seek is:", total)

seek = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter initial head position: "))
direction = input("Enter direction (L/R): ")

scan(seek, head, direction)