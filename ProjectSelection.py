import sys

import heapq

def project_selection(c, k, cr):
    
    cr.sort(key=lambda x: x[0])
    
    max_heap = []
    
    index = 0 
    
    for _ in range(k):
        for i in range(index,len(cr)):
            if c >= cr[i][0]:
                heapq.heappush(max_heap, (cr[i][0]-cr[i][1]))
                index += 1
                
            else:
                break
        
        if not max_heap:
            return 'impossible'
        
        selected_profit = heapq.heappop(max_heap)
        c -= selected_profit

    return c


a = [int(s) for s in sys.stdin.readline().split()]
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k, cr))
