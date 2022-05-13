# Program Name: Inches to Meters Conversion
# Author: Jackson Dues
# Date: 5/12/2022
# Summary: convert a measurement in inches entered by user into meters
# Variables:
#   inches: measurement in inches entered by the user (int)
#   meters: measurement in meters (float)

def main():
    # Get measurement in inches from user
    inches = int(input("How many inches do you want to convert? "))
    while inches < 0:
        inches = int(input("ERROR...Please enter a number greater than 0: "))
    # Compute meters and display result with label
    meters = inches * 0.0254
    print("Measurement in meters: ", format(meters, '.4f'))
main()
