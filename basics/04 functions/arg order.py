# / - to co przed tym znakiem musi zostać podane bez nazwy
# * - to co po tym znaku musi byc podane z nazwą

def printCar(brand, /, name="concept", *, year=1960, color="black"):
    print(brand, name, year, color)


printCar("Ford", "Mustang", color="blue", year=1973)
