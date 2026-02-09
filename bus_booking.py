# Bus booking system
import random


bus1 = "101A"
bus1dest = "New York"
bus1seats = 40
bus1booked = 0
bus1fare = 15.00

bus2 = "202B"
bus2dest = "Los Angeles"
bus2seats = 50
bus2booked = 0
bus2fare = 20.00

bus3 = "303C"
bus3dest = "Chicago"
bus3seats = 30
bus3booked = 0
bus3fare = 18.00

bus4 = "404D"
bus4dest = "Miami"
bus4seats = 45
bus4booked = 0
bus4fare = 22.00

bookings_ids= []
bookings_bus = []

try:
    file = open("bookings.txt", "r")
    for line in file:
        data = line.strip().split(",")
        bookings_ids.append(int(data[0]))
        bookings_bus.append(data[1])

        if data[1] == bus1:
            bus1booked += 1
        elif data[1] == bus2:
            bus2booked += 1
        elif data[1] == bus3:
            bus3booked += 1
        elif data[1] == bus4:
            bus4booked += 1
    file.close()
except:
    pass

while True:
    print("\n")
    print("--- Bus Booking System ---")
    Menu= print(" 1. View available buses\n 2. Book a seat\n 3. Cancel a booking\n 4. Exit ")
    Menu_choice= input("Enter your choice (1-4): ")



    if Menu_choice == "1":

        bus1available = bus1seats - bus1booked
        bus2available = bus2seats - bus2booked
        bus3available = bus3seats - bus3booked
        bus4available = bus4seats - bus4booked

        if bus1available > 0:
            print(f"Bus {bus1} to {bus1dest} has {bus1available} seats at ${bus1fare}")
        else:
            print(f"Bus {bus1} to {bus1dest} is fully booked")

        if bus2available > 0:
            print(f"Bus {bus2} to {bus2dest} has {bus2available} seats at ${bus2fare}")
        else:
            print(f"Bus {bus2} to {bus2dest} is fully booked")

        if bus3available > 0:
            print(f"Bus {bus3} to {bus3dest} has {bus3available} seats at ${bus3fare}")
        else:
            print(f"Bus {bus3} to {bus3dest} is fully booked")

        if bus4available > 0:
            print(f"Bus {bus4} to {bus4dest} has {bus4available} seats at ${bus4fare}")
        else:
            print(f"Bus {bus4} to {bus4dest} is fully booked")


    elif Menu_choice == "2":
        Costumer_name= input("Enter your name: ")
        Bus_choice= input("Enter the bus number you want to book (101A, 202B, 303C, 404D): ")


        booking_id= random.randint(1000, 9999)
        while booking_id in bookings_ids:
            booking_id= random.randint(1000, 9999)
        bookings_ids.append(booking_id)

        if Bus_choice == bus1:
            bus1available = bus1seats - bus1booked
            if bus1available > 0:
                bus1booked += 1
                bus1available -= 1
                print(f"Booking confirmed for {Costumer_name} on bus {bus1} to {bus1dest}. And your booking ID is {booking_id}.")
                bookings_bus.append(bus1)
            else:
                print(f"Sorry, bus {bus1} is fully booked.")
        elif Bus_choice == bus2:
            bus2available = bus2seats - bus2booked
            if bus2available > 0:
                bus2booked += 1
                bus2available -= 1
                print(f"Booking confirmed for {Costumer_name} on bus {bus2} to {bus2dest}. And your booking ID is {booking_id}.")
                bookings_bus.append(bus2)
            else:
                print(f"Sorry, bus {bus2} is fully booked.")   
        elif Bus_choice == bus3:
            bus3available = bus3seats - bus3booked
            if bus3available > 0:
                bus3booked += 1
                bus3available -= 1
                print(f"Booking confirmed for {Costumer_name} on bus {bus3} to {bus3dest}. And your booking ID is {booking_id}.")
                bookings_bus.append(bus3)
            else:
                print(f"Sorry, bus {bus3} is fully booked.")
        elif Bus_choice == bus4:
            bus4available = bus4seats - bus4booked
            if bus4available > 0:
                bus4booked += 1
                bus4available -= 1
                print(f"Booking confirmed for {Costumer_name} on bus {bus4} to {bus4dest}. And your booking ID is {booking_id}.")
                bookings_bus.append(bus4)
            else:
                print(f"Sorry, bus {bus4} is fully booked.")
        else:
            print("Invalid bus number selected.")

        file = open("bookings.txt", "a")
        file.write(str(booking_id) + "," + Bus_choice + "\n")
        file.close()

    elif Menu_choice == "3":
        Cancel_id= int(input("Enter your booking ID to cancel: "))
        if Cancel_id in bookings_ids:
            index = bookings_ids.index(Cancel_id)
            bus = bookings_bus[index]

            if bus == bus1:
                bus1booked -= 1
            elif bus == bus2:
                bus2booked -= 1
            elif bus == bus3:
                bus3booked -= 1
            elif bus == bus4:
                bus4booked -= 1

            bookings_ids.pop(index)
            bookings_bus.pop(index)
            file = open("bookings.txt", "w")
            for i in range(len(bookings_ids)):
                file.write(str(bookings_ids[i]) + "," + bookings_bus[i] + "\n")
            file.close()
            print(f"Booking with ID {Cancel_id} has been cancelled.")
        else:
            print("Invalid booking ID.")
    elif Menu_choice == "4":
        print("Thank you for using the Bus Booking System")
        break
    else:
        print("Invalid menu choice")