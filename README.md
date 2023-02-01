# ACM Research coding challenge (Spring 2023)

### Brainstorming and Background Knowledge:
Looking at this data, and given it's a .csv (Comma-Separated Values) file, I would use Python to read the data. In HackUTD the project my group worked on was taking
UTD Grades professor data, stored in .csv files and combining it with the results of a professor on RateMyProfessor.com all in one screen as many students use both
websites when searching for professors for their classes. This was all done in Python, though the project itself was incomplete by the end of the event. But I learned
about Python's many applications in file reading and writing.

### Plan:
With the data about the stars, I will write a Python program that prompts the user to enter a star type and returns the average Temperature, Luminosity, Radius, and
Absolute Visual Magnitude of the star. The program will also find other attributes of the star using Physics equations (which utilize the averages the 4 given attributes) and display that information back to the user.

### Physics Equations to Use:
Surface Area of Star = 4pi * r^2
Volume of Star = 4/3 * pi * r^3
Wien's Displacement Law
Stefan-Boltzmann's Law

### Program Performance and Display
The program runs well utilizing 4 functions and returns information on the average Temperature, Luminosity, Radius, and Absolute Visual Magnitude along with the average
Wavelength Peak and Black-Body Radiant Emittance using Wien's Displacement Law and Stefan-Boltzmann's Law respectively. Additionally, the program calculates the surface
area and volume of the star using the equations for a sphere, though stars are not exact sphereical object, but resemble closely to them.

The display of the information is pretty simple. Lines (---) are used to separate different sections of information. Each value has its respective unit of measurement.
Overall the program completes the basic goals I had with this challenge.

### Extra Features/Missed Opportunities
There are more Physics equations that can be used with the found information. While searching through different Physics equations, it was difficult to find values that
could be found with the already found inputs. Wien's Displacement Law and Stefan-Boltzmann's Law were the only immediate equations that could be used. However, there
exists derivable equations that contain just the found inputs. And if this program is to go futher in displaying information about each star to the user, it needs to
utilize those derivable equations.

Additionally there is the opportunity to write another program that returns derivable Physics equations for use in the main program. Utilizing a list of all existing
Physics Laws, this program can conduct a search through the list with given inputs or attempt to derive and equation with the given inputs.

>Psudecode:
>```
{
    function deriveEq (value to find, input1, input 2, ...)
	foreach index in eqList:
		if (index.contains(value to find, input1, input 2, ...)):
			return index
		else if (index.contains(value to find + "=") || index.contains(input1 + "=") || index.contains(input2 + "=") || ...):
			index
	return "No Derivable Equation Found"
}
```