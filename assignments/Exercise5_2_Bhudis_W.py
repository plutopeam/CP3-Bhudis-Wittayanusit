displacement = float(input("Displacement(S) : "))
time = float(input("Time(t) : "))
if (displacement >= 1  and time >= 1):
    velocity = displacement/time
    print(velocity, "(m/s or km/hr)")
else:
    print("Please fill values more than 1 !!!")
