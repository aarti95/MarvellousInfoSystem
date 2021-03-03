def ChkPrime(arr):
    brr= []
    sum = 0
    for i in arr:
        c=0
        for j in range(1,i):
            if i%j==0:
                c=c+1
        if c==1:
            sum = sum + i
            brr.append(i)

    return brr


