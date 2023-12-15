dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

print(dictionary["Hotel"])
def addItem(key, value):
    dictionary[key] = value

addItem("Blau", "Weiß")
print(dictionary["Blau"])