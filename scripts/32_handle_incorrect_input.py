def ask():
    try:
        a = int(input("Enter integer "))
        return a
    except:
        print("Enter Integer only")

while True:
    z = ask()
    print(z)