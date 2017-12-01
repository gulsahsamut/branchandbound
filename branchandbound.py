import numpy as np
import string


def def_branch(s1, s2, cost=0, bound=0):
    cost += 1
    n = len(s1)
    m = len(s2)

    if n == 0 and m == 0:
        return 0
    if n == 0:
        return m
    if m == 0:
        return n

    hx1 = abs((n - 1) - m)
    fx1 = hx1 + cost

    hx2 = abs(n - (m - 1))
    fx2 = hx2 + cost

    hx3 = abs((n - 1) - (m - 1))
    if s1[-1] == s2[-1]:
        fx3 = hx3 + cost - 1
    else:
        fx3 = hx3 + cost

    if bound >= fx1:
        # print("Branch 1")
        return def_branch(s1[:-1], s2, cost, bound) + 1  # Deletion
    if bound >= fx2:
        # print("Branch 2")
        return def_branch(s1, s2[:-1], cost, bound) + 1  # Insertion
    if bound >= fx3:
        # print("Branch 3")
        # update bound
        bound += 1
        if (s1[-1] != s2[-1]):
            return def_branch(s1[:-1], s2[:-1], cost, bound) + 1
        else:
            return def_branch(s1[:-1], s2[:-1], cost, bound)

s1 ="intention"
s2 ="execution"
result = def_branch(s1,s2,0,abs(len(s1)-len(s2))+1)
print(result)
