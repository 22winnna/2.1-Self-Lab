#!/usr/bin/env python3
import csv

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

def write_trips(mpg_list):
    #connects to the csv file
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(mpg_list)
#reads the csv file
def read_trips(mpg_list):
        with open("trips.csv", newline="") as file:
            reader = csv.reader(file)
            
#lists the information in the csv
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
        write_trips(mpg_list)
        read_trips(mpg_list)
        list_trips(mpg_list)
    
    print("Bye")

if __name__ == "__main__":
    main()