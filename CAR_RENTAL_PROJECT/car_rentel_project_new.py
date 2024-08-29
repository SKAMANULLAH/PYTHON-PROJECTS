class rent_:
    def __init__(self):
        self.b = int(input("Enter number bikes that you want :- " ))
        if self.b < 1001: 
           print(f"The total price for your {self.b} number of bikes is {(self.b)*100}")
        else:
            print("Sorry, wee have only 1000 bikes!")
class rent(rent_):
   def __init__(self):
     print("""
          1.Display available stocks
          2.Request a bike for rent (1 bike => 100 , Enter no of bikes)
          3.Finish """)    
     self.a = int(input("Enter Your Choice:- "))
   def bike(self):
        if self.a==1: 
             print("The total number of available bikes is 1000 ")
             self.__init__()
        if self.a == 2:
            super().__init__()
        if self.a == 3:
            print("Thanks for Visiting:-")
obj = rent()
obj.bike()




    