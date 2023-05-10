def main():
    try:
        while True:
            choice = int(input("Enter 1 to deserialize, enter 2 to serialize (enter -1 to exit): "))
            if choice == -1:
                print("bye bye!")
                return
            elif choice == 1:
                deserialize()
            elif choice == 2:
                serialize()
    except:
        print("<=ERROR=> Enter a valid number.")
        main()

def deserialize():
    try:
        file = input("Enter the file name to deserialize: ")
        fileName = input("Enter the new file name after serialize: ")
        with open(f"Data/ex3/output/{fileName}.txt", 'w') as finale:
            with open(f"Data/ex3/{file}.txt", 'r') as start:
                for line in start:
                    finale.write(listsToText(formatTextToLists(line.replace('\n','')))+"\n")

    except:
        print("<=ERROR=> file name was wrong or file was corrupted.")

def serialize():
    try:
        file = input("Enter the file name to serialize: ")
        fileName = input("Enter the new file name after serialize: ")
        with open(f"Data/ex3/output/{fileName}.txt",'w') as finale:
            with open(f"Data/ex3/{file}.txt", 'r') as start:
                for line in start:
                    formatLine = listsToFormatText(stringToLists(line.rstrip()))+"\n"
                    finale.write(formatLine)
    except:
        print("<=ERROR=> file name was wrong or file was corrupted.")


def stringToLists(string):
    Lists = []
    save = None
    count = -1
    for char in string:
        if char == save:
            Lists[count][1] = Lists[count][1]+1
        else:
            count += 1
            save = char
            Lists.append([char,1])
    return Lists

def listsToFormatText(Lists):
    string = ""
    for line in Lists:
        string += str(line[1])+line[0]
    return string

def getList(text):
    for pos,char in enumerate(text):
        if not char.isdigit():
            list = ([char,int(text[:pos])])
            text = text[pos+1:]
            return list,text


def formatTextToLists(text):
    lists = []
    while len(text) != 0:
        list, text = getList(text)
        lists.append(list)
    return lists

def listsToText(Lists):
    line = ""
    for char in Lists:
        for i in range(char[1]):
            line += char[0]
    return line


if __name__ == '__main__':
    main()