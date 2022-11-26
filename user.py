import hashlib
import random

from vehicles import Bike
from brta import BRTA
from vehicles import Car
from vehicles import Cng
from ride_manager import uber


license_authority = BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open("user.txt","a")as file:
            file.write(f'{email} {pwd_encrypted}\n')
        file.close()
        print(self.name , "User Created")

    @staticmethod
    def log_in(email,password):
        store_pass = ''
        with open("user.txt","r")as file:
            lines = file.readlines()
            for line in lines:
             if email in line:
               store_pass = line.split(' ')[1]
                   
        file.close()
        print(store_pass)

        log_in_pass = hashlib.md5(password.encode()).hexdigest()

        if store_pass == log_in_pass:
            print("Logged In Succcessfully\n")
        else:
            print("Wrong Password\n")

class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.money = balance
    
    def set_location(self,location):
        self.location = location
    
    def get_location(self):
        return self.location
    
    def request_trip(self,destination):
        pass
    
    def start_trip(self,fare):
        self.balance -=fare


class Driver(User):
    def  __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valide_driver =  license_authority.validate_license(email,license)
        self.earning = 0

    def driving_test(self):
       result =  license_authority.driving_test(self.email)

       if result == False:
         print("Sorry.. Failed")
       else:
        self.license = result
        self.valide_driver = True
   
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
    
        if self.valide_driver == True:
          
          if vehicle_type == 'car':
            # new_vehicle = Car(vehicle_type,rate,self.email,license_plate)
            new_vehicle = Car(vehicle_type,rate,self,license_plate)
            uber.add_vehicle(vehicle_type,new_vehicle)
          elif vehicle_type== 'bike':
            new_vehicle = Bike(vehicle_type,rate,self,license_plate)
            uber.add_vehicle(vehicle_type,new_vehicle)
          else:
            new_vehicle = Cng(vehicle_type,rate,self,license_plate)
            uber.add_vehicle(vehicle_type,new_vehicle)
        else:
            print("You are not valid")

    def start_trip(self,destination,fare):
        self.earning+=fare
        self.location = destination
    


rider1 = Rider("rider1","rider1@gmail.com","rider1234",random.randint(0,100),5000)
# print(dir(rider1))


rider2 = Rider("rider2","rider2@gmail.com","rider1234",random.randint(0,100),1000)
# print(dir(rider1))


driver1 = Driver("driver1","driver1@gmail.com","driver1234",random.randint(0,100),100)
driver1.driving_test()
driver1.register_a_vehicle('car',1245,10)

driver2 = Driver("driver2","driver2@gmail.com","driver1234",random.randint(0,100),100)
driver2.driving_test()
driver2.register_a_vehicle('car',1245,10)


driver3 = Driver("driver3","driver3@gmail.com","driver1234",random.randint(0,100),100)
driver3.driving_test()
driver3.register_a_vehicle('car',1245,10)

driver4 = Driver("driver4","driver4@gmail.com","driver1234",random.randint(0,100),100)
driver4.driving_test()
driver4.register_a_vehicle('car',1245,10)

print(uber.get_available_cars())

uber.match_a_vehicle(rider1,'car',90)
