if "__main__"==__name__:
    N = int(input())
    mydict ={}
    A = 65
    for _ in range(N):
        mydict[chr(A)] = 0
        A+=1
    loop = int(N*(N-1)/2)
    for _ in range(loop):
        Team1, Team2, Score = input().split(' ')
        T1S = int(Score[0])
        T2S = int(Score[2])
        if T1S == T2S:
            mydict[Team1]+=1
            mydict[Team2]+=1
        elif T1S > T2S:
            mydict[Team1]+=3
        else:
            mydict[Team2]+=3
    max_key = max(mydict, key=mydict.get)
    print(max_key)
    print(mydict[max_key])
