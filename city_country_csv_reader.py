from locations import City, Country, test_example_countries_and_cities
import csv

def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Purpose: Reads a CSV file given its path and creates instances of City and Country for each line.
    Argument: path_to_csv (string)
    Return value: None
    Funtion body: A list named content is created.
                  csvfile is then read using csv.reader then assgined to csv_reader.
                  First line of the csvfile is then assigned to a variable called headers to be the header.
                  For every row in csv_reader the value for key and the value in zip of the headers and row is assgined to row_data,
                  row_data is then appended to the list content.
                  For every city in the list content, an instance for the name, latitude, longitude, country, capital_type and 
                  city_id of the city is created as well as an instance for the country and is03 is create for a country.
    """
    content = []
    with open(path_to_csv) as csvfile:
        #read csv file into csv_reader with csv.reader
        csv_reader = csv.reader(csvfile)

        #assign first line of the csv file as the header
        headers = next(csv_reader)

        #save every content here into a list of dictionary (content)
        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)

        #create instances for all city
        for city in content:
            City(name = city['city_ascii'], latitude = city['lat'], longitude = city['lng'], country = city['country'], capital_type = city['capital'], city_id = city['id'])
            Country(city['country'], city['iso3'])

if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()
