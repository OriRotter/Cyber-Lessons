import re

MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-','/':' '}
def fileCheck(file):
    with open(file,'r') as f:
        data = f.read().replace('\n','')
    f.close()
    pattern = r'^[-./ ]*$'
    match = re.match(pattern, data)
    if not match:
        print("Error in Morse Code")
        return

    for word in data.split(' '):
        if len(word) > 6:
            print("Error in Morse Code")
            return
    return data

def countSymbols(message):
    count = {}
    for symbol in message.split(' '):
        message = message.replace(symbol,MORSE_CODE_DICT[symbol],1)
        if MORSE_CODE_DICT[symbol] != ' ':
            if MORSE_CODE_DICT[symbol] not in count:
                count[MORSE_CODE_DICT[symbol]] = 1
            else:
                count[MORSE_CODE_DICT[symbol]] += 1
    count = dict(sorted(count.items()))
    return message,count

def main():
    # file = input("Enter file name: ")
    # data = fileCheck(f"D:\Desktops\Ori\data\{file}}")
    data = fileCheck("D:\Desktops\Ori\data\\morse2.txt")
    if(data != None):
        data, count = countSymbols(data)
        print(data)
        print(count)



if __name__ == '__main__':
    main()