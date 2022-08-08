a, b = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))


def prime(x):
    x = x + 1
    primes = []
    for a in range(1, 10000):
        for b in range(2, a):
            if a % b == 0: break
        else:
            primes.append(a)
        if len(primes) == x:
            return primes[1:]


primes = prime(b)
L = []
for i in primes:
    temp_nums = []
    L2 = []
    for j in range(len(nums)):
        num = nums[j]
        if num % i == 0:
            L2 += [num]
        else:
            temp_nums += [num]
    L += L2
    nums = list(reversed(temp_nums))

for i in L:
    print(i)
for i in list(reversed(nums)):
    print(i)



