def priority_scheduling(n, arrival_time, burst_time, priority):
    CPU = 0
    gantt_chart = []
    waiting_time = [0] * n
    turnaround_time = [0] * n

    processes = [(arrival_time[i], burst_time[i], priority[i], i + 1) for i in range(n)]
    processes.sort(key=lambda x: (x[0], x[2]))

    completed = [False] * n
    remaining = n

    while remaining > 0:
        available = []
        for i in range(n):
            if not completed[i] and processes[i][0] <= CPU:
                available.append(processes[i])

        if not available:
            gantt_chart.append("Idle")
            CPU += 1
            continue

        available.sort(key=lambda x: x[2])
        process = available[0]
        idx = processes.index(process)

        gantt_chart.append(f"P{process[3]}")

        waiting_time[idx] = CPU - process[0]
        CPU += process[1]
        turnaround_time[idx] = waiting_time[idx] + process[1]

        completed[idx] = True
        remaining -= 1

    print("\nGantt Chart:")
    print(" -> ".join(gantt_chart))

    print("\nProcess_Number\tBurst_Time\tPriority\tArrival_Time\tWaiting_Time\tTurnaround_Time\n")
    for i in range(n):
        print(f"P{i+1}\t\t{burst_time[i]}\t\t{priority[i]}\t\t{arrival_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print(f"\nAverage Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")

n = int(input("Enter number of processes: "))
arrival_time = []
burst_time = []
priority = []

for i in range(n):
    at, bt, pr = map(int, input(f"Enter Arrival Time, Burst Time, and Priority for P{i+1}: ").split())
    arrival_time.append(at)
    burst_time.append(bt)
    priority.append(pr)

priority_scheduling(n, arrival_time, burst_time, priority)