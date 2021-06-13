def main_menu():
    comb_name = input("Which combustible are you trying to use?\n").strip()
    print("I'll need its chemical composition in %. Make sure they add up to 100.")
    index = {
        "Carbon": 0,
        "Hydrogen": 1,
        "Oxygen": 2,
        "Nitrogen": 3,
        "Sulphur": 4,
        "Moisture": 5,
        "Ashes": 6
    }
    properties = []
    try:
        for i in index:
            property = float(input(f"{i} %: ").strip())
            properties.append(property)
        print(properties)
        n = float(input("Dilution factor n = "))
        T = float(input("Temperature for mean specific heat (in K) T = "))
    except ValueError:
        print("One of the entries you gave wasn't a float number.")
    else:
        return [[comb_name.title(), properties], T, n]


