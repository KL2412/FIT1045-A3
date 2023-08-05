from locations import create_example_countries_and_cities
from locations import CapitalType, Country, City
from city_country_csv_reader import create_cities_countries_from_CSV
from vehicles import create_example_vehicles
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from trip import Trip, create_example_trips
from path_finding import find_shortest_path
from map_plotting import plot_trip
import time

def print_progress_bar(fraction_downloaded:float, replaceable):
    """
        Purpose: Print progress bar slowly (with delays per every loading bars)
        Argument 1: fraction_downloaded: Float
        Argument 2: replaceable: String
        Return Value: None
        Function Body: Print the progress bar according to the travel time
    """
    #bar size is alsways 50
    bar_size = 50

    #assigning last character by determining if it is replaceable
    end_char = None
    if replaceable:
        end_char = '\r'
    else:
        end_char = '\n'
    
    #progress bar printing
    progress = int(fraction_downloaded * bar_size)
    print("{:3.0f}".format(100*fraction_downloaded) + '% ['+ '*'*progress + ' '*(bar_size-progress)+']', flush=True, end=end_char)

#Main Function
def main_function():
    #create cities and countries from CSV file
    create_cities_countries_from_CSV('worldcities_truncated.csv')

    #create Countries and Cities
    create_example_countries_and_cities()

    #create example Vehicles
    example_vehicles = create_example_vehicles()

    #create example Trips
    example_trips = create_example_trips()

    #creating list for added vehicles or trips
    list_vehicles = []
    list_trips = []

    while True:
        #print Menu
        print("\nMenu Screen \n" + "-"*20)
        print("1. Create a fleet of vehicles")
        print("2. Create a trip")
        print("3. Find the fastest vehicle for the trip")
        print("4. Plot the trip")
        print("5. Simulate a trip")
        print("6. Exit")
        
        #prompt and validate user input using try except
        while True:
            try:
                user_input = int(input("\nSelect your choice [1-5]: "))
                while(user_input < 1 or user_input > 5):
                    print("Invalid input!")
                    user_input = int(input("\nSelect your choice [1-5]: "))
                if 1<= user_input <= 5:
                    break
            except:
                print("Invalid input!")
        
        #create vehicle
        if user_input == 1: 
            #print sub menu
            print("\nModes of creating vehicles: ")
            print("1. By choosing from example vehicles")
            print("2. By creating vehicles with custom parameters")

            #prompt and validate user input
            mode_vehicle_input = int(input("\nSelect your choice [1-2]: "))
            assert mode_vehicle_input >= 1 and mode_vehicle_input <= 2

            #choose from example vehicle
            if mode_vehicle_input == 1:
                #print example vehicles for user to choose
                print("\nList of example vehicles: ")
                iterator = len(example_vehicles)-len(example_vehicles)+1
                for display_example_vehicles in example_vehicles:
                    print("{}. {}".format(iterator, display_example_vehicles))
                    iterator += 1
                
                #prompt and validate user's input for example vehicle choice
                valid_sample_vehicle_input = False
                while not valid_sample_vehicle_input:
                    select_from_example_vehicle_input = int(input("\nSelect your choice [1-3]: "))
                    valid_sample_vehicle_input = 1 <= select_from_example_vehicle_input <= 3
                    if select_from_example_vehicle_input == 1:
                        list_vehicles.append(example_vehicles[0])
                    elif select_from_example_vehicle_input == 2:
                        list_vehicles.append(example_vehicles[1])
                    elif select_from_example_vehicle_input == 3:
                        list_vehicles.append(example_vehicles[2])
                    if not valid_sample_vehicle_input:
                        print("Please enter only integer between 1 to 3(inclusive)")
                        
            #creating vehicles with custom parameters
            elif mode_vehicle_input == 2:
                print("\nList of vehicles can be created: ")
                print("1. CrappyCrepeCar")
                print("2. DiplomacyDonutDinghy")
                print("3. TeleportingTarteTrolley")

                #prompt and validate vehicle type chosen by user
                valid_vehicle_type = False
                while not valid_vehicle_type:
                    create_vehicle_input = int(input("\nSelect your choice [1-3]: "))
                    valid_vehicle_type = 1 <= create_vehicle_input <= 3

                    #create crappycrepecar vehicle
                    if create_vehicle_input == 1:
                        crappy_speed_vehicle_input = int(input("Enter speed: "))
                        list_vehicles.append(CrappyCrepeCar(crappy_speed_vehicle_input))

                    #create DiplomacyDonutDinghy vehicle
                    elif create_vehicle_input == 2:
                        diplomacy_country_speed_vehicle_input = int(input("Enter country speed: "))
                        diplomacy_between_primary_speed_vehicle_input = int(input("Enter between primary speed: "))
                        list_vehicles.append(DiplomacyDonutDinghy(diplomacy_country_speed_vehicle_input, diplomacy_between_primary_speed_vehicle_input))

                    #create TeleportingTarteTrolley vehicle
                    elif create_vehicle_input == 3:
                        teleporting_travel_time = int(input("Enter travel time: "))
                        teleporting_max_distance = int(input("Enter max distance: "))
                        list_vehicles.append(TeleportingTarteTrolley(teleporting_travel_time, teleporting_max_distance))
                    
                    #print error message if invalid choice is entered
                    else:
                        print("Please enter only integer between 1 to 3(inclusive)")
        #create trip
        elif user_input == 2:
            #print sub menu
            print("\nModes of creating trips")
            print("1. By choosing from example trips")
            print("2. By manually adding all cities")
            print("3. By finding a shortest path between 2 given cities for 1 vehicle or a fleet of vehicles")

            #prompt and validate user input choice
            mode_trip_input = int(input("\nSelect you choice [1-3]: "))
            assert mode_trip_input >= 1 and mode_trip_input <= 3

            #choose trip from example trips
            if mode_trip_input == 1:
                #print example trips
                print("\nList of example trips: ")
                iterator = len(example_trips)-len(example_trips)+1
                for display_example_trips in example_trips:
                    print("{}. {}".format(iterator, display_example_trips))
                    iterator += 1
                
                #prompt and validate user's choice on example trips
                valid_example_trip = False
                while not valid_example_trip:
                    select_from_example_trips_input = int(input("\nSelect your choice [1-4]: "))
                    valid_example_trip = 1 <= select_from_example_trips_input <= 4

                    #append chosen trip to the list 
                    if select_from_example_trips_input == 1:
                        list_trips.append(example_trips[0])
                    elif select_from_example_trips_input == 2:
                        list_trips.append(example_trips[1])
                    elif select_from_example_trips_input == 3:
                        list_trips.append(example_trips[2]) 
                    elif select_from_example_trips_input == 4:
                        list_trips.append(example_trips[3])  
                    #print error message if invalid trip is chosen 
                    else:
                        print("Please enter only integer between 1 to 4(inclusive)")

            #add trip by manually adding all cities
            elif mode_trip_input == 2:
                #declare variables needed
                cityAddedCount = 0
                continueAddingCities = True

                #keep continue adding cities until user wants to stop
                while continueAddingCities == True:
                    #prompt user to choose city by calling a method 
                    chosen_city = prompt_country(cityAddedCount)

                    if cityAddedCount == 0:
                        #first country added is departure city
                        trip = Trip(chosen_city)
                    else:
                        #non-first added country is added into next_city
                        trip.add_next_city(chosen_city)

                    cityAddedCount += 1

                    #ask user if they want to continue
                    continueFlag = input("Do you want to continue adding cities to your trip?[Y-Yes, N-No]: ")
                    continueAddingCities = continueFlag == "Y" or continueFlag == "y"

                #print final added trip for user to review
                print("\n-------- Added Trip --------")
                print(trip)
                print("----------------------------")

                #add the trip into list_trip
                list_trips.append(trip)

            #add trip by finding the shortest path of each vehicle added
            elif mode_trip_input == 3:
                departure_arrival = [None, None]
                #prompt user for departure and arrival locations
                for cityAddedCount in range(2):
                    chosen_city = prompt_country(cityAddedCount)
                    if cityAddedCount == 0:
                        departure_arrival[0] = chosen_city
                    else:
                        departure_arrival[1] = chosen_city
                
                #print all the shortest trips available for each vehicles
                print('\n-----------')
                print('Valid Trips')
                print('-----------')
                valid_trips = 0
                for index, vehicle in enumerate(list_vehicles):
                    shortest_path = find_shortest_path(vehicle, departure_arrival[0], departure_arrival[1])
                    if shortest_path != None:
                        print(f"{index + 1}. {shortest_path}")
                        valid_trips += 1
                
                #prompt user choice and add the trip to list_trips if the trip is valid
                if valid_trips > 0:
                    while not 1 <= path_choice <= valid_trips:
                        path_choice = int(input(f"\nSelect your choice [1-{valid_trips}]: "))
                    for index, vehicle in enumerate(list_vehicles):
                        shortest_path = find_shortest_path(vehicle, departure_arrival[0], departure_arrival[1])
                        if shortest_path != None:
                            if index == path_choice - 1:
                                #print the trip chosen by the user
                                print("\n-------- Added Trip --------")
                                print(shortest_path)
                                print("----------------------------")
                                list_trips.append(shortest_path)
                #print error message if the user cannot get from departure location to arrival location with the existing vehicles 
                else:
                    print(f"There is no valid trips for your vehicles to go from {departure_arrival[0]} to {departure_arrival[1]}")
            #error message for unavailable input from user
            else:
                print("Input is not available!") 

        #find fastest vehicle for the trips in list_trips
        elif user_input == 3:
            #print the fastest vehicle for each trip
            if(list_trips != []):
                for trip in list_trips:
                    vehicle, duration = trip.find_fastest_vehicle(list_vehicles)
                    print("The trip {} will take {} hours with {}".format(trip, duration, vehicle))
            #error message for no trip in list_trip
            else:
                print("No data found!")  

        #plot all trips on map
        elif user_input == 4:    
            if(list_trips != []):
                for trip in list_trips:
                    plot_trip(trip)
            #error message for no trip in list_trips
            else:
                print("No data found!")

        #simulate the trip with progress bar
        elif user_input == 5:
            if(list_trips != []):
                for trip in list_trips:
                    vehicle, duration = trip.find_fastest_vehicle(list_vehicles)
                
                    time_between_updates = 0.1 
                    download_speed = 0.1
            
                    progress_between_updates = download_speed * time_between_updates 
                    
                    size_downloaded = 0
                    print("{}: ".format(trip))
                    while size_downloaded < duration:
                        time.sleep(time_between_updates)
                        size_downloaded = min(duration, size_downloaded + progress_between_updates)
                        fraction_downloaded = size_downloaded / duration
                        print_progress_bar(fraction_downloaded, True)
                    print("Trip {} with {} is successful! \n".format(trip, vehicle))
            else:
                 print("No data found!")

        #exit program
        elif user_input == 6:
            return "Program is exited!"

        #error message when user inputted invalid choice
        else:
            print("Input is not available!")

def prompt_country(cityAddedCount):
    """
        Purpose: Prompt the user to choose cities
        Argument 1: cityAddedCount: Int
        Return Value: chosen_city: City
        Function Body: Print all countries for user to choose
                        print all the cities in the chosen country
                        return the selected city
    """
    if cityAddedCount == 0:
        departure_arrival = "Departure"
    else:
        departure_arrival = "Arrival"
        
    #print all countries
    print('\n-----------------')
    print(f'{departure_arrival} Country')
    print('-----------------')
    for index, country in enumerate(Country.countries.values()):
        print(f'{index + 1}. {country.name}')
    
    #prompt and validate user choice of country
    valid_country_choice = False
    while not valid_country_choice:
        country_choice = int(input("Select you choice [1-" + str(len(Country.countries)) + "]: ")) - 1
        valid_country_choice = 0 <= country_choice <= (len(Country.countries) - 1)
        if not valid_country_choice:
            print(f"Please enter only integer between 1 to {str(len(Country.countries))}(inclusive)")

    for index, country in enumerate(Country.countries.values()):
        if index == country_choice:
            chosen_country = country
    
    #print all the cities in the chosen country
    print()
    print('--------------')
    print(f'{departure_arrival} City')
    print('--------------')
    num_of_cities_in_selected_country = 0
    for city in City.cities.values():
        if city.country == chosen_country.name:
            print(f'{num_of_cities_in_selected_country + 1}. {city.name}')
            num_of_cities_in_selected_country += 1
    
    #prompt and validate user choice of country
    valid_city_choice = False
    while not valid_city_choice:
        city_choice = int(input("Select you choice [1-" + str(num_of_cities_in_selected_country) + "]: ")) - 1
        valid_city_choice = 0 <= city_choice <= (num_of_cities_in_selected_country - 1)
        if not valid_city_choice:
            print(f"Please enter only integer between 1 to {num_of_cities_in_selected_country}(inclusive)")

    #look for the city chosen in City.cities() and assign it to chosen_city
    city_counter_in_selected_country = 0
    for city in City.cities.values():
        if city.country == chosen_country.name:
            if city_counter_in_selected_country == city_choice:
                chosen_city = city
            city_counter_in_selected_country += 1
    
    #print the city chosen
    print(f'\n{departure_arrival} City chosen is {chosen_city.name}')
    time.sleep(1)

    #return the city chosen
    return chosen_city

#Run command
if __name__ == "__main__":
    main_function()
