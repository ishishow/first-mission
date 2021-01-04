def loadByPath(file_path):
    f = open(file_path, 'r', encoding='UTF-8')
    drive_log = f.read().split("\n")
    f.close()
    return drive_log
