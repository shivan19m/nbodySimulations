def exp(a,n):
    if(n==1):
        return a
    else:
        return (a*exp(a,n-1))

def perms(v): #assumes string not list
    if len(v) <= 1: #for single character use case
        return [v]
    else:
        perm = []
        for x in perms(v[:-1]): 
            for i in range(len(x)+1):
                #generating new string for every permutation
                perm.append(x[:i] + v[-1] + x[i:])
        return perm #returns permutations in list form

def isPalindrome(w):
    if len(w) < 2: 
        return True
    if w[0] != w[-1]: 
        return False
    return isPalindrome(w[1:-1])



