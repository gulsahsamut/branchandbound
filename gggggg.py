import string
from time import time

def def_branch(s1, s2, cost=0, bound=0):
    n = len(s1)
    m = len(s2)
    if n == 0 and m == 0:
        return 0, [], []
    if n == 0:
        return m, ["_" for i in range(m)], [s2[i] for i in range(m)]
    if m == 0:
        return n, [s1[i] for i in range(n)], ["_" for i in range(n)]

    hx1 = abs((n - 1) - m)
    fx1 = hx1 + cost

    hx2 = abs(n - (m - 1))
    fx2 = hx2 + cost

    hx3 = abs((n - 1) - (m - 1))
    if s1[-1] == s2[-1]:
        fx3 = hx3 + cost - 1
    else:
        fx3 = hx3 + cost
    ad1, ad2, ai1, ai2, ac1, ac2 = [], [], [], [], [], []
    if bound >= fx1:
        # print("Branch 1")
        deletion,ad1,ad2  = def_branch(s1[:-1], s2, cost + 1, bound)  # Deletion
        deletion += 1
    else:
        deletion = 1000000
    if bound >= fx2:
        # print("Branch 2")
        insertion,ai1,ai2 = def_branch(s1, s2[:-1], cost + 1, bound)  # Insertion
        insertion += 1
    else:
        insertion = 1000000
    if bound >= fx3:
        # print("Branch 3")
        if (s1[-1] != s2[-1]):
            change,ac1,ac2 = def_branch(s1[:-1], s2[:-1], cost + 1, bound)
            change += 1
        else:
            change,ac1,ac2 = def_branch(s1[:-1], s2[:-1], cost, bound)
    else:
        change = 1000000

    values = [deletion, insertion, change]
    minval = min(deletion, insertion, change)
    if values.index(minval) == 0:
        ad1 = ad1 + [s1[-1]]
        ad2 = ad2 + ["_"]
        return minval, ad1, ad2
    elif values.index(minval) == 1:
        ai1 = ai1 + ["_"]
        ai2 = ai2 +[s2[-1]]
        return minval, ai1, ai2
    else:
        ac1 = ac1 + [s1[-1]]
        ac2 = ac2 + [s2[-1]]
        return minval, ac1, ac2

def get_steps(al1, al2):
    n = len(al1)
    for i in range(n):
        if al1[i] == "_":
            print("Deletion at index " + str(i))
        elif al2[i] == "_":
            print("Insertion " + al1[i] + " at index " + str(i))
        elif al1[i] != al2[i]:
            print("Substitution " + al1[i] + " for " + al2[i] + " at index " + str(i))

def recursive(s1,s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    deletion = recursive(s1[:-1], s2) + 1
    insertion = recursive(s1, s2[:-1]) + 1
    if (s1[-1] != s2[-1]):
        change = recursive(s1[:-1], s2[:-1]) + 1
    else:
        change = recursive(s1[:-1], s2[:-1])
    return min(deletion, insertion, change)

if __name__ == "__main__":
    print('=============================================================================')
    print("Branch and bound for edit distance")
    print('==========================================================================')
    s1 =input("Enter your first string: ")
    s2 =input("Enter your next string: ")
    start_time=time()
    result, a1, a2  = def_branch(s1,s2,0,max(len(s1),len(s2)))
    print(a1,a2)
    print('The edit distance is: ',result)
    end_time=time()
    print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
    start_time=time()
    result = recursive(s1,s2)
    print('The edit distance is: ',result)
    end_time=time()
    print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
    print('*****************')
    print('END OF PROGRAM')
    print('*****************')
