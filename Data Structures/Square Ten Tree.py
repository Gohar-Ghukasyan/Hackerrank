# Enter your code here. Read input from STDIN. Print output to STDOUT
# work with big numbers as strings
L = input()
R = input()

# look for largest possible level
d = len(R)
level = 0
n = 1
tree = [n]  # chunk dimension
while d >= n + 1:
    tree.append(n)
    level += 1
    n = 2 ** level


# go backwards from largest level
def breakdown(N, k):
    if k == 0:
        return [int(N)]

    div = tree[k]
    chunks = breakdown(N[-div:], k - 1)
    chunks.append(N[:-div].lstrip('0') or 0)
    return chunks


divL = breakdown(L, level)
divR = breakdown(R, level)
seq = []

# add up to higher level for L
carry = 0
for k, n in enumerate(map(int, divL)):
    if k == 0:
        carry = -1  # add up lowest number

    n += carry
    carry = 0

    if k < level:
        if n > 0:
            n = 10 ** tree[k] - n
            carry = 1
        elif n < 0:
            n = 1  # if lowest was zero

        seq.append((k, n))

# sum up last level of L and R
if n != 0:
    divR[k] = int(divR[k]) - n
    while divR[-1] == 0:
        del divR[-1]
        n = seq.pop()[1]
        if n != 0:
            divR[-1] = int(divR[-1]) + n

# add R in reversed order
seq.extend(reversed(list(enumerate(divR))))

# exclude empty levels
seq = [s for s in seq if s[1] != 0]
print(len(seq))

for s in seq:
    print(*s)
