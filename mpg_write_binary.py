#!/usr/bin/env python3
import pickle

def get_miles_driven():
    while True:
        miles_driven = float(input("Distance:  "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    #Gets input from user
def get_gallons_used():
    while True:
        gallons_used = float(input("Gallons:  "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
print()
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        mpg = round((miles_driven / gallons_used), 2)
        print("MPG:\t" + str(mpg))
        print()
        #list for mpg
        mpg_list = [["Distance", "Gallons", "MPG"],
                    [miles_driven, gallons_used, mpg]]
        for trips in mpg_list:
            print(trips[0],"\t", trips[1],"\t", trips[2])

        #connects to the bin file
        with open("trips.bin", "wb") as file:
            pickle.dump(trips, file)

        with open("trips.bin", "rb") as file:
           trips = pickle.load(file)

        more = input("More entries? (y or n): ")
    
    print("Bye")

if __name__ == "__main__":
    main()