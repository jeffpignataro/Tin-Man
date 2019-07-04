import sys


def decryptTinMan(numbers):
    return charToNum(numbers)


def charToNum(number):
    return chr(int(number) + 96)

    # 505091 02411030 02108002 9121515160 5021209021211270 508002 815160 9190 0291819060 508002
    # The first one is for the gullible fools that cant see


decryptedText = ""
for i in sys.argv:
    if(i != sys.argv[0]):
        numbersString = i
        numbersStringArray = numbersString[::-1].split(' ')
        for numberWord in numbersStringArray:
            numBuilder = ''
            for num in numberWord:
                numBuilder += num
                if(len(numBuilder) == 2):
                    decryptedText += decryptTinMan(numBuilder)
                    numBuilder = ''
            decryptedText += ' '
for word in decryptedText.split(' ')[::-1]:
    print(word, end=' ')
