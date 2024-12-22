def fifo(size,pages):
    frame = [None]*size
    hit = 0 
    miss = 0
    head=0
    for page in pages:
        print (page,end=": \t")
        if page in frame:
            hit +=1
            print(frame,end="\t hit \n")
        else:
            miss +=1
            frame[head]=page
            head = int((head+1)%size)
            print(frame,end="\t miss \n")
        
    print("\n\nhits are : ",hit)
    print("\n\nmiss are : ",miss)

size = int(input("Enter number of frames : "))
pages = list(map(int,input("Enter pages : ").split()))

fifo(size,pages)