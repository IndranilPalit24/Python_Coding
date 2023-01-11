class Process:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        '''self.price = price'''

        #If price is negative then there will be a problem so to counter that we need to have something put max function
        self._price = price

        # now how do we get the property decorator


    def complete_Specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price,0)



    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")


    def full_name(self):
        return f"{self.brand}{self.model_name}"


phone1 = Process("Nokia",1100, -1000)
print(phone1.complete_Specification())
