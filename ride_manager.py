class Ride_Manager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__available_vehicle_cars = []
        self.__available_vehicle_bus = []
        self.__available_vehicle_bike = []
        self.__available_vehicle_cng = []
    
   

    
    def get_available_cars(self):
        return self.__available_vehicle_cars

    def add_vehicle(self,vehicle_type,vehicle):
        if(vehicle_type=='car'):
           self.__available_vehicle_cars.append(vehicle)
        elif(vehicle_type=='bus'):
           self.__available_vehicle_bus.append(vehicle)
        elif(vehicle_type=='bike'):
           self.__available_vehicle_bike.append(vehicle)
        elif(vehicle_type=='cng'):
           self.__available_vehicle_cng.append(vehicle)
    

    def match_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            if len(self.__available_vehicle_cars) == 0:
                print("Sorry No cars are available\n\n")
                return False
            else:
                for car in self.__available_vehicle_cars:
                    print('potential : ',rider.location, car.driver.location)
                    if(abs(rider.location - car.driver.location) <= 30):
                        print("Find a Match")



uber = Ride_Manager()