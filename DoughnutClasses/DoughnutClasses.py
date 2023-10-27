class doughnut:
    '''an object of this class is a specific recipe, not an individual physical
doughnut.'''
####made default the first item           ####underscore, no
#blanks
    allowed_doughs = ['raised','cake','fritter','cruller','sour_cream'] #list of all the possible doughs
    allowed_fillings = ['none','custard','raspberry','blueberry','creme'] #list of all the possible fillings
    allowed_toppings = ['none','peanuts','sprinkles','bacon'] #list of all the possible toppings
    allowed_icings = ['none','maple','chocolate','white'] #list of all possible icings
    def __init__(self,name='',price=1.50,dough='raised',filling='none',topping = 'none',icing='none',glazed=False):
        '''constructor, parameters are name (a string) and price (a float)'''
        self.name = name
        if 0<=price<=10.00:
            self.price = price
        else:
            self.price = 1.50
        if dough in self.allowed_doughs:
            self.dough = dough
        else:
            self.dough = self.allowed_doughs[0]
        self.glazed = glazed
        if filling in self.allowed_fillings:
            self.filling = filling
        else:
            self.filling = self.allowed_fillings[0]
        if topping in self.allowed_toppings:
            self.topping = topping
        else:
            self.topping = self.allowed_toppings[0]
        if icing in self.allowed_icings:
            self.icing = icing
        else:
            self.icing = self.allowed_icings[0]
    def __str__(self):
        return (f'{self.name}{self.icing}{self.glazed}{self.filling}{self.dough}{self.topping}{self.price}') #complete this with the other attributes
    def setDough(self,newDough):
        if newDough in self.allowed_doughs:
            self.dough = newDough
        return self.dough
    def setPrice(self,newPrice):
        if 0<=newPrice<=10.00:
            self.price = newPrice
        else:
            pass #leave price unchanged
    def setIcing(self,icing):
        if icing in self.allowed_icings:
            self.icing = icing #check allowed values

        else:
            self.icing = self.allowed_icings[0] #defaulting icing
        return self.icing
    #add functions to change the other attributes (after checking) and to report (return) each attribute
    def setName(self, newName):
        self.name = newName
        return self.name
    def setFilling(self, newFilling):
        if newFilling in self.allowed_fillings:
            self.filling = newFilling
        else:
            self.filling = self.allowed_fillings[0] #default
        return self.filling
    def setGlazed(self, newGlazed):
        self.glazed = newGlazed
        return self.glazed
    def setTopping(self, newTopping):
        if newTopping in self.allowed_toppings:
            self.topping = newTopping
        else:
            self.topping = self.allowed_toppings[0]
        return self.topping
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getDough(self):
       return self.dough
    def getFilling(self):
        return self.filling
    def getTopping(self):
        return self.topping
    def getIcing(self):
        return self.icing
    def getGlazed(self):
        return self.glazed
if __name__ == '__main__':
    menu = []
    menu.append(doughnut('maple_log',1.25))
    menu.append(doughnut('Boston_creme',1.15,'raised','custard','none',False))
    menu.append(doughnut('bacon_maple',1.75))
    for option in menu:
        print(option)
    print()
    menu[1].setDough('cake')
    menu[1].setPrice(0.90)

for option in menu:
    print(option)
testing1 = doughnut('checking1',11.50,filling='custard')
testing2 = doughnut('checking2',1.50,filling='mud')
print(testing1)
print(testing2)
testing2.setPrice(3.45)
