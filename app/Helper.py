# Helper file


def idGenerator(dataDict: dict):
    id = None
    if len(dataDict) == 0:
        id = 1
    else:
        lastID = max(int(key) for key in dataDict.keys())
        id = lastID + 1
    print(id)
    return id


if __name__ == "__main__":
    pass
