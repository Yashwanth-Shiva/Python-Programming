def climbingLeaderboard(ranked, player):
   ranked=sorted(set(ranked),reverse=True)
   l=len(ranked)
   r=[]
   for i in player:
    while (l>0 and i>=ranked[l-1]):
        l-=1
    print(l+1)
    
rc=int(input())
ranked=list(map(int, input().split()))
pc=int(input())
player=list(map(int, input().split()))
climbingLeaderboard(ranked, player)
