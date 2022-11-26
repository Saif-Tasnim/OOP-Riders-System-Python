from abc import ABC , abstractmethod

class Vehicle(ABC):
    speed ={
            'car' : 30,
            'bike' : 40,
            'cng' : 25,
            'bus' : 35
         } 
    def __init__(self,vehicle_type,rate,driver,license_plate) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = 'avaliable'
        self.speed = self.speed[vehicle_type]
        self.license_plate = license_plate

    @abstractmethod
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finished(self):
        pass
    

   

class Car(Vehicle):
    def __init__(self, vehicle_type, rate, driver,license_plate) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type,self.license_plate,"  --- Start a trip")
       
    
    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, " --- complete a trip")



class Bike(Vehicle):
    def __init__(self, vehicle_type, rate, driver,license_plate) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type,self.license_plate,"  --- Start a trip")
       
    
    def trip_finished(self):
         self.status = "available"
         print(self.vehicle_type, self.license_plate, " --- complete a trip")


class Cng(Vehicle):
    def __init__(self, vehicle_type, rate, driver,license_plate) -> None:
        super().__init__(vehicle_type, rate, driver,license_plate)
    

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type,self.license_plate,"  --- Start a trip")
       
    
    def trip_finished(self):
         self.status = "available"
         print(self.vehicle_type, self.license_plate, " --- complete a trip")