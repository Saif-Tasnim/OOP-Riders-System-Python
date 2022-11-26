import random


class BRTA:
    def __init__(self) -> None:
        self.__licenses = {}
    
    def driving_test(self,email):
        score = random.randint(0,100)
        if score>=33:
            print("Congrats!!! You have passed" , score)
            license_no = random.randint(100000,900000)
            self.__licenses[email] = license_no
            return license_no
        
        else:
            print("Sorry ... Failed. Better Luck Next Time" , score)
            return False
    

    def validate_license(self,email,license):
        for key,value in self.__licenses.items():
            if key == email and value == license:
                return True
            
            
        return False
        