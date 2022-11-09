from vehicles import Vehicle, create_example_vehicles
from locations import City, Country
from locations import create_example_countries_and_cities
import math


class Trip:
    """
    Represents a sequence of cities.
    """

    def __init__(self, departure: City) -> None:
        """
        Initialises a Trip with a departure city.

        Arguments:
            -departure: Departing City object
        """
        self.departure = departure
        self.cities = [departure]

    def add_next_city(self, city: City) -> None:
        """
        Adds the next city to this trip.

        Arguments:
            -city: City object being added
        """
        self.cities.append(city)

    def total_travel_time(self, vehicle: Vehicle) -> float:
        """
        Returns a travel duration for the entire trip for a given vehicle.
        Returns math.inf if any leg (i.e. part) of the trip is not possible.

        Arguments:
            -vehicle: Vehicle object used to determine the travel duration for the entire trip
        """
        travel_duration = 0

        for index in range(1, len(self.cities)):
            if vehicle.compute_travel_time(self.cities[index - 1], self.cities[index]) == math.inf:
                return math.inf

            else:
                travel_duration += vehicle.compute_travel_time(self.cities[index - 1], self.cities[index])

        # The travel duration between two cities in the cities list is calculated by looping through the index from
        # one (inclusive) to the length of the cities list (exclusive), starting with the city at index minus one
        # (zero) and the city at index one, followed by the city at index minus one (one) and the city at index two,
        # etc. The calculated travel time between each pair of cities is then added to the travel_duration variable,
        # which will be returned once the travel duration for the entire trip for a given vehicle has been
        # calculated. However, if there are any two cities that cannot be calculated (math.inf), math.inf will be
        # returned instead.

        return travel_duration

    def find_fastest_vehicle(self, vehicles: list[Vehicle]) -> (Vehicle, float):
        """
        Returns the Vehicle for which this trip is fastest, and the duration of the trip.
        If there is a tie, return the first vehicle in the list.
        If the trip is not possible for any of the vehicle, return (None, math.inf).

        Arguments:
            -vehicles: List of Vehicle objects that are being compared to determine the fastest vehicle for the trip
        """
        fastest_vehicle = None
        fastest_travel_duration = math.inf

        for vehicle in vehicles:
            if self.total_travel_time(vehicle) < fastest_travel_duration:
                fastest_vehicle = vehicle
                fastest_travel_duration = self.total_travel_time(vehicle)

        # Assign math.inf and None as the fastest vehicle and fastest travel duration, respectively, which will be
        # used to compare values in a for loop. By looping through every vehicle in the vehicles list, the one whose
        # total travel time is less than the fastest travel duration will then be designated as the new fastest
        # vehicle and its total travel time will be set as the new fastest travel duration.

        return fastest_vehicle, fastest_travel_duration

    def __str__(self) -> str:
        """
        Returns a representation of the trip as a sequence of cities:
        City1 -> City2 -> City3 -> ... -> CityX
        """

        out_string = f"{self.cities[0]}"

        for city in self.cities[1:]:
            out_string += f" -> {city}"

        return out_string

    def __repr__(self) -> str:
        return self.__str__()


def create_example_trips() -> list[Trip]:
    """
    Creates examples of trips.
    """

    # first we create the cities and countries
    create_example_countries_and_cities()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")
    canberra = australia.get_city("Canberra")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    # then we create trips
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
