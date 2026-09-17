import random
arr = []
#gen arr
n = 15
miss = 2
for i in range(1,n+1):
    rand = random.random()*2
    # print(rand)
    if miss and int(rand):
        miss-=1
    else:
        arr.append(i)

print(arr)

sum2 = 0

for i in range(len(arr)):
    sum2 = sum2 ^ arr[i]
for i in range(1,len(arr)+3):
    sum2 = sum2 ^ i

mask = sum2 & (~(sum2-1))


sum_1 = 0
for i in range(len(arr)):
    if (arr[i] & mask):
        sum_1 = sum_1 ^ arr[i]
for i in range(1,len(arr)+3):
    if (i & mask):
        sum_1 = sum_1 ^ i
print(sum_1)

sum_1 = 0
for i in range(len(arr)):
    if not(arr[i] & mask):
        sum_1 = sum_1 ^ arr[i]
for i in range(1,len(arr)+3):
    if not(i & mask):
        sum_1 = sum_1 ^ i
print(sum_1)
