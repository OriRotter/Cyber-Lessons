def factorial(num):
    if num <= 0:
        return 1
    return num * factorial(num - 1)


def readMaze(filename):
    with open(f"Data/ex4/{filename}", 'r') as f:
        mazeF = f.readlines()
    maze = []
    for line in mazeF:
        maze.append(list(line.replace('\n', '')))

    return maze


def findStart(maze):
    for y, line in enumerate(maze):
        if line[0] == '1':
            return 0, y


def solveMaze(filename="maze.txt"):
    maze = readMaze(filename)
    try:
        x, y = findStart(maze)
        printMaze(maze)
        solve = solver(y, x, maze)
        try:
            printMaze(solve)
        except TypeError:
            print("Can not be solved.")
    except TypeError:
        print("Can not be solved. no exit or entrance.")


def printMaze(maze):
    mazeT = ""
    for line in maze:
        for char in line:
            mazeT += char
        mazeT = mazeT.replace('0', '⬛')
        mazeT = mazeT.replace('1', '⬜')
        mazeT = mazeT.replace('2', '🔳')
        mazeT = mazeT.replace('3', '⬜')
        mazeT += "\n"
    print(mazeT)


def solver(y, x, maze):
    if (y == len(maze) - 1 and maze[y][x] == '1') or (x == len(maze[0]) - 1 and maze[y][x] == '1'):
        maze[y][x] = '2'
        print("Solved.")
        return maze
    if maze[y][x] != '0' and maze[y][x] != '2' and maze[y][x] != '3':
        maze[y][x] = '2'

        r = solver(y, x + 1, maze)
        if r is not None:
            return r
        r = solver(y + 1, x, maze)
        if r is not None:
            return r
        r = solver(y - 1, x, maze)
        if r is not None:
            return r
        r = solver(y, x - 1, maze)
        if r is not None:
            return r
        maze[y][x] = '3'


def main():
    choice = input("Enter 1 to calculate factorial enter 2 to solve a maze (enter -1 to exit): ")
    if choice == '1':
        try:
            num = int(input("enter a num to calculate: "))
            print(factorial(num))
        except ValueError:
            print("Error enter a valid int")

    elif choice == '2':
        filename = input("Enter filename to solve the maze (press enter to solve the default): ")
        if len(filename) == 0:
            solveMaze()
        else:
            solveMaze(filename)
    elif choice == '-1':
        print("Bye bye!")


if __name__ == '__main__':
    main()
