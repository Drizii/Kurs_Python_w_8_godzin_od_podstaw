# immutable: int, float, bool, str, frozenset

def modifyStr(strData):
    print(id(strData))
    strData += "!"
    print(id(strData))
    print(strData)


string = "Hello"
print(id(string))
modifyStr(string)
print(string)


# mutable: list, str, dict

def modifyList(listData):
    print(id(listData))
    listData = [1,2,3,4,5,6]
    listData.append(10)
    print(id(listData))


listValue = [0,1,2,3]
print(id(listValue))

modifyList(listValue)