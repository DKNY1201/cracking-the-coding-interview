"""
FooCorp In-Memory Key-Value Store

Your first programming project at FooCorp is to build an interactive shell that allows access to a transactional
in-memory key / value store. For ease of use, this store will have a Read-Eval-Print loop (REPL) accessible via the
command line that allows users to interactively write and query data in a session.

Implementation considerations
Speed: Should optimize for read performance over writes
Memory: Expect that this database will fit within the bounds of memory on a single machine.
Durability: Data written to the database is not required to be durable beyond the interactive session.
Multi-user: Multiple users are not supported (single session only)
Code reuse: Please refrain from using off-the-shelf components for transactional storage (e.g. sqlite)

Data Types
Keys and values within this system are simple alpha-numeric sequences with no spaces or special characters.

REPL Operations
In the following examples, “>” denotes the REPL prompt of the program, bolded strings represent user input and normal
values represent output from the program.

SET [KEY] [VALUE]
Sets the given key to the specified value. If the key is already present, overwrite the old value.

> SET A 2
> GET A
A = 2
> SET A 3
> GET A
A = 3

DELETE [KEY]
Deletes the given key. If the key has not been set, ignore.

> SET A 2
> GET A
A = 2
> DELETE A
> DELETE B
> GET A
A not set

GET [KEY]
Prints out the current value of the specified key. If the key has not been set, prints a message.

> SET A 2
> GET A
A = 2
> GET B
B not set

COUNT [VALUE]
Returns the number of keys that have been set to the specified value. If no keys have been set to that value, prints 0.

> SET A FOO
> SET B BAR
> SET C FOO
> COUNT FOO
2
> COUNT BAR
1
> COUNT BAZ
0

BEGIN
Starts a transaction. These transactions allow you to modify the state of the system and commit or rollback your changes. Transactions can be nested as well, as will be illustrated below.

COMMIT
Commits the changes made within the context of the active transaction and ends the active transaction. If no transaction is active, prints NO TRANSACTION

> COMMIT
NO TRANSACTION
> BEGIN
> SET A 1
> GET A
A = 1
> COMMIT
> GET A
A = 1

ROLLBACK
Throws away changes made within the context of the active transaction and ends the active transaction. If no transaction is active, prints NO TRANSACTION

> ROLLBACK
NO TRANSACTION
> BEGIN
> SET A 1
> GET A
A = 1
> ROLLBACK
> GET A
A not set


Illustrative examples

Example 1:
> SET A 1
> SET B 1
> BEGIN
> SET A 2
> SET C 3
> COUNT 1
1
> ROLLBACK
> COUNT 1
2
> GET C
C not set

Example 2:
> SET A 1
> SET B 1
> BEGIN
> SET A 2
> DELETE B
> BEGIN
> COUNT 1
0
> DELETE A
> SET C 1
> COMMIT
> GET A
A not set
> COMMIT
> COUNT 1
1

Example 3:
> SET A 1
> BEGIN
> GET A
A = 1
> BEGIN
> SET A 4
> COMMIT
> GET A
A = 4
> ROLLBACK
> GET A
A = 1

Example 4:
> SET A 1
> SET B 1
> BEGIN
> SET A 2
> SET B 2
> COUNT 1
0
> BEGIN
> SET A 3
> COUNT 2
1
> ROLLBACK
> COUNT 2
2
> BEGIN
> DELETE B
> COUNT 2
1
> BEGIN
> GET B
B not set
> SET B 1
> COMMIT
> COUNT 2
1
> COMMIT
> GET B
B = 1
> ROLLBACK
> GET A
A = 1
> COUNT 1
2
> BEGIN
> BEGIN
> SET A 2
> SET A 3
> ROLLBACK
> GET A
A = 1
> BEGIN
> SET A 4
> COMMIT
> GET A
A = 4
> ROLLBACK
> GET A
A = 1
"""


class Transaction:
    def __init__(self):
        self.key_val_map = {}
        self.count_map = {}

    def set(self, key, val):
        if key in self.key_val_map:
            existing_val = self.key_val_map[key]
            self.count_map[existing_val] -= 1

        self.key_val_map[key] = val

        if val not in self.count_map:
            self.count_map[val] = 0
        self.count_map[val] += 1

    def delete(self, key):
        if key not in self.key_val_map:
            return

        if key in self.key_val_map:
            existing_val = self.key_val_map[key]
            self.count_map[existing_val] -= 1

        del self.key_val_map[key]

    def get(self, key):
        if key not in self.key_val_map:
            return key + ' not set'

        return self.key_val_map[key]

    def count(self, val):
        return self.count_map.get(val, 0)


class FooCorp:
    def __init__(self):
        default_transaction = Transaction()
        self.transactions = [default_transaction]

    def clone_transaction(self, transaction):
        new_transaction = Transaction()

        for key, val in transaction.key_val_map.items():
            new_transaction.key_val_map[key] = val

        for val, count in transaction.count_map.items():
            new_transaction.count_map[val] = count

        return new_transaction

    def set(self, key, val):
        self.transactions[-1].set(key, val)

    def get(self, key):
        return self.transactions[-1].get(key)

    def delete(self, key):
        self.transactions[-1].delete(key)

    def count(self, val):
        return self.transactions[-1].count(val)

    def begin(self):
        new_transaction = self.clone_transaction(self.transactions[-1])
        self.transactions.append(new_transaction)

    def commit(self):
        if len(self.transactions) <= 1:
            print("NO TRANSACTION")
            return

        del self.transactions[-2]

    def rollback(self):
        if len(self.transactions) <= 1:
            print("NO TRANSACTION")
            return

        self.transactions.pop()

fc = FooCorp()

# example 1
# fc.set('A', 1)
# fc.set('B', 1)
# fc.begin()
# fc.set('A', 2)
# fc.set('C', 3)
# print(fc.count(1))
# fc.rollback()
# print(fc.count(1))
# print(fc.get('C'))

# example 2
# fc.set('A', 1)
# fc.set('B', 1)
# fc.begin()
# fc.set('A', 2)
# fc.delete('B')
# fc.begin()
# print(fc.count(1))
# fc.delete('A')
# fc.set('C', 1)
# fc.commit()
# print(fc.get('A'))
# fc.commit()
# print(fc.count(1))

# example 3
# fc.set('A', 1)
# fc.begin()
# print(fc.get('A'))
# fc.begin()
# fc.set('A', 4)
# fc.commit()
# print(fc.get('A'))
# fc.rollback()
# print(fc.get('A'))

# example 4
fc.set('A', 1)
fc.set('B', 1)
fc.begin()
fc.set('A', 2)
fc.set('B', 2)
print("fc.count(1)", fc.count(1))
fc.begin()
fc.set('A', 3)
print("fc.count(2)", fc.count(2))
fc.rollback()
print("fc.count(2)", fc.count(2))
fc.begin()
fc.delete('B')
print("fc.count(2)", fc.count(2))
fc.begin()
print("fc.get('B')", fc.get('B'))
fc.set('B', 1)
fc.commit()
print("fc.count(2)", fc.count(2))
fc.commit()
print("fc.get('B')", fc.get('B'))
fc.rollback()
# print(fc.transactions[-1].key_val_map)
print("fc.get('A')", fc.get('A'))
print("fc.count(1)", fc.count(1))
fc.begin()
fc.begin()
fc.set('A', 2)
fc.set('A', 3)
fc.rollback()
print("fc.get('A')", fc.get('A'))
fc.begin()
fc.set('A', 4)
fc.commit()
print("fc.get('A')", fc.get('A'))
fc.rollback()
print("fc.get('A')", fc.get('A'))
