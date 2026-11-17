#jeep
route = ["Terminal", "Perez park", "Pacific mall"]
passengers= []
seats = 6
fare = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of" , seats , "seats")
    print("1 sakay | 2 priority seat 3 | para po!")
    print("4 baba sa pinto | 5 baba sa harap")
    print("6 seat check | 7 balikan | 8 exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == seats:
            print("PUNO NA PO!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "sakay sa likod")

    elif choice == "2":
        if len(passengers) == seats:
            print("PUNO NA PO!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + fare
            print(name, "sakay sa priority seat")

    if choice == "3":
        name = input("sino po ans bababa?: ")

        if name in passengers:
            passengers.remove(name)
            print(name, "INGAT PO!")

        else:
            print(name, "Nakaalis na")

    elif choice == "4":
        if len(passengers) == 0:
            print("Jeep is empty")
        else:
            left = passengers.pop()
            print(left, "Dumaan sa pinto")   

    elif choice == "5":
        if len(passengers) == 0:
            print("Jeep is empty")
        else:
            left = passengers.pop()
            print(left, "dumaan sa harap") 

    elif choice == "6":
        for  i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route", route)

    elif choice == "8":
        print("Total fare today:", total)
        break
    else:
        print("invalid choice.")