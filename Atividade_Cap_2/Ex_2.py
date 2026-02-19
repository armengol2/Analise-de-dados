n = int(input())
i = int(input())
multi = 1
print("---------------")
while multi <= i:
    print("{} * {} = ".format(n, multi), n * multi)
    print("---------------")
    multi+=1