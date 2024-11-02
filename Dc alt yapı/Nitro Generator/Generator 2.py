import random
import string

print("  ____    _                                   _                ____               _               ")
print(" |  _ \  (_)  ___    ___    ___    _ __    __| |              / ___|   ___     __| |   ___   _ __ ")
print(" | | | | | | / __|  / __|  / _ \  | '__|  / _` |    _____    | |      / _ \   / _` |  / _ \ | '__|")
print(" | |_| | | | \__ \ | (__  | (_) | | |    | (_| |   |_____|   | |___  | (_) | | (_| | |  __/ | |   ")
print(" |____/  |_| |___/  \___|  \___/  |_|     \__,_|              \____|  \___/   \__,_|  \___| |_|   ")
print("                                                                                                  ")
print("                                                                                                  ")
print("                                                                              -==[ BY SHURIJO ]==-")
print("                                                                                                  ")
print("                                                                                                  ")

amount = input("How many codes should be generated?: ")
amount = int(amount)
index = 0


def gen(index, amount):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    print (code)
    index = index +1
    return code

while index < amount:
    f = open("CodesS.txt", "a")
    f.write(gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n" + gen(index, amount) + "\n")