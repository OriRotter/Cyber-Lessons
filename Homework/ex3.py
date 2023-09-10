def listFiller(lists):
    longest_string = len(max(lists, key=len))
    for place,line in enumerate(lists):
        for i in range(longest_string-len(line)):
            line += " "
        lists[place] = line
    return lists

def readConversion():
    table = []
    with open("Data/ex3/conversion.txt",'r') as f:
        table.append(list(f.readline().replace('\n','')))
        table.append(list(f.readline().replace('\n','')))
        table.append(list(f.readline().replace('\n','')))
    return table

def serialize(filename,degree,conversion):
    fileData = fileToLists(filename)
    fileData = con(fileData,conversion)
    dataSerFill = listFiller(fileData)
    fileData = rotator(degree,dataSerFill)
    dataSer = listsSerializer(fileData)
    dataString = ""
    for line in dataSer:
        dataString += f"{line}\n"
    with open(f"Data/ex3/output/SE-{filename}", 'w') as f:
        f.write(dataString)
    f.close()
    print(f"Serialization complete. file save SE-{filename}.")

def con(image,conversion):
    if conversion == 0:
        return image
    accept = []
    tableCon = readConversion()
    for place,line in enumerate(image):
        for i in range(3):
            line = line.replace(tableCon[i][0],tableCon[i][conversion])
            accept.append(tableCon[i][conversion])
        image[place] = line
    for place, line in enumerate(image):
        image[place] = ''.join(['x' if c not in accept else c for c in line])
    return image


def fileToLists(filename):
    try:
        with open(f"data/ex3/{filename}", 'r', encoding="utf-8") as f:
            data = f.readlines()
        f.close()
        for place, line in enumerate(data):
            data[place] = line.replace('\n', '')
        return data
    except FileNotFoundError:
        print("<=ERROR=> Can't find file.")


def listsSerializer(lists):
    listSer = []
    for line in lists:
        listSer.append(lineSer(line))
    return listSer


def lineSer(line):
    lineSer = ""
    try:
        save = line[0]
    except IndexError:
        save = ''
    count = 0
    for place, char in enumerate(line):
        if char == save:
            count += 1
        else:
            lineSer += f"{count}{save}"
            save = char
            count = 1
    lineSer += f"{count}{save}"
    return lineSer


def deserialize(filename,degree,conversion):
    fileData = fileToLists(filename)
    fileDes = listsDeserializer(fileData)
    fileDes = con(fileDes,conversion)
    fileDesFill = listFiller(fileDes)
    fileDesFillRotated = rotator(degree,fileDesFill)
    text = ""
    for line in fileDesFillRotated:
        for char in line:
            text += char
        text += "\n"
    print(text)
    with open(f"Data/ex3/output/DE-{filename}", 'w') as f:
        f.write(text)
    f.close()
    print(f"Deserialization complete. file save DE-{filename}.")


def listsDeserializer(lists):
    image = []
    for line in lists:
        count = 0
        text = ""
        for char in line:
            if char.isdigit():
                count = (count * 10) + int(char)
            else:
                for i in range(count):
                    text += char
                count = 0
        image.append(text)
    return image

def rotator(degree,image):
    if degree == 0:
        return image
    if degree == 360:
        for place,line in enumerate(image):
            image[place] = line[::-1]
        return image
    degree -= 90
    rotated = list(reversed(list(zip(*image))))
    return rotated

def main():
    try:
        while True:
            choice = int(input("Enter 1 to serialize a file. Enter 2 to deserialize a file (enter -1 to exit): "))
            if choice == 1:
                filename = input("Enter the file name you want to serialize: ")
                degree = int(input("Enter the degree you want to rotate the image: "))
                conversion = int(input("Enter if to do conversion (0/1/2): "))
                if degree%90 != 0 or conversion <= -1 or conversion >= 3:
                    raise ValueError
                serialize(filename,degree,conversion)
            elif choice == 2:
                filename = input("Enter the file name you want to deserialize: ")
                degree = int(input("Enter the degree you want to rotate the image: "))
                conversion = int(input("Enter if to do conversion (0/1/2): "))
                if degree%90 != 0 or conversion <= -1 or conversion >= 3:
                    raise ValueError
                deserialize(filename,degree,conversion)
            elif choice == -1:
                print("Bye bye!")
                break

    except (TypeError,ValueError):
        print("<=ERROR=> Please enter a valid input.")
        main()


if __name__ == '__main__':
    main()
