filename = "demo.txt"


def getTest():
    testArray = []
    with open(filename) as file:
        for line in file:
            testArray.append({"message": line.rstrip("\n\r")})
    return testArray


def addTest(message):
    with open(filename, "a") as file:
        file.write(message + "\n")