def minCoin(coins,total):

    for c in coins:
        if c == total: return c
        if c < total:
            flag = c

    return  [flag] + [minCoin(coins,total-flag)]



def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except:
            yield item



c = [1,5,6,8]
t = 11
ans =minCoin(c,t)
l = list(flatten(ans))
print(l)
