def add_range(min = 0,max = 0):
    ans = 0
    if max == 0:
        for i in range(min+1):
            ans += i
        return ans
    for i in range(min,max+1):
        ans += i
    return ans

print(add_range(5,7))


