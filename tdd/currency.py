class Money(object):
    def __init__(self,amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

class BritishPound(Money):

    # def __init__(self,amount):
    #     self.amount = amount
    #
    # def __eq__(self, other):
    #     return self.amount == other.amount

    def times(self, multiplier:int):
        return self.__class__(self.amount * multiplier)


class Dollar(Money):

    # def __init__(self,amount):
    #     self.amount = amount
    #
    # def __eq__(self, other):
    #     return self.amount == other.amount

    def times(self, multiplier:int):
        return self.__class__(self.amount * multiplier)