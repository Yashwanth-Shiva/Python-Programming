def strangeCounter(t):
    time = 1
    value = 3
    while t >= (time+value):
        time = time + value 
        value *= 2
    return value - (t - time)
        

t = int(input())
print(strangeCounter(t))
