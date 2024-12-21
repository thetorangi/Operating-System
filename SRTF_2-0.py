import copy

def srtf():
    p_info = []
    process_order = []

    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME AND BURST TIME RESPECTIVELY: ')
    for _ in range(n):
       temp_list = list(map(int, input().split()))
       temp_list.append(0)
       p_info.append(temp_list)
    original_p_info = copy.deepcopy(p_info)

    p_info.sort(key=lambda k: k[1])
    original_p_info.sort(key=lambda p: p[1])

    cur_time = 0
    tot_time_req = 0
    for i in range(n):
        tot_time_req += p_info[i][2]

    counter = 0
    j = 0

    while(counter < tot_time_req):
        min_bt = 99999999
        p_no = None
        for j in range(n):
            if p_info[j][2] != 0:
                if p_info[j][1] <= cur_time:
                    if p_info[j][2] < min_bt:
                        min_bt = p_info[j][2]
                        p_no = p_info[j][0]
        if p_no is None:
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            cur_time += 1
            counter += 1
            for k in range(n):
                if p_no == p_info[k][0]:
                    p_info[k][2] -= 1
                    p_info[k][3] = cur_time

    gantt_chart = []
    i = 0
    ct = 0
    while i < len(process_order):
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        gantt_chart.append([process_order[i], ct])
        i += x
    
    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_chart)):
        print(gantt_chart[p][1], '\t', end='')

    print()

    p_info.sort(key=lambda k: k[0])
    original_p_info.sort(key=lambda p: p[0])

    print("\nTABLE:\n")

    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n):
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', p_info[i][3], '\t\t\t', p_info[i][3] - p_info[i][1], '\t\t\t\t', p_info[i][3] - p_info[i][1] - original_p_info[i][2])

    tot_tat = 0
    tot_wt = 0

    for i in range(n):
        tot_tat += p_info[i][3] - p_info[i][1]
        tot_wt += p_info[i][3] - p_info[i][1] - original_p_info[i][2]

    avg_tat = tot_tat / n
    avg_wt = tot_wt / n

    print('\nAVERAGE TURN AROUND TIME: ', avg_tat)
    print('AVERAGE WAITING TIME: ', avg_wt)


srtf()