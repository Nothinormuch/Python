n = [10,9,8,6,5,4,3,2,1]

l = len(n)

for i in range(1,l):
    key = n[i]
    j = i-1
    while(j>=0 and key<n[j]):
        n[j+1]=n[j]
        j-=1
    else:
        n[j+1]=key

print(n)

