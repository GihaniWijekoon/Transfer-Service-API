from models import accounts, Transaction

class TransferService:
    @staticmethod
    def transfer_funds(transaction: Transaction):
        source_acc = accounts.get(transaction.source)
        dest_acc = accounts.get(transaction.destination)

        if not source_acc or not dest_acc:
            return{"status": "error", "message":"Invalid account number"}
        
        if source_acc.balance < transaction.amount:
            return{"status":"error", "message":"Insufficient balance"}
        
        source_acc.balance -= transaction.amount
        dest_acc.balance += transaction.amount

        return{"status":"success", "message":"Transfer completed successfully"}