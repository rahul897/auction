class Bid:
    def __init__(self, buyer, auction, amount):
        self.buyer = buyer
        self.auction = auction
        self.amount = int(amount)

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __eq__(self, other):
        return self.buyer == other.buyer and self.auction == other.auction

    def __cmp__(self, other):
        return self.buyer == other.buyer and self.auction == other.auction

    def __hash__(self):
        return self.buyer + self.auction

    def __str__(self):
        return "{} {} {}".format(self.buyer,self.auction,self.amount)
