#!/usr/bin/env python3
import pickle

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def dump_trips(mpg_list):
    #connects to the bin file
    with open("trips.bin", "wb") as file:
        pickle.dump(dump_trips, file)
        #dump.dumprows(mpg_list)
#reads the bin file
def load_trips(mpg_list):
        with open("trips.bin", "rb") as file:
           trips = pickle.load(file)
            
#lists the information in the bin
def list_trips(mpg_list):
        for trip in mpg_list:
            print(trip[0],"\t", trip[1],"\t", trip[2])

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        #list for mpg
        mpg_list = [["Distance", "Gallons", "MPG"],
                    [miles_driven, gallons_used, mpg]]
    
        more = input("More entries? (y or n): ")
        #calls functions
        dump_trips(mpg_list)
        load_trips(mpg_list)
        list_trips(mpg_list)
    
    print("Bye")

if __name__ == "__main__":
    main()