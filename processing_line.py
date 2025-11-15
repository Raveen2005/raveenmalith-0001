from data_structures import linked_queue
from data_structures import linked_stack

class Transaction:
    def __init__(self, timestamp, from_user, to_user):
        self.timestamp = timestamp
        self.from_user = from_user
        self.to_user = to_user
        self.signature = None
    
    def sign(self):
        """
        Constructing message: O(m)
        forward loop over message: O(m)
        Backward loop over message: O(m)
        Converting to base-36 and padding: O(1)
        
        The overall complexity: O(m) where m is the length of the message 
        which consisits of(timestap + from_user + to_user)
        """

        message = str(self.timestamp) + '|' + self.from_user + '|' + self. to_user
        M = 36 ** 36 
        acc = 1469598103934665603
        B1 = 257 
        i = 0 
        while i < len(message): 
            acc = (acc * B1 + ord(message[i])) % M 
            i += 1 
        B2 = 263 
        i = len(message) - 1 
        while i >= 0 : 
            acc = (acc * B2 + ord(message[i])) % M 
            i -= 1 
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        if acc == 0 : 
            enc = '0'
        else : 
            enc=''
            while acc > 0 : 
                rem = acc % 36 
                enc = digits[rem] + enc 
                acc //= 36 
        if len(enc) < 36 : 
            enc = ("0" * (36 - len(enc))) + enc 
        elif len(enc) > 36 : 
            enc = enc[-36:]
        self.signature = enc 
        pass


class ProcessingLine:
    def __init__(self, critical_transaction):
        """
        - Constatnt number of checks: O(1)
        - Creating empty linked queue and linked stack and assigning them to 
          self.__before and self.__after: O(1)
        - Assigning boolean values to _locked, _iter_created, _yielded_critical: O(1)
        - The overall complxity is O(1)
        
        """
        if critical_transaction is None : 
            raise ValueError("Crirtcal transaction can't be None")
        if not hasattr(critical_transaction, "timestamp"):
            raise TypeError("Critical transaction should have a timestamp")
        if not hasattr(critical_transaction, "sign"):
            raise TypeError("Critical transcation should have a sign() method")
        self._critical = critical_transaction
        self.__before = linked_queue.LinkedQueue()
        self.__after = linked_stack.LinkedStack()
        self._locked = False 
        self._iter_created = False 
        self._yielded_critical = False 

    def add_transaction(self, transaction):
        """
        costant checks(if statements): O(1)
        insertion of elements into Linked_queue and Linked_stack:O(1)
        The overall complexity is O(1)
        """
        if self._locked: 
            raise RuntimeError("Can't add transactions already locked")
        if transaction is None : 
            raise ValueError('Transaction can not be none')
        if not hasattr(transaction,'timestamp'):
            raise TypeError("Transaction should have a timestamp")
        if not hasattr(transaction, 'sign'):
            raise TypeError("Trnsaction should have a sign() method")
        
        if transaction.timestamp <= self._critical.timestamp:
            self.__before.append(transaction)
        else:
            self.__after.push(transaction)
        
    def __iter__(self):
        if self._iter_created : 
            raise RuntimeError("An iterator already exists for the following transaction ")
        self._iter_created = True 
        self._locked = True 
        return self
    
    def __next__(self):
        if not self.__before.is_empty():
            transaction = self.__before.serve()
            if transaction.signature is None:
                transaction.sign()
            return transaction  
        if not self._yielded_critical:
            self._yielded_critical = True
            if self._critical.signature is None:
                self._critical.sign()
            return self._critical  
        if not self.__after.is_empty():
            transaction = self.__after.pop()
            if transaction.signature is None:
                transaction.sign()
            return transaction 
        raise StopIteration
        

      


if __name__ == "__main__":
    # Write tests for your code here...
    # We are not grading your tests, but we will grade your code with our own tests!
    # So writing tests is a good idea to ensure your code works as expected.
    
    # Here's something to get you started...
    transaction1 = Transaction(50, "alice", "bob")
    transaction2 = Transaction(100, "bob", "dave")
    transaction3 = Transaction(120, "dave", "frank")

    line = ProcessingLine(transaction2)
    line.add_transaction(transaction3)
    line.add_transaction(transaction1)

    print("Let's print the transactions... Make sure the signatures aren't empty!")
    line_iterator = iter(line)
    while True:
        try:
            transaction = next(line_iterator)
            print(f"Processed transaction: {transaction.from_user} -> {transaction.to_user}, "
                  f"Time: {transaction.timestamp}\nSignature: {transaction.signature}")
        except StopIteration:
            break

