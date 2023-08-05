import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def plot_trip(trip: Trip, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Purpose:
        Plots a trip on a map and writes it to a file.
        Ensures a size of at least 50 degrees in each direction.
        Ensures the cities are not on the edge of the map by padding by 5 degrees.
        The name of the file is map_city1_city2_city3_..._cityX.png.
    Argument 1: trip: Trip
    Argument 2: projection: String - initialized to 'robin'
    Return Value: None
    Function Body: plot and trip on the map and save it to a png file 
    """

    #append all the cities in the trip into a list
    city = [trip.departure]
    for cityy in trip.next_city:
        city.append(cityy)

    #detertime which part to zoom on map
    #find the two furthest countries in the trip
    max_distance_countries = (-1, None, None) #distance, city 1, city 2
    for i in range(len(city)):
        for j in range(i + 1, len(city)):
            distance = city[i].distance(city[j])
            if distance > max_distance_countries[0]:
                max_distance_countries = (distance, city[i], city[j])

    #determine coordinates of left bottom corner and right top corner of the map
    coord = [[0, 0], [0, 0]] #leftbtm [long, lat], righttop [long, lat]
    coord[0][0] = min(max_distance_countries[1].longitude, max_distance_countries[2].longitude) - 5 #leftbottom longitude
    coord[0][1] = min(max_distance_countries[1].latitude, max_distance_countries[2].latitude) - 5 #leftbottom latitude
    coord[1][0] = max(max_distance_countries[1].longitude, max_distance_countries[2].longitude) + 5 #righttop longitude
    coord[1][1] = max(max_distance_countries[1].latitude, max_distance_countries[2].latitude) + 5 #righttop latitude

    #determine center point of the map
    longitude_centre_of_the_locations = ((max_distance_countries[1].longitude + max_distance_countries[2].longitude) / 2) % 90
    latitude_centre_of_the_locations = ((max_distance_countries[1].latitude + max_distance_countries[2].latitude) / 2) % 90

    # setup Lambert Conformal basemap.
    m = Basemap(width=100, height = 100, llcrnrlon=coord[0][0], llcrnrlat=coord[0][1], urcrnrlon=coord[1][0], urcrnrlat=coord[1][1],
            projection='lcc',lat_0=longitude_centre_of_the_locations, lon_0=longitude_centre_of_the_locations)

    # draw coastlines.
    m.drawcoastlines()

    #draw the lines connecting two cities
    for index in range(len(city) - 1):
        m.drawgreatcircle(city[index].longitude, city[index].latitude, city[index + 1].longitude, city[index + 1].latitude, linewidth=line_width, color=colour)

    #picture file name
    pic_name = 'map'
    for cityy in city:
        pic_name += '_'
        pic_name += cityy.name
    pic_name += '.png'

    #save picture into directory
    plt.savefig(pic_name)

    #clear basemap
    plt.clf()


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)
