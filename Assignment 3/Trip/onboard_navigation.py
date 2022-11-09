import os 
import time 
import math

from locations import Country, City
from city_country_csv_reader import create_cities_countries_from_CSV
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley, create_example_vehicles
from trip import Trip, create_example_trips
from path_finding import find_shortest_path
from map_plotting import plot_trip

class Application:
    def __init__(self):
        create_cities_countries_from_CSV("worldcities_truncated.csv")
        self.vehicles = []
        self.trips = []

        example_vehicles = create_example_vehicles()
        for vehicle in example_vehicles:
            self.vehicles.append(vehicle)

        example_trips = create_example_trips()
        for trip in example_trips:
            self.trips.append(trip)

        # self.find_fastest_vehicle_for_trip()
        # self.create_trip()
        # self.plot_trip()
        # print(self.find_fastest_vehicle_for_trip())
        # print(self.trips)
        # self.simulate_trip()


    def display_main_menu(self):
        print("----------------Main Menu----------------")
        print("~ Welcome to Papa Pierre's Pâtisseries ~")
        print("1. Vehicles")
        print("2. Trips")
        print("3. Rules")
        print("4. Exit")
        print("-----------------------------------------")
    
    def vehicle_select(self):
        print("Current vehicle fleet: ")
        for vehicleindex in range(len(self.vehicles)):
            print(f"{vehicleindex+1}. {self.vehicles[vehicleindex]}")
        vehicle_index_selection = int_input("Please Select a vehicle: ")
        while vehicle_index_selection < 1 or vehicle_index_selection > len(self.vehicles):  
            vehicle_index_selection = int_input("Please Select a vehicle: ")

        vehicle = self.vehicles[vehicle_index_selection-1]
        return vehicle

    def trip_select(self):
        print("Current trips: ")
        for tripindex in range(len(self.trips)):
            print(f"{tripindex+1}. {self.trips[tripindex]}")
        trip_index_selection = int_input("Please select a trip: ")
        while trip_index_selection < 1 or trip_index_selection > len(self.trips):
            trip_index_selection = int_input("Please select a trip: ")
        
        trip = self.trips[trip_index_selection-1]
        return trip 

    def create_vehicle(self):
        print("Select a type of Vehicle to create: ")
        print("1. Create a Vehicle from example vehicles")
        print("2. Create a custom vehicle")

        option = int_input("Please enter an option: ")
        while option < 1 or option > 2:
            option = int_input("Please enter an option: ")

        if option == 1:   
            vehicle = self.create_vehicle_from_example()
        elif option == 2:    
            vehicle = self.create_custom_vehicle()

        self.vehicles.append(vehicle)   
        return vehicle

    def create_vehicle_from_example(self):
        example_vehicles = create_example_vehicles()

        print("Example Vehicles: ")
        for i in range(len(example_vehicles)):
            print(f"{i+1}. {example_vehicles[i]}")

        vehicle_option = int_input("Please enter an option: ")
        while vehicle_option < 1 or vehicle_option > len(example_vehicles):
            vehicle_option = int_input("Please enter an option: ")

        vehicle = example_vehicles[vehicle_option-1] 
        return vehicle

    def create_custom_vehicle(self):
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
    
    def create_trip(self):
        print("Select a type of Trip to create: ")
        print("1. Create a Trip from example trips")
        print("2. Create a custom Trip")
        print("3. Create a custom Trip with the shortest path ")

        option = int_input("Please enter an option: ")
        while option < 1 or option > 3:
            option = int_input("Please enter an option: ")

        if option == 1:   
            trip = self.create_trip_from_example()
        elif option == 2:    
            trip = self.create_custom_trip()
        elif option == 3:
            trip = self.create_trip_by_shortest_path()

        self.trips.append(trip)   
        return trip

    def create_trip_from_example(self):
        example_trips = create_example_trips()

        print("Example Trips: ")
        for i in range(len(example_trips)):
            print(f"{i+1}. {example_trips[i]}")
        
        trip_option = int_input("Please enter an option: ")
        while trip_option < 1 or trip_option > len(example_trips):
            trip_option = int_input("Please enter an option: ")
        
        trip = example_trips[trip_option-1]
        return trip

    def create_custom_trip(self):
        add_another_destination = False
        ### DEPARTURE STUFF
        country_option = Country.countries[input("Please enter departure country: ")]

        for cityindex in range(len(country_option.cities)):
            print(f"{cityindex+1}. {country_option.cities[cityindex]}")

        city_option = int_input("Please enter an option for departure city: ")
        while city_option < 1 or city_option > len(country_option.cities):
            city_option = int_input("Please enter an option for departure city: ")

        departure_city = country_option.cities[city_option-1]
        trip = Trip(departure_city)


        ### DESTINATION STUFF
        while add_another_destination is True or len(trip.cities) < 2: 
            country_option = Country.countries[input("Please enter destination country: ")]

            for cityindex in range(len(country_option.cities)):
                print(f"{cityindex+1}. {country_option.cities[cityindex]}")

            city_option = int_input("Please enter an option for destination city: ")
            while city_option < 1 or city_option > len(country_option.cities):
                city_option = int_input("Please enter an option for destination city: ")

            destination_city = country_option.cities[city_option-1]
            trip.add_next_city(destination_city)

            ### CONTINUE LOOP ? 
            print("Add Another Destination?")
            print("1. Yes")
            print("2. No")

            continue_option = int_input("Please enter an option: ")
            while continue_option < 1 or continue_option > 2:
                continue_option = int_input("Please enter an option: ")

            if continue_option == 1:
                add_another_destination = True
            else:
                add_another_destination = False 

        return trip

    def create_trip_by_shortest_path(self):
        ### DEPARTURE STUFF
        country_option = Country.countries[input("Please enter departure country: ")]

        for cityindex in range(len(country_option.cities)):
            print(f"{cityindex+1}. {country_option.cities[cityindex]}")

        city_option = int_input("Please enter an option for departure city: ")
        while city_option < 1 or city_option > len(country_option.cities):
            city_option = int_input("Please enter an option for departure city: ")

        departure_city = country_option.cities[city_option-1]
        trip = Trip(departure_city)

        ### DESTINATION STUFF
        country_option = Country.countries[input("Please enter destination country: ")]

        for cityindex in range(len(country_option.cities)):
            print(f"{cityindex+1}. {country_option.cities[cityindex]}")

        city_option = int_input("Please enter an option for destination city: ")
        while city_option < 1 or city_option > len(country_option.cities):
            city_option = int_input("Please enter an option for destination city: ")

        destination_city = country_option.cities[city_option-1]
        trip.add_next_city(destination_city)

        ### VEHICLE SELECTION
        vehicle_selection = self.vehicle_select()
        print(vehicle_selection)

        ### SHORTEST PATH 
        shortest_path = find_shortest_path(vehicle_selection, departure_city, destination_city)

        return shortest_path

    def find_fastest_vehicle_for_trip(self):
        trip_selection = self.trip_select()

        shortest_time = math.inf
        fastest_vehicle = self.vehicles[0]

        for eachvehicle in self.vehicles:
            total_time = trip_selection.total_travel_time(eachvehicle)
            if total_time < shortest_time:
                shortest_time = total_time
                fastest_vehicle = eachvehicle

            print(f"{eachvehicle}: {total_time}")
            
        return fastest_vehicle

    def plot_trip(self):
        trip_selection = self.trip_select()

        plot_trip(trip_selection)
        
    def simulate_trip(self):
        vehicle_selection = self.vehicle_select()
        trip_selection = self.trip_select()

        progress_bar_size = 10

        # in hours
        total_time_taken = trip_selection.total_travel_time(vehicle_selection) * 0.1
        each_unit = total_time_taken / progress_bar_size

        progress_bar = f"[{progress_bar_size * ' '}]"
        

        # print(total_time_taken)
        # print(progress_bar)


        print(f"Simulating trip: {trip_selection}")
        for i in range(progress_bar_size):
            time.sleep(each_unit)
            progress_bar = "[" + i*"*" + (progress_bar_size-(i+1)) * " " + "]"
            print(progress_bar, end="\r")
            


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

    
if __name__ == "__main__":
    Application()