class InMemoryDB:

    def __init__(self):
        self.data = {}
        self.transaction_in_progress = False
        self.transaction_data = {}

    # Returns value associated with a key, null if key doesn't exist
    def get(self, key):
        return self.data.get(key, None)
        
    # Creates new key value pair or updates existing one
    def put(self, key, value):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_data[key] = value

    # Starts tansaction
    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in progress")
        self.transaction_in_progress = True
        self.transaction_data = self.data.copy()

    # Saves transaction data
    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.data.update(self.transaction_data)
        self.transaction_in_progress = False
        self.transaction_data = {}

    # Aborts transaction data
    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_in_progress = False
        self.transaction_data = {}


def example_code():

    # Given Example Usage
    inmemoryDB = InMemoryDB()

    print('Running: inmemoryDB.get("A")')
    print(inmemoryDB.get("A"))  # should return None, because A doesn't exist in the DB yet

    # should throw an error because a transaction is not in progress
    print('Running: inmemoryDB.put("A", 5)')
    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print(e)

    print('Running: inmemoryDB.begin_transaction()')
    inmemoryDB.begin_transaction()  # starts a new transaction

    print('Running: inmemoryDB.put("A", 5)')
    inmemoryDB.put("A", 5)  # set's value of A to 5, but its not committed yet

    print('Running: inmemoryDB.get("A")')
    print(inmemoryDB.get("A"))  # should return None, because updates to A are not committed yet

    print('Running: inmemoryDB.put("A", 6)')
    inmemoryDB.put("A", 6)  # update A's value to 6 within the transaction

    print('Running: inmemoryDB.commit()')
    inmemoryDB.commit()  # commits the open transaction

    print('Running: inmemoryDB.get("A")')
    print(inmemoryDB.get("A"))  # should return 6, that was the last value of A to be committed

    print('Running: inmemoryDB.commit()')
    # throws an error, because there is no open transaction
    try:
        inmemoryDB.commit()
    except Exception as e:
        print(e)

    print('Running: inmemoryDB.rollback()')
    # throws an error because there is no ongoing transaction
    try:
        inmemoryDB.rollback()
    except Exception as e:
        print(e)

    print('Running: inmemoryDB.get("B")')
    print(inmemoryDB.get("B"))  # should return None because B does not exist in the database

    print('Running: inmemoryDB.begin_transaction()')
    inmemoryDB.begin_transaction()  # starts a new transaction

    print('Running: inmemoryDB.put("B", 10)')
    inmemoryDB.put("B", 10)  # Set key B's value to 10 within the transaction

    print('Running: inmemoryDB.rollback()')
    inmemoryDB.rollback()  # Rollback the transaction - revert any changes made to B

    print('Running: inmemoryDB.get("B")')
    print(inmemoryDB.get("B"))  # Should return None because changes to B were rolled back


def user_input():

    # Create an instance of InMemoryDB
    inmemoryDB = InMemoryDB()

    # Allow users to choose the transactions they want to make
    while True:
        print("\nChoose an action:")
        print("1. Get value by key")
        print("2. Put key-value pair")
        print("3. Begin transaction")
        print("4. Commit transaction")
        print("5. Rollback transaction")
        print("6. Exit")
        print("7. Run given example code")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = inmemoryDB.get(key)
            print("Value:", value)

        elif choice == "2":
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            try:
                inmemoryDB.put(key, value)
            except Exception as e:
                print(e)

        elif choice == "3":
            try:
                inmemoryDB.begin_transaction()
                print("Transaction started")
            except Exception as e:
                print(e)

        elif choice == "4":
            try:
                inmemoryDB.commit()
                print("Transaction committed and ended")
            except Exception as e:
                print(e)

        elif choice == "5":
            try:
                inmemoryDB.rollback()
                print("Transaction rolled back and ended")
            except Exception as e:
                print(e)

        elif choice == "6":
            print("Exiting...")
            break

        elif choice == "7":
            example_code()
            break

        else:
            print("Invalid choice")


def main():
    user_input()

if __name__ == "__main__":
    main()


