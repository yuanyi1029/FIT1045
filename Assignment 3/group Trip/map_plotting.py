import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def plot_trip(trip: Trip, projection="merc", line_width=2, colour="c") -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    Arguments:
        -trip: Trip object that will be plotted on the map
        -projection: String value representing the map projection
        -line_width: Integer value representing the the line width of the plotted lines
        -colour: String value representing the colour of plotted lines
    """
    city_name_list = []
    longitude_list = []
    latitude_list = []

    for city in trip.cities:
        city_name_list.append(city.name)
        longitude_list.append(float(city.longitude))
        latitude_list.append(float(city.latitude))

    padding = 10

    m = Basemap(projection=projection, llcrnrlat=min(latitude_list) - padding, urcrnrlat=max(latitude_list) + padding,
                llcrnrlon=min(longitude_list) - padding, urcrnrlon=max(longitude_list) + padding)

    # The latitude and longitude of each city visited will be added to the longitude_list and latitude_list. The
    # lower and higher bounds of the map's longitude and latitude are then set using the minimum (lower boundary)
    # and maximum (upper boundary) values of the longitude_list and latitude_list, padded with 20 degrees to
    # prevent any cities from appearing on the map's border.

    m.drawmapboundary(fill_color='#A6CAE0')
    m.fillcontinents(color='grey', alpha=0.3)

    x, y = m(longitude_list, latitude_list)
    plt.plot(x, y, 'co')
    m.plot(x, y, linewidth=line_width, color=colour)

    for index in range(len(trip.cities)):
        plt.annotate(city_name_list[index], xy=m(longitude_list[index], latitude_list[index]), ha="center", va="center")

    # Each city on the trip is labelled on the map with its name and a marker with its coordinates, and then lines
    # are drawn linking the cities traveled.

    file_name = "map"

    for city in trip.cities:
        file_name += f"_{city.name}"

    plt.savefig(f"{file_name}.png")
    plt.show()
    plt.clf()

    # The finished map with the generated trip lines is then saved with the file_name, which has the format
    # map_city1_city2_city3_..._cityX.png, and the map is cleared off to avoid map overlap when a new map is generated.


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)
