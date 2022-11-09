import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles
import networkx
import math


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
        path = networkx.Graph()

        if vehicle.__class__.__name__ == "DiplomacyDonutDinghy":
            for city in City.cities.values():
                if city.country == from_city.country or city.country == to_city.country:
                    path.add_node(city)

        else:
            for city in City.cities.values():
                path.add_node(city)

        for city in path.nodes():
            for other_city in path.nodes():
                path.add_edge(city, other_city, weight=vehicle.compute_travel_time(city, other_city))

        shortest_path_list = networkx.dijkstra_path(path, from_city, to_city)

        if vehicle.compute_travel_time(from_city, shortest_path_list[1]) != math.inf:
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
