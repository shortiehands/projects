import sys

def num_grouping(n, m, k):
    
    def stirling(children, group):
        
        if group == 1:
            return 1

        if children == group:
            return 1
        
        if children < group or group == 0:
            return 0

        if (children,group) in combi:
            # print(combi.get(children,group))
            return combi[(children, group)]

        # print(f"num children is {children}, num group of {group}")
        c = stirling(children-1, group-1) + (group * stirling(children-1, group))
        combi[children,group] = c
        # print(combi)

        return c

    children = n
    twin = m
    group = k
    combi = {}
    
    if twin > 0:
            if children == group:
                return 0
            
            if twin * 2 > children:
                return 0
            
    if group == 0:
        return 0 
    
    if group == 1 and twin > 0:
        return 0
    
    # if group == 1 and twin == 0:
    #     return 1
    
    if twin == 0:
        return stirling(children, group)
    
    

    # (children - 2) choose (max_pax_per_group - 2)

    def choose(n,k):
        if n == k: 
            return 1

        if k > n:
            return 0

        choice = factorial(n)//(factorial(k)*factorial(n-k))

        return choice


    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    combinations = 0
    for i in range (0, m+1):
         if n - i >= k:
            combinations += (-1)**i * choose(m, i) * stirling(n-i,k)
            
    return combinations
        

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    print(num_grouping(n, m, k))
