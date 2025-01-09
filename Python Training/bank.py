#Construct a ATM Process using Access Modifier

class Bank:
    _bal = None
    _user = None
    def __init__(self,bal,user):
        _bal = bal
        _user = user
    class Customer(Bank):
        _pin = None
        def __init__(self,pin,user):
            _pin = pin
            _user = user
            