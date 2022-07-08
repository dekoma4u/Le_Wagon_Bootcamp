import random
class OrangeTree:
    def __init__(self, age, height, fruits):
        self.age = age 
        self.height = height
        self.fruits = fruits 
        self.dead = True
        
    def pick_a_fruit(self):
        return 
       
    def one_year_passes(self):
        #tall = 0
        #for one in self.age:
        if self.age <= 1:
                #self.age += 1
            return self.age
        #elif self.age >= 1 and self.age <= 4:
            #height of the tree
            #return self.height, "==> Height"
        elif self.age in range(1, 5):
            #self.fruits == 100
            return self.age, "==> age"
        elif self.age in range(5, 9):
            return f"Tree can produce {self.fruits} fruits a year"
            #Checking for age above 10 and notifying for death from 50
        elif self.age in range(10, 101): 
            self.height = 10
            #self.fruit
            return f"Tree is {self.age}, can produce {self.fruits} fruits a year. Stops producing from the 15th year and can die from 50"

        else:
            self.age == random.randrange(100, 1000)
            return "is the tree dead?", self.dead
        
                


    
check = OrangeTree(age=115, height=11, fruits=100)
check.one_year_passes()