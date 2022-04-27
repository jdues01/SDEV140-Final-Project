# Program Name: Inches to Meters Conversion
# Author: Jackson Dues
# Date: 4/21/2022
# Summary: convert a measurement in inches entered by user into meters
# Variables:
#   inches: measurement in inches entered by the user (int)
#   meters: measurement in meters (float)

def main():
    # Get measurement in inches from user
    inches = int(input("How many inches do you want to convert? "))
    while inches <= 1:
        inches = int(input("ERROR...Please enter a whole number greater than 1: "))
    # Compute meters and display result with label
    meters = inches * 0.0254
    print("Measurement in meters: ", format(meters, '.4f'))
main()
