from locations import Country
from city_country_csv_reader import create_cities_countries_from_CSV
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley, create_example_vehicles
from trip import Trip
from path_finding import find_shortest_path
from map_plotting import plot_trip
import os
import math
import time


def main() -> None:
    """
    Initialize all countries and cities objects from worldcities truncated.csv and begin the main loop, which allows
    users to navigate to the vehicle menu, trip menu, or exit the application.
    """
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    vehicles = []
    trips = []

    main_menu(vehicles, trips)


def main_menu(vehicles, trips) -> None:
    """
    Displays the main menu and allows users to browse to the vehicle menu, trip menu, or exit the application.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    os.system("clear")
    print("------------Main Menu------------")
    print("Welcome to Papa Pierre's Pâtisseries!")
    print("1. Vehicle")
    print("2. Trip")
    print("3. Exit")
    print("---------------------------------")

    option = int_input("Enter an option: ")

    while option < 1 or option > 3:
        option = int_input("Enter an option: ")

    # Range check.

    if option == 1:
        vehicle_menu(vehicles, trips)

    elif option == 2:
        trip_menu(vehicles, trips)

    else:
        print("Exiting Papa Pierre's Pâtisseries...")


def vehicle_menu(vehicles, trips) -> None:
    """
    Displays the vehicle menu, allowing users to view and remove the vehicles they created, create new vehicle
    objects, identify the fastest vehicle capable of completing a trip, and return to the main menu.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    print("\n------------Vehicle Menu------------")
    print("1. Display current vehicle fleet")
    print("2. Create new vehicle")
    print("3. Find the fastest vehicle capable of completing a trip")
    print("4. Return to main menu")
    print("---------------------------------")

    option = int_input("Enter an option: ")

    while option < 1 or option > 4:
        option = int_input("Enter an option: ")

    # Range check.

    if option == 1:
        display_vehicle(vehicles, trips)

    elif option == 2:
        create_vehicle(vehicles, trips)

    elif option == 3:
        find_fastest_vehicle_for_trip(vehicles, trips)

    else:
        main_menu(vehicles, trips)


def display_vehicle(vehicles, trips) -> None:
    """
    Allows users to view and remove the vehicles they created.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(vehicles) > 0:

        # Presence check for the vehicles list.

        print("\nCurrent vehicle fleet: ")

        for index in range(len(vehicles)):
            print(f"{index + 1}. {vehicles[index]}")

        print("\nRemove a vehicle from the fleet?")
        print("1. Yes")
        print("2. No")

        option = int_input("Enter an option: ")

        while option < 1 or option > 2:
            option = int_input("Enter an option: ")

        # Range check.

        if option == 1:
            vehicle_index = int_input("Select a vehicle to be removed: ")

            while vehicle_index < 1 or vehicle_index > len(vehicles):
                vehicle_index = int_input("Select a vehicle to be removed: ")

            # Range check.

            vehicles.pop(vehicle_index - 1)

    else:
        print("\nNo vehicle fleet is available")

    vehicle_menu(vehicles, trips)


def create_vehicle(vehicles, trips) -> None:
    """
    Allows users to create new vehicle objects by creating a vehicle from the examples provided or by customizing
    their own.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    print("\nSelect a method for creating a vehicle: ")
    print("1. Create a vehicle using the examples provided")
    print("2. Create a custom vehicle")
    print("3. Back")

    method = int_input("Select a method: ")

    while method < 1 or method > 3:
        method = int_input("Select a method: ")

    # Range check.

    if method == 1:
        vehicles.append(create_vehicle_from_example())

    elif method == 2:
        vehicles.append(create_custom_vehicle())

    # Append the newly created vehicle to the vehicles list (as returned by the functions create_vehicle_from_example
    # and create_custom_vehicle).

    vehicle_menu(vehicles, trips)


def create_vehicle_from_example() -> Vehicle:
    """
    Allows users to create new vehicle objects by creating a vehicle from the examples provided.

    Returns the created Vehicle object.
    """
    example_vehicles = create_example_vehicles()

    print("\nSelect a vehicle to create from the examples: ")

    for index in range(len(example_vehicles)):
        print(f"{index + 1}. {example_vehicles[index]}")

    vehicle_index = int_input("Select a vehicle: ")

    while vehicle_index < 1 or vehicle_index > len(example_vehicles):
        vehicle_index = int_input("Select a vehicle: ")

    # Range check.

    return example_vehicles[vehicle_index - 1]


def create_custom_vehicle() -> Vehicle:
    """
    Allows users to create new vehicle objects by customizing their own.

    Returns the created Vehicle object.
    """
    print("\nSelect a type vehicle to create: ")

    for index in range(len(Vehicle.__subclasses__())):
        print(f"{index + 1}. {Vehicle.__subclasses__()[index].__name__}")

    # Access vehicle types by using the __subclasses__ magic method on the Vehicle class (parent class).

    vehicle_type_index = int_input("Select a type vehicle: ")

    while vehicle_type_index < 1 or vehicle_type_index > len(Vehicle.__subclasses__()):
        vehicle_type_index = int_input("Select a type vehicle: ")

    # Range check.

    if Vehicle.__subclasses__()[vehicle_type_index - 1].__name__ == "CrappyCrepeCar":
        speed = int_input("\nEnter CrappyCrepeCar's speed in km/h: ")

        while speed <= 0:
            speed = int_input("Enter CrappyCrepeCar's speed in km/h: ")

        # Range check.

        return CrappyCrepeCar(speed)

    elif Vehicle.__subclasses__()[vehicle_type_index - 1].__name__ == "DiplomacyDonutDinghy":
        in_country_speed = int_input(
            "\nEnter DiplomacyDonutDinghy's speed for two cities in the same country in km/h: ")

        while in_country_speed <= 0:
            in_country_speed = int_input("Enter DiplomacyDonutDinghy's speed for two cities in the same country in "
                                         "km/h: ")

        # Range check.

        between_primary_speed = int_input("\nEnter DiplomacyDonutDinghy's speed between two primary cities in km/h: ")

        while between_primary_speed <= 0:
            between_primary_speed = int_input("Enter DiplomacyDonutDinghy's speed between two primary cities in km/h: ")

        # Range check.

        return DiplomacyDonutDinghy(in_country_speed, between_primary_speed)

    else:
        travel_time = int_input("\nEnter TeleportingTarteTrolley's travel time between any two cities in hours: ")

        while travel_time <= 0:
            travel_time = int_input("Enter TeleportingTarteTrolley's travel time between any two cities in hours: ")

        # Range check.

        max_distance = int_input("\nEnter TeleportingTarteTrolley's maximum travel distance between any two cities in "
                                 "km: ")

        while max_distance <= 0:
            max_distance = int_input("Enter TeleportingTarteTrolley's maximum travel distance between any two cities "
                                     "in km: ")

        # Range check.

        return TeleportingTarteTrolley(travel_time, max_distance)


def find_fastest_vehicle_for_trip(vehicles, trips) -> None:
    """
    Allows users to identify the fastest vehicle capable of completing a trip.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(vehicles) == 0 and len(trips) == 0:
        print("\nNo vehicle fleet and trips are available")

    elif len(vehicles) == 0:
        print("\nNo vehicle fleet is available")

    elif len(trips) == 0:
        print("\nNo trips are available")

    # Presence check for the vehicles and trips list.

    else:
        print("\nCurrent trips: ")

        for index in range(len(trips)):
            print(f"{index + 1}. {trips[index]}")

        trip_index = int_input("Select a trip: ")

        while trip_index < 1 or trip_index > len(trips):
            trip_index = int_input("Select a trip: ")

        # Range check.

        trip = trips[trip_index - 1]

        fastest_vehicle = trip.find_fastest_vehicle(vehicles)

        if fastest_vehicle[0] is None:
            print("\nThe trip cannot be completed by any vehicle")

        # Presence check for fastest_vehicle.

        else:
            print(f"\n{fastest_vehicle[0]} is the fastest vehicle that can travel {trip} in {fastest_vehicle[1]} hour")

    vehicle_menu(vehicles, trips)


def trip_menu(vehicles, trips) -> None:
    """
    Displays the trip menu, allowing users to view and remove the trips they created, create new trip
    objects, plot a trip on a map, simulate a trip for a vehicle, and return to the main menu.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    print("\n------------Trip Menu------------")
    print("1. Display current trips")
    print("2. Create new trip")
    print("3. Plot a trip on a map")
    print("4. Simulate a trip for a vehicle")
    print("5. Return to main menu")
    print("---------------------------------")

    option = int_input("Enter an option: ")

    while option < 1 or option > 5:
        option = int_input("Enter an option: ")

    # Range check.

    if option == 1:
        display_trip(vehicles, trips)

    elif option == 2:
        create_trip(vehicles, trips)

    elif option == 3:
        plot_trip_on_map(vehicles, trips)

    elif option == 4:
        simulate_trip(vehicles, trips)

    else:
        main_menu(vehicles, trips)


def display_trip(vehicles, trips) -> None:
    """
    Allows users to view and remove the trips they created.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(trips) > 0:

        # Presence check for the trips list.

        print("\nCurrent trips: ")

        for index in range(len(trips)):
            print(f"{index + 1}. {trips[index]}")

        print("\nRemove a trip?")
        print("1. Yes")
        print("2. No")

        option = int_input("Enter an option: ")

        while option < 1 or option > 2:
            option = int_input("Enter an option: ")

        # Range check.

        if option == 1:
            trip_index = int_input("Select a trip to be removed: ")

            while trip_index < 1 or trip_index > len(trips):
                trip_index = int_input("Select a trip to be removed: ")

            # Range check.

            trips.pop(trip_index - 1)

    else:
        print("\nNo trips are available")

    trip_menu(vehicles, trips)


def create_trip(vehicles, trips) -> None:
    """
    Allows users to create new trip objects by creating a trip from the examples provided, customizing
    their own, or finding a shortest path between two cities for one vehicle or a fleet of vehicles.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    print("\nSelect a method for creating a trip: ")
    print("1. Create a trip using the examples provided")
    print("2. Create a custom trip")
    print("3. Create a trip by finding a shortest path between two cities for one vehicle or a fleet of vehicles")
    print("4. Back")

    method = int_input("Select a method: ")

    while method < 1 or method > 4:
        method = int_input("Select a method: ")

    # Range check.

    if method == 1:
        trips.append(create_trip_from_example())

    elif method == 2:
        trips.append(create_custom_trip())

    # Append the newly created trip to the trips list (as returned by the functions create_trip_from_example and
    # create_custom_trip).

    elif method == 3:
        create_trip_from_shortest_path(vehicles, trips)

    trip_menu(vehicles, trips)


def create_trip_from_example() -> Trip:
    """
    Allows users to create new trip objects by creating a trip from the examples provided.

    Returns the created Trip object.
    """
    example_trips = create_example_trips()

    print("\nSelect a trip to create from the examples: ")

    for index in range(len(example_trips)):
        print(f"{index + 1}. {example_trips[index]}")

    trip_index = int_input("Select a trip: ")

    while trip_index < 1 or trip_index > len(example_trips):
        trip_index = int_input("Select a trip: ")

    # Range check.

    return example_trips[trip_index - 1]


def create_example_trips() -> list[Trip]:
    """
    Creates 4 examples of trips.

    Returns the Trip objects in a list.
    """
    trip_example_1 = Trip(Country.countries["Australia"].get_city("Melbourne"))
    trip_example_1.add_next_city(Country.countries["Australia"].get_city("Sydney"))

    trip_example_2 = Trip(Country.countries["Australia"].get_city("Canberra"))
    trip_example_2.add_next_city(Country.countries["Japan"].get_city("Tokyo"))

    trip_example_3 = Trip(Country.countries["Australia"].get_city("Melbourne"))
    trip_example_3.add_next_city(Country.countries["Australia"].get_city("Canberra"))
    trip_example_3.add_next_city(Country.countries["Japan"].get_city("Tokyo"))

    trip_example_4 = Trip(Country.countries["Australia"].get_city("Canberra"))
    trip_example_4.add_next_city(Country.countries["Australia"].get_city("Melbourne"))
    trip_example_4.add_next_city(Country.countries["Japan"].get_city("Tokyo"))

    return [trip_example_1, trip_example_2, trip_example_3, trip_example_4]


def create_custom_trip() -> Trip:
    """
    Allows users to create new trip objects by customizing their own.

    Returns the created Trip object.
    """
    print_available_countries(10)

    country = input("\nEnter a country of departure: ")

    while country not in Country.countries:
        country = input("Enter a country of departure: ")

    # Format checks.

    for index in range(len(Country.countries[country].cities)):
        print(f"{index + 1}. {Country.countries[country].cities[index]}")

    city_index = int_input("Select a city: ")

    while city_index < 1 or city_index > len(Country.countries[country].cities):
        city_index = int_input("Select a city: ")

    # Range check.

    trip = Trip(Country.countries[country].cities[city_index - 1])

    while True:
        country = input("\nEnter a destination country: ")

        while country not in Country.countries:
            country = input("Enter a destination country: ")

        # Presence and format checks (verify a valid country is entered).

        for index in range(len(Country.countries[country].cities)):
            print(f"{index + 1}. {Country.countries[country].cities[index]}")

        city_index = int_input("Select a city: ")

        while city_index < 1 or city_index > len(Country.countries[country].cities) or \
                Country.countries[country].cities[city_index - 1] == trip.cities[-1]:
            city_index = int_input("Select a city: ")

        # Range and distinct checks (ensure that cities are not visited consecutively during a trip).

        trip.add_next_city(Country.countries[country].cities[city_index - 1])

        print("\nAdd another city to this trip?")
        print("1. Yes")
        print("2. No")

        option = int_input("Enter an option: ")

        while option < 1 or option > 2:
            option = int_input("Enter an option: ")

        # Range check.

        if option == 2:
            return trip

        # The code to add destination cities will loop endlessly until the user enters option 2 (which means not to
        # add another city to the journey), at which point it will return the trip that was created by the user.


def create_trip_from_shortest_path(vehicles, trips) -> None:
    """
    Allows users to create new trip objects by finding a shortest path between two cities for one vehicle or a
    fleet of vehicles.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(vehicles) == 0:
        print("\nNo vehicle fleet is available")

    # Presence check for the vehicles list.

    else:
        print_available_countries(10)

        country = input("\nEnter a country of departure: ")

        while country not in Country.countries:
            country = input("Enter a country of departure: ")

        # Presence and format checks (verify a valid country is entered).

        for index in range(len(Country.countries[country].cities)):
            print(f"{index + 1}. {Country.countries[country].cities[index]}")

        city_index = int_input("Select a city: ")

        while city_index < 1 or city_index > len(Country.countries[country].cities):
            city_index = int_input("Select a city: ")

        # Range checks.

        from_city = Country.countries[country].cities[city_index - 1]

        country = input("\nEnter a destination country: ")

        while country not in Country.countries:
            country = input("Enter a destination country: ")

        # Presence and format checks (verify a valid country is entered).

        for index in range(len(Country.countries[country].cities)):
            print(f"{index + 1}. {Country.countries[country].cities[index]}")

        city_index = int_input("Select a city: ")

        while city_index < 1 or city_index > len(Country.countries[country].cities) or \
                Country.countries[country].cities[city_index - 1] == from_city:
            city_index = int_input("Select a city: ")

        # Range and distinct checks (ensure that cities are not visited consecutively during a trip).

        to_city = Country.countries[country].cities[city_index - 1]

        print("\nPlease wait for a moment...")

        available_vehicles = []
        shortest_path_list = []

        for vehicle in vehicles:
            shortest_path = find_shortest_path(vehicle, from_city, to_city)
            if shortest_path is not None:
                available_vehicles.append(vehicle)
                shortest_path_list.append(shortest_path)

        # Loop through the vehicles list, appending vehicles that can produce the shortest path between the two
        # cities provided by the users (do not return None) into the available_vehicles list and the shortest path of
        # that vehicle into the shortest_path_list.

        if len(available_vehicles) == 0:
            print("\nThere are no vehicles available to find the shortest path")

        # Presence check for the available_vehicles list.

        else:
            print("\nCurrent trips: ")

            for index in range(len(available_vehicles)):
                print(f"{index + 1}. {available_vehicles[index]}: {shortest_path_list[index]}")

            trip_index = int_input("Select a trip: ")

            while trip_index < 1 or trip_index > len(shortest_path_list):
                trip_index = int_input("Select a trip: ")

            # Range check.

            trips.append(shortest_path_list[trip_index - 1])


def plot_trip_on_map(vehicles, trips) -> None:
    """
    Allows users to plot a trip on a map.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(trips) == 0:
        print("\nNo trips are available")

    # Presence check for the trips list.

    else:
        print("\nCurrent trips: ")

        for index in range(len(trips)):
            print(f"{index + 1}. {trips[index]}")

        trip_index = int_input("Select a trip: ")

        while trip_index < 1 or trip_index > len(trips):
            trip_index = int_input("Select a trip: ")

        # Range check.

        plot_trip(trips[trip_index - 1])

    trip_menu(vehicles, trips)


def simulate_trip(vehicles, trips) -> None:
    """
    Allows users to simulate a trip for a vehicle.

    Arguments:
        -vehicles: List of Vehicle objects created by users and saved in the application.
        -trips: List of Trip objects created by users and saved in the application.
    """
    if len(vehicles) == 0 and len(trips) == 0:
        print("\nNo vehicle fleet and trips are available")

    elif len(vehicles) == 0:
        print("\nNo vehicle fleet is available")

    elif len(trips) == 0:
        print("\nNo trips are available")

    # Presence check for the vehicles and trips list.

    else:
        print("\nCurrent trips: ")

        for index in range(len(trips)):
            print(f"{index + 1}. {trips[index]}")

        trip_index = int_input("Select a trip: ")

        while trip_index < 1 or trip_index > len(trips):
            trip_index = int_input("Select a trip: ")

        # Range check.

        trip = trips[trip_index - 1]

        available_vehicles = []

        for vehicle in vehicles:
            if trip.total_travel_time(vehicle) != math.inf:
                available_vehicles.append(vehicle)

        # Loop through the vehicles list, appending vehicles that can travel the trip provided by the users (do not
        # return math.inf) into the available_vehicles list.

        if len(available_vehicles) == 0:
            print("\nThere are no vehicles available to simulate the trip")

        # Presence check for the available_vehicles list.

        else:
            print("\nSelect a vehicle to simulate the trip: ")

            for index in range(len(available_vehicles)):
                print(f"{index + 1}. {available_vehicles[index]}")

            vehicle_index = int_input("Select a vehicle: ")

            while vehicle_index < 1 or vehicle_index > len(available_vehicles):
                vehicle_index = int_input("Select a vehicle: ")

            # Range checks

            vehicle = available_vehicles[vehicle_index - 1]

            print(f"\nSimulating {trip} for {vehicle}")

            progress_bar_size = 50
            time_between_hour_in_seconds = 0.1

            for index in range(1, len(trip.cities)):
                temporary_trip = Trip(trip.cities[index - 1])
                temporary_trip.add_next_city(trip.cities[index])

                # The variable temporary trip is used to assign each individual trip of the user-selected trip. For
                # the trip Canberra (AUS) -> Melbourne (AUS) -> Tokyo (JPN), for example, a trip from Canberra (AUS)
                # to Melbourne (AUS) will be assigned first, followed by a trip from Melbourne (AUS) to Tokyo (JPN).
                # This is accomplished by looping through the index from one (inclusive) to the length of the trip's
                # city list (exclusive), starting with the city at index minus one (zero) and the city at index one,
                # followed by the city at index minus one (one) and the city at index two, etc.

                total_travel_time_in_seconds = temporary_trip.total_travel_time(vehicle) * time_between_hour_in_seconds

                # The total travel time of a trip using a specific vehicle in seconds is derived by multiplying the
                # total travel time of the trip using a specific vehicle by the time between an hour in seconds.

                progress_time_per_bar = total_travel_time_in_seconds / progress_bar_size

                # The time required to advance each individual bar in the progress bar is computed by dividing the
                # total travel time of a trip in seconds by the progress bar size.

                print(f"\nTravelling from {temporary_trip.cities[0]} to {temporary_trip.cities[1]}")

                for progress in range(progress_bar_size + 1):
                    print_progress_bar(progress, progress_bar_size)
                    time.sleep(progress_time_per_bar)

    trip_menu(vehicles, trips)


def int_input(prompt="", restricted_to=None) -> int:
    """
    Helper function that modifies the regular input method, and keeps asking for input until a valid one is entered.
    Input can also be restricted to a set of integers.

    Arguments:
      -prompt: String representing the message to display for input
      -restricted: List of integers for when the input must be restricted to a certain set of numbers

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


def print_available_countries(column: int) -> None:
    """
    Helper function that neatly displays all available countries for travel in lines.

    Arguments:
      -row: Integer representing the number of countries displayed in a single line
    """
    print("\nAvailable countries to travel: ")

    available_countries = list(Country.countries.keys())
    country_index = 0

    for row_index in range(int(len(available_countries) / column) - 1):

        # The number of rows to be printed may be determined by calculating the integer value of
        # len(available_countries) / column, and all rows are printed with countries based on the number of columns.

        out_string = ""

        for column_index in range(column):
            out_string += f"{available_countries[country_index + column_index]}, "

        country_index += column

        # After each row is printed, the country_index is incremented by the number of columns to keep track of which
        # country was finished in the previous row and which country should be resumed when printing a new row.

        print(out_string)

    # The loop will end when it reaches the second last partitioned row to determine whether there are any remaining
    # countries that have not been partitioned into the allocated column size per row by using the formula
    # len(available_countries) % column to determine the remainder.

    remaining = len(available_countries) % column
    out_string = ""

    if int(len(available_countries) / column) == 0:
        for country_index in range(len(available_countries) - 1):
            out_string += f"{available_countries[country_index]}, "

        out_string += f"{available_countries[-1]}."

        # If the number of available countries is less than the number of countries to be displayed in a single line.

    else:
        if remaining == 0:

            for column_index in range(column - 1):
                out_string += f"{available_countries[country_index + column_index]}, "

            out_string += f"{available_countries[-1]}."

            # If the remainder is zero, the last partitioned row is displayed.

        else:
            for column_index in range(column):
                out_string += f"{available_countries[country_index + column_index]}, "

            country_index += column
            print(out_string)

            out_string = ""

            for remaining_index in range(remaining - 1):
                out_string += f"{available_countries[country_index + remaining_index]}, "

            out_string += f"{available_countries[-1]}."

            # If the remainder is not zero, the last partitioned row will be printed, followed by the remaining
            # unprinted available countries.

    print(out_string)


def print_progress_bar(progress: int, progress_bar_size: int) -> None:
    """
    Helper function that prints a progress bar of given size with given progress

    Arguments:
        -progress_bar_size: Integer representing the number of characters to fill in
        -progress: Integer representing the number of characters of progress
    """
    if progress_bar_size == progress:
        print("[" + progress * "*" + (progress_bar_size - progress) * " " + "]")

    else:
        print("[" + progress * "*" + (progress_bar_size - progress) * " " + "]", end="\r")


main()
