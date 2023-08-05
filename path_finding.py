import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles
import networkx as nx
import math


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Purpose:
        Returns a shortest path between two cities for a given vehicle,
        or None if there is no path.
    Argument 1: vehicle: Vehicle
    Argument 2: from_city: City
    Argument 3: to_city: City
    Return Value: trip: Trip
    Function Body: plot the graph  
                    connect all the cities if the travel is possible with the vehicle
                    find the shortest path by using method in networkx
                    return the trip of the shortest path
    """ 
    graph = nx.Graph()

    for city in City.cities.values():
        for city2 in City.cities.values():
            travel_time = vehicle.compute_travel_time(city, city2)
            if travel_time != math.inf:
                graph.add_edge(city, city2, weight = travel_time)
    
    shortest_trip = None
    trip = None
    try:
        shortest_trip = nx.shortest_path(graph, from_city, to_city, weight="weight")
    except:
        print("No path")
    
    if shortest_trip != None:
        trip = Trip(from_city)
        for path in shortest_trip[1:]:
            trip.add_next_city(path)
    
    return trip
    


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))
