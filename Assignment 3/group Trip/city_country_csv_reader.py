from locations import City, Country, test_example_countries_and_cities
import csv


def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """

    with open(path_to_csv, "r", encoding="UTF-8") as csv_file:

        contents = list(csv.reader(csv_file))

        # Lists are created for all of the rows in the CSV file using the columns from each row, which are then
        # stored in the contents list.

        data_header_extraction_list = ["city_ascii", "lat", "lng", "country", "iso3", "capital", "id"]

        # The data_header_extraction_list stores the string of data headers required to create City and Country
        # instances.

        data_index_extraction_list = []

        for data_header in data_header_extraction_list:
            data_index_extraction_list.append(contents[0].index(data_header))

        # Using the first row of the CSV file, loop through the data headers in the data_header_extraction_list and
        # add the index of each data header to the data_index_extraction_list.

        # data_index_extraction_list:   index 0 contains city_ascii's index (column number)
        #                               index 1 contains lat's index (column number)
        #                               index 2 contains lng's index (column number)
        #                               index 3 contains country's index (column number)
        #                               index 4 contains iso3's index (column number)
        #                               index 5 contains capital's index (column number)
        #                               index 6 contains id's index (column number)

        for content in contents[1:]:
            if content[data_index_extraction_list[3]] not in Country.countries:
                Country(content[data_index_extraction_list[3]], content[data_index_extraction_list[4]])

            City(content[data_index_extraction_list[0]], content[data_index_extraction_list[1]],
                 content[data_index_extraction_list[2]], content[data_index_extraction_list[3]],
                 content[data_index_extraction_list[5]], content[data_index_extraction_list[6]])

        # Excluding the first row (data header row), loop through the CSV file's other rows; if a row has a country
        # that is not in the countries dictionary, a new country instance will be created using that row's country and
        # iso3's string value. Additionally, a new city instance will be created using the content of each row.


if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()

