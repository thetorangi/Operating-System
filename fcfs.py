def fcfs(process_list):
    t = 0
    completed = {}  
    gantt = []      
    a_wt = []       
    a_tt = []       
    
    while process_list:
        if process_list[0][0] > t:
            gantt.append("Idle")
            t += 1
            continue
        
        process = process_list.pop(0)
        gantt.append(process[2])  
        
        t += process[1]          
        pid = process[2]         
        ct = t                   
        tt = ct - process[0]     
        wt = tt - process[1]     
        
        a_wt.append(wt)
        a_tt.append(tt)
        completed[pid] = [ct, tt, wt]

    print("Gantt Chart:")
    print(" | ".join(str(p) for p in gantt))

    print("\nProcess ID | Completion Time | Turnaround Time | Waiting Time")
    for pid in completed:
        ct, tt, wt = completed[pid]
        print(f"   {pid}\t\t{ct}\t\t{tt}\t\t{wt}")
    
    print("\nAverage Turnaround Time:", sum(a_tt) / len(a_tt))
    print("Average Waiting Time:", sum(a_wt) / len(a_wt))


process_list = [[0, 20, 'P1'], [1, 4, 'P2'], [3, 3, 'P3']]
print("Input Process List:", process_list)
print("\nSolution:\n")
fcfs(process_list)
