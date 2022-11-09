from __future__ import annotations
from enum import Enum
from geopy.distance import great_circle
import math


class CapitalType(Enum):
    """
    The different types of capitals (e.g. "primary").
    """
    primary = "primary"
    admin = "admin"
    minor = "minor"
    unspecified = ""

    # Each Enum element in CapitalType is assigned a distinct string value according to the capital's type.

    def __str__(self) -> str:
        return self.value

    # When print() is used, the magic method __str__ is implemented to output the CapitalType's string value.


class Country:
    """
    Represents a country.
    """

    countries = dict()  # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        Arguments:
            -name: String of country's name
            -iso3: String of country's ISO code with 3 characters
        """
        self.name = name
        self.iso3 = iso3
        self.cities = []

        Country.countries[name] = self

        # The country's name is used as a key to add a new instance of the country to the countries dictionary.

    def _add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        Arguments:
            -city: City object being added
        """
        self.cities.append(city)

    def get_cities(self, capital_types: list[CapitalType] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument capital_types can be given to specify a subset of the capital types that must be returned.
        Cities that do not correspond to these capital types are not returned.
        If no argument is given, all cities are returned.

        Arguments:
            -capital_types: List of CapitalType subsets that must be returned
        """
        if capital_types is None:
            return self.cities

        else:
            return [city for city in self.cities if city.capital_type in capital_types]

    def get_city(self, city_name: str) -> City:
        """
        Returns a city of the given name in this country.
        Returns None if there is no city by this name.
        If there are multiple cities of the same name, returns an arbitrary one.

        Arguments:
            -city_name: String of city's name
        """
        for city in self.cities:
            if city.name == city_name:
                return city

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class City:
    """
    Represents a city.
    """

    cities = dict()  # a dict that associates city IDs to instances.

    def __init__(self, name: str, latitude: str, longitude: str, country: str, capital_type: str, city_id: str) -> None:
        """
        Initialises a city with the given data.

        Arguments:
            -name: String of city's name
            -latitude: String of city's latitude
            -longitude: String of city's longitude
            -country: String of city's country's name
            -capital_type: String of city's capital type
            -city_id: String of city's city id
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.capital_type = CapitalType(capital_type)
        self.city_id = city_id

        City.cities[city_id] = self
        # The city's city id is used as a key to add a new instance of the city to the cities dictionary.

        Country.countries[country]._add_city(self)
        # Using the _add_city method, a new instance of the city is added to the list of cities in its country by
        # accessing it through the countries dictionary with the city's country as the key.

    def distance(self, other_city: City) -> int:
        """
        Returns the distance in kilometers between two cities using the great circle method,
        rounded up to an integer.

        Arguments:
            -other_city: City object used to compare with a City instance to determine the distance in kilometres
        """
        return math.ceil(great_circle((self.latitude, self.longitude), (other_city.latitude, other_city.longitude)).km)

    def __str__(self) -> str:
        """
        Returns the name of the city and the country ISO3 code in parentheses.
        For example, "Melbourne (AUS)".
        """
        return f"{self.name} ({Country.countries[self.country].iso3})"

    def __repr__(self) -> str:
        return self.__str__()


def create_example_countries_and_cities() -> None:
    """
    Creates a few Countries and Cities for testing purposes.
    """
    australia = Country("Australia", "AUS")
    melbourne = City("Melbourne", "-37.8136", "144.9631", "Australia", "admin", "1036533631")
    canberra = City("Canberra", "-35.2931", "149.1269", "Australia", "primary", "1036142029")
    sydney = City("Sydney", "-33.865", "151.2094", "Australia", "admin", "1036074917")

    japan = Country("Japan", "JPN")
    tokyo = City("Tokyo", "35.6839", "139.7744", "Japan", "primary", "1392685764")


def test_example_countries_and_cities() -> None:
    """
    Assuming the correct cities and countries have been created, runs a small test.
    """
    australia = Country.countries['Australia']
    canberra = australia.get_city("Canberra")
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")

    print("The distance between {} and {} is {}km".format(melbourne, sydney, melbourne.distance(sydney)))

    for city in australia.get_cities([CapitalType.admin, CapitalType.primary]):
        print("{} is a {} capital of {}".format(city, city.capital_type, city.country))


if __name__ == "__main__":
    create_example_countries_and_cities()
    test_example_countries_and_cities()
