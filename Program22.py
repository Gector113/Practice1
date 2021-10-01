objects = input("Напишіть текст з пробілами: ").split(" ")
if len(objects) == 1:
    print("".join(objects))
elif len(objects) == 2:
    print(" and ".join(objects))
elif len(objects) > 2:
    print(", ".join(objects[0: -1]) + ", and " + "".join(objects[-1]))