# In-Memory Database with Transaction Support

This Python program implements an in-memory key-value database with transaction support. It allows users to perform operations like get, put, begin transaction, commit transaction, and rollback transaction.

## Usage
1. **Clone the repository:**
    ```bash
    git clone https://github.com/elilowe1/storageManagement.git
    ```

3. **Run the program:**
    ```bash
    python InMemoryDB.py
    ```

4. **Follow the on-screen prompts to interact with the database:**
    - Choose an action from the menu by entering the corresponding number.
    - For `Put key-value pair`, enter the key and value when prompted.
    - For `Get value by key`, enter the key when prompted.
    - For `Begin transaction`, a new transaction will be started.
    - For `Commit transaction`, the current transaction will be committed.
    - For `Rollback transaction`, the changes made in the current transaction will be rolled back.
    - For `Exit`, the program will terminate.
    - For `Run given example code`, the program will run the given examples


## Example
![Screenshot 2024-04-21 221309](https://github.com/elilowe1/storageManagement/assets/91981498/10be733e-1281-4d8d-b304-88efe5bd67cd)
![Screenshot 2024-04-21 221254](https://github.com/elilowe1/storageManagement/assets/91981498/23f65019-f684-48b3-b5c3-ca93fad90b82)


## Modification to become an "official" assignment in the future
- Alllow multiple users to make transactions
- Make authentication so only certain users can access certain data/transactions
- Unit tests to ensure the correctness of each function
- 
