elevation_gain = 0
count = int(input("Enter the total number of steps "))

for i in range(count):
    n = int(input("Enter the starting point: "))
    a = int(input("Enter the altitude of point"))
    b = a-n
    if b>0:
        elevation_gain = elevation_gain + b
        print("elevation gain: ",elevation_gain)
    


        
                  


