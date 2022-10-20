from locations import City, Country, test_example_countries_and_cities
import csv


def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """

    with open(path_to_csv, "r", encoding="utf-8") as file:

        lines = file.readlines()

        data_extraction_index_list = []  # list for storing header indexes to be used later on

        data_extraction_header_list = ["city_ascii", "lat", "lng", "country", "iso3", "capital", "id"]
        # # list of headers in the csv file

        for data_header in data_extraction_header_list:  # loop through all headers
            data_extraction_index_list.append(lines[0].strip().split(",").index(data_header))
            # get the index of the header and append into list after strip split
        
        print(lines)

        clean_lines = map(lambda line: line.strip().replace(",,", ",") , lines[1:])
        print(list(clean_lines))
        # for eachline in list(clean_lines):
        #     print(eachline.split(","))


        # print(data)


            # formatted_line = line.strip().split(",")  # strip stripe shit
            # print(formatted_line)

            # if formatted_line[data_extraction_index_list[3]] not in Country.countries:
            #     # if new country is found from a city baru buat if not hari hari buat hari hari suck
            #     Country(formatted_line[data_extraction_index_list[3]],
            #             formatted_line[data_extraction_index_list[4]])
        
            # City(formatted_line[data_extraction_index_list[0]], formatted_line[data_extraction_index_list[1]],
            #      formatted_line[data_extraction_index_list[2]], formatted_line[data_extraction_index_list[3]],
            #      formatted_line[data_extraction_index_list[5]], formatted_line[data_extraction_index_list[6]])


if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    # print(Country.countries)
    # print(City.cities)
    # test_example_countries_and_cities()