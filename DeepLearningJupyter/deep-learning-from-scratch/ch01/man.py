class Man:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        print("Initialized!")
        
    def hello(self): 
        print("Hello " + self.name1 + "!")
        
    def goodby(self): 
        print("Goodby " + self.name1 + "!")
        
    def Goodby2(self):        
        print("Goodby " + self.name2 + "!")
        
m = Man("GouDan", "ErYa")
m.hello()
m.goodby()
m.Goodby2()
