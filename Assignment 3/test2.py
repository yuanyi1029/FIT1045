import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips

from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot

def plot_trip(trip: Trip, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """
    map = Basemap(projection="robin", lon_0=0)
    # map = Basemap(projection=projection, lon_0 = 100, lat_0 = 100)

    map.drawcoastlines()
    map.fillcontinents()

    # lat,lng = -37.8136,144.9631
    # xlat, xlng = map(lat, lng)
    # map.plot(xlat,xlng, "c*")
    # map.plot(lat, lng, marker='D',color='b')


    # pyplot.annotate('test', xy=(-37.8136,144.9631), xycoords="data")
    pyplot.show()
    pyplot.savefig('wow.png')

if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()
    trip1 = trips[0]

    print(trip1)
    plot_trip(trip1)

    # for trip in trips:
    #     plot_trip(trip)