import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles

import math
import networkx as nx 


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    if vehicle.__class__.__name__ == "CrappyCrepeCar":
        shortest_path = Trip(from_city)
        shortest_path.add_next_city(to_city)

        return shortest_path
    
    else:
        graph = nx.Graph()
        # create all nodes 
        for eachcity in City.cities.values():
            graph.add_node(eachcity)

        # create all edges 
        for eachcity in City.cities.values():
            for eachcity2 in City.cities.values():
                if vehicle.compute_travel_time(eachcity, eachcity2) != math.inf:
                    graph.add_edge(eachcity, eachcity2, weight=vehicle.compute_travel_time(eachcity,eachcity2))

        shortest_path_list = nx.shortest_path(graph, from_city, to_city)

        shortest_path = Trip(from_city)

        for city in shortest_path_list[1:]:
            shortest_path.add_next_city(city)

        return shortest_path


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))
