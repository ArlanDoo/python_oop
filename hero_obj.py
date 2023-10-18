class GameHero():
    
    def __init__(self, name, healf, x_pos, y_pos):
        self._name = name
        self.healf = healf if healf >= 0 and healf <=4 else 0
        self.xpos = x_pos if x_pos >= 0 and x_pos <=1000 else 0
        self.ypos = y_pos if y_pos >= 0 and y_pos <=100 else 0
    
    def healf_fail(self, power_fail):
        if (power_fail and power_fail < self.healf):
            self.healf -= power_fail
        elif (power_fail and power_fail >= self.healf):
            self.healf = 0
            print("Game over")
        else:
            self.healf -= 1
        
        print(self.healf)
    
    def set_step(self, order_step):
        if (self.xpos + order_step >=0 and
            self.xpos + order_step <= 100):
            self.xpos += order_step
        
        print(self.xpos)
    
    def get_info(self):
        print(f"Hero name is {self._name}")
        print(f"Current healf: {self.healf}")
        print(f"Current level of X: {self.xpos}")
        print(f"Current level of Y: {self.ypos}")


# hero_Mario = GameHero("Mario", 33, 10, 100)
# hero_Mario.get_info()
# hero_Mario.set_step(-100)
# hero_Mario.set_step(0)
# hero_Mario.set_step(10)