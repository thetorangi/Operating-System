def fcfs(process,n):
    wt =[]
    tt = []
    ct = []
    completed=0
    for i in range(n):
        print(process[i][2] ,end="\t|")
        completed+=process[i][1]
        ct.append(completed)
        tt.append(completed-process[i][0])
        wt.append(tt[i]-process[i][1])

    print()
    for i in range(n):
        print("\t",ct[i],end="")
        
    print("\n\nprocess\t| arrivaltime\t| burst Time\t| completeTime\t| turaround\t| waitingtime\t| ")
    for i in range(n):
        print(process[i][2],"\t\t",process[i][0],"\t\t",process[i][1],"\t\t",ct[i],"\t\t",tt[i],"\t\t",wt[i])
    print("\nAverage waiting time is : " ,sum(wt)/n)
    print("\nAverage complete time is :",sum(ct)/n)
n = int (input("Enter size :"))
process=[]
for i in range(n):
    av = int(input("\nEnter arrival time : "))
    bt = int(input("\nEnter burst time : "))
    name = input("Process name : ")
    process.append([av,bt,name])

fcfs(process,n)