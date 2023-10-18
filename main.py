class Pet:
    
    def __init__(self, pet_name, pet_type, pet_age, pet_gender):
        self.__name = pet_name
        self.__type = pet_type
        self.__age = pet_age
        self.__gender = pet_gender
    
    def get_info(self):
            print(f"Name: {self.__name}")
            print(f"Type: {self.__type}")
            print(f"Gender: {self.__gender}")
            print(f"Age: {self.__age}")
            
class Dog(Pet):
    
    def __init__(self, dog_name, dog_type, dog_age, dog_gender, dog_breed="Sheepdog"):
        super().__init__(dog_name, dog_type, dog_age, dog_gender)
        self.__breed = dog_breed
    
    def barking(self):
        print("Gaw-gaw-gaw!!!")


class Cat(Pet):
    
    def __init__(self, cat_name, cat_type, cat_age, cat_gender, cat_coat="Black"):
        super().__init__(cat_name, cat_type, cat_age, cat_gender)
        self.__coat = cat_coat
    
    def meow(self):
        print("Meow-meow-meow!")
        
dog = Dog("Buddy", "Male", 2, "Golden Retriever")
cat = Cat("Fluffy", "Female", 3, "Calico", "Range")

dog.barking()