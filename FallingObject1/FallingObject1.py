t = int(input("Enter number of seconds: "))
g = float(9.80665)
#Iterative Calculations
initvel = 0
initloc = 0
for n in range(0, t+1):
    if n==0:
        print(n, initvel, "meters", initloc, "meters per second")
    else:
        newvel = initvel + g
        loc = g/2*n**2
        print(n, loc, "meters", newvel, "meters per second.")
        initvel = newvel
#output
print()
print("After", t, "seconds:")
print()
print("Iterative method:")
print(" Distance:", loc, "meters")
print(" Velocity:", initvel, "meters per second")
print()
#closed Calculations
loc2 = g/2*t**2
vel2 = g*t
print("Closed Calculation:")
print(" Distance:", loc2, "meters")
print(" Velocity:", vel2, "meters per second")
