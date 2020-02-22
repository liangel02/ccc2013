def year(start):
    for a in range(len(start)):
        for b in range(a+1, len(start)):
            if start[a] == start[b]:
                return True
    return False


startingYear = int(input())

nextYear = startingYear + 1
startList = list(map(int, str(nextYear)))

while True:
    result = year(startList)
    if result is False:
        break
    nextYear = nextYear + 1
    startList = list(map(int, str(nextYear)))
print("".join(map(str, startList)))



