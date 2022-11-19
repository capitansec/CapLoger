def counterArray(fullList: list, uniqueList: list):
    for i in uniqueList:
        print(f"Source: {i} => times: {fullList.count(i)}")