"""This converts a temperature in Celsius to a temperature in Fahrenheit """

done = False

while not done:
    
    cTemp = input("Input a Celsius temperature or 'e' to exit ")
    if cTemp == "e":
        print("Exiting")
        done = True
    else:
        fTemp = (9/5) * float(cTemp) + 32
        print(str(cTemp)+"C is "+str(fTemp)+"F") 
   
