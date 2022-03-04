import math
def solution(progresses, speeds):
    answer = []
    count, i = 0, 0
    while i < len(progresses) :
        
        days = math.ceil((100 - progresses[i]) / speeds[i])
        count, b = 1, False
        i += 1
        j = i
        for s in speeds[i:] :
            progresses[j] += s*days
            if b == False and progresses[j] >= 100 :
                i += 1
                count += 1
            elif progresses[j] < 100 :
                b = True
            j += 1
        answer.append(count)
        count = 0
    return answer