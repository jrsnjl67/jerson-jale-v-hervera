
gas = True
while gas == True:
    q = bool(input("Still pricy?"))
    if q == True:
        print("Loop activated.")
        continue
    else:
        print("Loop ended.")
        break