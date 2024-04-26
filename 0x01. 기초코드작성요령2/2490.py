for i in range(3):
    T = list(map(int, input().split()))
    Z = T.count(0)
    if (Z == 1):
        print("A")
    elif (Z == 2):
        print("B")
    elif (Z == 3):
        print("C")
    elif (Z == 4):
        print("D")
    else:
        print("E")
