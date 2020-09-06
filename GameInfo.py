class Game:
    def __init__(self, name, regular_price, discounted_price = None, discount_percentage = None):
        self.name = name
        self.regular_price = regular_price
        self.discounted_price = discounted_price
        self.discount_percentage = discount_percentage

    
    def getCurrentPrice():
        cr_price = None
        if self.discounted_price is not None:
            cr_price = self.discounted_price
            return cr_price
        return self.regular_price
    

    def setDiscount(disc_price):
        self.discounted_price = price

    def calculateDiscount(original, discount):
        if self.discounted_price is not None:
            original = self.regular_price
            discount = self.discounted_price

            percentage = int(((original-discount) / original) * 100)

            return percentage
        else:
            print("This game is not discounted")
        


