#28/06/2025
from classes_to_use import Car
# object = A "bundle" of related attribures (varialbles) and methods (funtions)


car_1 = Car("Suzuki",2002,"deep blue",False)
car_1.turn_off_car() # this will try to turn off but it can't due is already turn off
car_1.show_state() #this will show us the state of the car at hand
car_1.drive() # this will attempt to drive but it can't due the car is turn off by default
car_1.turn_on_car() #this will turn on the car
car_1.drive() # now the car can drice due is turn on
car_1.turn_off_car() # this will try to turn off but it can't due is driving
car_1.stop() # this will stop the carr
car_1.turn_off_car()#now it can turn off due it doesnt driving or it turn on...

        