def opt(pages, size):
    frames = []  
    hit = 0      
    miss = 0     

    for i in range(len(pages)): 
        if pages[i] in frames:
            hit += 1
        else:
            miss += 1  
            if len(frames) < size:
                frames.append(pages[i])  
            else:
                idx = -1
                far =-1
                for j in range(len(frames)):
                    try:
                        nxt=pages[i+1:].index(frames[j])+i+1
                    except ValueError:
                        nxt = float('inf')
                        idx=j
                        break
                    if nxt > far:
                        far=nxt
                        idx=j
                frames[idx]=pages[i]
    print("Misses are:", miss)
    print("Hits are:", hit)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
size = 3

opt(pages, size)