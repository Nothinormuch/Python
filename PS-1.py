def solution(varDistance):
    banana=[3000,0]
    maxCap=1000
    totalDistance=1000
    trip=0
    while (totalDistance>0):
        isinstance=0
        while (banana[trip]>0):
            print(banana)
            if (banana[trip]>maxCap):
                banana[trip+1]+=maxCap-(2*varDistance)
                banana[trip]-=maxCap
            elif (banana[trip]<=maxCap and isinstance==0):
                banana[trip+1]+=banana[trip]-(maxCap-(trip*varDistance))
                banana[trip]=0
                if banana[-1]>=0:
                    return banana
                else:
                    return None
            else:
                banana[trip+1]+=banana[trip]-varDistance
                banana[trip]=0
            isinstance+=1
        banana.append(0)
        totalDistance-=varDistance
        trip+=1

for i in range(1,2):
    result=solution(i)
    if (result and (result[-1]>500)):
        print("The result is {} for the varDistance of {}!".format(result[-1],i))
