
from locations import City, Country, test_example_countries_and_cities
import csv


def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """

    with open(path_to_csv, "r", encoding="utf-8") as file:

        # produces a list of each line inside the outer list 
        lines = list(csv.reader(file))

        data_extraction_index_list = []

        data_extraction_header_list = ["city_ascii", "lat", "lng", "country", "iso3", "capital", "id"]

        for data_header in data_extraction_header_list:  # loop through all headers
            data_extraction_index_list.append(lines[0].index(data_header))

        for linelist in lines[1:]:
            if linelist[data_extraction_index_list[3]] not in Country.countries:
                Country((linelist)[data_extraction_index_list[3]],
                        (linelist)[data_extraction_index_list[4]])

            City(linelist[data_extraction_index_list[0]], linelist[data_extraction_index_list[1]],
                 linelist[data_extraction_index_list[2]], linelist[data_extraction_index_list[3]],
                 linelist[data_extraction_index_list[5]], linelist[data_extraction_index_list[6]])

if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()
    # print(Country.countries)
    # print(City.cities)