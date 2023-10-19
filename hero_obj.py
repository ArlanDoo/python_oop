class Mario():
    
    def __init__(self, x=0, y=0, healf=4):
        self.x = x
        self.y = y
        self.healf = healf
    
    def __check_bounds__(self, event, val):
        if (event in ["left", "right"]):
            return ((self.x + val) >=0 and (self.x + val) <= 100)
        elif (event == "jump"):
            return ((self.y + val) >=0 and (self.y + val) <= 1000)
        else:
            return False        
    
    def move_left(self, step):
        if (self.__check_bounds__("left", -step)):
            self.x -= step
        #     print(f"X: {self.x}")
        # print("Move left")
    
    def move_right(self, step):
        if (self.__check_bounds__("right", step)):
            self.x += step
        #     print(f"X: {self.x}")
        # print("Move right")
    
    def jump(self, hight):
        if (self.__check_bounds__("jump", hight)):
            self.y += hight
        #     print(f"Y: {self.y}")
        # print("Move jump")
    
player = Mario()
player.move_right(100)
player.jump(50)
print(player.x, player.y) # Выведет: 100, 50