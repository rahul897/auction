from model.User import User


class Buyer(User):
    def __init__(self,name):
        self.preffered_buyer = False
        super().__init__(name)
