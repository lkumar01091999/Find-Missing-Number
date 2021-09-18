#author : Lokesh Kumar
import random

def missingNumber(mainList):
    length = len(mainList)

    logic = ((length+1)*(length+2))//2

    listSum = sum(mainList)

    result = logic - listSum

    return result

if __name__ == '__main__':
    mainList =[];

    for i in range(100):
        mainList.append(i+1)

    print(f"Sorted List - {mainList}\n")
    random.shuffle(mainList)
    print(f"Original Shuffled List - {mainList}\n")
    mainList.pop()
    
    print(f"Shuffled List with a missing number - {mainList}\n")

    print(f'missing Number = {missingNumber(mainList)}')





    




