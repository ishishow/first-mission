import sys


def loadByPath(file_path):
    try:
        f = open(file_path, 'r', encoding='UTF-8')
    except:
        print(file_path)
        print("!!! FileNotFoundError !!!")
        sys.exit("Error")
    drive_log = f.read().split("\n")
    f.close()
    return drive_log

