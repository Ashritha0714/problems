import heapq
def find_klarge(arr,k):
    arr=[-i for i in arr]
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s*-1
arr=list(map(int,input().split()))
k=int(input())
ans=find_klarge(arr,k)
print(ans)
