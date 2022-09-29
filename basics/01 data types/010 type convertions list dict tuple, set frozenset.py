

listData = [1, 2, 3, 4]

tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 234))

setData = set(otherList)
print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Ola", 12312), ("Adam", 1233123))

dictData = dict(tupleData)
print(dictData)
print(dictData["Ola"])
