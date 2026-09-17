force = float(input("Enter a force in newtons: "))
distance = input("Enter a distance in meters:")
distance = float(distance)
work = force * distance
print("work:", work)
print(type(work))

time = 6
power = work / time
print("power:" , power)
print(type(power))

