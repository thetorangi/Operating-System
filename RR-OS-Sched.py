def round_robin(process_list, quantum):  
    n = len(process_list)
    queue = []           
    gantt = []           
    wt = [0] * n         
    tat = [0] * n        
    remaining_bt = [p[1] for p in process_list]  
    time = 0             
    completed = 0        
    
    process_list.sort(key=lambda x: x[0])  
    queue.append(0)  
    
    visited = [False] * n
    visited[0] = True
    
    while completed < n:      
        idx = queue.pop(0)
        if remaining_bt[idx] > 0:
            gantt.append(process_list[idx][2])              
            
            if remaining_bt[idx] > quantum:
                time += quantum
                remaining_bt[idx] -= quantum
            else:
                time += remaining_bt[idx]
                remaining_bt[idx] = 0
                completed += 1
                
                tat[idx] = time - process_list[idx][0] 
                wt[idx] = tat[idx] - process_list[idx][1]  
        
        for i in range(n):
            if (process_list[i][0] <= time and not visited[i] and remaining_bt[i] > 0):
                queue.append(i)
                visited[i] = True
        
        if remaining_bt[idx] > 0:
            queue.append(idx)
               
        if len(queue) == 0:
            gantt.append("Idle")
            time += 1
    
    print("\nGantt Chart:")
    print(" | ".join(str(p) for p in gantt))
    
    print("\nProcess ID | Arrival Time | Burst Time | Turnaround Time | Waiting Time")
    for i in range(n):
        print(f"   {process_list[i][2]}\t\t{process_list[i][0]}\t\t{process_list[i][1]}\t\t{tat[i]}\t\t{wt[i]}")
    
    print(f"\nAverage Turnaround Time: {sum(tat) / n:.2f}")
    print(f"Average Waiting Time: {sum(wt) / n:.2f}")

n = int(input("Enter number of processes: "))
process_list = []
for i in range(n):
    at, bt = map(int, input(f"Enter Arrival Time and Burst Time for P{i+1}: ").split())
    process_list.append([at, bt, f'P{i+1}'])

quantum = int(input("Enter Time Quantum: "))

print("\nSolution:\n")
round_robin(process_list, quantum)