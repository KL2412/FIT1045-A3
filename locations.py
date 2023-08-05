from __future__ import annotations 
from enum import Enum
from geopy.distance import great_circle
from math import ceil as ceil

class CapitalType(Enum):
    """
    The different types of capitals (e.g. "primary").
    """
    primary = "primary"
    admin = "admin"
    minor = "minor"
    unspecified = ""

    def __str__(self) -> str:
        """
        Purpose: Used for determine the different types of capitals
        Argument: Self object
        Return Value: string
        """
        return self.value


class Country():
    """
    Represents a country.
    """

    countries = dict() # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Purpose: Creates an instance with a country name and a country ISO code with 3 characters.
        Argument 1: Self object || Argument 2: name (string) || Argument 3: iso3 (string)
        Return Value: None
        """
        self.name = name
        self.iso3 = iso3

        Country.countries.update({self.name: self})

    def _add_city(self, city: City):
        """
        Purpose: Adds a city to the country
        Argument 1: Self object || Argument 2: city (City object)
        Return Value: None 
        """	
        City.cities.update({city.city_id: self})

    def get_cities(self, capital_types: list[CapitalType] = None) -> list[City]:
        """
        Purpose: Returns a list of cities of this country.
        Argument 1: self object || Argument 2: capital_types
        Return Value: list[City]
        Function Body: If the list[CapitalType] is equals to None then a list called capital_types is created. For all the capitals
                       types is CapitalType, they are then added into the list capital_types. 
                       A list called return_ls is created. For all the cities in City.cities.values(), if the capital type of those 
                       cities in the list capital_types and the cities are from the given country then the cities are appended to 
                       return_ls
        """
        if capital_types == None:
            capital_types = []
            for capital in CapitalType:
                capital_types.append(capital)

        return_ls = []
        for city in City.cities.values():
            if city.capital_type in capital_types and city.country == self.name:
                return_ls.append(city)
        return return_ls

    def get_city(self, city_name: str) -> City:
        """
        Purpose: Returns a city of the given name in this country.
        Argument 1: Self object || Argument 2: city_name (string)
        Return values: City or None
        Function body: For the cities in City.cities.values(), if city.name is equals to city_name and city.country is equals to the
                       country name then the city is returned.
        """
        for city in City.cities.values():
            if city.name == city_name and city.country == self.name:
                return city
        return None

    def __str__(self) -> str:
        """
        Purpose: Returns the name of the country.
        Argument 1: Self object
        Return Value: string
        """
        return self.name


class City():
    """
    Represents a city.
    """

    cities = dict() # a dict that associates city IDs to instances.

    def __init__(self, name: str, latitude: str, longitude: str, country: str, capital_type: str, city_id: str) -> None:
        """
        Purpose: Initialises a city with the given data.
        Argument 1: Self object || Argument 2: name (string) || Argument 3: latitude (stirng) || Argument 4: longitude (string)
        Argument 5: country (string) || Argument 6: capital_type (string) || Argument 7: city_id (string)
        Return value: None
        Function body: name is assigned to self.name, latitude accepted as a float is assigned to self.latitude,
                       longitude accepted as a float is assigned to self.longitude, country is assigned to self.country,
                       city_id is assigned to self.city_id
                       For all the types in CapitalType, if the type.value is equals to capital_type then types is assigned to 
                       self.capital_type. 
        """
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.country = country
        
        for types in CapitalType:
            if types.value == capital_type:
                self.capital_type = types

        self.city_id = city_id

        City.cities.update({self.city_id: self})

    def distance(self, other_city: City) -> int:
        """
        Purpose: Returns the distance in kilometers between two cities using the great circle method, rounded up to an integer.
        Argument 1: Self object || Argument 2: other_city (City object)
        Return value: integer
        """
        return int(ceil(great_circle((self.latitude, self.longitude), (other_city.latitude, other_city.longitude)).km))

    def __str__(self) -> str:
        """
        Purpose: Returns the name of the city and the country ISO3 code in parentheses.
        Argument: Self object
        Return value: string
        Function body: For all the country in Country.countries.values(), if country.name is equals to self.country, then country.iso3
                       is assigned to countryISO
        """
        for country in Country.countries.values():
            if country.name == self.country:
                countryISO = country.iso3
        return self.name + " (" + countryISO + ")"


def create_example_countries_and_cities() -> None:
    """
    Purpose: Creates a few Countries and Cities for testing purposes.
    Argument: None
    Return value: None
    """
    australia = Country("Australia", "AUS")
    melbourne = City("Melbourne", "-37.8136", "144.9631", "Australia", "admin", "1036533631")
    canberra = City("Canberra", "-35.2931", "149.1269", "Australia", "primary", "1036142029")
    sydney = City("Sydney", "-33.865", "151.2094", "Australia", "admin", "1036074917")
    japan = Country ("Japan", "JPN")
    tokyo = City("Tokyo", "35.6839", "139.7744", "Japan", "primary", "1392685764")


def test_example_countries_and_cities() -> None:
    """
    Purpose: Assuming the correct cities and countries have been created, runs a small test.
    Argument: None
    Return value: None
    Function body: "The distance between {} and {} is {}km" is printed with each curly bracket representing Melbourne, Sydney and
                   melbourne.distance(sydney).
                   "{} is a {} capital of {}" is printed with each curly bracket representing city, city.capital_type and
                   city.country.
    """
    australia = Country.countries['Australia']
    canberra =  australia.get_city("Canberra")
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")

    print("The distance between {} and {} is {}km".format(melbourne, sydney, melbourne.distance(sydney)))

    for city in australia.get_cities([CapitalType.admin, CapitalType.primary]):
        print("{} is a {} capital of {}".format(city, city.capital_type, city.country))


if __name__ == "__main__":
    create_example_countries_and_cities()
    test_example_countries_and_cities()
