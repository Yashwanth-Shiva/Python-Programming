def flatlandSpaceStations(n, c):
    c.sort()
    dbl_dist = 0
    max_dist = 0
    for i in range(len(c)-1):
         dbl_dist =  c[i+1] - c[i]
         #print(dbl_dist)
         max_dist = max(max_dist, dbl_dist//2)
         #print(max_dist)
    max_dist = max(c[0]-0, max_dist)
    max_dist = max(n-1-c[-1], max_dist)
    return max_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
