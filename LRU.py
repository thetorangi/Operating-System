def opt(pages, size):
    frames = []  
    hit = 0      
    miss = 0     

    for i in range(len(pages)): 
        print(pages[i],end="  ")
        if pages[i] in frames:
            hit += 1
        else:
            miss += 1  
            if len(frames) < size:
                frames.append(pages[i])  
            else:
                idx = float('inf')
                far =float('inf')
                for j in range(len(frames)):
                    try:
                        nxt=pages[:i-1:-1].index(frames[j])-i-1
                    except ValueError:
                        nxt = float('inf')
                        idx=j
                        break
                    if nxt < far:
                        far=nxt
                        idx=j
                frames[idx]=pages[i]
        print(frames)
    print("Misses are:", miss)
    print("Hits are:", hit)

size = int (input("Enter no of frames  : "))
pages = list(map(int,input("Enter pages : ").split()))
opt(pages, size)