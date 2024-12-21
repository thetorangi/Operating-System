def fcfs(process_list):
    t = 0
    completed ={}
    gantt = []
    a_wt=[]
    a_tt=[]
    while process_list != [] :
        if process_list[0][0] > t :
            t+=1
            completed.append("Idel")
            continue
        else:
            process  = process_list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct= t
            tt = ct - process[0]
            wt = tt-process[1]
            a_wt.append(wt)
            a_tt.append(tt)
            completed[pid]=[ct,tt,wt]

    print("Gantt Chart")
    print(gantt)

    print("\nProcess id , Complete Time , Turnaround Time , Waiting Time ")
    print(completed)
        

    
    sum = 0
    for num in a_tt :
        sum += num
    print("\nAverage Turnaround Time")
    average_tt = (sum/len(a_tt))
    print(average_tt)

    sum = 0
    for num in a_wt :
        sum += num
    print("\nAverage Waiting Time")
    average_tt = (sum/len(a_wt))
    print(average_tt)

process_list = [[0,5,'P1'],[1,3,'P2'],[2,4,'P3'],[4,1,'P4']]
fcfs(process_list)
