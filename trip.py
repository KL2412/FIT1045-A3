from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from vehicles import create_example_vehicles
from locations import City, Country
from locations import create_example_countries_and_cities
import math

class Trip():
    """
    Represents a sequence of cities.
    """

    def __init__(self, departure: City) -> None:
        """
        Purpose:
            Initialises a Trip with a departure city.
        Argument:
            self object
            departure:City
        Return Value:
            None
        Function Body:
            initialize two instance variables
        """
        self.departure = departure
        self.next_city = []

    def add_next_city(self, city: City) -> None:
        """
        Purpose:
            Adds the next city to this trip.
        Argument:
            self object
            city: City
        Return Value:
            None
        Function Body:
            append the city into next_city list
        """
        self.next_city.append(city)

    def total_travel_time(self, vehicle: Vehicle) -> float:
        """
        Function:
            Returns a travel duration for the entire trip for a given vehicle.
            Returns math.inf if any leg (i.e. part) of the trip is not possible.
        Argument:
            self object
            vehicle: Vehicle
        Return Value:
            travel_time: float
        Function Body:
            initialize travel time to 0
            add the travel time from departure city to next city
            iterate through the list of next_city to add the travel time from every city to their next city into travel time_between_updates
            return travel time

        """
        travel_time = 0
        travel_time += vehicle.compute_travel_time(self.departure, self.next_city[0])
        for trip in range(1, len(self.next_city)):
            travel_time += vehicle.compute_travel_time(self.next_city[trip - 1], self.next_city[trip])
                
        return travel_time


    def find_fastest_vehicle(self, vehicles: list[Vehicle]) -> (Vehicle, float):
        """
        Purpose:
            Returns the Vehicle for which this trip is fastest, and the duration of the trip.
            If there is a tie, return the first vehicle in the list.
            If the trip is not possible for any of the vehicle, return (None, math.inf).
        Argument:
            self object
            vehicles: a list of Vehicle
        Return Value:
            a tuple (fastest_vehicle, travel_time) 
        Function body:
            initialize a fastest_vehicle tuple
            iterate through every vehicle to find the vehicle with shortest travel time
            return the vehicle and the travel time
        """
        fastest_vehicle = (None, math.inf) #vehicle object, fastest vehicle travel time 
        for vehicle in vehicles:
            travel_time = self.total_travel_time(vehicle)
            if travel_time < fastest_vehicle[1]:
                fastest_vehicle = (vehicle, travel_time)

        return fastest_vehicle

    def __str__(self) -> str:
        """
        Returns a representation of the trip as a sequence of cities:
        City1 -> City2 -> City3 -> ... -> CityX
        """
        output_str = f"{self.departure}"
        if len(self.next_city) != 0:
            output_str += " -> "
        for city in self.next_city:
            output_str += f"{city}"
            if city != self.next_city[-1]:
                output_str += " -> "

        return output_str


def create_example_trips() -> list[Trip]:
    """
    Creates examples of trips.
    """

    #first we create the cities and countries
    create_example_countries_and_cities()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")
    canberra = australia.get_city("Canberra")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    #then we create trips
    trips = []

    for cities in [(melbourne, sydney), (canberra, tokyo), (melbourne, canberra, tokyo), (canberra, melbourne, tokyo)]:
        trip = Trip(cities[0])
        for city in cities[1:]:
            trip.add_next_city(city)

        trips.append(trip)

    return trips


if __name__ == "__main__":
    vehicles = create_example_vehicles()
    trips = create_example_trips()

    for trip in trips:
        vehicle, duration = trip.find_fastest_vehicle(vehicles)
        print("The trip {} will take {} hours with {}".format(trip, duration, vehicle))
