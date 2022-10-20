import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles

import math
import networkx as nx 
import matplotlib.pyplot as plt

# def plotgraph(vehicle: Vehicle, from_city: City, to_city: City, graph):

#     for eachcity in City.cities.values():
#         if vehicle.compute_travel_time(from_city, eachcity) != math.inf and from_city.name != eachcity.name:
#             # print(f"{from_city} {eachcity} {vehicle.compute_travel_time(from_city, eachcity)}")
#             graph.add_node(eachcity)
#             graph.add_edge(from_city, eachcity, weight=vehicle.compute_travel_time(from_city, eachcity))



def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    G = nx.Graph()
    # depart_to = []

    # for eachcity in City.cities.values():
    #     G.add_node(eachcity)
    #     if vehicle.compute_travel_time(from_city, eachcity) != math.inf and from_city.name != eachcity.name:
    #         depart_to.append(eachcity)

    # for confirmed_city in depart_to:
    #     G.add_edge(from_city, confirmed_city, weight=vehicle.compute_travel_time(from_city, confirmed_city))
        # G.add_edge(confirmed_city, from_city, weight=vehicle.compute_travel_time(from_city, confirmed_city))



    # print(depart_to)
    # print(G.nodes)
    # print(G.edges)
    #     for eachcity in City.cities:


    # # create all nodes 
    # for eachcity in City.cities.values():
    #     G.add_node(eachcity)
    # # create all edges 
    # for eachnode in G.nodes:
    #     for eachnode2 in G.nodes:
    #         G.add_edge(eachnode,eachnode2)
    


    # print(G.edges)
    #     for eachnode2 in City.cities.values():
    #         G.add_edge(eachnode1, eachnode2, weight=vehicle.compute_travel_time(eachnode1, eachnode2))
            # if vehicle.compute_travel_time(eachnode1, eachnode2) != math.inf and eachnode1.name != eachnode2:
            
    # assert nx.has_path(G, from_city, to_city), 'no path '




    # G.add_node(from_city)
    # G.add_node(to_city)
    # G.add_edge(from_city, to_city, weight=vehicle.compute_travel_time(from_city, to_city))
    # print(G.nodes)
    # print(nx.has_path(G, from_city, to_city))
    # print(nx.shortest_path(G, from_city, to_city))
    # shortest = nx.has_path(G, from_city, to_city)
    # return shortest


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    crap = vehicles[2]
    # plotgraph(crap, melbourne, tokyo)
    find_shortest_path(crap, melbourne, tokyo)

    # for vehicle in vehicles:
    #     print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))
