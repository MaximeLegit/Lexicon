## Lesson 4

# Part 1


flights = [
    {"flight_number": "SK142", "destination": "London", "departure_time": "14:30",
     "gate": "B4", "passengers": 132, "capacity": 180, "delay": 25, "cancelled": False},

    {"flight_number": "SK143", "destination": "Riga", "departure_time": "15:00",
     "gate": "A2", "passengers": 150, "capacity": 160, "delay": 0, "cancelled": False},

    {"flight_number": "SK144", "destination": "Stockholm", "departure_time": "15:20",
     "gate": "C1", "passengers": 90, "capacity": 150, "delay": 0, "cancelled": True},

    {"flight_number": "SK145", "destination": "Paris", "departure_time": "15:45",
     "gate": None, "passengers": 110, "capacity": 140, "delay": 10, "cancelled": False},

    {"flight_number": "SK146", "destination": "Amsterdam", "departure_time": "16:00",
     "gate": "A1", "passengers": 0, "capacity": 120, "delay": 0, "cancelled": False},

    {"flight_number": "SK147", "destination": "Madrid", "departure_time": "16:20",
     "gate": "B2", "passengers": 176, "capacity": 180, "delay": 65, "cancelled": False},

    {"flight_number": "SK148", "destination": "Zurich", "departure_time": "16:40",
     "gate": "C3", "passengers": 60, "capacity": 100, "delay": 5, "cancelled": False},

    {"flight_number": "SK149", "destination": "Riga", "departure_time": "17:00",
     "gate": "A4", "passengers": 45, "capacity": 90, "delay": 0, "cancelled": False},

    {"flight_number": "SK150", "destination": "Helsinki", "departure_time": "17:15",
     "gate": "B1", "passengers": 130, "capacity": 150, "delay": 40, "cancelled": False},

    {"flight_number": "SK151", "destination": "Lulea", "departure_time": "17:30",
     "gate": "C4", "passengers": 88, "capacity": 100, "delay": 0, "cancelled": False},
]


# Part 3

def get_flight_status(flight):
    if flight["cancelled"]:
        return "CANCELLED"
    elif flight["delay"] >= 60:
        return "Severly Delayed"
    elif flight["delay"] >= 20:
        return "Delayed"
    elif flight["delay"] >= 1:
        return "Slight Delay"
    else:
        return "On Time"

# Part 2

def departure_board():
    print("\nDEPARTURE BOARD")
    for index, flight in enumerate(flights):
        status = get_flight_status(flight)
        gate = flight["gate"] 
        if flight["gate"] == "None":
            print("\nGate not assigned")
            
        print(f"{index}. {flight["flight_number"]} - {flight["destination"]} - "
              f"{flight["departure_time"]} - {gate} - {status}")

#departure_board()

# Part 4

def analyse_flights():
    total_scheduled = len(flights)
    cancelled_flights = 0
    delayed_flights = 0
    on_time_flights = 0
    total_passengers = 0
    avg_number_of_passengers = 0
    total_flights = 0
    current_highest_passenger_count = flights[0]["passengers"]
    flight_with_largest_passengers = None
    #print("\nShow init:",flight_with_largest_passengers)
    busiest_flight = ""
    above_80_percent = []
 
    for flight in flights:
        if flight["cancelled"]:
            cancelled_flights += 1
            continue
 
        if flight["delay"] > 0:
            delayed_flights += 1
        else:
            on_time_flights += 1
 
        total_passengers += flight["passengers"]
 
        # Flights with 0 passengers should not be included in the average
        if flight["passengers"] > 0:
            avg_number_of_passengers += flight["passengers"]
            total_flights += 1
            if current_highest_passenger_count < flight["passengers"]:
                current_highest_passenger_count = flight["passengers"]
                flight_with_largest_passengers = flight["flight_number"]
                busiest_flight = f"{flight['flight_number']} - {flight['destination']} - {flight['passengers']} passengers"
 
        if flight["capacity"] > 0 and (flight["passengers"] / flight["capacity"]) > 0.8:
            above_80_percent.append(flight)

    average_passengers =  avg_number_of_passengers / total_flights

    print(
        "\nTotal flights scheduled", total_scheduled,
        "\nTotal flights cancelled", cancelled_flights,
        "\nTotal flights delayed", delayed_flights,
        "\nTotal flights on_time", on_time_flights,
        "\nTotal_passengers", total_passengers,
        "\nAverage_passengers per flight", average_passengers,
        "\nBusiest_flight", busiest_flight,
        "\nFlight with highest passenger count", flight_with_largest_passengers,
        "\nFlights above_80_percent", above_80_percent,
    )
    return {
        "total_scheduled": total_scheduled,
        "cancelled_flights": cancelled_flights,
        "delayed_flights": delayed_flights,
        "on_time_flights": on_time_flights,
        "total_passengers": total_passengers,
        "average_passengers": average_passengers,
        "busiest_flight": busiest_flight,
        "above_80_percent": above_80_percent,
    }

# Part 5

def search_flight():
    flight_number = input("\nEnter flight number: ").strip().upper()
    gate = None 
    for flight in flights:
        if flight["flight_number"] == flight_number:
            status = get_flight_status(flight) 
            if (flight["gate"] != None):
                gate = flight["gate"] 
            else:
                gate = "Gate not assigned"

            print("\nDestination:", flight["destination"], "Departure:", flight["departure_time"],
            "Gate", gate, "Passengers:", flight["passengers"], "Status", status)
            break
    else:
        print("\nFlight not found.")

#search_flight()


# Part 7

def show_gate_overview():
    print("\nGate Ooverview")
    terminals = ["A", "B", "C"]
    for terminal in terminals:
        for gate_number in range(1, 5):
            print("Terminal:", terminal,"Gate:", gate_number)

#show_gate_overview()

# Part 8


def show_delayed_flights():
    print("\nDelayed Flights:")
    for flight in flights:
        status = get_flight_status(flight)
        if(flight["delay"] > 0):
            print("",flight["flight_number"], "-", flight["destination"], "-", status)

def show_cancelled_flights():
    print("\nCancelled Flights:")
    for flight in flights:
        if(flight["cancelled"]):
            print("",flight["flight_number"], "-", flight["destination"]) 


def menu():
    print("\nAIRPORT DEPARTURE SYSTEM")
    print("1. View all flights")
    print("2. View delayed flights")
    print("3. View cancelled flights")
    print("4. Search for a flight")
    print("5. View flight statistics")
    print("6. Quit")

    while True:
        choice = input("Choose an option: ").strip()
 
        if choice == "1":
            departure_board()
        elif choice == "2":
            show_delayed_flights()
        elif choice == "3":
            show_cancelled_flights()
        elif choice == "4":
            search_flight()
        elif choice == "5":
            analyse_flights()
        elif choice == "6":
            print("\nSayanara")
            break
        else:
            print("\nInvalid option. Please try again.")



def show_operations_report():
    parsed_flight_data = analyse_flights()

    print("\nAIRPORT OPERATIONS REPORT")
    print("Scheduled flights:", parsed_flight_data["total_scheduled"])
    print("Cancelled flights:", parsed_flight_data["cancelled_flights"])
    print("Delayed flights:", parsed_flight_data["delayed_flights"])
    print("On-time flights:", parsed_flight_data["on_time_flights"])
    print("\n\nPassengers today:", parsed_flight_data["total_passengers"])
    print("\nBusiest_flight\n", parsed_flight_data["busiest_flight"])
    print("\nFlights above_80_percent:")
    for flight in parsed_flight_data["above_80_percent"]:
        print(f"{flight['flight_number']} - {flight['destination']}")
 
    # Destination with most passengers
    unique_flight_destinations = set()
    for flight in flights:
        if not (flight["cancelled"]):
            unique_flight_destinations.add(flight["destination"])
 
    top_destination = None
    top_passenger_count = 0
    for destination in unique_flight_destinations:
        passenger_total = 0
        for flight in flights:
            if not (flight["cancelled"]):
                if flight["destination"] == destination:
                    passenger_total += flight["passengers"]

        if passenger_total > top_passenger_count:
            top_destination = destination
            top_passenger_count = passenger_total
 
    print("\nDestination with the most passengers:", top_destination, top_passenger_count)


if __name__ == '__main__':
    menu()
    show_operations_report()

"""
I think the show operations method is a bit wonky. I am not sure about the last operation, specifically this
extra part about destination with most passengers you asked to implemnt. So far, I use the set to grab unique
values, but then I have to loop thourgh the oriringal lips to see if there is a match, it feels a bit backwards,
but right now I am not certain how to fix it. Maybe there is a more ennhanced comparison.

All the code I wrote is the original code, based on what we studied and based on what I remember + googling.
I improved almost nothing, but I expect you may see an improvement here. I think there could be use for more
enhanced if statements, it has been a while since I used them. For now, this should work as you require.


"""