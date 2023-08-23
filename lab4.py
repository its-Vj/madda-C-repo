#publishing 
class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_for_city(self, city):
        city_flights = []
        for flight in self.flights:
            if flight.from_city == city or flight.to_city == city:
                city_flights.append(flight)
        return city_flights

    def get_flights_from_city(self, from_city):
        from_city_flights = []
        for flight in self.flights:
            if flight.from_city == from_city:
                from_city_flights.append(flight)
        return from_city_flights

    def get_flights_between_cities(self, from_city, to_city):
        between_cities_flights = []
        for flight in self.flights:
            if flight.from_city == from_city and flight.to_city == to_city:
                between_cities_flights.append(flight)
        return between_cities_flights

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        city_flights = flight_table.get_flights_for_city(city)
        for flight in city_flights:
            print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
    elif choice == 2:
        from_city = input("Enter the departure city: ")
        from_city_flights = flight_table.get_flights_from_city(from_city)
        for flight in from_city_flights:
            print(f"To: {flight.to_city}, Flight ID: {flight.flight_id}, Price: {flight.price}")
    elif choice == 3:
        from_city = input("Enter the departure city: ")
        to_city = input("Enter the destination city: ")
        between_cities_flights = flight_table.get_flights_between_cities(from_city, to_city)
        for flight in between_cities_flights:
            print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
