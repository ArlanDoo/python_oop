class Pet:
    
    def __init__(self, pet_name, pet_type, pet_age, pet_gender):
        self.name = pet_name
        self.type = pet_type
        self.age = pet_age
        self.gender = pet_gender
    
    def get_info(self):
            print(f"Name: {self.name}")
            print(f"Type: {self.type}")
            print(f"Gender: {self.gender}")
            print(f"Age: {self.age}")
            
class Dog(Pet):
    
    def __init__(self, dog_name, dog_type, dog_age, dog_gender, dog_breed):
        super().__init__(dog_name, dog_type, dog_age, dog_gender)
        self._breed = dog_breed
    
    def barking():
        print("Gaw-gaw-gaw!!!")


class Cat(Pet):
    
    def __init__(self, cat_name, cat_type, cat_age, cat_gender, cat_coat):
        super().__init__(cat_name, cat_type, cat_age, cat_gender)
        self._coat = cat_coat
    
    def meow():
        print("Meow-meow-meow!")