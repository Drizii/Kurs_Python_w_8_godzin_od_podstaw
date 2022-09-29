
for v in [1,2,3,4]:
    print(v * 2)

for v in ("Ania", "Ola", "Rafal"):
    print(v)

for el in {3,4,5,6,"Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("petla zakonczona")

dicData = {"Ania": "ania@example.com", "Adam": "adam@example.com"}

for key in dicData:
    print(key)

for key in dicData.keys():
    print(key)

for key in dicData.keys():
    print(dicData[key])

for key, value in dicData.items():
    print(key, " : ", value)

for v in dicData.values():
    print(v)