#unittest
from payment_system import Database, calculate_final_amount


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
        assert db.get_transaction(id) == amount*.25