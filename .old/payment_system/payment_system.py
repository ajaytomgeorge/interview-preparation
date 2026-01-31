class Database:
    def __init__(self):
        self.memory = {}

    def insert_transaction(self,id:int,amout:float):
        self.memory[id] = amout
        return True
    def get_transaction(self, id):
        return self.memory[id]
    def process_transactions(self,transactions:list[dict[str,float]]):
        for transaction in transactions:
            self.insert_transaction(*transaction)

def calculate_final_amount(amount:float):
    return amount*1.25

def process_transaction(amount):
    db = Database()
    db.insert_transaction(calculate_final_amount(amount))

#unittest
def test_calculate_final_amount():
    assert 6.25 == calculate_final_amount(5)

#intergration_Test
def test_process_transaction():
    db = Database()
    db.insert_transaction("1",calculate_final_amount(7))
    print(db.get_transaction("1"))
    assert db.get_transaction("1") == 8.75

# end to end test
def test_process_batch_processing():
    transactions = [("1",7),
                   ("2",6),
                   ("3",9),]
    db = Database()
    db.process_transactions([(id,calculate_final_amount(amount)) for id, amount in transactions])
    for id, amount in transactions:
        print(db.get_transaction(id))
        assert db.get_transaction(id) == amount*1.25


test_calculate_final_amount()
test_process_transaction()
test_process_batch_processing()






