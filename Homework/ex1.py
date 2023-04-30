

def stringHexToNumPrint(numS):
    try:
        print(int(numS,16))
    except(ValueError):
        print("<ERROR> invalid hex number.")


def sentenceHexToNum(numS,base):
    for i in numS:
        try:
            int(i,base)
        except(ValueError):
            numS = numS.replace(i,'z')
    numS = numS.split('z')


    sum = 0
    for i in numS:
        try:
            sum += int(i,base)
        except(ValueError):
            pass
    return sum


stringHexToNumPrint("11")
stringHexToNumPrint("0xa")
stringHexToNumPrint("10dz")

print(sentenceHexToNum("ABRAKADABRA",16))
print(sentenceHexToNum("10g10fke",2))
print(sentenceHexToNum("10g10fke",8))
print(sentenceHexToNum("10g10fke",16))

numbers = []
while True:
    try:
        numbers.append(int(input("Enter a digit: "),16))
    except(ValueError):
        sum = 0
        for num in numbers:
            sum += num
        print(sum)
        break

