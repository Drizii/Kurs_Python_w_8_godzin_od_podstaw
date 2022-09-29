
print("Hello " + "World!")
print("Hello" * 3)

string = "Hello World!"
print( string[0])  # H
print( string[0:5])  # Hello

print("Hello" in string)  # True
print("Hello" not in string)  # False

multiline = """line1
line2
line3
"""

print("ala".capitalize())
print("Ola ma kota, Ola ma psa.".count("ola"))

print("Hello".center(20, "-"))

print(string.startswith("Hello"))
print(string.endswith("World!"))

print(string.find("Ola"))
print(string.find("World"))
print("Ola ma psa, Ola ma kota".rfind("Ola"))  # 12

print("2342345234".isalnum())
print("2342345234.".isalnum())
print("2342345234 k".isalnum())

print("2342345234 k".isalpha())
print("kot".isalpha())  # True
print("kot2".isalpha())  # False bo 2
print(" kot2".isalpha())  # False bo spacja

print("test".islower())
print("tesT".islower())
print("TEST".islower())

print("TEST".isspace())  # False
print("\n\n\n\t        ".isspace())

print("-|".join(["Ala", "Ola", "Adam"]))

print("Hello World". lower())
print("Hello World". upper())
print("Hello World". swapcase())

print("\n\n\n\t    Hello World again   \n\n\n\t ".lstrip())
print("\n\n\n\t    Hello World again   \n\n\n\t ".rstrip())
print("\n\n\n\t    Hello World    again   \n\n\n\t ".strip())

print("Ola ma psa. Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}. I'm from {country}".format(myName="Wojtek", country="Poland"))
print("My name is {myName}. My postal code is {code}".format(myName="Wojtek", code=12456))
print("My name is {0}. I'm from {1}".format("Wojtek","Poland"))
print("My name is {}. I'm from {}".format("Wojtek","Poland"))
