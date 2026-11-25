def findZigZagSequence(a, n):
    a.sort()        #[1,2,3,4,5]----12543
    mid = int((n + 1)/2)#3
    a[mid], a[n-1] = a[n-1], a[mid] #[4,5]=[5,4]---1 2 3 5 4

    st = mid  #4----3
    ed = n - st  #4-----2
    while(st<= n-1):
        a[st], a[ed] = a[ed], a[st]#-- 12534
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
