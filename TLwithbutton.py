from gpiozero import Button, TrafficLights
from time import sleep

Car_red = 18
Car_amber = 17
Car_green = 27
Pd_red = 12
Pd_green = 6
button_pin = 13

Car = TrafficLights(Car_red, Car_amber, Car_green)
Ped = TrafficLights(Pd_red, 14, Pd_green)
button = Button(button_pin)

Car.off()
Ped.off()

try:
    def change():
        Car.green.off()
        Car.amber.on()
        print ("Car yellow, Pedestrian red")
        sleep(1)
        Car.amber.off()
        Car.red.on()
        Ped.red.off()
        Ped.green.on()
        print("Car red, Pedestrian green")
        sleep(5)
        Car.red.off()
        Car.amber.on()
        print("Car yellow, Pedestrian green")
        sleep(1)
        Car.amber.off()
        Ped.green.off()
    while True:
        Car.green.on()
        Ped.red.on()
        print ("Car green, Pedestrian red")
        button.wait_for_press()
        print("button Press")
        change()

finally:
    Car.off()
    Ped.off()
    Car.close()
    Ped.close()
    button.close()
