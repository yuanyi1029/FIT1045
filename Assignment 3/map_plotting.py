import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot


def plot_trip(trip: Trip, projection='merc', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """
    longitude_list = []
    latitude_list = []

    for city in trip.cities:
        longitude_list.append(float(city.longitude))
        latitude_list.append(float(city.latitude))

    padding = 20

    path_map = Basemap(llcrnrlat=min(latitude_list) - padding, urcrnrlat=max(latitude_list) + padding,
                       llcrnrlon=min(longitude_list) - padding, urcrnrlon=max(longitude_list) + padding,
                       projection=projection)

    path_map.drawcoastlines()

    for index in range(len(longitude_list) - 1):
        path_map.drawgreatcircle(longitude_list[index], latitude_list[index], longitude_list[index + 1],
                                 latitude_list[index + 1], linewidth=line_width, color=colour)

    file_name = "map"

    for city in trip.cities:
        file_name += f"_{city.name}"

    matplotlib.pyplot.savefig(f"{file_name}.png")
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)