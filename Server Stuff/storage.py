filename = "demo.txt"


def getTest():
    testArray = []
    with open(filename) as file:
        for line in file:
            testArray.append({"action": line.rstrip("\n\r")})
    return testArray


def addTest(action):
    with open(filename, "a") as file:
        file.write(action + "\n")