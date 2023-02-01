from collections import Counter
import csv
import math
from operator import countOf
Temperature = 0.0;
Luminosity = 0.0;
Radius = 0.0;
AbsoluteMagnitude = 0.0;
StarType = int(input("Star Type (6 classes ranging from 0-5): "))
Star = ""
def printLine():
    print("-----------------------------------------------------------------------------------------------------------------------")
def findStar(st, sr):
    if st == 0:
        print("Star Type: Brown Dwarf")
        return "Brown Dwarf"
    elif st == 1:
        print("Star Type: Red Dwarf")
        return "Red Dwarf"
    elif st == 2:
        print("Star Type: White Dwarf")
        return "White Dwarf"
    elif st == 3:
        print("Star Type: Main Sequence")
        return "Main Sequence"
    elif st == 4:
        print("Star Type: Supergiant")
        return "Supergiant"
    elif st == 5:
        print("Star Type: Hypergiant")
        return "Hypergiant"
def calcStars(st, temp, lum, rad, absm, sr):
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for row in csv_reader:
            if st == int(f'{row["Star type"]}'):
                temp += float(f'{row["Temperature (K)"]}')
                lum += float(f'{row["Luminosity(L/Lo)"]}')
                rad = float(f'{row["Radius(R/Ro)"]}')
                absm = float(f'{row["Absolute magnitude(Mv)"]}')
                count += 1
        temp /= count
        lum /= count
        rad /= count
        absm /= count
        print("Average Temperature of " + sr + ": " + str(temp) + " K")
        print("Average Luminosity of " + sr + " With Respect to the Luminosity of the Sun: " + str(lum) + " L/Lo")
        print("Average Radius of " + sr + " With Respect to the Radius of the Sun: " + str(rad) + " R/Ro")
        print("Average Absolute Magnitude of " + sr + ": " + str(absm) + " Mv")
        print("Average Wavelength Peak of " + sr + ": " + str(0.002898/temp) + " m")
        print("Average Black-Body Radiant Emittance of " + sr + ": " + str((5.67*(10**(-8)))*(temp**4)) + " W/m^2")
        print("Average Surface Area of " + sr + ": " + str(4.0*math.pi*((rad*(6.9551 * (10**8)))**2)) + " m^2")
        print("Average Volume of " + sr + ": " + str((4.0/3.0)*math.pi*((rad*(6.9551 * (10**8)))**3)) + " m^3")
def checkError(st):
    while st > 5 or st < 0:
        printLine()
        st = int(input("Please enter a Star Type ranging from 0-5: "))
    return st
StarType = checkError(StarType)
printLine()
Star = findStar(StarType, Star)
printLine()
calcStars(StarType, Temperature, Luminosity, Radius, AbsoluteMagnitude, Star)
printLine()
print("Lo = 3.828 x 10^26 Watts (Avg Luminosity of Sun)")
print("Ro = 6.9551 x 10^8 m (Avg Radius of Sun)")