totalWeight = int(input())
cars = int(input())

weightList = []
num = 0

for i in range(cars):
    weight = int(input())
    weightList.append(weight)

for i in range(len(weightList)):
    if i == 0:
        if weightList[i] > totalWeight:
            break
        else:
            weightOfOne = weightList[i]
            num = i + 1
    elif i == 1:
        weightOfTwo = sum(weightList[i-1:i+1])
        if weightOfTwo <= totalWeight:
            num = i + 1
        else:
            break
    elif i == 2:
        weightOfThree = sum(weightList[i-2:i+1])
        if weightOfThree <= totalWeight:
            num = i + 1
        else:
            break
    elif i >= 3:
        weightOfFour = sum(weightList[i-3:i+1])
        if weightOfFour <= totalWeight:
            num = i + 1
        else:
            break

print(num)
