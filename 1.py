n = int(input())            # count of grades
grades = input().split(' ') # string with grades

maxFive = -1        # max count of 5
countFive = 0       # current count of 5
lenFive = 0         # len result
curIndex = 0        # index of first element in current sublist

for i in range(len(grades)):
    
    grade = grades[i]
    
    if(grade == '2' or grade == '3'):
        # reset counters
        countFive = 0
        lenFive = 0

    elif(grade == '4' or grade == '5'):
        if(lenFive == 0):
            lenFive += 1
            curIndex = i
            if(grade == '5'): countFive += 1
        
        elif(lenFive < 7):
            # increase len counter and five counter, if necessary, then continue
            lenFive += 1
            if(grade == '5'): countFive += 1
            
        elif(lenFive == 7): 
            # update maxFive and shift the current sublist to the right
            maxFive = max(maxFive, countFive)
            # if fisrt element in current sublist is 5, decrease count of 5 (because of shift)
            if(grades[curIndex] == '5'): countFive -= 1
            # shift
            curIndex += 1
            # increase five counter
            if(grade == '5'): countFive += 1
            
if(lenFive == 7): maxFive = max(maxFive, countFive)
print(maxFive)
        
