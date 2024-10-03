#Just a testing file

print("Time?")

for i in range(5):
    for j in range(i):
        print(end="-")
    for j in range(14-i):
        if i==j:
            print(end="*")
        else: print(end="-")
    for j in range(14-i):
        if False:
            print("hey")
    print()

