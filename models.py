class Account:
    def __init__(self, account_number:str, balance: float):
        self.account_number = account_number
        self.balance = balance

class Transaction:
    def __init__(self, source: str, destination: str, amount:float):
        self.source = source
        self.destination = destination
        self.amount = amount

accounts = {
    "123": Account("123", 500.0),
    "456": Account("456", 300.0),
}