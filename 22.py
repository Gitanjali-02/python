
def count_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    return len(lines)


print("Total lines:", count_lines("data.txt"))
