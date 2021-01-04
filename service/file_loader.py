def fileLoader(file_path):
    f = open(file_path, 'r', encoding='UTF-8')
    data = f.read().split("\n")
    f.close()
    return data
