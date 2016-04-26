numberList = []
for i in range(5):
    userInput = int(input('Numbers:'))
    numberList.append(userInput)
print("First number: {}".format(numberList[0]))
print("Last number: {}".format(numberList[-1]))
print("Smallest number: {}".format(min(numberList)))
print("Largest number: {}".format(max(numberList)))
print("Average number: {}".format(sum(numberList)/len(numberList)))
