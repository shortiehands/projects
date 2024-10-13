import sys

def power_modulo(m, k, n):
    if n == 0:
        return 0
        
    if k == 0:
            
        return 1
    #anything to the power of 0 returns 1, hence the mod will be 1
        
    else:
            
        #reducing k by half
        new_k = k // 2
        even = power_modulo(m,new_k,n) % n
        result = (even * even) % n
        
        #if odd number
        if k % 2 == 1:
            result = (m * result) % n
            
        return result

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
