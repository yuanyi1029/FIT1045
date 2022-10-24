import os 
import time 

from locations import Country, City
from city_country_csv_reader import create_cities_countries_from_CSV
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley, create_example_vehicles
from trip import Trip, create_example_trips
from path_finding import find_shortest_path
from map_plotting import plot_trip

def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.-

    Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input

def display_main_menu():
    print("----------------Main Menu----------------")
    print("~ Welcome to Papa Pierre's Pâtisseries ~")
    print("1. Vehicles")
    print("2. Trips")
    print("3. Rules")
    print("4. Exit")
    print("-----------------------------------------")


def create_vehicle():
    print("Select a type of Vehicle to create: ")
    print("1. Create a Vehicle from example vehicles")
    print("2. Create a custom vehicle")

    option = int_input("Please enter an option: ")
    while option < 1 or option > 2:
        option = int_input("Please enter an option: ")

    if option == 1:   
        vehicle = create_vehicle_from_example()
    elif option == 2:    
        vehicle = create_custom_vehicle()

    return vehicle

def create_vehicle_from_example():
    example_vehicles = create_example_vehicles()

    print("Example Vehicles: ")
    for i in range(len(example_vehicles)):
        print(f"{i+1}. {example_vehicles[i]}")

    vehicle_option = int_input("Please enter an option: ")
    while vehicle_option < 1 or vehicle_option > len(example_vehicles):
        vehicle_option = int_input("Please enter an option: ")

    vehicle = example_vehicles[vehicle_option-1]
    return vehicle

def create_custom_vehicle():
    print("Select a type of Vehicle to create: ")
    print("1. Crappy Crepe Car")
    print("2. Diplomacy Donut Dinghy")
    print("3. Teleporting Tarte Trolley")

    vehicle_option = int_input("Please enter an option: ")
    while vehicle_option < 1 or vehicle_option > 3:
        vehicle_option = int_input("Please enter an option: ")

    if vehicle_option == 1:
        speed = int_input("Please enter the speed of Crappy Crepe Car (km/h): ")
        vehicle = CrappyCrepeCar(speed)
    elif vehicle_option == 2:
        in_country_speed = int_input("Please enter the speed of Diplomacy Donut Dinghy within a country (km/h): ")
        between_primary_speed = int_input("Please enter the speed of Diplomacy Donut Dinghy between capital cities (km/h): ")
        vehicle = DiplomacyDonutDinghy(in_country_speed, between_primary_speed)        
    elif vehicle_option == 3:
        travel_time = int_input("Please enter the travel time of Teleporting Tarte Trolley (h): ")
        max_distance = int_input("Please enter the maximum distance of Teleporting Tarte Trolley (km): ")
        vehicle = TeleportingTarteTrolley(travel_time, max_distance)

    return vehicle 

def create_trip_from_example():
    example_trips = create_example_trips()

    print("Example Trips: ")
    for i in range(len(example_trips)):
        print(f"{i+1}. {example_trips[i]}")
    
    trip_option = int_input("Please enter an option: ")
    while trip_option < 1 or trip_option > len(example_trips):
        trip_option = int_input("Please enter an option: ")
    
    trip = example_trips[trip_option-1]
    return trip

def create_custom_trip():
    ### NOT DONE YET
    create_cities_countries_from_CSV("worldcities_truncated.csv")

    country_option = Country.countries[input("Please enter departure country: ")]

    for cityindex in range(len(country_option.cities)):
        print(f"{cityindex+1}. {country_option.cities[cityindex]}")

    city_option = int_input("Please enter an option for departure city: ")
    while city_option < 1 or city_option > len(country_option.cities):
        city_option = int_input("Please enter an option for departure city: ")

    departure_city = country_option.cities[city_option-1]
    trip = Trip(departure_city)
    return trip

if __name__ == "__main__":
    # print(create_vehicle())
    # print(create_trip_from_example())
    print(create_custom_trip())
