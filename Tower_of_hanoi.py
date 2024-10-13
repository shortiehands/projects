import sys


def tower_hanoi(n, state):
    Largest = n
    LastDisks = []

    for i, sublist in enumerate(state):
        if sublist:  # Ensure sublist is not empty
            LastDisks.append(sublist[-1])

    # Sort the list of last disks
    LastDisks.sort()

    CheckDisk = LastDisks[-2]  # second largest disk

    ####### Finding the origin peg #######

    def find_peg(disk):
        pegs = ["A", "B", "C"]
        for i, sublist in enumerate(state):
            if disk in sublist:
                return pegs[i]


    ####### Movement dictionary #######
    
    movementforward_dict = {0:{'A':'B', 'B':'C', 'C':'A'},
                   1:{'A':'C', 'C':'B', 'B':'A'}
                  }
    
    movementbackwards_dict = {0:{'A':'C', 'C':'B', 'B':'A'},
                   1:{'A':'B', 'B':'C', 'C':'A'}
                  }
    
    ####### Checking second largest disk's next move #######
    
    r = CheckDisk % 2
    checkdisk_nextmove = movementforward_dict[r][find_peg(CheckDisk)]
    #print("check disk will move to", checkdisk_nextmove)


    ####### Largest disk has been moved, origin peg will be the largest disk's move before #######
    if checkdisk_nextmove == find_peg(Largest):   
        move = True
        OriginPeg = movementbackwards_dict[Largest % 2][find_peg(Largest)]
        #print('original peg is on', OriginPeg, '\n')
    
    ####### Largest disk has not moved, origin peg will at where the largest disk is at #######
    else:
        move = False
        OriginPeg = find_peg(Largest)
        #print('Original peg is on', OriginPeg,'\n')

        ####### Count movements #######
    
    
    def startcount(n):
        count = 0      
        if move:
            count += 2**(n-1)
            for i in range (n-1, 0, -1):
                if find_peg(i) == find_peg(i+1):  #same stack
                    n = i
                    count += 2 ** (i-1)
                    continue
                else:
                    break
                        
                        ####### Largest disks have not move #######
                        
        else:
            for i in range(n-1,0,-1):
                if find_peg(i) == find_peg(i+1):  #no move, no count
                    continue
                                    
                else:
                    #print(f"{i} is in {find_peg(i)}. {i+1} is in {find_peg(i+1)}. hence, it should end here")
                    count += 2 ** (i-1)
                    #print(f"count is now {count}")
                    n = i
                    break
                
        return count, n
            
            
    def move_count(count, n):
        if n == 1:
            return count
        
        peg_current_largest = find_peg(n)
        #print('current largest disk',n, "is on", peg_current_largest)
                    
        r = n % 2
        stack_build = movementforward_dict[r][peg_current_largest]
        #print('For',n,'to move to', peg_current_largest, 'we need to build on',n-1, 'on', stack_build)
                        
        for i in range (n-1,0,-1):
            if stack_build == find_peg(i):
                n -= 1
                
            elif movementforward_dict[(i)%2][stack_build] != find_peg(i):
                return 'impossible'
            
            else:
                count += 2**(i-1)
                return move_count(count,n-1)
            
        return count
    


    # Return both origin peg and move count
    count, n = startcount(n)
    final_count = move_count(count, n)
    
    if final_count == 'impossible':
        return 'impossible'
    
    else:
        return f"{OriginPeg} {final_count}"


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    state = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    n = len(state[0]) + len(state[1]) + len(state[2])
    print(tower_hanoi(n, state))
