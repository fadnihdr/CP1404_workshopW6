import random

pickList = []
randomNum = random.randint(1,46)
userInput = int((input("How many picks:")))
while True:
    for i in range(userInput):
        pickList.append(randomNum)
        if randomNum not in pickList:
            continue
        else:
            pickList.append(randomNum)
            break

print("{:2d}, {:2d}, {:2d}, {:2d}, {:2d}, {:2d}".format(pickList[0]),(pickList[1]),(pickList[2]),(pickList[3]),
      (pickList[4]),(pickList[5]))
