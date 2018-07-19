def gather_details():
    lnt = int(input("Enter length"))
    brt = int(input("enter breadth"))
    return (lnt, brt)
    

def compute(lnth, brth):
    area = lnth*brth
    return area    


while True:
    ln, br = gather_details()
    area = compute(ln, br)
    print(f"area is {area}")